for fizzbuzz in range(100):
    if fizzbuzz % 4 == 0 and fizzbuzz % 7 == 0:
        print("FIZZBUZZ")
        continue
    elif fizzbuzz % 4 == 0:
        print("FIZZ")
        continue
    elif fizzbuzz % 7 == 0:
        print("BUZZ")
        continue
    print(fizzbuzz)
