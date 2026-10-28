from demo import add, div, sub


def test_add():
    assert add(1, 2) == 3


def test_sub():
    assert sub(5, 3) == 2


def test_div():
    assert div(8, 2) == 4
