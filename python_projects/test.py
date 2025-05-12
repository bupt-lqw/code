print("hello word")
for i in range(10):
    print(i)


print(1 * 1)

import torch
print(torch.__version__)
device = torch.device("mps")

a = torch.tensor([1, 2])
print(a.device)


a = torch.tensor([1, 2]).to(device)
print(a.device)

print('test dev branch')

print('branch dev')