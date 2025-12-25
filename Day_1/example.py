# example.py
def greet(name):
    return f"Hello, {name}!"

print("This always runs")

if __name__ == "__main__":
    print("This only runs when script is executed directly")
    print(greet("World"))