from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result1 = cal.add(a, b)

        # assert
        expected = 5555
        assert result1 == expected



    def test_subtract(self): 
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result2 = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result2 == expected



    def test_multiply(self): 
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result3 = cal.multiply(a, b)

        # assert
        expected = 5332114
        assert result3 == expected     


    def test_divide(self): 
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result4 = cal.divide(a, b)

        # assert
        expected = 3.5016207455429496
        assert result4 == expected

    
    def test_divide_zero(self): 
        # arrange
        a = 4321
        b = 0
        cal = Calculator()

        # act and assert
        with pytest.raises(ZeroDivisionError):
            cal.divide(a,b)

            
