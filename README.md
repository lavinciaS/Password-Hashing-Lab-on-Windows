# 🔐 Password Hashing and Verification with bcrypt

This is a beginner-friendly lab to learn how to securely hash and verify passwords using the `bcrypt` library in Python. The goal is to simulate part of an authentication system by securely storing and checking user passwords.

---

## 📌 What You’ll Learn

- How to hash passwords with bcrypt  
- How to verify a password against a hash  
- Basic structure for secure Python scripts  
- Command-line usage of Python for cybersecurity

---

## 🛠️ Technologies Used

- Python 3.x  
- bcrypt (Python package)  
- Windows Terminal / PowerShell  
- Optional: Kali Linux VM

---

## 🧪 Lab Instructions

## ✔️ Step 1: Install Python

- Go to https://www.python.org/downloads/  
- Download and install Python 3.x  
- During installation, check this box:

✅ Add Python to PATH
- Click **Install Now**

---

### ✔️ Step 2: Open Terminal and Create a Project Folder

Open Command Prompt or PowerShell and run:
<pre>
mkdir python-labs
cd python-labs
</pre>
---
### ✔️ Step 3: Create a Virtual Environment
- In the same terminal:
<pre>
python -m venv venv
</pre>
- Then activate it:
<pre>
venv\Scripts\activate
(venv) C:\Users\YourName\python-labs>
</pre>
---
### ✔️ Step 4: Install bcrypt
<pre>
pip install bcrypt
</pre>
---
### ✅ Step 5: Create Your Python Script
Create your script file in the terminal:
<pre>
notepad password_security.py
</pre>

### Paste the following code inside password_security.py, then save and close it:
<pre>
import bcrypt

# Ask the user to enter a password
password = input("Enter your password: ").encode('utf-8')

# Generate salt and hash the password
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)

print(f"🔒 Hashed password: {hashed_password.decode()}")

# Ask the user to re-enter the password
password_check = input("Re-enter your password for verification: ").encode('utf-8')

# Verify the password
if bcrypt.checkpw(password_check, hashed_password):
    print("✅ Password is correct!")
else:
    print("❌ Password is incorrect.")
</pre>

---
### ✅ Step 6: Run Your Script
In the terminal:
<pre>
python password_security.py
</pre>
---
## You will:

- Enter a password
- See the hashed output
- Re-enter the password for verification
- Get a success or failure message
---
### 👩🏽‍💻 Author
Lavincia S
Cybersecurity Student | Secure Coding Enthusiast
