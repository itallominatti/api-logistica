import pytest

from src._shared.domain.value_objects.money_value_object import MoneyValueObject

@pytest.fixture
def money_with_1000_cents() -> MoneyValueObject:
    return MoneyValueObject(1000)

@pytest.fixture
def money_with_2000_cents() -> MoneyValueObject:
    return MoneyValueObject(2000)

@pytest.fixture
def money_with_negative_cents() -> MoneyValueObject:
    return MoneyValueObject(-1000)

@pytest.fixture
def money_in_str() -> str:
    return "10,00"

@pytest.fixture
def money_in_str_without_correct_format() -> str:
    return "10.00"

def test_create_instance_money_value_object_with_integer_value():
    v = MoneyValueObject(1000)
    assert isinstance(v, MoneyValueObject)
    assert 1000 == v.money

def test_format_money_integer_to_brl_money_string(money_with_2000_cents):
    v = money_with_2000_cents
    value_formatted = v.format_brl()
    assert "R$ 20,00" == value_formatted

def test_sum_multiple_values(money_with_1000_cents, money_with_2000_cents):
    v_list = [money_with_1000_cents,money_with_2000_cents]
    new_v = MoneyValueObject.total(v_list)
    print(new_v)

def test_sum_multiple_values_formatted_in_brl_string(money_with_1000_cents, money_with_2000_cents):
    v_list = [money_with_1000_cents,money_with_2000_cents]
    new_v = MoneyValueObject.total(v_list)
    print(new_v)
