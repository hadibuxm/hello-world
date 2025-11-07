#!/usr/bin/env python3

"""Simple command-line calculator supporting basic arithmetic."""

from typing import Callable, Dict


def calculate(first: float, second: float, operator: str) -> float:
    """Compute the result of applying `operator` to the operands."""
    operations: Dict[str, Callable[[float, float], float]] = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    if operator not in operations:
        raise ValueError(f"Unsupported operator: {operator}")

    if operator == "/" and second == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return operations[operator](first, second)


def main() -> None:
    print("Simple Calculator")
    print("Supported operations: +, -, *, /")

    try:
        first = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ").strip()
        second = float(input("Enter the second number: "))
        result = calculate(first, second, operator)
    except ValueError as exc:
        print(f"Input error: {exc}")
        return
    except ZeroDivisionError as exc:
        print(f"Math error: {exc}")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
