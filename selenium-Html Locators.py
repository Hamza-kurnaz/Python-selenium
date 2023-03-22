#HTML, HTML Locators ve Selenium'da Aksiyonlar örnekleriyle birlikte açıklamalar:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Örnek Sayfa</title>   
</head>
<body>
    <h1>Merhaba Dünya!</h1>     
    <p>Benim adım Örnek Sayfa ve ben bir HTML sayfasıyım.</p>   
    <img src="ornek-resim.jpg" alt="Örnek Resim">   
    <a href="https://www.google.com">Google'a Git</a>  
</body>
</html>
```

# Bu HTML kodu, bir web sayfasının temel yapısını ve öğelerini içerir. Başlık, paragraf, resim ve bağlantılar gibi öğeler etiketler yardımıyla oluşturulur.

HTML Locators örneği:

```python
from selenium import webdriver

driver = webdriver.Chrome()   # Tarayıcıyı başlat

driver.get("https://www.example.com")   # Örnekleme web sayfasını aç

# Metin kutusunu bul ve veri gönder
metin_kutusu = driver.find_element_by_css_selector("#kullanici-adi")
metin_kutusu.send_keys("ornek-kullanici-adi")
```

#Bu Python kodu, Selenium ile bir web sayfasındaki öğeleri otomatik olarak bulmak için CSS seçicilerini kullanır. find_element_by_css_selector() fonksiyonu, bir CSS seçici kullanarak bir öğeyi bulur. send_keys() fonksiyonu, bir öğeye metin göndermek için kullanılır.

Selenium'da Aksiyonlar örneği:

```python
from selenium import webdriver

driver = webdriver.Chrome()   # Tarayıcıyı başlat

driver.get("https://www.example.com")   # Örnekleme web sayfasını aç

# Düğmeye tıkla
dugme = driver.find_element_by_id("ornek-dugme")
dugme.click()
```

#Bu Python kodu, Selenium ile bir web sayfasındaki öğeleri otomatik olarak kontrol etmek için click() fonksiyonunu kullanır. find_element_by_id() fonksiyonu, bir ID kullanarak bir öğeyi bulur. click() fonksiyonu, bir öğeye tıklamak için kullanılır.
