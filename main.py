#! /usr/bin/python
# Exercise No.   2
# File Name:     hw8Project2.py
# Programmer:    James Molin
# Date:          July 16, 2020
#
# Problem Statement: make a picture grayscale
#
#
# Overall Plan:
# 1. import the picture
# 2. calculate a way to turn the picture grayscale
# 3. print the result
#
#
# import the necessary python libraries

from graphics import *
import math

def main():

  flower = Image(Point(110, 83), "flower.gif")

  width = flower.getWidth()
  height = flower.getHeight()

  win = GraphWin("Grayscale", width, height)

  flower.draw(win)

  i = 0
  j = 0

  for i in range(0, width):

    for j in range(0, height):

      r, g, b = flower.getPixel(i, j)

      brightness = int(round(0.299*r + 0.587*g + 0.114*b))

      flower.setPixel(i, j, color_rgb(brightness, brightness, brightness))

      j = j + 1

    i = i + 1

  




  







main()