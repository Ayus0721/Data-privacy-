import hashlib
def sha256_hash(password):
    hash_object= hashlib.sha256(password.encode())
    return hash_object.hexdigest()
password=input("Enter password:")
hashed_password = sha256_hash(password)
print("SHA-256 Hash:", hashed_password)
