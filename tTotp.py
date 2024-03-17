import pyotp

key="UtsavChatterjeeIsHere"


totp=pyotp.TOTP(key)

current_otp=totp.now()

print(current_otp)

res=totp.verify(current_otp)

print(res)