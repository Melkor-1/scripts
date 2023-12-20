#!/usr/bin/env python3

import functools
import os
import sys
from pathlib import Path
from typing import Iterable

import typer
from cryptography.fernet import Fernet

KEY_FILE_PATH = "key.txt"


def save_key() -> str:
    key = Fernet.generate_key()

    with open(KEY_FILE_PATH, "wb") as file:
        file.write(key)

    return key


def encrypt_file(path: str, key: str, file: str) -> None:
    with open(os.path.join(path, file), "rb") as target:
        encrypted_contents = Fernet(key).encrypt(target.read())

    with open(os.path.join(path, file), "wb") as target:
        target.write(encrypted_contents)


def main(path: Path) -> None:
    key = save_key()
    modified_encrypt_file = functools.partial(encrypt_file, path, key)
    list(
        map(
            modified_encrypt_file,
            (f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))),
        )
    )


if __name__ == "__main__":
    typer.run(main)
