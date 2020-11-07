import random
import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms


class Net(nn.Module):
    def __init__(self):

        super(Net, self).__init__()

        # 2 Layers
        self.fc1 = nn.Linear(784, 100)
        self.fc2 = nn.Linear(100, 10)

    def forward(self, x):

        # Layer 1
        x = self.fc1(x)

        # Activation 1
        x = torch.sigmoid(x)

        # Layer 2
        x = self.fc2(x)

        return x


def train(model, use_cuda, train_loader, optimizer, epoch):

    model.train()  # Tell the model to prepare for training

    correct = 0
    total = 0
    
    for batch_idx, (data, target) in enumerate(train_loader):  # Get the batch

        # Converting the target to one-hot-encoding from categorical encoding
        # Converting the data to [batch_size, 784] from [batch_size, 1, 28, 28]
            
        data = data.view([data.shape[0], 784])

        if use_cuda:
            data, target = data.cuda(), target.cuda()  # Sending the data to the GPU

        optimizer.zero_grad()  # Setting the cummulative gradients to 0
        output = model(data)  # Forward pass through the model
        loss = torch.nn.functional.cross_entropy(output, target)  # Calculating the CEL
        loss.backward()  # Calculating the gradients of the model. Note that the model has not yet been updated.
        optimizer.step()  # Updating the model parameters. Note that this does not remove the stored gradients!

        pred = output.argmax(dim=1, keepdim=True)  # get the index of the maximum output
        correct += pred.eq(target.view_as(pred)).sum().item()  # Get total number of correct samples
        total += output.shape[0]

        if batch_idx % 100 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))

    print('Training Accuracy: ', correct / total)


def test(model, use_cuda, test_loader):

    model.eval()  # Tell the model to prepare for testing or evaluation

    test_loss = 0
    correct = 0

    with torch.no_grad():  # Tell the model that gradients need not be calculated
        for data, target in test_loader:  # Get the batch

            # Converting the target to one-hot-encoding from categorical encoding
            # Converting the data to [batch_size, 784] from [batch_size, 1, 28, 28]

            data = data.view([data.shape[0], 784])

            if use_cuda:
                data, target = data.cuda(), target.cuda()  # Sending the data to the GPU

            output = model(data)  # Forward pass
            test_loss += torch.nn.functional.cross_entropy(output, target, reduction='sum')  # sum up batch loss
            pred = output.argmax(dim=1, keepdim=True)  # get the index of the maximum output
            correct += pred.eq(target.view_as(pred)).sum().item()  # Get total number of correct samples

    test_loss /= len(test_loader.dataset)  # Accuracy = Total Correct / Total Samples

    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


def seed(seed_value):

    # This removes randomness, makes everything deterministic

    torch.cuda.manual_seed_all(seed_value)  # if you are using multi-GPU.
    torch.manual_seed(seed_value)
    torch.cuda.manual_seed(seed_value)
    np.random.seed(seed_value)
    random.seed(seed_value)
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True


def main():

    use_cuda = True  # Set it to False if you are using a CPU

    torch.manual_seed(0)  # Used to fix randomness in the code! Very important!

    # Convert the dataset to tensor and subtract the mean and divide by
    # standard deviation. Why? So that neurons don't saturate!
    transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    dataset1 = datasets.MNIST('../data', train=True, download=True, transform=transform)  # Get the train dataset
    dataset2 = datasets.MNIST('../data', train=False, transform=transform)  # Get the test dataset

    dataset1.data = dataset1.data[0:5000]
    dataset1.targets = dataset1.targets[0:5000]
    print(dataset1.data.shape, dataset1.targets.shape)

    train_loader = torch.utils.data.DataLoader(dataset1, num_workers=6, shuffle=True, batch_size=64)  # Get the train dataloader
    test_loader = torch.utils.data.DataLoader(dataset2, num_workers=6, shuffle=False, batch_size=1000)  # Get the test dataloader

    model = Net()  # Get the model

    if use_cuda:
        model = model.cuda()  # Put the model weights on GPU

    optimizer = optim.SGD(model.parameters(), lr=1)  # Choose the optimizer and the set the learning rate

    for epoch in range(1, 100 + 1):
        train(model, use_cuda, train_loader, optimizer, epoch)  # Train the network
        if epoch % 10 == 0:
            test(model, use_cuda, test_loader)  # Test the network

    torch.save(model.state_dict(), "mnist_cnn.pt")


if __name__ == '__main__':

    main()
