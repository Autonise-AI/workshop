import random

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms


class Net(nn.Module):
    def __init__(self):  # Constructor

        super(Net, self).__init__()

        # 2 Layers
        self.fc1 = nn.Linear(784, 100)
        self.fc2 = nn.Linear(100, 10)

        # xavier_initialization

    def forward(self, x):
        # x - shape = [64, 784]
        # Layer 1
        l1 = self.fc1(x)  # l1 - shape = [64, 100]

        # Activation 1
        l1_a1 = torch.sigmoid(l1)  # l1_a1 - shape = [64, 100]

        # Layer 2
        l2 = self.fc2(l1_a1)  # l2 - shape = [64, 10]

        # Activation 2
        l2_a2 = torch.sigmoid(l2)  # l2_a2 - shape = [64, 10]
        
        return l2_a2


def train(model, use_cuda, train_loader, optimizer, epoch):

    model.train()  # Tell the model to prepare for training
    
    for batch_idx, (data, target) in enumerate(train_loader):  # Get the batch

        # Converting the target to one-hot-encoding from categorical encoding
        # Converting the data to [batch_size, 784] from [batch_size, 1, 28, 28]

        y_onehot = torch.zeros([target.shape[0], 10])  # Zero vector of shape [64, 10]
        y_onehot[range(target.shape[0]), target] = 1

        data = data.view([data.shape[0], 784])

        if use_cuda:
            data, y_onehot = data.cuda(), y_onehot.cuda()  # Sending the data to the GPU

        optimizer.zero_grad()  # Setting the cumulative gradients to 0
        output = model(data)  # Forward pass through the model
        loss = torch.mean((output - y_onehot)**2)  # Calculating the loss
        loss.backward()  # Calculating the gradients of the model. Note that the model has not yet been updated.
        optimizer.step()  # Updating the model parameters. Note that this does not remove the stored gradients!

        if batch_idx % 100 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))


def test(model, use_cuda, test_loader):

    model.eval()  # Tell the model to prepare for testing or evaluation

    test_loss = 0
    correct = 0

    with torch.no_grad():  # Tell the model that gradients need not be calculated
        for data, target in test_loader:  # Get the batch

            # Converting the target to one-hot-encoding from categorical encoding
            # Converting the data to [batch_size, 784] from [batch_size, 1, 28, 28]

            y_onehot = torch.zeros([target.shape[0], 10])
            y_onehot[range(target.shape[0]), target] = 1
            data = data.view([data.shape[0], 784])

            if use_cuda:
                data, target, y_onehot = data.cuda(), target.cuda(), y_onehot.cuda()  # Sending the data to the GPU

            # argmax([0.1, 0.2, 0.9, 0.4]) => 2
            # output - shape = [1000, 10], argmax(dim=1) => [1000]
            output = model(data)  # Forward pass
            test_loss += torch.sum((output - y_onehot)**2)  # sum up batch loss
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
    # Colab And Kaggle

    seed(0)  # Used to fix randomness in the code! Very important!

    # Convert the dataset to tensor and subtract the mean and divide by standard
    # deviation. Why? So that neurons don't saturate!
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))  # ((mean), (std))    (x - mean)/std
    ])
    # [a1, a2, a3] / [b1, b2, b3] = [a1/b1, a2/b2, a3/b3]

    # Wx + b =~ b

    dataset1 = datasets.MNIST('../data', train=True, download=True, transform=transform)  # Get the train dataset
    dataset2 = datasets.MNIST('../data', train=False, transform=transform)  # Get the test dataset

    # Get the train data-loader
    train_loader = torch.utils.data.DataLoader(dataset1, num_workers=6, shuffle=True, batch_size=64)
    # Get the test data-loader
    test_loader = torch.utils.data.DataLoader(dataset2, num_workers=6, shuffle=False, batch_size=1000)

    model = Net()  # Get the model

    if use_cuda:
        model = model.cuda()  # Put the model weights on GPU

    optimizer = optim.SGD(model.parameters(), lr=10)  # Choose the optimizer and the set the learning rate

    for epoch in range(1, 10 + 1):
        train(model, use_cuda, train_loader, optimizer, epoch)  # Train the network
        test(model, use_cuda, test_loader)  # Test the network

    torch.save(model.state_dict(), "mnist.pt")

    model.load_state_dict(torch.load('mnist.pt'))

    # Loading a saved model - model.load_state_dict(torch.load('mnist_cnn.pt'))


if __name__ == '__main__':
    main()
