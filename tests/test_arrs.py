from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3], 1) == 2
    assert arrs.get([1, 2, 3], 3, default="Not found") == "Not found"
    assert arrs.get([1, 2, 3], -1, default="Not found") == "Not found"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, 5) == [3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], 1, -2) == [2, 3]
    assert arrs.my_slice([], 1, 4) == []
    assert arrs.my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
