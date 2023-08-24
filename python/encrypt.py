#!/usr/bin/env python3

import os
import sys
from cryptography.fernet import Fernet 

if len(sys.argv) < 2:
    print("Usage: <program name> <directory path>.");
    quit();

# Add all the files in the directory to the list.
path = sys.argv[1]
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

# Generate a symmetric encryption key. 
key = Fernet.generate_key()

# Save the key to a file.
with open("key.txt", "wb") as file:
    file.write(key)

# Encrypt the contents of each file in the list. 
for file in files:
    with open(os.path.join(path, file), "rb") as target:
        contents = target.read()

    encrypted_contents = Fernet(key).encrypt(contents)
    
    with open(os.path.join(path, file), "wb") as target:
        target.write(encrypted_contents)

print ("All the files in the directory have been encrypted.\n")
