#%%
import numpy as np


array=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
a=array.reshape(3,4)
print("shape ",a.shape)#dizi matris şekli
print("dimention ", a.ndim)#dizi boyutu
print("data type ",a.dtype.name) #dizi değişken type i
print("size ",a.size)# dizi size i
print("type ",type(array))

b=np.zeros((3,4))#3,4 lük 0 dolu dizi belirtir
C=np.empty((3,4))#3,4 lük matrisi içi bos seklinde olusturur
d=np.arange(5,30,5)# 5 den 30 a kadar 5er 5 er diziye doldurur
e=np.linspace(5,30,5)#5 ile 30 arasında 5 adet değer ile doldurur.
#%%
#Basic operations
a=np.array([1,2,3])
b=np.array([4,5,6])

print(a+b)
print(a*b)
print(a.dot(b.T)) #a ile bnin transpozunu matris çarpımı yap
x=np.random.random((6,6))
print(x.sum())
print(x.max())
print(x.min())

print(x.sum(axis=0))# sütunları topla
print(x.sum(axis=1))#satırları topla

#%% Indexing and Slicing
import numpy as np
array=np.array([1,2,3,4,5,6,7,8,9])
print(array[0:4])
reverseArray=array[::-1]
print(reverseArray)

print(array[:,1]) #1. sütunda olan tüm satırları ver
print(array[1,2:4])#1. satırdaki 2. ve 3. sütunları ver
#%%
#shape manipulation
array=np.array([1,2,3],[4,5,6],[7,8,9])
a=array.ravel()#diziyi flat hale çeviriyor
array2=a.reshape(3,3)#reshape ediliyor

#Array birleştirme
arrayx=np.array([1,2,3],[4,5,6])
arrayy=np.array([6,7,8,],[9,1,2])
array1=np.vstack((arrayx,arrayy))
array2=np.hstack((arrayx,arrayy))
#%%
liste=[12,3,3,4,5,6,7]
array=np.array(liste)
liste2=list(array)
#listeyi array'e array'i listeye çevirme

