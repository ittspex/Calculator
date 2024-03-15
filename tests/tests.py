import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self,1, 1) == 2

    def test_adding_subtraction(self):
        assert self.calc.subtraction(self,4,1) == 3

    def test_adding_multiply(self):
        assert self.calc.multiply(self,4,4) == 16

    def test_adding_division_(self):
        assert self.calc.division(self,15,5) == 3


    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,1 , 0)

    def teardown(self):
        print('Выполнение метода Teardown')


