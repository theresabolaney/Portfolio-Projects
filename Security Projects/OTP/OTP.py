########################################################################################
# Program: OTP.py
# Author: Theresa Bolaney
# Date: 11/17/2021
# Description: The OTP.py program will create a QR png file that can be used to create
#   an account with Google Authenticator. The program can also create an OTP using
#   the TOTP algorithm referenced in RFC 6238. For full instructions, check the README.
########################################################################################

import qrcode
import time
import math
import hashlib
import hmac
import base64
import sys

# Generate a QR code that will set up an account with Google Authenticator
# Note that this uses the example provided by Google in its URI page.
# Source: https://github.com/google/google-authenticator/wiki/Key-Uri-Format
def generate_qr():
    img = qrcode.make("otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example")
    type(img)
    img.save("QR.png")

# Generate a TOTP
def get_otp():
    # We set the counter using the clock time
    # It will refresh every 30 seconds
    counter = math.floor(time.time()/30)
    byte_counter = (counter).to_bytes(8, byteorder = "big")

    # Key provided by Google is decoded into bytes
    key = "JBSWY3DPEHPK3PXP"
    byte_key = base64.b32decode(key)

    # Here we generate the HMAC-SHA-1 value using the key and the counter
    generated_hmac = hmac.new(byte_key, byte_counter, digestmod = "sha1")

    # Now we need to generate a 4-byte string using dynamic truncation
    # The idea for how to do this was found on page 12 of RFC 6238
    # Source: https://datatracker.ietf.org/doc/html/rfc6238
    offset = generated_hmac.digest()[19] & 0x0f
    bin_code = ((generated_hmac.digest()[offset] & 0x7f) << 24) | ((generated_hmac.digest()[offset+1] & 0xff) << 16) | ((generated_hmac.digest()[offset+2] & 0xff) << 8) | (generated_hmac.digest()[offset+3] & 0xff)

    # Divide to get a 6-digit password and print to the screen
    otp = bin_code % 1000000
    print(otp)

def main():
    args = sys.argv[1:]
    if args[0] == "--generate-qr":
        generate_qr()
    elif args[0] == "--get-otp":
        get_otp()
    else:
        print("Your entry was invalid.")

if __name__ == "__main__":
    main()