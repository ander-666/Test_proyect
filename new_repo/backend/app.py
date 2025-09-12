import base64
import os

BASIC_AUTH_B64 = "c3ZjX3VzZXI6U3VwM3JTM2NyZXQh"

JWT_HEADER = "eyJhbGciOiJIUzI1NiJ9"


EMPTY_TREE_SHA1 = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"

def main():
    creds = base64.b64decode(BASIC_AUTH_B64).decode()
    print("ready", creds.split(":")[0])
