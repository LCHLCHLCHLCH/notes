import torch  
import numpy as np
from torch.utils.data import dataset
from torch.utils.data import dataloader

class DiabetesDataset(dataset):
	def __init__(self):
		xy = np.loadtxt(filepath,delimiter=',', dtype=np.float32)
		self.len = xy.shape[0]
		self.x_data = torch.from_numpy(xy[:, :-1])
		self.y_data = torch.from_numpy(xy[:,[-1]])
		pass

	def _getitem__(self, index):##可以给数据集编号
		return self.x_data[index], self.y_data[index]
		pass

	def __len__(self):##返回数据集的数据个数
		return self.len
		pass

dataset = DiabetesDataset('databetes.csv')

##初始化数据,其中num_works代表线程数,不要超过电脑核数
train_loader = dataloader(dataset = dataset, batch_size = 32, shuffle = True, num_workers = 2)


def main():
	for epoch in range(10):
		for i, data in enumerate(train_loader, 0):
			inputs, labels = data

			y_pred = model

if __name__ == 'main':
	main()