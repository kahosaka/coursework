/*
  Kiana Hosaka

*/

#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <ctype.h>


// Number of response our robot can make
#define NUM_RESPONSE 5

// Input the robot can recognize
char *INPUT_STR[] = {"Good",
                     "Leaving",
                     "Age",
                     "Weather",
                     "Sports"};

// Corresponding response the robot should make
char *RESPONSE_STR[] = {"Good day to you as well.",
                        "Good bye.",
                        "I am a robot and I am 4 hours old.",
                        "It's raining.",
                        "Go Ducks!",
                        "I don't understand what you are saying."};


// Function prototypes
void arg_test(int argc, char **argv);
void arg_print(int argc, char **argv);
void str_comparison(int argc, char **argv);
void str_case(int argc, char **argv);
void print_input();
void print_response();
void respond(int argc, char **argv);


int main(int argc, char **argv)
{
    arg_test(argc, argv);
    arg_print(argc, argv);
    //str_comparison(argc, argv);
    //str_case(argc, argv);
    print_input();
    print_response();
    respond(argc, argv);

    return 0;
}

// Testing if there is input entered
void arg_test(int argc, char **argv)
{
    if(argc < 2) {
        fprintf(stderr, "Error: no input entered\n");
        fprintf(stderr, "usage: %s <some input string>\n", argv[0]);
        fprintf(stderr, "\n");
    } else {
        // Do nothing
    }

}

// Prints the arguments one character at a time
void arg_print(int argc, char **argv)
{
    // Command is ./a.out that we are subtracting for
    printf("# input (excluding the command): %d\n", argc - 1);

    // i starts from 1 to skip command
    for(int i = 1; i < argc; i++)
    {
        // 2 is minimum width the output should be
        printf("Token %2d: ", i);

        // Value since length of a string will always >= 0
        // strlen returns the length of the string
        // uint32_t guarantees unsigned, 32 bits, integer
        uint32_t length = strlen(argv[i]);

        // Print each character from the string one at a time
        for(int j = 0; j < length; j++) {
            printf("%c", argv[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

// Test string comparison
void str_comparison(int argc, char **argv)
{
    printf("---- String Comparison ----\n");
    int comp = strcmp("a", "d");
    printf("Return value of comparing 'a' and 'd': %d\n", comp);

    comp = strcmp("d", "a");
    printf("Return value of comparing 'd' and 'a': %d\n", comp);

    comp = strcmp("a", "a");
    printf("Return value of comparing 'a' and 'a': %d\n", comp);

    comp = strcmp("Hello", "hello");
    printf("Return value of comparing 'Hello' and 'hello': %d\n", comp);

    comp = strcmp("hello", "Hello");
    printf("Return value of comparing 'hello' and 'Hello': %d\n", comp);

    comp = strcmp("hello", "good bye");
    printf("Return value of comparing 'hello' and 'good bye': %d\n", comp);

    comp = strcmp("good bye!", "good bye");
    printf("Return value of comparing 'good bye!' and 'good bye': %d\n", comp);

    comp = strcmp("good bye", "good bye");
    printf("Return value of comparing 'good bye' and 'good bye': %d\n", comp);

    printf("--------\n\n");
}

// Changing to lower and upper case
void str_case(int argc, char **argv)
{
    char *test_str = "HelLO";
    printf("---- String Case Change ----\n");
    printf("%s to all lower case letters: ", test_str);

    // Make every character lower case
    for(int i = 0; i < strlen(test_str); i++)  {
        printf("%c", tolower(test_str[i]));
    }
    printf("\n");

    // Make every character upper case
    printf("%s to all upper case letters: ", test_str);
    for(int i = 0; i < strlen(test_str); i++)  {
        printf("%c", toupper(test_str[i]));
    }
    printf("\n");

    printf("--------\n\n");
}

// Print the recognized inputs
void print_input()
{
    printf("---- Recognized Input ----\n");
    for(int i = 0; i < NUM_RESPONSE; i++) {
        printf("%d ::: %s\n", i, INPUT_STR[i]);
    }
    printf("--------\n\n");
}

// Print the responses assoicated with the input
void print_response()
{
    printf("---- Response ----\n");
    // Printing NUM_RESPONSE + 1 because of the
    // last undefined input response "I don't understand what you are saying."
    for(int i = 0; i < NUM_RESPONSE + 1; i++) {
        printf("%d ::: %s\n", i, RESPONSE_STR[i]);
    }
    printf("--------\n\n");
}

/*

Respond function takes input from user and responds appropriately if a recognizable
word is inputted. The input is not case sensitive.

*/
void respond(int argc, char **argv)
{
    printf("---- Answer ----\n");

    if(argc == 1)
    {
      printf("--------\n\n");
      return;
    }
    
    int num = 0;
    for(int i = 1; i < argc; i++)
    {
      // Length of the argument
      int arg_len = strlen(argv[i]);

      for(int k = 0; k < NUM_RESPONSE; k++)
      {
        // Length of input
        int inp_len = strlen(INPUT_STR[k]);

        // If the lengths aren't equal add to the number
        if(arg_len != inp_len)
        {
          num += 1;
        }
      }
    }

    // Number % number of responses should not be 0
    if(num % NUM_RESPONSE == 0)
    {
      printf("%s\n", RESPONSE_STR[NUM_RESPONSE]);
      printf("--------\n\n");
      return;
    }

    // If we get to this point, then at least one of the
    // arguments had matching lenghts to recognized input,
    // now check if the characters are the same.

    // Keeps track if an input has been recognized
    int count = 0;

    // Loop through arguments
    for(int i = 1; i < argc; i++)
    {
      int len = strlen(argv[i]);
      // Make everything lowercase, then the first char uppercase
      for(int j = 0; j < len; j++)
      {

        argv[i][j] = tolower(argv[i][j]);
        argv[i][0] = toupper(argv[i][0]);
      }

      // Compare argument with recognized inputs
      for(int k = 0; k < NUM_RESPONSE; k++)
      {
        // If strcmp is 0, argument and recognized inputs matched
        if(strcmp(argv[i], INPUT_STR[k]) == 0)
        {
          // Count becomes 1, meaning strcmp has been equal to 0
          count = 1;

          // Print the respose that is associated with the recognized input
          printf("%s\n", RESPONSE_STR[k]);
        }
      }
    }

    // If count is still 0, means that no comparison was the same
    if(count == 0)
    {
      // Print the response for no matches
      printf("%s\n", RESPONSE_STR[NUM_RESPONSE]);
    }

    printf("--------\n\n");
}
