from dataclasses import dataclass

from src._shared.domain.value_objects.money_value_object import Money

@dataclass(frozen=True, slots=True)
class OrderItemValueObject:
    sku: Sku
    quantity: int
    unity_price: Money