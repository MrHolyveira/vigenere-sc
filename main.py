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

dicAplha
'''
if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = ScGuiMainFrame(None)
    frm.Show()
    app.MainLoop()'''