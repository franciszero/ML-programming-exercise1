# coding=utf-8
from __future__ import print_function

import time
import pandas as pd
from scipy.sparse import lil_matrix
import matplotlib.pyplot as plt

import math
import sys


class Car:
    def __init__(self, year, mpg, speed):
        self.year = year
        self.mpg = mpg
        self.speed = speed
        self.owners = []

    def accelerate(self):
        self.speed += 30

    def brake(self):
        self.speed -= 60
        if self.speed < 0:
            self.speed = 0

    def __str__(self):
        return "car year {} mpg {} speed {}.".format(self.year, self.mpg, self.speed)


def func():
    car1 = Car(2016, 20, 80)
    print(car1)
    car1.accelerate()
    print(car1)

    car2 = Car(2013, 25, 60)
    print(car2)
    car2.brake()
    print(car2)


if __name__ == '__main__':
    func()
