# -*- coding: utf-8 -*-
"""partB.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xvhtCpVUcN0Y2qKOlacKP-6ixQRRspzm
"""

!pip install wandb

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.models as models
from torch.utils.data import DataLoader, random_split
from torchvision.datasets import ImageFolder
import wandb


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)

wandb.login(key='e3c892d4f8c9cd9b9043d31938ad090f0a32cec1')


def get_data_loaders(batch_size=64):
    train_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])

    val_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])

    train_dataset = ImageFolder(root='/content/drive/MyDrive/inaturalist_12K/train', transform=train_transform)
    test_dataset = ImageFolder(root='/content/drive/MyDrive/inaturalist_12K/val', transform=val_transform)


    train_size = int(0.8 * len(train_dataset))
    val_size = len(train_dataset) - train_size
    train_dataset, val_dataset = random_split(train_dataset, [train_size, val_size])

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size)
    test_loader = DataLoader(test_dataset, batch_size=batch_size)

    return train_loader, val_loader, test_loader


def fine_tune_pretrained_model(model, train_loader, val_loader, num_epochs=10, learning_rate=0.001):
    model = model.to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)


    for epoch in range(num_epochs):
        model.train()
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()


        model.eval()
        total = 0
        correct = 0
        with torch.no_grad():
            for images, labels in val_loader:
                images, labels = images.to(device), labels.to(device)
                outputs = model(images)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        val_accuracy = 100 * correct / total
        print(f'Epoch [{epoch+1}/{num_epochs}], Validation Accuracy: {val_accuracy:.2f}%')


sweep_config = {
    'method': 'grid',
    'metric': {'name': 'val_accuracy', 'goal': 'maximize'},
    'parameters': {
        'freeze_percentage': {
            'values': [0.85, 0.90, 0.95]  #freeze 85%, 90%, or 95% of layers
        }
    }
}


sweep_id = wandb.sweep(sweep=sweep_config, project='DLassignment2B')


def main():
    with wandb.init() as run:
        config = wandb.config
        model = models.resnet50(pretrained=True)
        freeze_layers = int(len(list(model.parameters())) * config.freeze_percentage)


        for idx, param in enumerate(model.parameters()):
            if idx < freeze_layers:
                param.requires_grad = False


        train_loader, val_loader, _ = get_data_loaders()


        fine_tune_pretrained_model(model, train_loader, val_loader)


wandb.agent(sweep_id, function=main,count=3)