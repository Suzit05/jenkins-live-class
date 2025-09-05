import pytest
from app.calculator import subtract,add,mutliply,divide

def test_add():
    assert add(2,3) == 5

def test_subtract():
    assert subtract(7,3) == 4

def test_multiply():
    assert mutliply(3,9) == 27
    
def test_divide():
    assert divide(14,7) == 2