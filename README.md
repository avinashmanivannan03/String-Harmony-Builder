# Avinash_AI_CIA_2
CIA-2 AI Assignment (Using Python Programming Language)

#IMPLEMENTATION EXPLANATION:
Explanation of find_common() function:
1) The Function find_common() is used inorder to find the common strings from the input strings.
2) In find_common() I used min_len inorder to calculate the minimum length between two strings (So that it won't index out of bound while comparing).
3) str[-i:]==str2[:i] => Here using if condition I checked whether the last string characters of string 1 and first characters of string 2 is equal. (Checks first two and last two Characters of String 1 and 2 Respectively).
4) Now add the common Character of Strings in the variable called common_suffix.

Explanation of join_strings() function:
1) Result initially contains the first word (here input first word is 'SNU_').
2) words[i] Contain the second word (here second word is 'U_CH').
3) [len(common_suffix):] => Here common_suffix length is 2 so I take the part of second word starting from end of common suffix. ('U_CH[2:] is 'CH)
4) So the result becomes 'SNU_'+'CH'='SNU_CH'
5) Similarly the process gets repeated for the each pair of Strings and add it onto the result.

Getting Input from User:
1) I get input from user for the total number of words
2) And The user need to input each words.
3) Then I pass the input_words as parameter in join_strings() [Function Call] and Print the Final output.

#IDEA EXPLANATION:
Basic Idea:
1) I planned to get the common Characters from input string.
2) If the Input strings has common Characters (Last in String 1 and First in String 2), I remove the common character of string 2 and concatinate with string 1 and store it in a variable.
3) And perform the Same for all input Strings.

        
