####################################
# Program: bloomFilter.py
# Author: Theresa Bolaney
# Date: 11/3/2021
# This program loops over an input file of possible passwords and evaluates
#   if they are already contained in a list of bad passwords. Three different
#   hash functions are used over a list of approximately 600K passwords, which
#   results in a "low" false positive rate of about 21%.
####################################

from bitarray import bitarray
from Crypto.Hash import SHA256
from Crypto.Hash import BLAKE2s

# Create an large bit array and set to all 0s
bitArray = bitarray(2000000)
bitArray.setall(0)

dictionary = open("dictionary.txt", "r")

# This will loop through all the lines in the dictionary and run them
# on five different hashes. Results are stored in bitArray.
for word in dictionary:

    # First hash using hash() function
    hashedWord = hash(word)
    index = hashedWord % 2000000
    bitArray[index] = 1

    # Second hash using SHA256
    # Idea to use Crypto.Hash courtesy of Akshith Gunasekaran in Ed post 59
    # https://edstem.org/us/courses/14665/discussion/746134
    # Code to convert hex output to int provided by Kevin Tugenberg in Ed post 66
    # https://edstem.org/us/courses/14665/discussion/762811
    byteWord = bytearray(word, 'utf-8')
    SHA256Object = SHA256.new(data = byteWord)
    SHA256String = SHA256Object.hexdigest()
    index = int(SHA256String, 16) % 2000000
    bitArray[index] = 1

    # Third hash
    BLAKE2sObject = BLAKE2s.new(digest_bits = 256, data = byteWord)
    BLAKE2sString = BLAKE2sObject.hexdigest()
    index = int(BLAKE2sString, 16) % 2000000
    bitArray[index] = 1

dictionary.close()

# Open the input file, which must be named "input.txt"
inputFile = open("input.txt", "r")

# Open or create the output file
outputFile = open("output.txt", "w")

# Loop through entries and hash them with the same hashes from before and compare against the bitArray
# If all results are 1, the password is probably bad
for line in inputFile:
    hashedPass = hash(line)
    newIndex = hashedPass % 2000000
    if bitArray[newIndex] == 1:
        byteLine = bytearray(line, 'utf-8')
        newSHA256Object = SHA256.new(data = byteLine)
        newSHA256String = newSHA256Object.hexdigest()
        newIndex = int(newSHA256String, 16) % 2000000
        if bitArray[newIndex] == 1:
            newBLAKE2sObject = BLAKE2s.new(digest_bits = 256, data = byteLine)
            newBLAKE2sString = newBLAKE2sObject.hexdigest()
            newIndex = int(newBLAKE2sString, 16) % 2000000
            if bitArray[newIndex] == 1:
                outputFile.write("no\n")
            else:
                outputFile.write("maybe\n")
        else:
            outputFile.write("maybe\n")
    else:
        outputFile.write("maybe\n")

inputFile.close()
outputFile.close()
