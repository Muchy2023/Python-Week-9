   
def greet(name, greeting ="Hello"):
    print("Bob, 'Good morning'")
    
    def greet(name, greeting="Hello"):
     print(f"{greeting}, {name}")

greet("Alice")
greet("Bob", "Good morning")

def add(a, b):
    return a + b

results = add(2, 5)
print(results)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Example call
