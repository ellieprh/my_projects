# -*- coding: utf-8 -*-
"""My_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lDIaqeTpakupCJIDccQ4Gh-WXZ4UOkZz
"""

class Rectangle():
    
  def __init__(self, length, width, height):
    self.length = length
    self.width = width
    self.height = height

  def square(self):
    area_square = self.length ** 2
    perimeter_square = self.length * 4
    return f'The perimeter is {perimeter_square}', f'The area is {area_square}'
    
  def rectangle(self):
    area_rectangle = self.length * self.width 
    perimeter_rectangle = (self.length * 2) + (self.width * 2)
    return f' The area is {area_rectangle}', f'The perimeter is {perimeter_rectangle}'

  def cube(self):
    volume_cube = self.length ** 3
    surface_area_cube = (self.length **2) * 6
    return f'The volume is {volume_cube}', f'The surface area is {surface_area_cube}' 

  def rect_prism(self):
    volume_rect_prism = self.length * self.height * self.width
    surface_area_rect_prism = 2 * (self.length * self.width + self.length * self.height + self.height * self.width)
    return f'The volume is {volume_rect_prism}', f'The surface area is {surface_area_rect_prism}'

  def parallelogram(self):
    area_parallelogram = self.length * self.height
    perimeter_parallelogram = (self.length * 2) + (self.width * 2)
    return f' The area is {area_parallelogram}' , f'The perimeter is {perimeter_parallelogram}'

  def rect_pryramid(self):
    volume_rect_pryramid = (self.length * self.height * self.width) / 3
    return f' The volume is {volume_rect_pryramid}'

class Triangle():  
  def __init__(self, height, base):
    self.height = height
    self.base = base
  
  def area_triangle(self):
    area_triangle = self.height * self.base * 0.5
    return f'the area is {area_t}'
  
  def trapezoid (self, base2, side1, side2):
    area_trapezoid = 0.5 * self.height * (self.base + base2 )
    perimeter_trapezoid = side1 + side2 + self.base + base2
    return f'The area is {area_trapezoid}' , f'The perimeter is {perimeter_trapezoid}'

import numpy as np
class Circle():
  def __init__(self, radius, height = 1): 
    self.height = height
    self.radius = radius
  
  def circle(self):
    area_circle = (self.radius ** 2) * np.pi
    circumfrence_circle = self.radius*2 * np.pi
    return f'The area is {area_circle}' , f'The circumfrence is {circumfrence_circle}'

  def right_circular_cylindar(self):
    volume_right_circular_cylindar = np.pi * self.radius**2 * self.height
    surface_area_right_circular_cylindar = 2 * np.pi * self.radius * self.height + 2* np.pi 
    return f'The volume is {volume_right_circular_cylindar}' , f'the surface area is {surface_area_right_circular_cylindar}'
  
  def sphere(self):
    volume_sphere = (4/3) * np.pi * (self.radius ** 3) 
    surface_area_sphere = 4 * np.pi * (self.radius ** 2)
    return f'The volume is {volume_sphere}', f'The surface area is {surface_area_sphere}'

f1 = Circle(1, 2)
print(f1.right_circular_cylindar())

