"""
    Dinheiro em centavos (int)
"""
from dataclasses import dataclass

Money = int

def is_positive(m: Money) -> bool:
    return m > 0

def format_brl(m: Money) -> str:
    v = int(m)
    sign = ""
    if v < 0:
        sign = "-"
        v = -v
    return f"{sign} R$ {v // 100}, {v % 100:02d}"

def total(values) -> Money:
    return sum(int(v) for v in values)


class MoneyValueObject:
    money: int
    currency: str = "BRL"

    def _is_positive() -> bool:
        return self.money