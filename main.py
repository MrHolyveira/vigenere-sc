from numpy.core.fromnumeric import cumprod
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

b = createMatrix()
dicAlpha = createDicAlpha()


def cipher(plainText,key):
    
    key = cycle(key.lower())
    plainText = plainText.lower()
    keyStream = ''
    #Gerar o keyStream
    for char in plainText:
        if char != ' ':
            keyStream += next(key)
    keyStream = cycle(keyStream)
        
    #cifrar
    cipherText = ''
    for char in plainText:
        if char != ' ':
            cipherText += b[dicAlpha[char]][dicAlpha[next(keyStream)]]
        else:
            cipherText += ' '
    return cipherText
cipherText = cipher('ATTACK AT DAWN', 'LEMON' )
print(cipherText)

'''
if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = ScGuiMainFrame(None)
    frm.Show()
    app.MainLoop()'''