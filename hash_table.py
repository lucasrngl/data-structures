# Hash Table implementation

# Hash Table complexity: O(1) - The complexity for Hash Table will always be constant - so O(1)

# Create a table with size 10
table = [
    [],
] * 10


# Check if number is prime
def check_prime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n // 2):
        if n % i == 0:
            return 0

    return 1


# Get a prime number to use in hash function
def get_prime(n):
    if n % 2 == 0:
        n = n + 1

    while not check_prime(n):
        n += 2

    return n


# Hashing the key
def hash(key):
    capacity = get_prime(10)
    return key % capacity


# Insert data
def insert(key, data):
    index = hash(key)
    table[index] = [key, data]


# Remove data
def remove(key):
    index = hash(key)
    table[index] = []


insert(123, "apple")
insert(432, "mango")
insert(213, "banana")
insert(654, "guava")

print(table)

remove(123)

print(table)