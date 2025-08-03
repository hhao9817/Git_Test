def say_hello():
    print("Hello, World!")

def say_goodbye():
    print("Goodbye, World!")

if __name__ == "__main__":
    say_hello()
    say_goodbye()
    print("This script is running directly.")
else:
    print("This script is being imported.")
    print("This script is not running directly.")
# This script is designed to be run directly or imported as a module.