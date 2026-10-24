import torch.nn as nn

def create_cnn():
  model = nn.Sequential(
      nn.Conv2d(
          in_channels = 3,
          out_channels = 16,
          kernel_size = 3,
          padding = 1
      ),
      nn.ReLU(),
      nn.MaxPool2d(kernel_size = 2),

      nn.Conv2d(
          in_channels = 16,
          out_channels = 32,
          kernel_size = 3,
          padding = 1
      ),
      nn.ReLU(),
      nn.MaxPool2d(kernel_size = 2),
      nn.Flatten(),
      nn.Linear(
          in_features = 1568,
          out_features = 8
      )

  )
  return model
