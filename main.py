"""Compare delivered supplier prices, including freight and minimum orders."""
from decimal import Decimal as D


def landed_cost(quantity, unit_price, freight, minimum_order=0):
    values = [D(str(v)) for v in (quantity, unit_price, freight, minimum_order)]
    if any(not v.is_finite() or v < 0 for v in values):
        raise ValueError('Finite non-negative inputs required')
    quantity, unit_price, freight, minimum_order = values
    return max(quantity, minimum_order) * unit_price + freight


if __name__ == '__main__':
    quotes = {'North': landed_cost(80, '12.50', 90, 100),
              'South': landed_cost(80, '14', 20)}
    print(sorted(quotes.items(), key=lambda pair: pair[1]))
