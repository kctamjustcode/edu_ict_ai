# -*- coding: utf-8 -*-
### dynamic_game_testing_rl.ipynb

import csv

t2=time.time()
# Open the CSV file
data_using = []
with open('/content/output.csv', mode='r') as file:
    reader = csv.reader(file)
    #search_item = [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1]  # Replace with the value you're searching for
    for row in reader:
        try:
            int_row = list(map(int, row))
            if int_row[-1] > 0:
                data_using += [int_row]
        except:
            pass
t3=time.time()
print(t3-t2)
print(len(data_using))
search_item = [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1]

t4=time.time()
data_using.index(search_item)
t5=time.time()
print(t5-t4)

print(search_item[:30])
print(search_item[30:33])

x_data = [data[:30] for data in data_using]
y_data = [data[30:33] for data in data_using]

print(x_data[:3])


import random
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

x_linr = np.array(x_data, dtype=np.float32)
y_linr = np.array(y_data, dtype=np.float32)

x_trn = torch.tensor(x_linr)
y_trn = torch.tensor(y_linr)


class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(len(x_data[0]), 45)
        self.fc2 = nn.Linear(45, 20)
        self.fc3 = nn.Linear(20, 10)
        self.fc4 = nn.Linear(10, len(y_data[0]))
        self.sigmoid = nn.Sigmoid()
        self.relu = nn.ReLU()

    def forward(self, x):
        #x = torch.relu(self.fc1(x))
        #x = torch.sigmoid(self.fc2(x))
        #x = torch.relu(self.fc3(x))
        x = self.sigmoid(self.fc1(x))
        x = self.sigmoid(self.fc2(x))
        x = self.relu(self.fc3(x))
        x = self.fc4(x)
        return x


# Instantiate the Model, Define Loss Function and Optimizer
model = SimpleNN()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.05)

NUM_EPOCH = 200
for epoch in range(NUM_EPOCH):
    model.train()

    # Forward pass
    outputs = model(x_trn)
    loss = criterion(outputs, y_trn)

    # Backward pass and optimize
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    accuracy = (outputs.round() == y_trn.round()).float().mean()

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch + 1}/{NUM_EPOCH}], Loss: {loss.item():.4f}, Accuracy: {accuracy.item():.4f}')

model.eval()
with torch.no_grad():
    for _ in range(10):
      randindice = random.randint(0, 100)
      test_item = x_data[randindice]
      predictions = model(torch.tensor(test_item, dtype=torch.float32))
      print()
      predictions_rounded = torch.round(predictions)
      print(y_data[randindice])
      print(f'Predictions:\n{predictions_rounded.to(torch.int32)}')
