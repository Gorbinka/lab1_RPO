import sys
import os

# добавляем person1 в путь, чтобы импортировать utils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'person1')))

from utils import add

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -2) == -3

def test_add_zero():
    assert add(0, 5) == 5
