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

#Faz o shift-left nos valores do gráfico
def update_line(self):    
    self.axs[0].clear()
    x.append(x[0])
    x.pop(0)
    y.append(y[0])
    y.pop(0)
    print(x[0])
    self.axs[0].bar(x,y)
    plot.draw()

class ScGuiMainFrame(  scgui.ScGuiMainFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.fig, self.axs = plot.subplots(2)

    #Cifrador
    def cipher(self, event):
        plainText = self.txtPlainTextCi.GetValue().lower()
        key = self.txtKeyCi.GetValue().lower()
        keyStream = createKeyStream(plainText, key)
        keyStream = cycle(keyStream)
        cipherText = ''
        for char in plainText:
            if char != ' ':
                cipherText += vigenereMatrix[dicAlpha[char]][dicAlpha[next(keyStream)]]
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
                decipherText += vigenereMatrix[0][np.where(vigenereMatrix[dicAlpha[char]] == i)[0][0]]
            else:
                decipherText += ' '
        self.txtDecipherTextDe.SetValue(decipherText)
    
    def breakCipher(self, event):
        #fig.suptitle('Vertically stacked subplots')
        self.axs[0].bar(x,y)
        self.axs[0].set_title('Frequência de letras no texto')
        self.axs[1].bar(x1,y1)
        #axs[1].set_title('Frequência de letras em portugês')
        plot.show()
        
    def breakCipherClose(self, event):
        plot.close()
    
    def breakCipherUpdate(self, event):
        update_line(self)




from collections import Counter

import matplotlib.pyplot as plot


freqPortuguese = {'a':	14.63,'b':	1.04,'c':	3.88,'d':	4.99,'e':	12.57,'f':	1.02,'g':	1.30,'h':	1.28,'i':	6.18,'j':	0.40,'k':	0.02,'l':	2.78,'m':	4.74
,'n':	5.05,'o':	10.73,'p':	2.52,'q':	1.20,'r':	6.53,'s':	7.81,'t':	4.34,'u':	4.63,'v':	1.67,'w':	0.01,'x':	0.21,'y':	0.01,'z':	0.47}

texto = 'A frequencia de letras em um texto tem sido frequentemente estudada para uso em criptografia e analise de frequencia em particular Nenhuma distribuicao de frequencia de letras exata e subjacente a uma determinada lingua uma vez que todos os escritores escrevem um pouco diferente As maquinas de linotipo classificaram as frequencias das letras como'.lower()
counter = Counter(texto)
del counter[' ']
total = 0
for key in counter.keys():
    total += counter[key]

for freq in counter.keys():
    counter[freq] = counter[freq]*100/total
x = sorted(counter.keys())
y = list(counter.values())
x1 = sorted(freqPortuguese.keys())
y1 = freqPortuguese.values()


if __name__ == '__main__':
    vigenereMatrix = createMatrix()
    dicAlpha = createDicAlpha()
    app = wx.App()
    frm = ScGuiMainFrame(None)
    frm.Show()
    app.MainLoop()
  