#description -? ovverding -> inheritance
class parents(object):#Valideyin mirasci
    def __init__(self,ad,soyad ):
        self.ad = ad
        self.soyad = soyad

class child(parents):#ovlad-> miras alan
    def __init__(self,ad, soyad,goz_rengi):#inheritance
        parents.__init__(self,ad , soyad)
        self.goz_rengi = goz_rengi

wrk = parents('Ali', 'Hasan')
print('\nMirasci')
print(f'Ad:{wrk.ad}')
print(f'Soyad:{wrk.soyad}')
wrk1 = child('Hasan', 'Bozkurt', 'blue')#ovverding 
print('\nMiras alan')
print(f'Ad:{wrk1.ad}')
print(f'Soyad:{wrk1.soyad}')
print(f'Goz_rengi:{wrk1.goz_rengi}')

