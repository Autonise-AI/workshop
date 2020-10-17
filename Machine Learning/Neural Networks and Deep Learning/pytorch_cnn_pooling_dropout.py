import random

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.nn import functional as F
from torchvision import datasets, transforms


class Net(nn.Module):
    def __init__(self):  # Constructor

        super(Net, self).__init__()

        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

        # xavier_initialization

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        return x


def train(model, use_cuda, train_loader, optimizer, epoch):

    model.train()  # Tell the model to prepare for training
    
    for batch_idx, (data, target) in enumerate(train_loader):  # Get the batch

        # Converting the target to one-hot-encoding from categorical encoding
        # Converting the data to [batch_size, 784] from [batch_size, 1, 28, 28]
            
        if use_cuda:
            data, target = data.cuda(), target.cuda()  # Sending the data to the GPU

        optimizer.zero_grad()  # Setting the cumulative gradients to 0
        output = model(data)  # Forward pass through the model
        loss = F.cross_entropy(output, target)  # Calculating the loss
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

            if use_cuda:
                data, target = data.cuda(), target.cuda()  # Sending the data to the GPU

            # argmax([0.1, 0.2, 0.9, 0.4]) => 2
            # output - shape = [1000, 10], argmax(dim=1) => [1000]
            output = model(data)  # Forward pass
            test_loss += F.cross_entropy(output, target, reduction='sum')  # sum up batch loss
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

    # Get the train dataloader
    train_loader = torch.utils.data.DataLoader(dataset1, num_workers=6, shuffle=True, batch_size=64)
    # Get the test dataloader
    test_loader = torch.utils.data.DataLoader(dataset2, num_workers=6, shuffle=False, batch_size=1000)

    model = Net()  # Get the model

    if use_cuda:
        model = model.cuda()  # Put the model weights on GPU

    optimizer = optim.SGD(model.parameters(), lr=0.1)  # Choose the optimizer and the set the learning rate

    for epoch in range(1, 10 + 1):
        train(model, use_cuda, train_loader, optimizer, epoch)  # Train the network
        test(model, use_cuda, test_loader)  # Test the network

    torch.save(model.state_dict(), "mnist_cnn.pt")

    # Loading a saved model - model.load_state_dict(torch.load('mnist_cnn.pt'))


main()
