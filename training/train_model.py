import os
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from models.tictactoe_model import TicTacToeModel

class TicTacToeDataset(Dataset):
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        state = np.array(eval(self.data.iloc[idx, 0]), dtype=float)
        move = int(self.data.iloc[idx, 1])
        return torch.FloatTensor(state), torch.LongTensor([move])

def train_model(epochs=10, continue_training=False):
    print('Starting model training...')
    print(f'Training for {epochs} epochs...')
    dataset = TicTacToeDataset('data/tictactoe_data.csv')
    dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

    model = TicTacToeModel()
    if continue_training:
        model.load_state_dict(torch.load('models/tictactoe.pt'))
        print('Loaded existing model weights for continued training.')

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(epochs):
        total_loss = 0
        for states, moves in dataloader:
            optimizer.zero_grad()
            outputs = model(states)
            loss = criterion(outputs, moves.squeeze(1))
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        average_loss = total_loss / len(dataloader)
        print(f'Epoch {epoch+1}/{epochs} completed. Average Loss: {average_loss}')

    os.makedirs('models', exist_ok=True)
    torch.save(model.state_dict(), 'models/tictactoe.pt')
    print('Model training completed. Model saved to models/tictactoe.pt')

if __name__ == '__main__':
    train_model()
