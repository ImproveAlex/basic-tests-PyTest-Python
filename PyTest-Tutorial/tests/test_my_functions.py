import pytest
import sys
import os
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from source import my_functions

def test_add():
    result = my_functions.add(1, 4)
    assert result == 5

def test_add_strings():
    result = my_functions.add("i like ", "burgers")
    assert result == "i like burgers"

def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2

def test_devide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)

@pytest.mark.slow

def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10, 5)
    assert result == 2
    
@pytest.mark.skip(reason="This feature is currently broken")

def test_add_another():
    assert my_functions.add(1,2) == 3

@pytest.mark.xfail(reason="We know we can't divide by zero")

def test_devide_zero_broken():
    my_functions.divide(2, 0) 