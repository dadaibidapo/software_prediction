import torch
import torch.nn as nn
import numpy as np
import os

class LinearReg(nn.Module):
    def __init__(self, input_shape: int,
               hidden_units: int,
               output_shape: int)->None:
       super().__init__()
       self.linear_layer = nn.Sequential(
        nn.Linear(in_features=input_shape, out_features=hidden_units),
        nn.Linear(in_features=hidden_units, out_features=output_shape),
        # nn.Linear(in_features=input_shape, out_features=output_shape),
        )
    def forward(self, x):
        return self.linear_layer(x)
