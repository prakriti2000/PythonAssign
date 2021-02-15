from functools import reduce

fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
                              range(n - 2), [0, 1])

print("Fibonacci series upto 2:")
print(fib_series(2))
print("\nFibonacci series upto 3:")
print(fib_series(3))
print("\nFibonacci series upto 6:")
print(fib_series(6))
print("\nFibonacci series upto `10:")
print(fib_series(10))