from typing import KeysView
import wx
from scgui import ScGuiMainFrame
import string
import numpy as np
from itertools import cycle
import time 

#criação da matrix de Vigenere:
a = []
b = list(string.ascii_lowercase)
alphabets = list(string.ascii_lowercase)
start_index = 0
length = len(alphabets)

for i in range(length):
    for i in range(length):
        element_index = start_index % length
        a.append(alphabets[element_index]) 
        start_index += 1
    b = np.vstack((b,a))
    a=[]
    start_index += 1
b = np.delete(b, 0,0)

#criação do dicionário do alfabeto para consulta.
dicAplha = {}
for i in list(string.ascii_lowercase):
    number = ord(i) - 97
    dicAplha[number] = i
dicAplha2 ={}
for i in list(string.ascii_lowercase):
    number = ord(i) - 97
    dicAplha2[i] = number


#teste:
plainText = 'ATTACK AT DAWN'
key = cycle('LEMON'.lower())
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
        cipherText += b[dicAplha2[char]][dicAplha2[next(keyStream)]]
    else:
        cipherText += ' '
print(cipherText)


'''
if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = ScGuiMainFrame(None)
    frm.Show()
    app.MainLoop()'''