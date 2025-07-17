#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10"""
__version__ = "0.1.1"
__author__ = "Winter"
__dataCreate__ = "03-07-2025"

template = """
---Tabuada do 2---

{bloco:^20}

###################
"""

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros = list(range(1, 11))

# Iterable (percorriveis)

# para cada numero em numeros:
for n1 in numeros:
    print("{:-^20}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^20}".format(f"{n1} x {n2} = {resultado}"))

    print("#" * 20)
