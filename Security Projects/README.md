# SecurityProjects
Bloom filter, one-time password, and "Damn Vulnerable Web Application" projects.

IMPORTANT!! See additional README files in Bloom Filter and OTP folders for further instructions.

Bloom Filter:  
This program loops over an input file of possible passwords and evaluates if they are already contained in a list of bad passwords. 
Three different hash functions are used over a list of approximately 600K passwords, which results in a "low" false positive rate of about 21%.
Project folder also contains a report discussing implementation strategies, run time analysis, and future ideas to improve the false-positive rate.

OTP (One-Time Password:

The OTP.py program will create a QR png file that can be used to create an account with Google Authenticator. The program can also create an OTP using the TOTP algorithm referenced in RFC 6238.

Damn Vulnerable Web Application Report:

A report showing the types of security vulnerabilities I found in a mock web application. The report goes over the types of vulnerabilities, how to exercise them, their importance, and ways to fix them.
