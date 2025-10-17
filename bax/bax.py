from decimal import Decimal

from bar import big_one
from foo import embiggen


def big_two() -> Decimal:
    return embiggen(Decimal(1))


def boom():
    return big_one()
