from demo import add, mod, sub


def test_add():
    assert add(1, 2) == 3


def test_sub():
    assert sub(5, 3) == 2


def test_mod():
    assert mod(7, 3) == 1
    assert mod(6, 3) == 0
