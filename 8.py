def remove_char(str, n):
    first_part = str[:n]
    last_part = str[n + 1:]
    return first_part + last_part


print(remove_char('Prakriti', 0))
print(remove_char('prakriti', 3))
print(remove_char('Prakriti', 5))