import hashlib
import itertools
import string
import os

def hash_password(password, salt=None):
    if not salt:
        salt = os.urandom(16)
    pwd_salt = password.encode() + salt
    hashed = hashlib.sha256(pwd_salt).hexdigest()
    return hashed, salt

def brute_force_attack(target_hash, salt, max_length=3):
    chars = string.ascii_lowercase
    for length in range(1, max_length+1):
        for attempt in itertools.product(chars, repeat=length):
            attempt_pwd = ''.join(attempt)
            attempt_hash, _ = hash_password(attempt_pwd, salt)
            if attempt_hash == target_hash:
                return attempt_pwd
    return None

if __name__ == "__main__":
    print("🔐 Password Cracking Demonstration")
    print("---------------------------------\n")

    # Step 1: Enter a password (simulating what user sets)
    password = input("Enter a password to secure: ")

    # Step 2: Store hash (attacker only sees this)
    stored_hash, salt = hash_password(password)
    print("\n✅ Password has been securely hashed (attacker only sees the hash).")
    print("Stored Hash:", stored_hash)
    print("Salt:", salt.hex())

    # Step 3: Attacker attempts brute force
    print("\n--- Brute Force Attack ---")
    print("Trying weak passwords (a-z, up to 3 letters)...")

    cracked = brute_force_attack(stored_hash, salt, max_length=3)

    if cracked:
        print("💀 Password cracked successfully! ->", cracked)
    else:
        print("❌ Could not crack password (too strong).")

    print("\n📌 Demo complete: This shows how attackers guess passwords by brute force.")
