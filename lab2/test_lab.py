import pytest
from lab import Worker

# set up test class


def test_assert_error():
    with pytest.raises(ValueError) as exp:
        test_class = Worker()
        test_class.level = 123
        assert exp.value == ValueError
        del test_class

def test_default_values():
    test_class = Worker()
    assert test_class.bonus() == 3500
    del test_class

def test_set_values():
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

setters_data = [
    (0,1.0,7,ValueError()),
    (750000,0,17,ValueError()),
    (350000,2.5,1234567890,ValueError())
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