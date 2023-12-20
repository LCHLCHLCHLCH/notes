import torch
in_channel, out_channel = 5,10
width, height = 100, 100
kernal_size = 3
batch_size = 1

input = torch.randn(batch_size, in_channel, width, height)

conv_layer = torch.nn.Conv2d(in_channel, out_channel, kernal_size = kernal_size)

output = conv_layer(input)

print(input.shape)
print(output.shape)
print(conv_layer.weight.size)
