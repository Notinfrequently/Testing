import pytest
from lab import Worker

def test_default_values():
    """Test bonus calculation with default values"""
    test_class = Worker()
    assert test_class.bonus() == 3500
    del test_class

def test_set_values():
    """Test setters for values"""
    test_class = Worker()
    test_class.payment = 100000
    test_class.per_rew = 4.0
    test_class.level = 12
    assert test_class.bonus() == float(30000)
    del test_class

fine_data = [
    (70000,1.0,7,3500),
    (750000,5.0,17,450000),
    (350000,2.5,10,52500)
]

# equvilance classes
"""
L - most left accepted value
R - most right accepted value
1. [-inf, L]
2. [L, R]
3. [R, +inf]
4. Any type that differs from accepted type in setter
"""

setters_data = [
    (-1, 2.5, 5, ValueError()),
    (800000, 2.5, 10, ValueError()),
    (75000.0, 2.5, 10, ValueError()),

    (100000, -2.5, 10, ValueError()),
    (100000, 8.0, 10, ValueError()),
    (100000, 5, 10, ValueError()),

    (100000, 2.5, -5, ValueError()),
    (100000, 2.5, 20, ValueError()),
    (100000, 2.5, "string", ValueError())
]

@pytest.mark.parametrize("pay, pr, lvl, bonus", fine_data)
def test_correct_bonus_calculation(pay, pr, lvl, bonus):
    test_class = Worker()
    test_class.payment = pay
    test_class.per_rew = pr
    test_class.level = lvl
    assert test_class.bonus() == bonus
    del test_class

@pytest.mark.parametrize("pay, pr, lvl, bonus", setters_data)
def test_setters_methods(pay, pr, lvl, bonus):
    with pytest.raises(ValueError) as exp:
        test_class = Worker()
        test_class.payment = pay
        test_class.per_rew = pr
        test_class.level = lvl
    assert str(exp.value) == str(bonus)
    del test_class