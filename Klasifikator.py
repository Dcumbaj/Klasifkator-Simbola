#!/usr/bin/env python
# coding: utf-8

# In[841]:


import cv2 as cv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import randint


# In[842]:


ACCIDENTAL_DoubSharp = []
for i in range (1,497):
    ACCIDENTAL_DoubSharp.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_DoubSharp/" + "agata_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_DoubSharp.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_DoubSharp/" + "agnes_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_DoubSharp.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_DoubSharp/" + "ali_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_DoubSharp.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_DoubSharp/" + "anna_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_DoubSharp.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_DoubSharp/" + "josep_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_DoubSharp.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_DoubSharp/" + "juan_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_DoubSharp.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_DoubSharp/" + "marcal_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_DoubSharp.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_DoubSharp/" + "xotazu_BN_" +  str(i) + ".bmp"))
    
    
ACCIDENTAL_DoubSharp = np.array(ACCIDENTAL_DoubSharp)
ACCIDENTAL_DoubSharp2 = [x for x in ACCIDENTAL_DoubSharp if x is not None]
print("Prije uzimanja None vrijednosti:", len(ACCIDENTAL_DoubSharp))
print("Poslije uzimanja None vrijednosti:",len(ACCIDENTAL_DoubSharp2))

plt.figure()
plt.imshow(ACCIDENTAL_DoubSharp2[30])
plt.colorbar()
plt.grid(False)
plt.title('DoubSharp200')
plt.show()


# In[843]:


PovecanjeTonaX2_Labela = np.repeat(0, 497)
print(len(PovecanjeTonaX2_Labela))
print(PovecanjeTonaX2_Labela)


# In[844]:


ACCIDENTAL_Flat = []
for i in range (1,517):
    ACCIDENTAL_Flat.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Flat/" + "agata_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Flat.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Flat/" + "agnes_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Flat.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Flat/" + "ali_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Flat.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Flat/" + "anna_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Flat.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Flat/" + "josep_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Flat.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Flat/" + "juan_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Flat.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Flat/" + "marcal_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Flat.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Flat/" + "xotazu_BN_" +  str(i) + ".bmp"))
    
ACCIDENTAL_Flat = np.array(ACCIDENTAL_Flat)
ACCIDENTAL_Flat2 = [x for x in ACCIDENTAL_Flat if x is not None]
print("Prije uzimanja None vrijednosti:", len(ACCIDENTAL_Flat))
print("Poslije uzimanja None vrijednosti:",len(ACCIDENTAL_Flat2))

plt.figure()
plt.imshow(ACCIDENTAL_Flat2[30])
plt.colorbar()
plt.grid(False)
plt.title('Flat')
plt.show()


# In[845]:


NiziTon_Labela = np.repeat(1, 517)
print(len(NiziTon_Labela))
print(NiziTon_Labela)


# In[846]:


ACCIDENTAL_Natural = []
for i in range (1,471):
    ACCIDENTAL_Natural.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Natural/" + "agata_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Natural.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Natural/" + "agnes_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Natural.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Natural/" + "ali_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Natural.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Natural/" + "anna_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Natural.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Natural/" + "josep_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Natural.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Natural/" + "juan_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Natural.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Natural/" + "marcal_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Natural.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Natural/" + "xotazu_BN_" +  str(i) + ".bmp"))
    
ACCIDENTAL_Natural = np.array(ACCIDENTAL_Natural)
ACCIDENTAL_Natural2 = [x for x in ACCIDENTAL_Natural if x is not None]
print("Prije uzimanja None vrijednosti:", len(ACCIDENTAL_Natural))
print("Poslije uzimanja None vrijednosti:",len(ACCIDENTAL_Natural2))

plt.figure()
plt.imshow(ACCIDENTAL_Natural2[30])
plt.colorbar()
plt.grid(False)
plt.title('Natural')
plt.show()


# In[847]:


PrirodniTon_Labela = np.repeat(2, 470)
print(len(PrirodniTon_Labela))
print(PrirodniTon_Labela)


# In[848]:


ACCIDENTAL_Sharp = []
for i in range (1,481):
    ACCIDENTAL_Sharp.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Sharp/" + "agata_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Sharp.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Sharp/" + "agnes_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Sharp.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Sharp/" + "ali_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Sharp.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Sharp/" + "anna_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Sharp.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Sharp/" + "josep_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Sharp.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Sharp/" + "juan_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Sharp.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Sharp/" + "marcal_BN_" +  str(i) + ".bmp"))
    ACCIDENTAL_Sharp.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/ACCIDENTAL_Sharp/" + "xotazu_BN_" +  str(i) + ".bmp"))
    
ACCIDENTAL_Sharp = np.array(ACCIDENTAL_Sharp)
ACCIDENTAL_Sharp2 = [x for x in ACCIDENTAL_Sharp if x is not None]
print("Prije uzimanja None vrijednosti:", len(ACCIDENTAL_Sharp))
print("Poslije uzimanja None vrijednosti:",len(ACCIDENTAL_Sharp2))

plt.figure()
plt.imshow(ACCIDENTAL_Sharp2[30])
plt.colorbar()
plt.grid(False)
plt.title('Sharp')
plt.show()


# In[849]:


Povisilica_Labela = np.repeat(3, 481)
print(len(Povisilica_Labela))
print(Povisilica_Labela)


# In[850]:


CLEF_Alto = []
for i in range (1,623):
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_agata_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_agnes_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_alicia_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_anna_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_anton_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_begonya_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_borja_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_edurad_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_gabriel_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_gemma_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_jilados_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_jordi_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_jrodriguez_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_monica_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_marsal_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_naxto_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_poal_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_raquel_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_silvana_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_josep_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_susana_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_juan_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_marcal_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do_xotazu_BN._" +  str(i) + ".bmp"))
    CLEF_Alto.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Alto/" + "do" +  str(i) + ".bmp"))
    
    
CLEF_Alto = np.array(CLEF_Alto)
CLEF_Alto2 = [x for x in CLEF_Alto if x is not None]
print("Prije uzimanja None vrijednosti:", len(CLEF_Alto))
print("Poslije uzimanja None vrijednosti:",len(CLEF_Alto2))

plt.figure()
plt.imshow(CLEF_Alto2[30])
plt.colorbar()
plt.grid(False)
plt.title('CLEF_Alto')
plt.show()


# In[851]:


Alto_Labela = np.repeat(4, 623)
print(len(Alto_Labela))
print(Alto_Labela)


# In[852]:


CLEF_Bass = []
for i in range (1,430):
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_agata_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_agnes_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_alicia_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_anna_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_anton_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_begonya_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_borja_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_edurad_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_gabriel_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_gemma_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_jilados_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_jordi_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_jrodriguez_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_monica_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_marsal_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_naxto_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_poal_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_raquel_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_silvana_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_josep_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_susana_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_juan_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_marcal_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa_xotazu_BN._" +  str(i) + ".bmp"))
    CLEF_Bass.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Bass/" + "fa" +  str(i) + ".bmp"))
    
    
CLEF_Bass = np.array(CLEF_Bass)
CLEF_Bass2 = [x for x in CLEF_Bass if x is not None]
print("Prije uzimanja None vrijednosti:", len(CLEF_Bass))
print("Poslije uzimanja None vrijednosti:",len(CLEF_Bass2))

plt.figure()
plt.imshow(CLEF_Bass2[1])
plt.colorbar()
plt.grid(False)
plt.title('CLEF_Bass')
plt.show()


# In[853]:


Bas_Labela = np.repeat(5, 430)
print(len(Bas_Labela))
print(Bas_Labela)


# In[854]:


CLEF_Trebble = []
for i in range (1,665):
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_agata_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_agnes_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_alicia_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_anna_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_anton_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_begonya_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_borja_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_edurad_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_gabriel_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_gemma_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_jilados_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_jordi_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_jrodriguez_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_monica_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_marsal_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_naxto_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_poal_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_raquel_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_silvana_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_josep_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_susana_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_juan_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_marcal_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol_xotazu_BN._" +  str(i) + ".bmp"))
    CLEF_Trebble.append(cv.imread("C:/Users/Dominik/Desktop/Slike/Music_Symbols/CLEF_Trebble/" + "sol" +  str(i) + ".bmp"))
    
    
CLEF_Trebble = np.array(CLEF_Trebble)
CLEF_Trebble2 = [x for x in CLEF_Trebble if x is not None]
print("Prije uzimanja None vrijednosti:", len(CLEF_Trebble))
print("Poslije uzimanja None vrijednosti:",len(CLEF_Trebble2))

plt.figure()
plt.imshow(CLEF_Trebble2[30])
plt.colorbar()
plt.grid(False)
plt.title('CLEF_Trebble')
plt.show()


# In[855]:


ViolinskiKljuc_Labela = np.repeat(6, 665)
print(len(ViolinskiKljuc_Labela))
print(ViolinskiKljuc_Labela)


# In[856]:


Slike = np.concatenate([ACCIDENTAL_DoubSharp2,ACCIDENTAL_Flat2,ACCIDENTAL_Natural2,ACCIDENTAL_Sharp2,CLEF_Alto2,CLEF_Bass2,CLEF_Trebble2])
len(Slike)


# In[857]:


Labele = np.concatenate([ViolinskiKljuc_Labela,Bas_Labela,Alto_Labela,Povisilica_Labela,PrirodniTon_Labela,NiziTon_Labela,PovecanjeTonaX2_Labela])
len(Labele)


# In[858]:


def get_labele(class_code):
    labele = {6:'Povećanje tona', 5: 'Niži Ton', 4:'Prirodan ton', 3:'Povisilica', 2:'Alto', 1:'Bas', 0:'Violinski Ključ'}

    return labele[class_code]


# In[859]:


class_imena = ['Violinski ključ','Niži Ton','Prirodan ton','Povisilica','Alto','Bas', 'Povećanje tona puta 2' ]


# In[860]:


plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(Slike[i], cmap=plt.cm.binary)
    plt.xlabel(class_imena[Labele[i]])
plt.show()


# In[861]:


f,ax = plt.subplots(5,5) 
f.subplots_adjust(0,0,3,3)
for i in range(0,5,1):
    for j in range(0,5,1):
        rnd_number = randint(0,len(Slike))
        ax[i,j].imshow(Slike[rnd_number])
        ax[i,j].set_title(get_labele(Labele[rnd_number]))
        ax[i,j].axis('off')


# In[862]:


from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D, BatchNormalization


# In[863]:


Slike = np.array(Slike)
Labele = np.array(Labele)
print (Slike.shape)
print (Labele.shape)


# In[864]:


Slike2 = []
for i in range(0,3683):
  image = cv.resize(Slike[i],(80,80))
  Slike2.append(image)
    
Slike3 = np.array(Slike2)
Slike3.shape


# In[865]:


model = Sequential() #sekvencijalni model


model.add(Conv2D(16, (3,3), input_shape = (80, 80, 3))) #Nakon Konvucijalnog sloja se mogu dodati aktivcacijski ili pooling sloj ovo je 2D  
model.add(Activation("relu")) #Rectify linear
model.add(MaxPooling2D(pool_size=(2,2)))  #Sveukupno prvi sloj

model.add(Conv2D(32, (3,3), activation='relu'))
model.add(BatchNormalization())

model.add(Dropout(0.3))

model.add(Conv2D(32, (3,3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(2,2))
model.add(Dropout(0.4))

model.add(Conv2D(64, (3,3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(2,2))
model.add(Dropout(0.5))


model.add(Conv2D(64, (3,3)))
model.add(Activation("relu")) 
model.add(MaxPooling2D(pool_size=(2,2))) # 2.sloj

model.add(Flatten())
model.add(Dense(64))#1D  3. sloj          


model.add(Dense(7, activation='softmax'))

model.compile(loss = "sparse_categorical_crossentropy",
             optimizer = "adam",
             metrics =['accuracy'])

treniraj = model.fit(Slike3,Labele,epochs=5,validation_split=0.30)


