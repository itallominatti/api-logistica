"""
    Dinheiro em centavos (int)
"""
from dataclasses import dataclass

@dataclass
class MoneyValueObject:
    money: int
    currency: str = "BRL"

    def _is_positive(self) -> bool:
        return self.money

    def format_brl(self) -> str:
        v = int(self.money)
        sign = ""
        if v < 0:
            sign = "-"
            v = -v
        return f"{sign}R$ {v // 100},{v % 100:02d}"

    @staticmethod
    def format_to_cents(value: str) -> int:
        clean = value.replace(",", ".")
        cents = int(float(clean) * 100)
        return cents

    @staticmethod
    def total(values: list["MoneyValueObject"]) -> int:
        total = 0
        for v in values:
            total += v.money
        return total
