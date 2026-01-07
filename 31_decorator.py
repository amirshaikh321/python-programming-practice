def simple_decorator(original_function):
    def wrapper():
        print("--- Start of Decoration ---")
        original_function()  # This runs the actual function
        print("--- End of Decoration ---")
    return wrapper
@simple_decorator # this is decorator
def say_hello():
    print("Hello! I am the main function.")
    
say_hello()