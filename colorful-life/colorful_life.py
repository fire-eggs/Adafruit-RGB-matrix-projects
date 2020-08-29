# "Colorful Life" from Adam Zheleznyak
# https://github.com/adam-zheleznyak/colorful-life
#
# Modified by fire-eggs to remove the uses of numpy and matplotlib,
# as these are the "display" functions superceded by using the RGB
# matrix.
#
import math
from random import random
from random import uniform

class Hue:
	"""This is a class to represent a color's hue as a float mod 1. Two Hue objects can be added together to get a new Hue object."""
	
	def __init__(self, value):
		self.value = float(value % 1)
	
	def __bool__(self):
		return True
	
	def __float__(self):
		return float(self.value)
	
	def __repr__(self):
		return repr(self.value)
	
	def __add__(self, other):
		return Hue(self.value + other.value)

def average_hue(list_of_hues):
	"""
	Gets the average hue from a list of hues.
	
	Parameters:
	list_of_hues (list of Hue objects)
	
	Returns:
	Hue
	"""
	
	x = 0.0
	y = 0.0
	# Take all the hues as points on a unit circle and average their coordinates to find the average
	for hue in list_of_hues:
		x += math.cos(hue.value*2*math.pi)
		y += math.sin(hue.value*2*math.pi)
	x /= len(list_of_hues)
	y /= len(list_of_hues)
	return Hue(math.atan2(y,x)/(2*math.pi))

def random_grid(height, width, density=.3, padding=0):
	"""
	Gives a random 2D grid of 1s and 0s.
	
	Parameters:
	height (int): How many rows the grid will have
	width (int): How many columns the grid will have
	density (float): The probability any given cell will be a 1
	padding (int): If a padding value is specified, cells within the padding distance of an edge will always be 0
	
	Returns:
	2D list
	"""
	
	if not padding:
		return [[1 if random()<density else 0 for x in range(width)] for y in range(height)]
	else:
		return [[(1 if random()<density else 0) if (not (x < padding or x >= width - padding)) and (not (y < padding or y >= height - padding)) else 0 for x in range(width)] for y in range(height)]

def random_colors(grid):
	"""
	Gives random colors to a grid of cells.
	
	Parameters:
	grid (2D list): Any cell that evaluates to True will become a random color
	
	Returns:
	2D list of Hue objects
	"""
	
	return [[Hue(random()) if cell else None for cell in row] for row in grid]

def colorful_life_step(colored_grid, color_variation=0.05, hard_boundary=True, rule=[[3],[2,3]]):
	"""
	Runs a step for The Colorful Game of Life.
	
	The Colorful Game of Life has the same rules as Conway's Game of Life, except that all living cells also have a color assigned to them. When a new cell is born, it will take on the average color of its parents. Color variation can be added so that newly born cells can deviate slightly in color. Living cells will keep their color fixed until they die.
	
	Parameters:
	colored_grid (2D list of Hue objects): The grid that should be stepped through
	color_variation (float): A newly born cell will deviate from its color randomly up or down, with this amount being the maximum possible deviation.
	hard_boundary (bool): Setting this to False will identify opposite edges so that cells touching the boundary will communicate with cells on the other side of the grid.
	rule (2D list of integers): The first set of elements is how many neighbors leads to a birth, and the second is how many neighbors lead to a cell surviving.
	
	Returns:
	2D list of Hue objects
	"""
	
	height = len(colored_grid)
	width = len(colored_grid[0])
	next_grid = []
	if not hard_boundary:
		if width >= 3 and height >= 3:
			for j in range(height):
				row = []
				for i in range(width):
					live_neighbors = [colored_grid[(j+a) % height][(i+b) % width] for a in (-1,0,1) for b in (-1,0,1) if ((a is not 0 or b is not 0) and colored_grid[(j+a) % height][(i+b) % width])]
					neighbor_count = len(live_neighbors)
					if colored_grid[j][i]:
						if neighbor_count in rule[1]:
							row.append(colored_grid[j][i])
						else:
							row.append(None)
					else:
						if neighbor_count in rule[0]:
							hue = average_hue(live_neighbors)
							row.append(Hue(hue.value+uniform(-color_variation, color_variation)))
						else:
							row.append(None)
				next_grid.append(row)
			return next_grid
		else:
			# Need to tweak things so cells aren't double-counted
			for j in range(height):
				row = []
				for i in range(width):
					if height >= 3:
						# width is short
						live_neighbors = [colored_grid[(j+a) % height][(i+b) % width] for a in (-1,0,1) for b in range(width) if ((a is not 0 or b is not 0) and colored_grid[(j+a) % height][(i+b) % width])]
					elif width >= 3:
						# height is short
						live_neighbors = [colored_grid[(j+a) % height][(i+b) % width] for a in range(height) for b in (-1,0,1) if ((a is not 0 or b is not 0) and colored_grid[(j+a) % height][(i+b) % width])]
					else:
						# width and height are short
						live_neighbors = [colored_grid[(j+a) % height][(i+b) % width] for a in range(height) for b in range(width) if ((a is not 0 or b is not 0) and colored_grid[(j+a) % height][(i+b) % width])]
						
						
					neighbor_count = len(live_neighbors)
					if colored_grid[j][i]:
						if neighbor_count in rule[1]:
							row.append(colored_grid[j][i])
						else:
							row.append(None)
					else:
						if neighbor_count in rule[0]:
							hue = average_hue(live_neighbors)
							row.append(Hue(hue.value+uniform(-color_variation, color_variation)))
						else:
							row.append(None)
				next_grid.append(row)
			return next_grid
	else:
		for j in range(height):
			row = []
			for i in range(width):
				live_neighbors = [colored_grid[j+a][i+b] for a in (-1,0,1) for b in (-1,0,1) if ((a is not 0 or b is not 0) and ((j+a) % height is j+a) and ((i+b) % width is i+b) and colored_grid[j+a][i+b])]
				neighbor_count = len(live_neighbors)
				if colored_grid[j][i]:
					if neighbor_count in rule[1]:
						row.append(colored_grid[j][i])
					else:
						row.append(None)
				else:
					if neighbor_count in rule[0]:
						hue = average_hue(live_neighbors)
						row.append(Hue(hue.value+uniform(-color_variation, color_variation)))
					else:
						row.append(None)
			next_grid.append(row)
		return next_grid
