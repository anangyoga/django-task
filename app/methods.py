# methods is a place for reusable login
import time

def do_something():
    print("Starting to do something")
    time.sleep(5)
    print("After sleep 5 secs")
    time.sleep(5)
    print("Something is done")

# Note: make sure redis is running. and then `pip install huey redis`