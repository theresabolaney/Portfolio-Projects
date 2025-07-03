!!! I had some trouble with dependencies when testing on flip. If you run into
any problems, please let me know!!!

Before running, you must have the extra modules installed. You can install with the commands:
"pip install --user bitarray"
"pip install --user pycryptodome"
"pip install --user cffi"

Make sure you have the following files in your run folder:
"input.txt" -- this file holds the possible passwords you want to check
"dictionary.txt" -- this file will be used to train the data

To run the program, type:
"python bloomFilter"

Results will be stored in a created or truncated "output.txt" file.
maybe = maybe the password is okay
no = the password is definitely not okay