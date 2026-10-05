from dataclasses import dataclass
from enum import Enum

from src._shared.domain.exceptions import CurrencyNotFoundException

class Currency(Enum):
    BRL = ("BRL", "R$")

    def __init__(self, code: str, symbol: str):
        self.code = code
        self.symbol = symbol

    


@dataclass(frozen=True)
class CurrencyValueObject:
    currency: Currency

    def format(self, cents: int) -> str:
        signal = "-" if cents < 0 else ""
        value = abs(cents)

        return (
            f"{signal}"
            f"{self.currency.symbol} "
            f"{value // 100},{value % 100:02d}"
        )