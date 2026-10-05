from dataclasses import dataclass
from uuid import UUID

from src._shared.domain.value_objects.money_value_object import MoneyValueObject

@dataclass(frozen=True, slots=True)
class OrderItemValueObject:
    id: UUID
    quantity: int
    unity_price: MoneyValueObject