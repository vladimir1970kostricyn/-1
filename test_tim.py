from main_tim import *


def test1():
    data = ['0,1,0,kirill,0,male,"6"', '0,1,0,kirill,0,male,"6"', '0,1,0,kirill,0,male,"6"', '0,1,0,kirill,0,male,"6"',
            '0,1,0,kirill,0,male,"6"']
    assert result(data) == ['kirill', 'kirill', 'kirill', 'kirill', 'kirill']


def test2():
    data = ['0,1,0,kirill,0,male,"6"', '0,1,0,kirill,0,male,"6"', '0,1,0,kirill,0,male,"6"', '0,1,0,kirill,0,male,"6"',
            '0,1,0,kirill,0,male,"6"']
    assert result2(data) == ['male', 'male', 'male', 'male', 'male']


def test3():
    data = ['0,1,0,kirill,0,male,"6"', '0,1,0,kirill,0,male,"6"', '0,1,0,kirill,0,male,"6"', '0,1,0,kirill,0,male,"6"',
            '0,1,0,kirill,0,male,"6"']
    assert result3(data) == ['"6"', '"6"', '"6"', '"6"', '"6"']



