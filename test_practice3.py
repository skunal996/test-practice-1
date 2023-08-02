import pytest

class Test_Arithmatic_03:

    # @pytest.mark.skip
    def test_subtraction(self):
        a = 3
        b = 7
        sub = a - b
        print("Subtraction of a and b is :" + str(sub))
        if sub == -4:
            assert True
        else:
            assert False

    def test_multiplication(self):
        a = 3
        b = 7
        mul = a * b
        print("Multiplication of a and b is :" + str(mul))
        if mul == 21:
            assert True
        else:
            assert False

    def test_division(self):
        a = 35
        b = 7
        div = a / b
        print("Division of a and b is :" + str(div))
        if div == 5:
            assert True
        else:
            assert False
