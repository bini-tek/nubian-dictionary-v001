"""
----------------
| [bini-tek] \\
----------------
By: [bini-tek]\\
Email: binitek.baltimore@gmail.com
Discord: Home of bini-tek (https://discord.gg/4GqDrH)




----------------
Version #: 001.
DATE: Jan/-3-2021.
----------------




---------------
| EXPLANATION |
---------------
The Nubian Dictionary.
----------------------
This program is based on the Lexicography work of Mr. Yousseff Sumbagh.
An interactive/digitized version of his Nubian Dictionary book.
This is the very first iteration of this project, hopefully it will be catalyst to more improved versions.




----------------
| CONTRIBUTORS |
----------------
Youssef Sumbagh: Lexicographer.
Asher Noor: coder.
50DD: coder.
"""


'''-------
IMPORTS
----------'''
from time import sleep
import re



'''-------
DEFINING THE FUNCTIONS
----------'''

'''/////////////////////////////////////////////////////////'''
"**************************"
"--- Main Menu Function ---"
"**************************"
def nd_mainMenu():
    print("\n\n---------------------"
          "\nThe Nubian Dictionary"
          "\n---------------------"
          "\nDigitized By: [bini-tek]\\\\"
          "\nBased on the work of: Youssef Sumbagh"
          "\nVersion #: 001"
          "\n--------------\n"
          "\nMain Menu"
          "\n----------"
          "\n[1]: Word Search"
          "\n[2]: Days of The Week"
          "\n[3]: Numbers"
          "\n[4]: Credits"
          "\n[5]: Exit")

    # User Input w/ Validation
    while True:
        choice = input("\nPlease enter your option: ")
        try:
            choice = int(choice) # <-- to make sure an int was entered
        except:
            print("Please enter one of the above numeric choices.") # <-- if a letter or blank was entered
            continue
        if choice == 1:
            TheDictionary() # <-- Word Search: The Dictionary Function
        elif choice == 2:
            nd_days() # <-- Days of The Week: The Days Function
        elif choice == 3:
            nd_numbers() # <-- Numbers: The Numbers function
        elif choice == 4:
            nd_credits() # <-- Credits: The Credits function
        elif choice > 5:
            print("Please choose between 1- 5: ") # <-- User choice validation
        else:
            outro()
"-- The End of Main Menu Function --"





'''/////////////////////////////////////////////////////////'''
"**************************"
"--- Mini Menu Function ---"
"**************************"
#-- This is a small menu appearing in some of the smaller functions.
def miniMenu():
    # -- the menu options // back to menu // exit
    print("\nMenu:"
          "\n1- Main Menu"
          "\n2- Exit")

    # User Input w/ Validation
    while True:
        choice = input("\nPlease enter your option: ")
        try:
            choice = int(choice)  # <-- to make sure an int was entered
        except:
            print("Please enter one of the above numeric choices.")  # <-- if a letter was entered
            continue
        if choice == 1:
            nd_mainMenu()  # <-- The Main Menu function
        elif choice > 3:
            print("Please choose 1 or 2")
        else:
            outro()  # <-- The Outro function

"-- The End of Mini Menu Function --"






'''/////////////////////////////////////////////////////////'''
"***********************************************"
"--- [ 1 ] : Word Search Dictionary Section  ---"
"***********************************************"
# -- The Line Print Function
# If a single letter is entered, it will print out all words starting with that letter
def TheLinePrint(eng_word):
      # Read the ND1 text file
      # ----- To open the text file
      open_text = open("nd-wordsearch.txt", "r")
      # ----- To read the text file
      read_text = open_text.readlines()  # open_text.read()
      # ---- test print
      # print(read_text)

      # Search for the word entered & Print that line
      for line in read_text:
            if re.match(eng_word, line):
                  print(line)  # the .strip() will take out the \n between the lines.

# --------- End of The Line Print Function --------- #


# -- Creating the Dictionary from the nd-wordsearch text file.
def TheDictionary():
    print("\n\t\t\t---------------"
          "\n\t\t\t| Word Search | "
          "\n\t\t\t---------------\n")

    # -- Opening the File
    f = open('nd-wordsearch.txt', 'r')

    # -- Creating the empty dictionary
    d = {}

    # -- Populating the dictionary list from the nd-wordsearch text file.
    for line in f:
        x = line.split(" ")  # // Split the words at the spaces
        a = x[0]  # // the KEY before the space
        b = x[1], x[2]  # // the VALUE after the space
        c = len(b)  # // to subtract the '\n' at the end
        b = b[0:c]  # // the new value starts at '0' and ends with 'c' calculation
        d[a] = b  # // combines the KEY to the VALUE


    '# -- User Input / the English word'
    eng_word = str(input("\nSearch For: ").lower())

    '# -- To validate the User Input is a string.'
    if eng_word.isalpha():                       # -- if the input is a string
            # -- The Search section
            if len(eng_word) <= 1:
                  TheLinePrint(str(eng_word))

            elif eng_word not in d:  # -- if the word is not in the dictionary
                  print("ERROR: This is not a word, please try again \n")
                  TheDictionary()  # -- recalling the function to get new User Input

            else:
                 # -- Print from the dictionary list
                 print("The Two Dialects:"
                       "\n(K-D) Kinzeeya - Dungulaweea."
                       "\n(F-M) Fadeega - Mahaseeya.\n\n"
                       "\t(K-D)  |  (F-M) \n  ", d[eng_word])


    else:                                         # -- if the input is NOT a string
        print("ERROR: No numbers or special characters, please try again \n")
        TheDictionary() # -- recalling the function to get new User Input

    #-- To check if user wants to search another word
    another_word = str(input("\nWould you like to search for another word? y/n: ").lower())
    #-- User Validation
    if another_word.isalpha():
            #-- if YES
            if another_word == 'y':
                  TheDictionary()
            else:
                  nd_mainMenu() #-- calling the Main Menu function
    else:
            print("That was not an option"
                  "\nGoing back to the Main Menu, please wait.")
            sleep(3)
            nd_mainMenu() #-- calling the Main Menu function

# --------- End of The Dictionary Function --------- #

"-- The End of Word Seach Dictionary Section --"








'''/////////////////////////////////////////////////////////'''
"*****************************************"
"--- [ 2 ] : Days of The Week Section  ---"
"*****************************************"
def nd_days():
    #-- open  & read the text file
    f = open("nd-days.txt", "r")
    #-- display the text file line by line
    for x in f:
        print(x.rstrip())
    #-- close the file
    f.close()

    #-- Calling the mini menu
    miniMenu()

"-- The End of Days of The Week Section --"










'''/////////////////////////////////////////////////////////'''
"*****************************************"
"--- [ 3 ] : Numbers Section  ---"
"*****************************************"
def nd_numbers():
    #-- open  & read the text file
    f = open("nd-numbers.txt", "r")
    #-- display the text file line by line
    for x in f:
        print(x.rstrip())
    #-- close the file
    f.close()

    # -- Calling the mini menu
    miniMenu()

"-- The End of Numbers Section --"









'''/////////////////////////////////////////////////////////'''
"*****************************************"
"--- [ 4 ] : Credits Section  ---"
"*****************************************"
def nd_credits():
    print("\n-----------------------------------------"
          "\nCredits for The Nubian Dictionary.       "
          "\n-----------------------------------------"
          "\nLexicographer: Youssef Sumbagh (Sabbaj)."
          "\nCoder: Asher Noor."
          "\nCoder: 50DD."
          "\nBrought to you by: [bini-tek]\\\\"
          "\nEmail: binitek.baltimore@gmail.com"
          "\nDiscord: Home of bini-tek (https://discord.gg/4GqDrH)."
          "\n----------------------------------------")

    # -- Calling the mini menu
    miniMenu()

"-- The End of the Credits Section --"








'''/////////////////////////////////////////////////////////'''
"**************************"
"--- Outro Function ---"
"**************************"
def outro():
    print("\nExiting Program, please wait.")
    sleep(2)

    print("\n-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-"
          "\nBrought to you by: [bini-tek]\\\\"
          "\nEmail: binitek.baltimore@gmail.com"
          "\nDiscord: Home of bini-tek (https://discord.gg/4GqDrH)"
          "\n-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-")
    sleep(5)
    exit()







'''-------
CALLING OF THE FUNCTIONS
----------'''

# Calling Main Menu - It calls all the others.
nd_mainMenu()









'''-------
END OF PROGRAM
----------'''