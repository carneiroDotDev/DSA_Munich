def addAsterisks(func):
    def wrapper(str):
        print("**********")
        result = func(str)
        print("**********")
        return f"**{str}**", result
    return wrapper

@addAsterisks
def sayHello(name):
    return f"Hello, {name}!"
@addAsterisks
def sayGoodbye(name):
    return f"Goodbye, {name}!"

#if __name__ == "__main__":
#    print(sayHello("John"))
#    print(sayGoodbye("John"))
# Output:
# **********
# **********
# ('**John**', 'Hello, John!')
# **********
# **********
# ('**John**', 'Goodbye, John!')
# This code demonstrates the decorator pattern in Python using functions.
# The `addAsterisks` function is a decorator that adds asterisks around the string passed to the decorated function.
# The `sayHello` and `sayGoodbye` functions are decorated with `addAsterisks`, which modifies their behavior.
# When the decorated functions are called, the decorator adds asterisks around the name and prints the result.
# The output shows the decorated functions' behavior, including the asterisks added by the decorator.
# The output also includes the original return values of the decorated functions.
# The decorator pattern allows for modifying the behavior of functions without changing their original implementation.
# This pattern is useful for adding functionality to existing functions in a clean and reusable way.

def makeDBcall(func):
    def wrapper(*args, **kwargs):
        print("Making DB call...")
        #make your DB call here
        # For example:
        # db = Database()
        # db.connect()
        # db.insert(args[0])
        # db.close()
        # Simulating a DB call with a print statement
        print(f"DB call with arguments: {args}, {kwargs}")
        # Simulating a delay for the DB call
        import time
        time.sleep(1)
        # Simulating a successful DB call
        # db.commit()
        # db.close()
        print("DB call complete.")
        return func(*args, **kwargs)
    return wrapper

@makeDBcall
def likePost(post):
    print(f"Change empty heart emoticon to filled heart emoticon")
    return f"Blog post '{post}' liked successfully!"

if __name__ == "__main__":
    print(likePost("Learning Go Programming language"))
# Output:
# Making DB call...
# DB call with arguments: ('Sample Data',), {}
# DB call complete.
# Saving data: Sample Data
# Data 'Sample Data' saved successfully!

