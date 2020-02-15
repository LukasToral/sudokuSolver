import numpy as np

class Board:

	def __init__(self, grid):
		self.grid = grid

	def displayNiceGrid(self):
		print (np.matrix(self.grid))

	def putNumber(self, coordinates):
		print(coordinates)

	def solve(self):
		for y in range(0,9):
			for x in range(0,9):
				if self.grid[y][x] == 0:
					self.putNumber([x,y])

