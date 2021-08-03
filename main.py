import wx
from scgui import ScGuiMainFrame
import string
import numpy as np
from itertools import cycle

#criação da matrix de Vigenere:
def createMatrix():
    a = []
    vigenereMatrix = list(string.ascii_lowercase)
    alphabets = list(string.ascii_lowercase)
    start_index = 0
    length = len(alphabets)

    for i in range(length):
        for i in range(length):
            element_index = start_index % length
            a.append(alphabets[element_index]) 
            start_index += 1
        vigenereMatrix = np.vstack((vigenereMatrix,a))
        a=[]
        start_index += 1
    vigenereMatrix = np.delete(vigenereMatrix, 0,0)
    return vigenereMatrix

#criação do dicionário do alfabeto para consulta.
def createDicAlpha():
    dicAlpha ={}
    for i in list(string.ascii_lowercase):
        number = ord(i) - 97
        dicAlpha[i] = number
    return dicAlpha

#Gerar o keyStream
def createKeyStream(plainText, key):
    key = cycle(key.lower())
    keyStream = ''
    for char in plainText:
        if char != ' ':
            keyStream += next(key)
    return keyStream

#Cifrador
def cipher(plainText, key):
    plainText = plainText.lower()
    keyStream = createKeyStream(plainText, key)
    keyStream = cycle(keyStream)
    cipherText = ''
    for char in plainText:
        if char != ' ':
            cipherText += b[dicAlpha[char]][dicAlpha[next(keyStream)]]
        else:
            cipherText += ' '
    return cipherText

#decifrador
def decipher(cipherText, key):
    decipherText = ''
    keyStream = createKeyStream(cipherText, key)
    lstSpaces = []
    keyStream = list(keyStream)

    for pos,char in enumerate(cipherText):
        if(char == ' '):
            lstSpaces.append(pos)
    
    for spaceIndex in lstSpaces:
        keyStream.insert(spaceIndex, ' ')
    keyStream = ''.join(keyStream)
    
    for char,i in zip(keyStream, cipherText):
        if char != ' ':
            decipherText += b[0][np.where(b[dicAlpha[char]] == i)[0][0]]
        else:
            decipherText += ' '
        
    return decipherText

b = createMatrix()
dicAlpha = createDicAlpha()
plainText = 'ATTACK AT DAWN'
key = 'LEMON'

cipherText = cipher(plainText, key)
decipherText = decipher( cipherText, key)
print(cipherText)
print(decipherText)


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = ScGuiMainFrame(None)
    frm.Show()
    app.MainLoop()