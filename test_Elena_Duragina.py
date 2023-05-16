from elena_duragina import counting


def test_counting_for_years_range_three_and_ten():
    data = [' , ,2, , , , 4, , , ,50',
            ' , ,1, , , , 7, , , ,100',
            ' , ,3, , , , 8, , , ,10',
            ' , ,1, , , , 9, , , ,100',
            ' , ,2, , , , 2, , , ,90',
            ' , ,3, , , , 15, , , ,20']
    assert counting(data, [3, 10]) == (200, 50, 10)


def test_counting_for_empty_class():
    data = [' , ,2, , , , 4, , , ,50',
            ' , , , , , , 7, , , ,100',
            ' , ,3, , , , 8, , , ,10',
            ' , ,1, , , , 9, , , ,100',
            ' , ,2, , , , 2, , , ,90',
            ' , ,3, , , , 15, , , ,20']
    assert counting(data, [3, 10]) == (100, 50, 10)


def test_counting_for_empty_price():
    data = [' , ,2, , , , 4, , , , ',
            ' , , , , , , 7, , , ,100',
            ' , ,3, , , , 8, , , ,10',
            ' , ,1, , , , 9, , , ,100',
            ' , ,2, , , , 2, , , ,90',
            ' , ,3, , , , 15, , , ,20']
    assert counting(data, [3, 10]) == (100, 0, 10)

