import pytest
import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from source import shapes

def test_area(my_rectangle):
    assert my_rectangle.area() == 10*20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimiter() == (10 * 2) + (20 * 2)

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle