import pyotp
import qrcode

key="UtsavChatterjeeIsHere"


totp=pyotp.TOTP(key)

uri=totp.provisioning_uri(
    name='utsav',
    issuer_name="MyApp"
)

qr=qrcode.make(uri)
print(type(qr))
qr.save("qr.png")