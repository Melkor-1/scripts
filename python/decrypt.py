#!/usr/bin/env python3

import functools
import os
import sys
from pathlib import Path
from typing import Iterable

import typer
from cryptography.fernet import Fernet


def decrypt_file(path: str, key: str, file: str) -> None:
    with open(os.path.join(path, file), "rb") as target:
        decrypted_contents = Fernet(key).decrypt(target.read())

    with open(os.path.join(path, file), "wb") as target:
        target.write(decrypted_contents)


def main(path: Path, key_file: str) -> None:
    modified_decrypt_file = functools.partial(decrypt_file, path, key_file)
    list(
        map(
            modified_decrypt_file,
            (f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))),
        )
    )


if __name__ == "__main__":
    typer.run(main)
