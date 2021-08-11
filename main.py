from numpy.lib.function_base import diff
import wx
import scgui
import string
import numpy as np
from itertools import count, cycle
from collections import Counter
import matplotlib.pyplot as plot
import re
from itertools import combinations

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
def updateLine(self):    
    self.axs[1].clear()
    self.x.append(self.x[0])
    self.x.pop(0)
    self.y.append(self.y[0])
    self.y.pop(0)
    self.axs[1].bar(self.x,self.y)
    plot.draw()

#Popula o Grid de frequências
def popGrid(self, dicWordsOccurrences):   
        gridRow = 0
        countDiv = {}
        for i in range(1,21):
            countDiv[i] = 0

        for i, word in enumerate(dicWordsOccurrences.values()):
            for j in word:
                self.gridFrequences.SetCellValue(gridRow,1,str(j))
                if j % 2 == 0:
                    self.gridFrequences.SetCellValue(gridRow,2,'x')
                    countDiv[2] +=1
                if j % 3 == 0:
                    self.gridFrequences.SetCellValue(gridRow,3,'x')
                    countDiv[3] +=1
                if j % 4 == 0:
                    self.gridFrequences.SetCellValue(gridRow,4,'x')
                    countDiv[4] +=1
                if j % 5 == 0:
                    self.gridFrequences.SetCellValue(gridRow,5,'x')
                    countDiv[5] +=1
                if j % 6 == 0:
                    self.gridFrequences.SetCellValue(gridRow,6,'x')
                    countDiv[6] +=1
                if j % 7 == 0:
                    self.gridFrequences.SetCellValue(gridRow,7,'x')
                    countDiv[7] +=1
                if j % 8 == 0:
                    self.gridFrequences.SetCellValue(gridRow,8,'x')
                    countDiv[8] +=1
                if j % 9 == 0:
                    self.gridFrequences.SetCellValue(gridRow,9,'x')
                    countDiv[9] +=1
                if j % 10 == 0:
                    self.gridFrequences.SetCellValue(gridRow,10,'x')
                    countDiv[10] +=1
                if j % 11 == 0:
                    self.gridFrequences.SetCellValue(gridRow,11,'x')
                    countDiv[11] +=1
                if j % 12 == 0:
                    self.gridFrequences.SetCellValue(gridRow,12,'x')
                    countDiv[12] +=1
                if j % 13 == 0:
                    self.gridFrequences.SetCellValue(gridRow,13,'x')
                    countDiv[13] +=1
                if j % 14 == 0:
                    self.gridFrequences.SetCellValue(gridRow,14,'x')
                    countDiv[14] +=1
                if j % 15 == 0:
                    self.gridFrequences.SetCellValue(gridRow,15,'x')
                    countDiv[15] +=1
                if j % 16 == 0:
                    self.gridFrequences.SetCellValue(gridRow,16,'x')
                    countDiv[16] +=1
                if j % 17 == 0:
                    self.gridFrequences.SetCellValue(gridRow,17,'x')
                    countDiv[17] +=1
                if j % 18 == 0:
                    self.gridFrequences.SetCellValue(gridRow,18,'x')
                    countDiv[18] +=1
                if j % 19 == 0:
                    self.gridFrequences.SetCellValue(gridRow,19,'x')
                    countDiv[19] +=1
                if j % 20 == 0:
                    self.gridFrequences.SetCellValue(gridRow,20,'x')
                    countDiv[20] +=1
                    
                self.gridFrequences.AppendRows(1)
                gridRow += 1
        gridRow = 0
        for i, word in enumerate(dicWordsOccurrences.keys()):
            for j in dicWordsOccurrences[word]:
                self.gridFrequences.SetCellValue(gridRow,0,word)
                gridRow += 1
        countDiv = sorted(countDiv.items(), key=lambda x: x[1], reverse=True)  
        for i in countDiv:
            self.txtMostFreq.AppendText('Tamanho: '+str(i[0])+" | Frequência: "+ str(i[1])+'\n') 	

def hideNkeys(self, hide,n):
    if hide:
        for i in range(0,n):
            attr = 'radCharKey'+str(i+1)
            getattr(self, attr).Hide()
            attr2 = 'txtCharKey'+str(i+1)
            getattr(self, attr2).Hide()    
    else:
        for i in range(0,n):
            attr = 'radCharKey'+str(i+1)
            getattr(self, attr).Show()
            attr2 = 'txtCharKey'+str(i+1)
            getattr(self, attr2).Show()

def setIdRadios(self):
    for i in range(0,20):
        attr = 'radCharKey'+str(i+1)
        getattr(self, attr).SetId(i+3000)
        attr2 = 'txtCharKey'+str(i+1)
        getattr(self, attr2).SetId(i+2000)

class diagGuess(scgui.diagGuess):
        def __init__(self, parent):
            super().__init__(parent)
            self.text = parent.txtCipherTextBr1.GetValue().lower()
            self.keyCharIndex = {
                '3000': 0,'3001': 1,'3002': 2,'3003': 3,'3004': 4,'3005': 5,'3006': 6,'3007': 7,
                '3008': 8,'3009': 9,'3010': 10,'3011': 11,'3012': 12,'3013': 13,'3014': 14,'3015': 15,
                '3016': 16,'3017': 17,'3018': 18,'3019': 19,
            }
            setIdRadios(self)
            hideNkeys(self, True,20 )

        def plotFreq(self, event):
            #Lista todos os espaços em branco no texto
            lstSpaces = []
            for pos,char in enumerate(self.text):
                if(char == ' '):
                    lstSpaces.append(pos)
            
            #retira todos os espaços em branco no texto
            self.text = self.text.replace(' ','')
            plotText = ''
            for i in range(self.keyIndex,len(self.text), +self.keySize):
                plotText += self.text[i]
            plotText = Counter(plotText)
            
            total = 0
            for key in plotText.keys():
                total += plotText[key]
            for freq in plotText.keys():
                plotText[freq] = plotText[freq]*100/total

            #Coloca os espaços de volta no texto
            self.text = list(self.text)
            for spaceIndex in lstSpaces:
                self.text.insert(spaceIndex, ' ')
            self.text = ''.join(self.text)

            for char in freqPortuguese.keys():
                if char not in plotText.keys():
                    plotText[char] = 0
            
            items = plotText.items()
            sorted1 = sorted(items)
            plotText = dict(sorted1)
            
            self.x = list(plotText.keys())
            self.y = list(plotText.values())
            x1 = freqPortuguese.keys()
            y1 = freqPortuguese.values()
            x2 = freqEnglish.keys()
            y2 = freqEnglish.values()

            self.fig, self.axs = plot.subplots(3,sharey=True)
            self.axs[0].bar(x2,y2)
            self.fig.suptitle('Diagramas de frequência de letras.')
            self.axs[0].set_title('Frequência de letras em inglês')
            self.axs[1].bar(self.x,self.y)
            self.axs[1].set_title('Frequência de letras no texto')
            self.axs[2].bar(x1,y1)
            self.axs[2].set_title('Frequência de letras em portugês')
            plot.subplots_adjust(hspace=0.5)
            plot.show()

            def selectKeySize (self,event):
                event.GetEventObject().GetLabel()
        
        def selectKeySize(self, event):
            self.keySize = int(event.GetEventObject().GetLabel())
            hideNkeys(self, True, 20)
            hideNkeys(self, False,self.keySize)

        def selectKeyIndex(self, event):
            radio = event.GetEventObject()
            id = str(radio.GetId())
            self.keyIndex = self.keyCharIndex[id] 
        
        def shiftPlot(self, event):
            updateLine(self)
        
        def setCharKey(self, event):
            for i in range(0,20):
                attr = 'radCharKey'+str(i+1)
                if getattr(self, attr).GetValue():
                    getattr(self, 'txtCharKey'+str(i+1)).SetValue(self.x[0])
            plot.close()

        def getGuessedKey(self, event):
            key = []
            for i in range(0,20):
                attr = 'txtCharKey'+str(i+1)
                if getattr(self, attr).GetValue():
                    key += getattr(self, 'txtCharKey'+str(i+1)).GetValue()
            
            self.guessedKey = ''.join(key)
            self.Destroy()
class ScGuiMainFrame(  scgui.ScGuiMainFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.txtCipherTextBr1.SetValue('l jdsdfizqvl hq zrevmg rx yy hrixa hrx wurb qvqehprfszprfs rdxgrnoe boel yec rx gdwcessfnqmm s nyexwfp hq tepugsanmm sz aedhvnyxoe yizvhxe pwfevuphtgmc qp jdsdfizqvl hq zrevmg riefo r dynxnnizhr l yyo qpxqfztrmrn wmzuhl yyo ipd cir espcf zw qgpcmfcepw qgpcihsz fq bchns pwspvqbgp ee anbyubnd hq zvysfwcz gxofdmrwplvma nd jdsdfizqvlw pof wiffnd gaab')
    #Cifrador
    def cipher(self, event):
        plainText = self.txtPlainTextCi.GetValue().lower().strip()
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
        cipherText = self.txtCipherTextDe.GetValue().lower().strip()
        key = self.txtKeyDe.GetValue().lower()
        keyStream = createKeyStream(cipherText, key)
        lstSpaces = []
        keyStream = list(keyStream)

        #Lista todos os espaços em branco no ciperText
        for pos,char in enumerate(cipherText):
            if(char == ' '):
                lstSpaces.append(pos)
        #Aplica todos os espaços em branco do ciperText no keyStream
        for spaceIndex in lstSpaces:
            keyStream.insert(spaceIndex, ' ')
        keyStream = ''.join(keyStream)
        
        for char,i in zip(keyStream, cipherText):
            if char != ' ':
                decipherText += vigenereMatrix[0][np.where(vigenereMatrix[dicAlpha[char]] == i)[0][0]]
            else:
                decipherText += ' '
        self.txtDecipherTextDe.SetValue(decipherText)
    
    def generateKeySize(self, event):
        cipherText = self.txtCipherTextBr1.GetValue().lower()
        lstSpaces = []
        cipherText = list(cipherText)
        #Retira os espaços do cipherText
        for pos,char in enumerate(cipherText):
            if(char == ' '):
                cipherText[pos] = ''
                lstSpaces.append(pos)
        cipherText = ''.join(cipherText)
        
        lstWords = []
        for i, char in enumerate(cipherText):
            if i <= len(cipherText)-3:
                word = cipherText[i]+cipherText[i+1]+cipherText[i+2]
                #conta quantas ocorrencias da palavra
                nCountWords = cipherText.count(word)
            if nCountWords >= 2:
                lstWords.append(word)
        dicWordsOccurrences = {}
        lstAux = []
        for word in lstWords:
            for occurrences in combinations([m.start() for m in re.finditer(word, cipherText)],2):
                lstAux.append( occurrences[1]-occurrences[0])
            dicWordsOccurrences[word] =  lstAux
            lstAux = [] 
        #Popula o Grid
        popGrid(self,dicWordsOccurrences)
        
        cipherText = list(cipherText)

        #Insere os espaços de volta no cipherText
        for spaceIndex in lstSpaces:
            cipherText.insert(spaceIndex, ' ')
        cipherText = ''.join(cipherText)
        
    def guessKey(self, event):
        diag = diagGuess(self)
        diag.ShowModal() 
        self.txtGuessedKey.SetValue(diag.guessedKey)

freqPortuguese = {'a':	14.63,'b':	1.04,'c':	3.88,'d':	4.99,'e':	12.57,'f':	1.02,'g':	1.30,'h':	1.28,'i':	6.18,'j':	0.40,'k':	0.02,'l':	2.78,'m':	4.74
,'n':	5.05,'o':	10.73,'p':	2.52,'q':	1.20,'r':	6.53,'s':	7.81,'t':	4.34,'u':	4.63,'v':	1.67,'w':	0.01,'x':	0.21,'y':	0.01,'z':	0.47}

freqEnglish ={'a' : 8.167,'b' : 1.492,'c' : 2.782,'d' : 4.253,'e' : 12.702,'f' : 2.228,'g' : 2.015,'h' : 6.094,'i' : 6.966,'j' : 0.153,'k' : 0.772,'l' : 4.025,'m' : 2.406,
'n' : 6.749,'o' : 7.507,'p' : 1.929,'q' : 0.095,'r' : 5.987,'s' : 6.327,'t' : 9.056,'u' : 2.758,'v' : 0.978,'w' : 2.360,'x' : 0.15,'y' : 1.974,'z' : 0.074,}

if __name__ == '__main__':
    vigenereMatrix = createMatrix()
    dicAlpha = createDicAlpha()
    app = wx.App()
    frm = ScGuiMainFrame(None)
    frm.Show()
    app.MainLoop()
