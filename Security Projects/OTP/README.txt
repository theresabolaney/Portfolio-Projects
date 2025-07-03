Dependencies:
 - Before starting, make sure you have installed the following packages:
 python3 -m pip install qrcode[pil] --user

To generate a QR code, enter "python3 OTP.py --generate-qr".
This will create a png file in the folder called "QR.png".
You can then open the Google Authenticator app and scan the image.
Note: this QR code will create the alice@google.com account provided by Google

To get the one time password, run "python3 OTP.py --get-otp".
This should match with Google Authenticator!