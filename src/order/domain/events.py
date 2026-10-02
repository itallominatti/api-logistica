from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID

@dataclass(frozen=True, kw_only=True)
class DomainEvent:
    happened_in: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

@dataclass(frozen=True, kw_only=True)
class OrderConfirmed(DomainEvent):
    order_id: UUID
    client_id: UUID
    total: "Dinheiro"

@dataclass(frozen=True, kw_only=True)
class OrderCanceled(DomainEvent):
    order_id: UUID
    reason: str