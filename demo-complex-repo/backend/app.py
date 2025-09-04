import os, json

# Obvious secret (should be flagged by regex): Google API key
GOOGLE_API_KEY = "AIzaSyDUMMYDUMMYDUMMYDUMMYDUMMYDUMMY"

# Looks like a JWT (may or may not be real) – the LLM should decide
DUMMY_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.cGF5bG9hZA.1q2w3e4r5t6y7u8i9o0p"

# Not-so-obvious: base64 of "svc_user:SuperS3cret!"
BASIC_AUTH_B64 = "c3ZjX3VzZXI6U3VwZXJTM2NyZXQh"

# False positive bait: checksum / commit hash (should NOT be a secret)
LINUX_KERNEL_COMMIT = "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"

def main():
    print("backend up")
    print(json.dumps({"ok": True}))

if __name__ == "__main__":
    main()
