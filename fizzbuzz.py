for fizzbuzz in range(30):
    if fizzbuzz % 3 == 0 and fizzbuzz % 6 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 6 == 0:
        print("buzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    print(fizzbuzz)

