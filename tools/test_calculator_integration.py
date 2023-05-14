import pytest
from src.calculator import Calculator

def test_addition():
    calc = Calculator()
    assert calc.addition(2, 3) == 5
    assert calc.addition(0, 0) == 0
    assert calc.addition(-1, 1) == 0

def test_subtraction():
    calc = Calculator()
    assert calc.subtraction(2, 3) == -1
    assert calc.subtraction(0, 0) == 0
    assert calc.subtraction(-1, 1) == -2

def test_multiplication():
    calc = Calculator()
    assert calc.multiplication(2, 3) == 6
    assert calc.multiplication(0, 0) == 0
    assert calc.multiplication(-1, 1) == -1

def test_division():
    calc = Calculator()
    assert calc.division(6, 3) == 2
    # try:
    #     assert calc.division(1, 0) == "division by zero"
    # except ZeroDivisionError:
    #     assert True
    with pytest.raises(ZeroDivisionError): 
        calc.modulus(7, 0)
    assert calc.division(-1, 1) == -1


def test_modulus():
    calc = Calculator()
    assert calc.modulus(5, 2) == 1
    assert calc.modulus(7, 3) == 1
    assert calc.modulus(0, 10) == 0
    # try:
    #     assert calc.division(1, 0) == "onteger modulo by zero"
    # except ZeroDivisionError:
    #     assert True
    with pytest.raises(ZeroDivisionError): 
        calc.modulus(10, 0)

def test_exponentiation():
    calc = Calculator()
    assert calc.exponentiation(2, 3) == 8
    assert calc.exponentiation(0, 0) == 1
    assert calc.exponentiation(-1, 2) == 1

def test_floor_division():
    calc = Calculator()
    assert calc.floor_division(7, 3) == 2
    # try:
    #     assert calc.division(1, 0) == "integer division or modulo by zero"
    # except ZeroDivisionError:
    #     assert True
    with pytest.raises(ZeroDivisionError): 
        calc.modulus(8, 0)
    assert calc.floor_division(-1, 2) == -1
