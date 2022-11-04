"""
Decimal system
0-9
numbering system is first number to whatever power

Binary
numbers are called bits
there are two bits
0=off
1=on
1byte=8bits
1nibble=4bits
1tidbit=2bits
"""

# print(chr(65)) #Encoding
# print(ord("A")) #Decoding
word=input("Enter a word to encrypt ")
encrypted=""
decrypted=""
for letter in word:
    i=ord(letter)+5
    newletter=chr(i)
    encrypted+=newletter
print(encrypted)