from uuid import UUID
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Order:
    id: UUID
    client_id: UUID
    ints: list