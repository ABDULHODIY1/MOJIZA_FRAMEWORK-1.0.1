# MOJIZA FRAMEWORK

- #### -version 0.0.1
***

`MOJIZA` — bu Python asosidagi zamonaviy, minimalistik va foydalanuvchi uchun qulay web framework. Bu framework orqali siz o'zingizning web sahifalaringizni oddiy, tushunarli va tez tarzda yaratishingiz mumkin.
***
[![MOJIZA Banner](/STATIC/mojza.png)](https://mojiza-doc-sitr.onrender.com/doc)
***
## 🚀 Xususiyatlar

-  HTML elementlarini Python'da deklarativ tarzda yaratish
-  Zamonaviy "Dark mode" dizayn
-  Tilni almashtirish tugmasi orqali O‘zbek va Ingliz tillarida ishlash
-  Framework ichida tayyor `engine` tuzilmasi
-  Dynamic `data` dict orqali elementlar avlodan chiqariladi
-  Minimal frontend + backend birlashtirish imkoni
- ️ API tarzida ishlatish imkoniyati
-  Django bilan integratsiya qilish mumkin (view → url)

## 📜Loixa Documentatsiyasi: 
***
[Document of Mojiza Framework](https://mojiza-doc-sitr.onrender.com/doc)
***
### ishlatish:
```bash
pip install mojiza==0.1.3b1
```
~~~
project faylingiz ichida app.py (yoki boshqa biron) nomdagi fayl oching va quydagilarni yozing:
~~~
```python
from MOJIZA.runer import main


if __name__ == "__main__":
    main()
```
~~~
va quyda keltrlgan kammandalarni ishlating:
~~~
### APP Generatsiya qilish:
```bash
python app.py generate -n appname
```
### appname icidagi views.py uchun example
```python
from MOJIZA.engine.server import HTML
from MOJIZA.static.make_static import Static
from urllib3 import request
import random

# Views will be written manually

def home(method, params):
    page = HTML(title_document="Mojiza Sahifa")
    page.img(src=Static("mojza.png"), alt="Mojiza logosi")
    page.video(src=Static("ajdar.mp4"), controls="true")
    page.h1("Hello")
    return page.end()


def guess_number_page(method, params):
    # Keep the secret in a module‑level var so it survives reloads
    if not hasattr(guess_number_page, "_secret"):
        guess_number_page._secret = random.randint(1, 100)

    page = HTML(title_document="🎲 Taxmin O'yini")
    page.link(rel="icon", href=Static("image/Sharingan_Kakashi.png"), type="image/png")

    page.add_styles("""
        body { font-family: Arial, sans-serif; padding: 20px; background: #f7f7f7; }
        .box { max-width: 400px; margin: auto; background: #fff; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        input, button { width: 100%; padding: 10px; margin-top: 10px; border-radius: 5px; }
        .msg { margin-top: 20px; font-weight: bold; text-align: center; }
    """)

    box = page.div(h_class="box")

    box.h1("1 dan 100 gacha sonni toping!", align="center")

    # Always render the form:
    form = box.form(action="/game", method="POST")
    form.input(type="number", name="guess", placeholder="Son kiriting", required=True, min="1", max="100")
    form.button("Yuborish", type="submit")

    if method == "POST":
        raw = params.get("guess", [""])[0]
        print(raw)
        print("PARAMS:",params)
        try:
            guess = int(raw)
            secret = guess_number_page._secret
            print("number of guests:",secret)
            print(raw, guess)

            js_code = '''
             let a = document.querySelector("#idx");
             '''

            if guess < secret:
                msg = "🔼 Kattaroq son kiriting!"
            elif guess > secret:
                msg = "🔽 Kichikroq son kiriting!"
            else:
                msg = f"🎉 To‘g‘ri topdingiz! Son: {secret}"
                guess_number_page._secret = random.randint(1, 100)

        except ValueError:
            msg = "❌ Iltimos, butun son kiriting."

        box.div(h_class="msg").p(msg)

    return page.end(AUTHOR="Thony")
```
### app name ichidagi urls.py uchun example test kodi:
```python
from MOJIZA.engine.routing import PAGE
from .views import home,guess_number_page

@PAGE('/')
def home_urls(method, params):
    return home(method, params)

@PAGE('/game')
def Test_game(method, params):
    return guess_number_page(method,params)

```

### ishga tushurish
```bash
python app.py generate -n run_script
```


loixa xali toliq bitrlmagan backend ustida hali ham ishlanmoqda!!
