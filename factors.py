#!/usr/bin/python3
import sys
import math

def factorize_number(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def main(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            n = int(line.strip())
            factors = factorize_number(n)
            p = factors[0]
            q = n // p
            print(f"{n}={p}*{q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
