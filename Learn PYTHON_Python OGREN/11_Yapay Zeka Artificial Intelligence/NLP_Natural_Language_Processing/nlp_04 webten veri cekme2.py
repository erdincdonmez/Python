# Şikayetvar'dan şikayetleri çekme
# pip install requests
# pip install BeautifulSoup4
# Veri çekilecek adres: https://www.sikayetvar.com/
# Kaynak : https://medium.com/kodluyoruz/python-beautiful-soup-k%C3%BCt%C3%BCphanesi-ile-i%CC%87nternetten-veri-%C3%A7ekme-1d5977c7e677

import requests # url adresinden bir şey almak için
from bs4 import BeautifulSoup as bs # metinden/xml/html’den ayıklama ve temizleme işlemleri için

# https://www.sikayetvar.com/ adresine gir, geliştirici seçenekleri için F12'ye bas, Alacağımız bilgilerin bulunduğu html elementlerinin class isimlerine bak.
# Bunları aşağıdaki gibi fonksiyonlara ekle.
site = "https://www.sikayetvar.com/"
while True:
    baslik = input('Baslik: ')
    # baslik = 'beko'
    if baslik=='q': break
    headers = {'User-Agent':(
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
      'AppleWebKit/537.36 (KHT, like Gecko) Chrome/39.0.2171.95 Safari/537.36)'         
    )}

    r = requests.get(site + baslik, headers=headers)

    if r.status_code != 200 : print('Bulunamadı')
    else: 
        soup = bs(r.content,'html.parser')
        entryler = soup.find('div',{"class":"brandsearch-card clearfix"}).find_all()
        # entryler = soup.find('div',{"class":"brandsearch-card clearfix"}).find_all('article')
        print('-'*20, 'ENTRYLER','-'*20,sep='\n')
    
        for num, entry in enumerate(entryler,1):
            yazar = entry.find('span','profil-name').get_text(strip=True)
            tarih = entry.find('span','time-history').get_text(strip=True)
            icerik = entry.find('span','card-text').get_text(strip=True)
            print('{}. {}\n\nyazar:{},tarih:{}'.format(num, icerik, yazar, tarih))
            print('='*25)

