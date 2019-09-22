import torch
from torch.utils.data import DataLoader
from datasets import MidiDataset
from models import SimpleRNN
from sacred import Experiment

ex = Experiment()
# ToDo add mongo observer

@ex.config
def config():
    model_name = "SimpleRNN"
    model_params = {"voc_size": 228, "latent_space": 1024}
    dataset_size = 100
    dataset_name = "maestro-midi"
    # ToDo: using gettatr get model object, dataset object
    # ToDo: option to continue training

    lr = 1e-4
    batch_size = 16
    epochs = 10

@ex.capture
def get_dataset(dataset_name, dataset_size, _log):
    # ToDo: use gettatr
    return MidiDataset(dataset_size=dataset_size)

@ex.capture
def get_model(model_name, model_params):
    # ToDo: use gettatr
    return SimpleRNN(**model_params)

@ex.capture
def get_loss():
    return lambda x, y: torch.tensor([0])

@ex.automain
def train(lr, batch_size, epochs, model_name, model_params, _log, _run):

    dataset = get_dataset()
    train_loader = DataLoader(dataset, batch_size=batch_size)
    test_loader = DataLoader(dataset, batch_size=batch_size) # ToDo train/test split

    model = get_model()
    device = torch.device('cpu' if torch.cuda.device_count() == 0 else 'cuda:0')
    model.to(device)

    loss_func = get_loss()

    # ToDo: add training loop
    for epoch in range(epochs):
        for batch in train_loader:
            out = model(batch)
            loss = loss_func(out, batch)

        # ToDo: log everything

        for batch in test_loader:
            out = model(batch)
            loss = loss_func(out, batch)

        # ToDo: save checkpoint
