from dataclasses import dataclass
from decimal import Decimal

from src._shared.domain.exceptions import CurrencyNotFoundException
from src._shared.domain.value_objects.currency_value_object import CurrencyValueObject

@dataclass(frozen=True)
class MoneyValueObject:
    money: int
    currency: CurrencyValueObject

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        if not isinstance(self.currency, CurrencyValueObject):
            raise CurrencyNotFoundException(
                f"Moeda inválida: {self.currency}"  
            )

    @property
    def is_positive(self) -> bool:
        return self.money > 0

    def format(self) -> str:
        return self.currency.format(self.money)

    @staticmethod
    def to_cents(value: str) -> int:
        return int(
            Decimal(value.replace(",", ".")) * 100
        )

    @staticmethod
    def total(values: list["MoneyValueObject"]) -> "MoneyValueObject":
        if not values:
            raise ValueError("Lista vazia")

        currency = values[0].currency

        if any(v.currency != currency for v in values):
            raise CurrencyNotFoundException()

        return MoneyValueObject(
            money=sum(v.money for v in values),
            currency=currency
        )