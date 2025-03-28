# Problem Statement:
# You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

# This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.

# For example, using a hash function called SHA256(...) something as simple as

# hello

# can be hashed into a much more complex

# 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

# Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's stored password hash in stored_logins is the same as the hash of password_to_check.

# (Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it works, just know that hash_password(...) returns the hash for the password!)


# Hashing:
# Hashing ek security technique hai jo kisi bhi text ya data ko ek unique fixed-length code me convert karti hai


# Passwords ko secure karny ke liye (sha256) hashing-function ko import kiya
from hashlib import sha256


def hash_password(password):
    return sha256(password.encode()).hexdigest() # it's a hashing function code line to generate hashing code 

# Store hashed passwords
stored_logins = {
    "example@gmail.com": hash_password("password"),
    "code_in_placer@cip.org": hash_password("Karel"),
    "student@stanford.edu": hash_password("123!456?789")
}

# Function to check login
def login(email, stored_logins, password_to_check):
    if email not in stored_logins:
        return False  # Email not found
    return stored_logins[email] == hash_password(password_to_check)  # Compare hashes

# Test cases
print(login("example@gmail.com", stored_logins, "word"))            # False
print(login("example@gmail.com", stored_logins, "password"))        # True 
print(login("code_in_placer@cip.org", stored_logins, "Karel"))      # True
print(login("code_in_placer@cip.org", stored_logins, "karel"))      # False
print(login("student@stanford.edu", stored_logins, "password"))     # False
print(login("student@stanford.edu", stored_logins, "123!456?789"))  # True


# output:

# False
# True 
# True 
# False
# False
# True 




