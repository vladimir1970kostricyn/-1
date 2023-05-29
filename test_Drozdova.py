from main_new_Kr_Drozdova import *


def test_result1():
    data = ["0,0,1,0,0,male", "0,0,1,0,0,female"]
    assert result1(data) == (1, 1)


def test_result2():
    data = ["0,0,2,0,0,male", "0,0,2,0,0,female"]
    assert result2(data) == (1, 1)




def test_result3():
    data = ["0,0,3,0,0,male", "0,0,3,0,0,female"]
    assert result3(data) == (1, 1)



