#%%
# normal fonksiyon tanımlama
def Carpma(a,b):
    return a*b
#%%
#çoklu parametre alan fonksiyon
def FlexibleFunc(a,b,*args):
    print(a)
    print(b)
    print(args)
    

#%%
#Lambda Fonksiyon
def Hesap(a):
    return a*a
sonuc= lambda a:a*a

print(sonuc)
#%%

