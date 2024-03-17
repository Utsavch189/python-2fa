import pyotp

"""
A helper function is provided to generate a 32-character base32 secret, compatible with Google Authenticator and other OTP apps:

pyotp.random_base32()
Some applications want the secret key to be formatted as a hex-encoded string:

pyotp.random_hex()  # returns a 40-character hex-encoded secret
"""

key="UtsavChatterjeeIsHere"

"""
Suppose I have 2 users,

ID   Name
---------
1    Utsav
2    Sourav
"""

hotp=pyotp.HOTP(key)

utsav_otp=hotp.at(1) # --> 052624
sourav_otp=hotp.at(2) # --> 773925

print(utsav_otp)
print(sourav_otp)


# OTP verified for user utsav
res1=hotp.verify(utsav_otp, 1) # => True
res2=hotp.verify('316439', 1) # => False

print(res1,' ',res2)