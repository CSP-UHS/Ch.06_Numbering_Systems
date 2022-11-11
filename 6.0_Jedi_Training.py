'''
Sign your name: Oded H
11.7.2022

1.) Convert Binary 101010 to Hexadecimal.
'''
code = input("\033[1;35mYou would like to encrypt a message (Press 1), \n\033[1;34mYou are Mr. Hermon and would like to see my answers for the Jedi training? (Press 2)\n\033[0;00m")
if code == "see your answers" or code == "2":
    print("\n1. 2A")
    '''
    2.) Convert Binary 11101001 to Octal.
     011/101/001 =
    '''
    print("\n2. 351")
    '''
    3.) Convert Hexadecimal FC to Binary.
    '''
    print("\n3. 11111100")
    '''
    4.) Convert Hexadecimal 1F to Decimal.
    '''
    print("\n4. 31")
    '''
    5.) Convert Hexadecimal #FAAFBD to RGB.
    '''
    print("\n5. #250,175,189")
    '''
    6.) Convert Octal 70 to Binary.
    '''
    print("\n6. 111000")
    '''
    7.) Convert RGB (32,128,64) to Hexadecimal.
    '''
    print("\n7.20,80,40")
    '''
    8.) Convert 01000001, 01010011, 01000011, 01001001, 01001001 to ASCII.
    '''
    print("\n8. ASCII")
    '''
'''
else:
    '''    
         '''
    # print(chr(65)) #gives you the ordinate value of the number
    # print(ord("A")) #decripts the ordinate value back to a number
    print("1.Encrypt\n2.Decrypt")


    done = False
    while not done:
        text = input("Choose an option")
        if text == "1":
            encrypted = ' '
            word=input("Enter a word to encrypt")
            for letter in word:
                i=ord(letter)+5
                newletter = chr(i)
                encrypted += newletter

            print(encrypted)
            reselect = input("Would you like to use again?")
            if reselect == "no" or reselect == "n":
                done = True
            else:
                print("")
        elif text == "2":
            encrypted = ' '
            word=input("Enter a word to decrypt")-5
            for letter in word:
                i=ord(letter)
                newletter = chr(i)
                encrypted += newletter

            print(encrypted)
            reselect = input("Would you like to use again?")
            if reselect == "no" or reselect == "n":
                done = True
            else:
                print("")
