import os

def generate_random_key(length=16):
    return os.urandom(length)
