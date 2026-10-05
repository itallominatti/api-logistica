from uuid import UUID
from dataclasses import dataclass
from typing import Set

@dataclass(frozen=True, slots=True)
class Order:
    id: UUID
    client_id: UUID
    quantity: int
    item: Set[UUID]