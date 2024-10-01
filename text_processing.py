import os
import random

def get_random_text(folder_path):
    texts = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    chosen_file = os.path.join(folder_path, random.choice(texts))
    with open(chosen_file, 'r') as file:
        content = file.read()
    return content
