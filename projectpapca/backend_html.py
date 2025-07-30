from MOJIZA.engine.server import HTML
import random

def project_home():
    page = HTML(title_document = "new page for mojiza test")
    page.div(h_class="ho").h1("hello")
    list_of_numbers = [i for i in range(100)]
    page.div(h_class="test").p(f"{list_of_numbers}")
    return page.end()




def guess_number_page(method, params):
    # Keep the secret in a module‑level var so it survives reloads
    if not hasattr(guess_number_page, "_secret"):
        guess_number_page._secret = random.randint(1, 100)

    page = HTML(title_document="🎲 Taxmin O'yini")

    page.add_styles("""
        body { font-family: Arial, sans-serif; padding: 20px; background: #f7f7f7; }
        .box { max-width: 400px; margin: auto; background: #fff; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        input, button { width: 100%; padding: 10px; margin-top: 10px; border-radius: 5px; }
        .msg { margin-top: 20px; font-weight: bold; text-align: center; }
    """)

    box = page.div(h_class="box")

    box.h1("1 dan 100 gacha sonni toping!", align="center")

    # Always render the form:
    form = box.form(action="/GAME", method="POST")
    form.input(type="number", name="guess", placeholder="Son kiriting", required=True, min="1", max="100")
    form.button("Yuborish", type="submit")

    # If it was a POST, check the guess
    if method == "POST":
        raw = params.get("guess", [""])[0]
        try:
            guess = int(raw)
            secret = guess_number_page._secret
            # print("number of guests:",secret)

            js_code = '''
             let a = document.querySelector("#idx");
             '''

            if guess < secret:
                msg = "🔼 Kattaroq son kiriting!"
            elif guess > secret:
                msg = "🔽 Kichikroq son kiriting!"
            else:
                msg = f"🎉 To‘g‘ri topdingiz! Son: {secret}"
                # reset for next game
                guess_number_page._secret = random.randint(1, 100)

        except ValueError:
            msg = "❌ Iltimos, butun son kiriting."

        box.div(h_class="msg").p(msg)

    return page.end(AUTHOR="Thony")

from MOJIZA.engine.server import HTML


# def mojiza_mtml_documentation():
#     page = HTML(title_document="MTML (Mojiza HTML) Documentation")
#
#     page.head()
#     page.title("MTML - Mojiza HTML Full Documentation")
#     page.meta(charset="UTF-8")
#     page.meta(name="description", content="Full documentation for MTML...")
#     page.meta(name="keywords", content="MTML, Mojiza, HTML, Python")
#     page.meta(name="author", content="thony")
#     page.meta(
#         charset="UTF-8",
#         name="description",
#         content="Full documentation for MTML (Mojiza HTML) - a lightweight markup syntax used in Mojiza Framework."
#     )
#     page.meta(
#         name="keywords",
#         content="MTML, Mojiza, Mojiza Framework, Mojiza HTML, Python Web Framework, Custom HTML"
#     )
#     page.meta(name="author", content="Muhiddinov Abdulhodiy")
#
#     page.h1("📚 MTML (Mojiza HTML) Full Documentation")
#     page.p("MTML is a lightweight, Mojiza-specific syntax for writing HTML components using Python.")
#
#     page.h2("🔧 Getting Started")
#     page.p("To use MTML, simply import HTML from MOJIZA.engine.server and create an instance.")
#
#     page.code('''
# from MOJIZA.engine.server import HTML
#
# page = HTML(title_document="Hello MTML")
#     ''')
#
#     page.h2("📄 Basic Page Structure")
#     page.code('''
# page.head(title="My First Page")
# page.meta(charset="UTF-8", name="description", content="My Mojiza Page")
# page.h1("Welcome to Mojiza")
# page.p("This page is built using MTML syntax.")
#     ''')
#
#     page.h2("🔠 Text Elements")
#     page.ul([
#         "h1(title)",
#         "h2(title)",
#         "h3(title)",
#         "p(text)",
#         "strong(text)",
#         "em(text)"
#     ])
#
#     page.h2("🔘 Buttons")
#     page.code('''
# page.button("Click Me", onclick="alert('Hello World!')")
#     ''')
#
#     page.h2("🖼️ Images")
#     page.code('''
# page.img(src="/static/image.png", alt="My Image", width="100%")
#     ''')
#
#     page.h2("🔗 Links")
#     page.code('''
# page.a("Visit Google", href="https://google.com", target="_blank")
#     ''')
#
#     page.h2("📦 Containers & Layout")
#     page.code('''
# page.div("Content inside div")
# page.section("This is a section")
# page.article("Article content")
# page.header("Header content")
# page.footer("Footer content")
#     ''')
#
#     page.h2("📃 Lists")
#     page.code('''
# page.ul(["Item 1", "Item 2", "Item 3"])
# page.ol(["Step 1", "Step 2", "Step 3"])
#     ''')
#
#     page.h2("📁 Forms")
#     page.code('''
# page.form(method="POST", action="/submit")
# page.input(type="text", name="username", placeholder="Enter name")
# page.input(type="submit", value="Send")
#     ''')
#
#     page.h2("🎨 Style & Scripts")
#     page.code('''
# page.style("""
# body {
#     background-color: #f0f0f0;
#     font-family: sans-serif;
# }
# """)
#
# page.script("""
# function greet() {
#     alert("Hello from MTML!");
# }
# """)
#     ''')
#
#     page.h2("🧩 Custom Components")
#     page.code('''
# def custom_box(content):
#     return f"<div class='box'>{content}</div>"
#
# page.add(custom_box("This is a custom box!"))
#     ''')
#
#     page.h2("🧠 Tips")
#     page.ul([
#         "All HTML methods follow standard HTML naming.",
#         "You can extend MTML with your own Python functions.",
#         "You can use loops and conditions to dynamically generate elements."
#     ])
#
#     page.h2("🚀 SEO Best Practices")
#     page.ul([
#         "Use relevant <title> and <meta> tags",
#         "Keep content structured (use headings wisely)",
#         "Avoid inline styles for better performance"
#     ])
#
#     page.h2("📦 Final Example")
#     page.code('''
# from MOJIZA.engine.server import HTML
#
# def final_page():
#     page = HTML(title_document="Final MTML Page")
#     page.head(title="Welcome to My MTML Page")
#     page.meta(name="description", content="This is a fully working MTML page")
#     page.h1("🎉 Success!")
#     page.p("You now know how to use MTML in Mojiza Framework.")
#     return page.render()
#     ''')
#
#     return page.end()

from MOJIZA.engine.server import HTML

def mojiza_mtml_documentation():
    page = HTML(title_document="🌑 MTML Documentation | Mojiza", path="/doc")

    # Dark mode styling
    page.style("""
    body {
        background-color: #111;
        color: #ddd;
        font-family: 'Segoe UI', sans-serif;
        padding: 40px;
    }
    h1, h2 {
        color: #BB86FC;
    }
    .block {
        background-color: #1e1e1e;
        padding: 20px;
        margin: 20px 0;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.5);
    }
    .method {
        color: #03DAC6;
        font-weight: bold;
    }
    .desc {
        color: #aaa;
        margin-bottom: 10px;
    }
    code {
        display: block;
        background: #2b2b2b;
        color: #e0e0e0;
        padding: 15px;
        border-radius: 6px;
        overflow-x: auto;
        font-size: 15px;
        margin-top: 10px;
    }
    """)

    page.head()
    page.meta(charset="UTF-8")
    page.meta(name="description", content="Full documentation for MTML (Mojiza HTML) — a Pythonic HTML rendering engine.")
    page.meta(name="keywords", content="Mojiza, MTML, Python HTML, web framework, dark theme")
    page.meta(name="author", content="Thony")

    page.h1("📘 Mojiza Framework — MTML Full Documentation")

    data = [
        {
            "title": "🎬 Getting Started",
            "desc": "Import HTML class and initialize a new page.",
            "code": '''from MOJIZA.engine.server import HTML \n
             page = HTML(title_document="My First MTML Page")'''
        },
        {
            "title": "🧠 Head & Meta Tags",
            "desc": "Define metadata and SEO-related headers.",
            "code": '''page.head(title="Mojiza App")
page.meta(charset="UTF-8")
page.meta(name="description", content="Mojiza FTW!")'''
        },
        {
            "title": "📦 Containers",
            "desc": "Wrap content using structural tags like div, section, etc.",
            "code": '''page.div(h_class="container").p("Hello from inside a div!")'''
        },
        {
            "title": "📑 Text Elements",
            "desc": "Use headings and paragraph tags to add content.",
            "code": '''page.h1("Heading 1")
page.h2("Heading 2")
page.p("Paragraph text goes here.")'''
        },
        {
            "title": "🔗 Links & Images",
            "desc": "Add links and images to your site.",
            "code": '''page.a("Google", href="https://google.com", target="_blank")
page.img(src="/static/image.png", alt="My image", width="100%")'''
        },
        {
            "title": "📋 Lists",
            "desc": "Create unordered and ordered lists.",
            "code": '''page.ul(["Apple", "Banana", "Cherry"])
page.ol(["Step 1", "Step 2", "Step 3"])'''
        },
        {
            "title": "📤 Forms",
            "desc": "Create interactive forms with inputs and buttons.",
            "code": '''form = page.form(action="/submit", method="POST")
form.input(type="text", name="username", placeholder="Enter your name")
form.button("Submit", type="submit")'''
        },
        {
            "title": "🎨 Styling & Scripts",
            "desc": "Inject custom CSS or JavaScript into the page.",
            "code": '''page.add_style("body { background-color: black; }")
page.add_script("console.log('Hello MTML!')")'''
        },
        {
            "title": "🧩 Custom Functions",
            "desc": "Use Python functions to modularize HTML generation.",
            "code": '''def badge(txt):
    return f"<span class='badge'>{txt}</span>"

page.add(badge("New!"))'''
        },
        {
            "title": "🧪 Rendering",
            "desc": "Finish page rendering and return HTML.",
            "code": '''return page.end()'''
        }
    ]

    for section in data:
        block = page.div(h_class="block")
        block.h2(section["title"])
        block.p(section["desc"], h_class="desc")
        block.code(section["code"])

    return page.end()

