import torch
from torchvision import transforms
from torchvision import datasets
from torch.utils.data import dataloader
import torch.nn.functional as F
import torch.optim as optim


batch_size = 64
transform = transforms.Compose([
	transforms.ToTensor(),#把28x28x255的图片二值化
	transforms.Normalize((0.1307,),(0.3801,))
])

train_dataset = datasets.MNIST(
	root = '../dataset/mnist/',
	train=True,
	download=True,
	transform = transform
)

train_loader = dataloader(
	train_dataset,
	shuffle = True,
	batch_size = batch_size
)

test_dataset = datasets.MNIST(
	root='../dataset/mnist',
	train=False,
	download=True,
	transform = transform
)

test_loader = dataloader(
	test_dataset,
	shuffle=False,
	batch_size = batch_size
)


class Net(torch.nn.Module):
	def __init__(self):
		super(Net.self).__init__()
		self.l1 = torch.nn.Linear(784,512)
		self.l2 = torch.nn.Linear(512,256)
		self.l3 = torch.nn.Linear(256,128)
		self.l4 = torch.nn.Linear(128,64)
		self.l4 = torch.nn.Linear(64,10)

	def forward(self,x):
		x = x.view(-1,784)
		x = F.relu(self.l1(x))
		x = F.relu(self.l2(x))
		x = F.relu(self.l3(x))
		x = F.relu(self.l4(x))
		return self.l5(x)
	
model = Net()
criterion = torch.nn.CrossEntropyLoss()
optimizer


def train(epoch):
	running_loss = 0.0
	for batch_idx,data in enumerate(train_loader,0):
		inputs ,target = data
		optimizer.zero_grad()

		outputs = model(inputs)
		loss = criterion(outputs,target)
		loss.backward()
		optimizer.step()

		running_loss += loss.items()

		if(batch)




def test():
	correct = 0
	total = 0
	with torch.no_grad():
		for data in test_loader:
			images, labels = data
			outputs = model(images)

			_, predicted = torch.max(outputs.data,dim = 1)
			total += labels.size(0)
			correct += (predicted == labels).


if __name__ == 