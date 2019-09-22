from torch.utils.data import DataLoader, Dataset
import torch

name2path = {"maestro-midi": "../data/maestro-v2.0-midi/"}

class MidiDataset(Dataset):
    def __init__(self, path=name2path['maestro-midi'], dataset_size=120):
        super().__init__()
        self.dataset_size = dataset_size
        pass

    def __len__(self):
        return self.dataset_size

    def __getitem__(self, ind):
        return torch.tensor([0])
