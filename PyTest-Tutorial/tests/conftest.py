import pytest
import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from source import shapes

@pytest.fixture

def my_rectangle():
    return shapes.Rectangle(10,20)

@pytest.fixture

def weird_rectangle():
    return shapes.Rectangle(5, 6)