import pyotp

key="UtsavChatterjeeIsHere"


totp=pyotp.TOTP(key)

print(totp.verify("879885"))