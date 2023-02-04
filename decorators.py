def announce(f):
    def wrapper():
        print("About to run de function...")
        f()
        print("Done with the function.")
    return wrapper
@announce
def hello():
    print("hola gil")

hello()