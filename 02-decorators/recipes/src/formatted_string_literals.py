#!/usr/bin/env python
import decimal

def get_name():
    return "John"

if __name__ == "__main__":
    # Formatted String Literals - simple usage
    name = "Joshua"
    age = 23
    print(f"My name is {name} and my age is {age}")

    # Functions formatting
    print(f"My name is {get_name()}")

    # Nested formatting
    value = decimal.Decimal("12.34567")
    width = 10
    precision = 4
    print(f"Value: {value:{width}.{precision}}")
