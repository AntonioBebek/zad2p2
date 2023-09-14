def generate_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def generate_odd_numbers(n):
    for i in range(n):
        if i % 2 != 0:
            yield i

n = int(input("Unesite broj: "))

print("Parni brojevi:")
for even_num in generate_numbers(n):
    print(even_num)

print("Neparni brojevi:")
for odd_num in generate_odd_numbers(n):
    print(odd_num)
