ogrenci_lıstem = ["Ayten","Eymen","Demir"]    # Öğrenci isim ve  soy isimlerinin kaydedildigi sistem.
print(ogrenci_lıstem)

ekleme = input("ogrenci listesine eklemek istediğiniz İsim ve soyisim giriniz: ")  # Listeye öğrenci ekleme
ogrenci_lıstem.append(ekleme)
print(ogrenci_lıstem)
print("")



silme = input("Silmek istediğiniz öğrenci isim ve soyismi giriniz: ")  #Listeden öğrenci silme
ogrenci_lıstem.remove(silme) 
print(ogrenci_lıstem)


CokluEkleme = []          #Listeye birden fazla isim ekleme
sor=int(input("Kaç ogrenci ismi  eklemek istiyorsunuz: "))
for i in range(sor):
    n=input("Eklemek istediğiniz öğrenci isimlerini sıra ile giriniz: ")
    CokluEkleme.append(n)

ogrenci_lıstem.extend(CokluEkleme)
print(ogrenci_lıstem)


a=0
while a < len(ogrenci_lıstem):            #Listedeki isimleri yazdırma
    print(a+1,". isim:",ogrenci_lıstem[a])
    a+=1

ara = input("Hangi öğrencinin sıra numarasını öğrenmek istiyorsunuz? ")
for  j in range(len(ogrenci_lıstem)):
    if ara == ogrenci_lıstem[j]:
        print(ara,"isimli öğrencinin numarası :",j)


sor=int(input("Kaç isim silmek istiyorsunuz: "))     # Listeki birden fazla ismi silme
for i in range(sor):
    isim=input("Silmek istediğiniz isim ? ")
    for j in ogrenci_lıstem:
            if j == isim:
                ogrenci_lıstem.remove(isim)

print(ogrenci_lıstem)
