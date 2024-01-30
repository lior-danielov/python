'''
Welcome to the cypher program

{logo}

Choose what would you like to do:
Encrypt (press 1)
decrypt (press 2)

---> 1
input -->"Hello"
OK, enter the offset >>>
input --> 2
Encrypted sentence: Jgnnq
Would you like to continue or quit? (C or Q)

--- 2
OK, enter the encrypted sentence >>> jgnnq
Enter the offset >>> -2
Decrypted sentence: Hello
Would you like to continue or quit? (C or Q)

# if the user chooses to quit, then the program exists. else, the screen will clear
and he will start over.


find the ASCII value of a given character
char = 'p'
print("The ASCII value of " + char + " is ", ord(char))

# print(chr(97))

# additional requirement:
# if the user, for example, writes: 'zzz' and +1 then --> 'aaa'
# Same with upper-case letters!  (Z+1=A)

<END of Ceasar-Cypher Assignment>
'''



# Write a function which gets a sentence from the user,  and converts it to
# title case (where each 1st letter is in upper-case
# e.g., hello sir  --> Hello Sir
'''
def convert():
    i = int
    choose1 = int(input("enter your number "))
    choose2 = input("enter your word: ")
    for i in choose2:
        res = chr(ord(i)+len(choose2))
        print(res)
print(convert())
'''

'''
choose1 = int(input("enter your number "))
choose2 = input("enter your word: ")
for i in choose2:
    res = chr(ord(i) + len(choose2))
    if res >= chr(122) or res >= chr(90):
        res1 = [res:str(26)]
        res = chr(ord(res1))
    print(res)     
    
    
    # i try to convert from z re circle to a back but not seceded by now so i hope you ok.     נ.ב  למרצה
'''

# TODO:1. Check for
