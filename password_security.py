import bcrypt

# Step 1: Ask the user to enter a password
password = input("Enter a password to hash: ").encode('utf-8')

# Step 2: Generate a salt
salt = bcrypt.gensalt()

# Step 3: Hash the password with the salt
hashed_password = bcrypt.hashpw(password, salt)

print(f"\nYour hashed password is:\n{hashed_password.decode()}")

# Step 4: Ask the user to enter the password again for verification
verify = input("\nRe-enter the password to verify: ").encode('utf-8')

# Step 5: Check if the original and entered password match
if bcrypt.checkpw(verify, hashed_password):
    print("✅ Password verified successfully!")
else:
    print("❌ Password does not match.")
