#!/usr/bin/env python3

import os
import sys
from cryptography.fernet import Fernet 

if len(sys.argv) < 3:
    print("Usage: <program name> <directory path> <encryption key>.");
    quit();

# Add all the files in the directory to the list.
path = sys.argv[1]
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
key = sys.argv[2]

# Decrypt the contents of each file in the list.
for file in files:
    with open(os.path.join(path, file), "rb") as target:
        contents = target.read()

    decrypted_contents = Fernet(key).decrypt(contents)
    
    with open(os.path.join(path, file), "wb") as target:
        target.write(decrypted_contents)

print ("All the files in the directory have been decrypted.\n")
