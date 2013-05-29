#!/usr/bin/env python
# encoding: utf-8
#
# Die Fibonacci Folge ist rekursiv definiert als:
#      f(n) = f(n-1) + f(n-2)
#
# Mit f0=0 und f1=1
#
# Was passt an folgender Funktion nicht?


def fibonacci(f0=0, f1=1, max_nums=10):
    'Generiere eine Liste mit Fibonacci-Nummern mit max_nums Zahlen.'
    results = [f1, f0]

    for _ in range(max_nums):
        f1, f0 = f1 + f0, f1
        results.append(f1)
    return results
