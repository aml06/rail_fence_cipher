# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 09:26:27 2023

my solution to the problem presented here @https://exercism.org/tracks/python/exercises/rail-fence-cipher
The pattern/encrypt/decrypt took me a while longer to make but are much more robust solution. The hardcoded elements 
were me just trying to make something that barely functions as fast as I could. 
"""
import math
#not going to worry about testing my inputs
def __main__():
    print("Rail Fence Cipher Program")
    print("Would you like to encrypt or decrypt a message?")
    selection = input("Type Encrypt (E) or Decrypt(D): ")
    if selection == "Encrypt" or selection == "E" or selection == "encrypt" or selection == "e":
        encryptMessage = input("Input Message to Encrypt: ")
        railCount = input("How many rails should be used? ")
        railCount = int(railCount) #don't forget to make this an Integer!
        #encryptedMessage = hardCodeEncrypt(encryptMessage)
        encryptedMessage = encrypt(encryptMessage, railCount)
        print("Encryped Message is: ")
        print(encryptedMessage)
    elif selection == "Decrypt" or selection == "decrypt" or selection == "D" or selection == "d":
        decryptMessage = input("Input Message to Decrypt: ")
        railCount = input("What is the number of rails that were used? ")
        railCount = int(railCount) #Again, same thing!
        #decryptedMessage = hardCodeDecrypt(decryptMessage)
        decryptedMessage = decrypt(decryptMessage, railCount)
        print("Decrypted Message is: ")
        print(decryptedMessage)
    else:
        print("Input Not Recognized")
    print()
    print()
    __main__()
    
#Let's do this a little more gracefully, and handle varying rail numbers
#we make a pattern tuple where the first tuple value is the rail and the second is the character position in the message
def patternGenerator(message, railCount): #fundamentally, the rail is generating a pattern based on the mod of the railcount
    positionList = []
    modRailCount = 2* (railCount - 1)
    i = 0
    while i < len(message):
        if i % modRailCount < railCount:
            positionList.append((i % modRailCount,i))
        else:
            positionList.append((modRailCount - (i % modRailCount),i))
        i+=1
    #print(positionList) #not removing all my debugging print statements
    return(sorted(positionList))

#Going to join each letter in the message to the pattern tuple and present the encrypted message by associated rail
def encrypt(message, railCount):
    eString = ""
    pattern = patternGenerator(message,railCount)
    for i in pattern:
        #print(i)
        eString = eString + message[i[1]]
    return eString

#Generate the pattern again and sort it by the second tuple value in the pattern to decrypt the associated character position
def decrypt(message, railCount):
    pattern = patternGenerator(message, railCount)
    joinList = []
    j = 0
    for i in pattern:
        joinList.append((i,message[j]))
        j+=1
    #print(joinList)
    dString = ""
    minVal = 0
    i = 0
    while i < len(message):
        if joinList[i][0][1] == minVal:
            dString = dString + joinList[i][1]
            minVal += 1
            i = 0
        i+=1
    return dString
    
#Stuff down here is a first run through, just got it working in 20 minutes
def hardCodeEncrypt(message):
    print("Encrypting ", message)
    i = 0
    topRail = ""
    midRail = ""
    bottomRail = ""
    k = 0 #controls actual rail
    m = 0 #controls direction, whether moving up or down on the rails
    while i < len(message):
        if k == 0:
            topRail = topRail + message[i]
            k+=1
            m = 0
        elif k == 1:
            midRail = midRail + message[i]
            if m == 0:
                k+=1
            else:
                k-=1
        elif k == 2:
            bottomRail = bottomRail + message[i]
            k-=1
            m = 1
        else:
            print("Error")
            break
        print("--------")
        print(topRail)
        print(midRail)
        print(bottomRail)
        i+=1
    eMessage = topRail + midRail + bottomRail
    print("Encrypted Message")
    print(eMessage)
    return eMessage
    
def hardCodeDecrypt(message):
    #I am really lazy right now and I don't want to figure out how to properly handle varying lengths
    print("Decrypting ", message)
    dString = ""
    if len(message) % 4 == 0: 
        topRail = message[0:math.ceil(len(message)/4)]
        midRail = message[math.ceil(len(message)/4):math.ceil(len(message)*3/4)]
        bottomRail = message[math.ceil(len(message)*3/4):len(message)]
    elif len(message) % 4 == 1: 
        topRail = message[0:math.ceil(len(message)/4)]
        midRail = message[math.ceil(len(message)/4):math.ceil(len(message)*3/4)-1]
        bottomRail = message[math.ceil(len(message)*3/4)-1:len(message)]
    elif len(message) % 4 == 2: 
        topRail = message[0:math.ceil(len(message)/4)]
        midRail = message[math.ceil(len(message)/4):math.ceil(len(message)*3/4)]
        bottomRail = message[math.ceil(len(message)*3/4):len(message)]
    else:
        topRail = message[0:math.ceil(len(message)/4)]
        midRail = message[math.ceil(len(message)/4):math.ceil(len(message)*3/4)-1]
        bottomRail = message[math.ceil(len(message)*3/4)-1:len(message)]
    print(topRail)
    print(midRail)
    print(bottomRail)
    i = 0
    k = 0
    m = 0
    while i < len(message):
        if k == 0:
            dString = dString + topRail[0]
            topRail = topRail[1:]
            k+=1
            m=0
        elif k == 1:
            dString = dString + midRail[0]
            midRail = midRail[1:]
            if m == 0:
                k+=1
            else:
                k-=1
        elif k == 2:
            dString = dString + bottomRail[0]
            bottomRail = bottomRail[1:]
            m = 1
            k-=1
        else:
            print("Error")
            break
        i+=1
    return dString
    
__main__()
