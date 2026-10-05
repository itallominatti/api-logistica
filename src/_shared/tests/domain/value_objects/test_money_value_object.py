import pytest

from src._shared.domain.exceptions import CurrencyNotFoundException
from src._shared.domain.value_objects.money_value_object import MoneyValueObject
from src._shared.domain.value_objects.currency_value_object import CurrencyValueObject, Currency

@pytest.fixture
def money_with_1000_cents() -> MoneyValueObject:
    return MoneyValueObject(money=1000,currency=CurrencyValueObject(currency=Currency.BRL))

@pytest.fixture
def money_with_2000_cents() -> MoneyValueObject:
    return MoneyValueObject(money=2000,currency=CurrencyValueObject(currency=Currency.BRL))

@pytest.fixture
def money_with_negative_cents() -> MoneyValueObject:
    return MoneyValueObject(money=-1000,currency=CurrencyValueObject(currency=Currency.BRL))

@pytest.fixture
def money_in_str() -> str:
    return "10,00"

@pytest.fixture
def money_in_str_without_correct_format() -> str:
    return "10.00"

def test_create_instance_money_value_object_with_integer_value():
    v = MoneyValueObject(money=1000,currency=CurrencyValueObject(currency=Currency.BRL))
    assert isinstance(v, MoneyValueObject)
    assert 1000 == v.money


def test_format_money_integer_to_brl_money_string(money_with_2000_cents):
    v = money_with_2000_cents
    v_formatted = v.format()
    assert "R$ 20,00" == v_formatted

def test_sum_multiple_values(money_with_1000_cents, money_with_2000_cents):
    v_list = [money_with_2000_cents, money_with_1000_cents]
    v_total = MoneyValueObject.total(v_list)
    assert isinstance(v_total, MoneyValueObject)
    assert v_total.format() == "R$ 30,00"
    assert v_total.money == 3000

def test_create_money_with_a_unfamiliar_currency():
    with pytest.raises(CurrencyNotFoundException):
        MoneyValueObject(
            money=1000,
            currency="ABUA"
        )
