#Ask the user for a string and print
#out whether this string is a palindrome
#or not. (A palindrome is a string that
#reads the same forwards and backwards.)

char = input()
char2 = ''
for i in range( (int(len(char))-1 ), -1, -1 ):
  char2 = char2 + char[i]
if char == char2:
   print('Its a palindrome')
