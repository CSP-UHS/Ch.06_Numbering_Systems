print(chr(65))
print(ord("!"))


word=input("Enter a word to encrypt: ")

encrypted=''
for letter in word:
    i=ord(letter)+5
    newLetter=chr(i)
    encrypted+=newLetter
print(encrypted)