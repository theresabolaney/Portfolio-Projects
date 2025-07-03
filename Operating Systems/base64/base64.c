//Program: BASE64
//Author: Theresa Bolaney
//Date: 04/15/2023 with updates on 7/3/2025
//Description: This program will take an input (provided file or user entry) and encode it
//according to base64 specifications. Output will be printed to the screen.
//Updates made for running on Windows instead of Linux


#include <stdio.h>
#include <errno.h>
#include <stdint.h>
#include <string.h>
//TAB 7/3/25: All err.h references removed for running on Windows
//#include <err.h>

static char const b64_alphabet[] =
  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  "abcdefghijklmnopqrstuvwxyz"
  "0123456789"
  "+/";

int main(int argc, char *argv[]) {
  FILE* inputFile;
  int charCount = 0;

  //This block will evaluate if we have the correct number of arguments
  //and will assign the file descriptor to the correct file or stdin
  //Citation: Skeleton provided by class
  if (argc > 2) {
    errno = EINVAL; /* "Invalid Argument" */
    //err(1, "Too many arguments");
    printf("Too many arguments");
  }
  else if (argc == 2 && strcmp(argv[1], "-")) {
    //open file
    inputFile = fopen(argv[1], "r");
    if (inputFile == NULL) {
      //err(2, "File could not be opened.");
      printf("File could not be opened.");
    }
  }
  else {
    //open stdin
    printf("Enter a string to be base64 encoded: ");
    inputFile = stdin;
  }

  //Here we will loop through our input file and encode to base64 format
  //Citation: Skeleton provided by class
  for (;;) {
    uint8_t input_bytes[3] = {0};
    size_t n_read = fread(input_bytes, sizeof *input_bytes, sizeof input_bytes/sizeof *input_bytes, inputFile);
    if (n_read != 0) {
        /* Have data */
        int alph_ind[4];
        //Place the first 6 bits of input into our first holder
        alph_ind[0] = input_bytes[0] >> 2;
        //Place 6 more bits (lower 2 then upper 4) from input into second holder
        alph_ind[1] = (input_bytes[0] << 4 | input_bytes[1] >> 4) & 0x3Fu;
        //Place 6 more bits (lower 4 then upper 2) from input into third holder
        alph_ind[2] = (input_bytes[1] << 2 | input_bytes[2] >> 6) & 0x3Fu;
        //Place final 6 lowest bits into fourth holder
        alph_ind[3] = input_bytes[2] & 0x3Fu;

        char output[4];
        output[0] = b64_alphabet[alph_ind[0]];
        output[1] = b64_alphabet[alph_ind[1]];
        output[2] = b64_alphabet[alph_ind[2]];
        output[3] = b64_alphabet[alph_ind[3]];

        //If we converted too few bits, then pad extra space with '='
        if (n_read < 3) {
          output[3] = '=';
        }
        if (n_read < 2) {
          output[2] = '=';
        }
        
        //Write output but make sure to insert a new line after every 76 characters
        size_t n_write = fwrite(output, sizeof (char), sizeof (output)/sizeof (char), stdout);

        charCount = charCount + n_write;

        if (charCount >= 76) {
          putchar('\n');
          charCount = 0;
        }

        //if (ferror(stdout)) err(3, "Write error occurred."); /* Write error */    
        if (ferror(stdout)) puts("Write error occurred."); /* Write error */
    }

       if (feof(inputFile)) break; /* End of file */
       //if (ferror(inputFile)) err(4, "Read error occurred."); /* Read error */   
       if (ferror(inputFile)) puts("Read error occurred."); /* Read error */ 
  }
  if (charCount != 0) putchar('\n');
  //Clean up by closing the file
  if (inputFile != stdin) fclose(inputFile);
  /* any other cleanup tasks? */
}
