from demo import add, mul, sub


def test_add():
    assert add(1, 2) == 3


def test_sub():
    assert sub(5, 3) == 2


def test_mul():
    assert mul(4, 3) == 12
