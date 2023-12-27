# Higher or Lower

This program takes in a range of numbers from the user, then chooses a random number from that range and takes in guesses from the user and tells the user if the number generated is higher or lower than the one guessed. The user has five tries to guess the right number, if they don't guess it they loose.

## Description

The game stars by taking in the lower and upper bounds from the user. Then, there are input validation checks to make sure that the range is valid. The range is considered invalid if the difference between the highest and lowest number is less than five or if the lwer bound is greater than the upper bound. Then a random number is generated within the given range. The user is then prompted to guess a number. There is another set of input validations at this step to make sure the number guessed is within the range. If the input is valid, the program tells the user if the random number generated is higher of lower than the number guessed. The program also keeps track of the number of guesses it takes the user to guess the number. After the user guesses the number, the program prints how many guesses it took for the user to guess the number right.


## Version History

* 0.1
    * Initial Release


## Acknowledgments

Inspiration, code snippets, etc.
* [Geeks-for-geeks](https://www.geeksforgeeks.org/number-guessing-game-in-python/)