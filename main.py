import wx
import scgui
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






b = createMatrix()
dicAlpha = createDicAlpha()
plainText = 'ATTACK AT DAWN'
key = 'LEMON'



class ScGuiMainFrame(  scgui.ScGuiMainFrame):
    #Cifrador
    def cipher(self, event):
        plainText = self.txtPlainTextCi.GetValue().lower()
        key = self.txtKeyCi.GetValue().lower()
        keyStream = createKeyStream(plainText, key)
        keyStream = cycle(keyStream)
        cipherText = ''
        for char in plainText:
            if char != ' ':
                cipherText += b[dicAlpha[char]][dicAlpha[next(keyStream)]]
            else:
                cipherText += ' '
        self.txtCipherTextCi.SetValue(cipherText)
    
    #decifrador
    def decipher(self, event):
        decipherText = ''
        cipherText = self.txtCipherTextDe.GetValue().lower()
        key = self.txtKeyDe.GetValue().lower()
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
        self.txtDecipherTextDe.SetValue(decipherText)

if __name__ == '__main__':
    app = wx.App()
    frm = ScGuiMainFrame(None)
    frm.Show()
    app.MainLoop()