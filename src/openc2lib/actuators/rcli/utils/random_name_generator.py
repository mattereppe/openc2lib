import random
import string
import time

words = ["Alpha", "Beta", "Gamma", "Delta", "Theta", "Sigma", "Omega", "Lambda", "Epsilon", "Zeta"]

def generate_unique_name():
    """Generate a unique name using a random word, number, and suffix."""
    random.seed(time.time_ns())  # Ensure randomness
    word = random.choice(words)  
    number = random.randint(1000, 9999)  
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))  # Extra uniqueness
    
    return f"{word}_{number}{suffix}"
