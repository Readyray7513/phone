# Phone Number Slicing Example
This Python program demonstrates how to slice a string (in this case, a phone number) to extract specific parts of it. It shows how to use indexing and slicing with positive and negative indexes to obtain various sections of a string.

Requirements:
Python 3.x

How to Use:
Run the script.
The program will print different slices of a phone number string, showing how to extract portions using various indexing methods.

Example Output:
For the phone number '01923-616-285', the program outputs:
019
019
6162
616-285
616-285

Explanation of the Code:
phone[0:3]: Extracts the first three characters, from index 0 up to (but not including) index 3.
phone[:3]: Another way to extract the first three characters (same as phone[0:3]).
phone[8:12]: Extracts characters from index 8 to index 11 (inclusive of 8, exclusive of 12), which corresponds to "6162".
phone[8:]: Extracts characters from index 8 to the end of the string, giving "616-285".
phone[-4:]: Extracts the last four characters using negative indexing, which corresponds to "285".

How It Works:
The program stores the phone number in a variable.
It then prints slices of the phone number using different slicing methods:
From the start to the third character.
From the eighth character onward.
From the fourth-to-last character onward.
