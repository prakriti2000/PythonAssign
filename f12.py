def func_compute(n):
 return lambda x : x * n
result = func_compute(2)
print("Double the number of 11 =", result(11))
result = func_compute(3)
print("Triple the number of 11 =", result(11))
result = func_compute(4)
print("Quadruple the number of 11 =", result(11))
result = func_compute(5)
print("Quintuple the number 11 =", result(11))