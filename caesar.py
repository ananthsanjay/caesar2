#This is a tutorial from the book Invent Your
#Own Computer Games with Python

#Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'#uppercase and lowercase letters
MAX_KEY_SIZE = len(SYMBOLS)#

def getMode():# define a function weather to encrypt or decrypt
    while True:
        print('Do you wish to encrypt or decrypt a message?')#prints the message
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:#look for e or encrypt or d or decrypt
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():# taking in what the user wants to encrypt
    print('Enter your message: ')# prints statement
    return input()

def getKey():# initializing varable key
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))# asks user for key
        key = int(input())# force integer
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key#if key givem is between 1 and 52 ( max size)

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol
        else:
            #Encrypt or decrypt
            symbolIndex += key
        if symbolIndex >= len(SYMBOLS):#the shift starts happening here depending on length of symbol list and the key
            symbolIndex -= len(SYMBOLS)
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)

        translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode()# these are the call functions
message = getMessage()
key = getKey()
print('Your translated text is: ')#print statement
print(getTranslatedMessage(mode, message, key))# print statements