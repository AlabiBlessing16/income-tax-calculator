# ...existing code...
from typing import Dict, List, Tuple
import sys

BRACKETS: Dict[int, List[Tuple[float, float]]] = {
    0: [  # Single
        (8350, 0.10),
        (33950, 0.15),
        (82250, 0.25),
        (171550, 0.28),
        (372950, 0.33),
        (float("inf"), 0.35)
    ],
    1: [  # Married filing jointly
        (16700, 0.10),
        (67900, 0.15),
        (137050, 0.25),
        (208850, 0.28),
        (372950, 0.33),
        (float("inf"), 0.35)
    ],
    2: [  # Married filing separately
        (8350, 0.10),
        (33950, 0.15),
        (68525, 0.25),
        (104425, 0.28),
        (186475, 0.33),
        (float("inf"), 0.35)
    ],
    3: [  # Head of household
        (11950, 0.10),
        (45500, 0.15),
        (117450, 0.25),
        (190200, 0.28),
        (372950, 0.33),
        (float("inf"), 0.35)
    ]
}

def compute_tax(status: int, income: float) -> float:
    """Compute 2009 federal tax for given filing status and taxable income.
    Raises ValueError for invalid status or negative income.
    """
    if status not in BRACKETS:
        raise ValueError("Invalid filing status (must be 0-3).")
    if income < 0:
        raise ValueError("Income must be non-negative.")

    tax = 0.0
    previous_limit = 0.0

    for limit, rate in BRACKETS[status]:
        if income > limit:
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax += (income - previous_limit) * rate
            break

    return round(tax, 2)

if __name__ == "__main__":
    print("Filing Status:")
    print("0 - Single")
    print("1 - Married Filing Jointly or Qualified Widow(er)")
    print("2 - Married Filing Separately")
    print("3 - Head of Household")

    try:
        status = int(input("Enter filing status (0-3): "))
    except ValueError:
        print("Invalid filing status (must be integer 0-3).")
        sys.exit(1)

    if status not in (0, 1, 2, 3):
        print("Invalid filing status (must be 0, 1, 2, or 3).")
        sys.exit(1)

    try:
        income = float(input("Enter taxable income: "))
    except ValueError:
        print("Invalid income (must be a number).")
        sys.exit(1)

    if income < 0:
        print("Income must be non-negative.")
        sys.exit(1)

    tax = compute_tax(status, income)
    print(f"Total tax is: ${tax:.2f}")
# ...existing code...
