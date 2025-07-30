from MOJIZA.engine.server import HTML
# from python_review.backend_html import *

def fullpage():
    page = HTML(title_document="Full HTML Elements Example")

    # CSS yaratish va qo'shish
    # css = """
    # body { font-family: Arial, sans-serif; }
    # header, footer { background-color: #f1f1f1; padding: 20px; text-align: center; }
    # nav ul { list-style-type: none; padding: 0; }
    # nav ul li { display: inline; margin-right: 10px; }
    # main { margin: 20px; }
    # section, article, aside { margin-bottom: 20px; }
    # table { width: 100%; border-collapse: collapse; }
    # table, th, td { border: 1px solid black; }
    # th, td { padding: 10px; text-align: left; }
    # """
    css = """
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    body {
        font-family: 'Segoe UI', sans-serif;
        background-color: #121212;
        color: #f5f5f5;
        line-height: 1.6;
        padding: 20px;
    }

    a {
        color: #1DB954;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    header, footer {
        background-color: #1c1c1c;
        padding: 20px;
        text-align: center;
        border-bottom: 2px solid #2c2c2c;
    }

    header h1 {
        color: #f5f5f5;
        font-size: 2rem;
    }

    nav ul {
        list-style-type: none;
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 15px;
    }

    nav ul li a {
        color: #f5f5f5;
        font-weight: bold;
        padding: 8px 12px;
        border-radius: 6px;
        transition: background 0.3s;
    }

    nav ul li a:hover {
        background: #1DB954;
        color: black;
    }

    main {
        padding: 30px;
        background-color: #181818;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        margin-top: 30px;
    }

    .section {
        margin-bottom: 40px;
    }

    h2, h3 {
        color: #1DB954;
        margin-bottom: 10px;
    }

    p, li, dd {
        color: #dcdcdc;
        font-size: 1rem;
    }

    input, textarea, button, select {
        width: 100%;
        padding: 12px;
        margin-top: 10px;
        border-radius: 6px;
        border: 1px solid #333;
        background-color: #2a2a2a;
        color: #fff;
        font-size: 1rem;
    }

    input:focus, textarea:focus {
        border-color: #1DB954;
        outline: none;
    }

    button {
        background-color: #1DB954;
        color: black;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    button:hover {
        background-color: #17a74a;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        background-color: #222;
        color: #fff;
        margin-top: 20px;
    }

    th, td {
        border: 1px solid #333;
        padding: 12px;
        text-align: left;
    }

    th {
        background-color: #333;
    }

    figure img {
        max-width: 100%;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }

    .aside {
        background-color: #1f1f1f;
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
    }

    details {
        background-color: #242424;
        padding: 12px;
        border-radius: 6px;
        margin-top: 20px;
        color: #ccc;
    }

    dialog {
        background-color: #1e1e1e;
        color: #f5f5f5;
        border: 1px solid #333;
        padding: 20px;
        border-radius: 10px;
        width: 90%;
        max-width: 400px;
    }

    footer p {
        color: #aaa;
        font-size: 0.85rem;
    }

    @media (max-width: 768px) {
        nav ul {
            flex-direction: column;
            gap: 10px;
        }

        main {
            padding: 20px;
        }

        table, th, td {
            font-size: 0.9rem;
        }
    }
    """

    page.add_styles(css)


    # Header
    header = page.header(h_id="main-header", h_class="header")
    header.h1("Full HTML Elements Example")
    header.nav().ul(
        header.li().a("Home", href="/"),
        header.li().a("document", href="/doc"),
        header.li().a("game", href="/GAME"),
        header.li().a("form test", href="/home")
    )

    # Main Content
    main = page.main()

    main.input(type="color")
    # Section: Article
    section_article = main.section(h_id="article-section", h_class="section")
    section_article.h2("Article Section")
    section_article.article(
        section_article.h3("Understanding MOJIZA Framework"),
        section_article.p(
            "MOJIZA is a custom Python web framework designed to simplify web development by allowing UI creation through Python code."),
        section_article.figure(
            section_article.img(src="https://via.placeholder.com/150", alt="Sample Image"),
            section_article.figcaption("Figure 1: Sample Image")
        ),
        section_article.footer("Article footer information.")
    )

    # Section: Sidebar (Aside)
    section_aside = main.aside(h_id="sidebar", h_class="aside")
    section_aside.h2("Sidebar")
    section_aside.p("This is a sidebar with additional information.")
    section_aside.nav(
        section_aside.ul(
            section_aside.li(section_aside.a("Link 1", href="#")),
            section_aside.li(section_aside.a("Link 2", href="#")),
            section_aside.li(section_aside.a("Link 3", href="#"))
        )
    )

    # Section: Forms
    section_form = main.section(h_id="form-section", h_class="section")
    section_form.h2("Contact Us")
    form = section_form.form(action="/submit", method="post")
    form.label("Name:",for_ ="name")
    form.input_tag(type="text", id="name", name="name", required=True)
    form.label("Email:",for_ ="email")
    form.input_tag(type="email", id="email", name="email", required=True)
    form.label("Message:",for_ ="message")
    form.textarea_tag(id="message", name="message", rows="4", cols="50")
    form.button_tag("Submit", type="submit")

    # Section: Tables
    section_table = main.section(h_id="table-section", h_class="section")
    section_table.h2("Sample Table")
    table = section_table.table_tag(h_id="data-table", h_class="table")
    table.caption("User Data")
    table.thead(
        table.tr(
            table.th("Name"),
            table.th("Age"),
            table.th("City")
        )
    )
    table.tbody(
        table.tr(
            table.td_tag("Alice"),
            table.td_tag("30"),
            table.td_tag("New York")
        ),
        table.tr(
            table.td_tag("Bob"),
            table.td_tag("25"),
            table.td_tag("Los Angeles")
        ),
        table.tr(
            table.td_tag("Charlie"),
            table.td_tag("35"),
            table.td_tag("Chicago")
        )
    )
    table.tfoot(
        table.tr(
            table.th("Total"),
            table.th("3 Users"),
            table.th("")
        )
    )

    # Section: Multimedia
    section_multimedia = main.section(h_id="multimedia-section", h_class="section")
    section_multimedia.h2("Multimedia Content")
    section_multimedia.video(src="https://www.w3schools.com/html/mov_bbb.mp4", controls=True, width="320")
    section_multimedia.audio(src="https://www.w3schools.com/html/horse.mp3", controls=True)

    # Section: Lists
    section_lists = main.section(h_id="lists-section", h_class="section")
    section_lists.h2("Lists")
    section_lists.ul(
        section_lists.li("Unordered List Item 1"),
        section_lists.li("Unordered List Item 2"),
        section_lists.li("Unordered List Item 3")
    )
    section_lists.ol(
        section_lists.li("Ordered List Item 1"),
        section_lists.li("Ordered List Item 2"),
        section_lists.li("Ordered List Item 3")
    )

    # Section: Definitions and Abbreviations
    section_defs = main.section(h_id="definitions-section", h_class="section")
    section_defs.h2("Definitions and Abbreviations")
    section_defs.dl(
        section_defs.dt("HTML"),
        section_defs.dd("HyperText Markup Language"),
        section_defs.dt("CSS"),
        section_defs.dd("Cascading Style Sheets"),
        section_defs.dt("JS"),
        section_defs.dd("JavaScript")
    )

    # Section: Interactive Elements
    section_interactive = main.section(h_id="interactive-section", h_class="section")
    section_interactive.h2("Interactive Elements")
    section_interactive.details(
        section_interactive.summary("More Information"),
        section_interactive.p("This section contains additional information that can be toggled.")
    )
    section_interactive.dialog(open=True, id="dialog-example")
    section_interactive.p("This is a dialog element.")
    section_interactive.button("Close Dialog", onclick="document.getElementById('dialog-example').close();")

    # Section: Semantic Elements
    section_semantic = main.section(h_id="semantic-section", h_class="section")
    section_semantic.h2("Semantic Elements")
    section_semantic.article(
        section_semantic.h3("Article"),
        section_semantic.p("This is an article element, which is used to represent a self-contained composition.")
    )
    section_semantic.aside(
        section_semantic.h3("Aside"),
        section_semantic.p("This aside contains information related to the main content.")
    )
    section_semantic.section(
        section_semantic.h3("Section"),
        section_semantic.p("This is a section element, used to define sections within the document.")
    )

    # Section: Meta Information
    section_meta = main.section(h_id="meta-section", h_class="section")
    section_meta.h2("Meta Information")
    section_meta.p(
        "Meta information is generally placed within the head element, but can also be included within the body.")
    section_meta.data_tag(value="12345", name="data-example", id="data-example")
    section_meta.output(value="Output Element Example")

    # Footer
    footer = page.footer(h_id="main-footer", h_class="footer")
    footer.p("© 2024 MOJIZA Framework. All rights reserved.")
    footer.p("Created by Muhiddinov Abdulhodiy.")

    # Scripts
    page.add_script("""
    // Example JavaScript
    console.log('Full Page Loaded');
    """)

    return page.end(AUTHOR="Muhiddinov Abdulhodiy")

def newpage():
    page = HTML(title_document = "new page for mojiza test")
    page.div(h_class="ho").p("hello")
    list_of_numbers = [i for i in range(100)]

    page.div(h_class="test").p(f"{list_of_numbers}")

    for i in range(100):
        page.div(h_class = "test-with-for").p(f"{i}")
    return page.end(AUTHOR='Muhiddinov Abdulhodiy')




def login_view():
    page = HTML(title_document="Login Page - Mojiza Framework")

    # CSS qo‘shamiz
    css = """
    body { font-family: sans-serif; background: #f4f4f4; }
    .container {
        max-width: 400px;
        margin: auto;
        background: #fff;
        padding: 30px;
        margin-top: 100px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    input, button {
        width: 100%;
        padding: 10px;
        margin-top: 10px;
    }
    """
    page.add_styles(css)

    # container
    div = page.div(h_class="container")

    # header
    div.h2("Login to Your Account")
    div.p("Welcome back! Please enter your credentials.")

    # form
    form = div.form(action="/", method="post")

    form.label("Username", for_="username")
    form.input(type="text", name="username", id="username", placeholder="e.g. thony123", required=True)

    form.label("Password", for_="password")
    form.input(type="password", name="password", id="password", placeholder="Your secret...", required=True)

    form.button("Login", type="submit")

    # Footer
    footer = page.footer()
    footer.p("© 2025 Mojiza Framework. Coded with ❤️ by Thony.")

    # Script (optional)
    page.add_script("""
    console.log("Login form loaded via Mojiza 🔥");
    """)

    return page.end(AUTHOR="Thony - Future Senior Dev 😎")


from .backend_html import project_home, guess_number_page, mojiza_mtml_documentation

project_home()
mojiza_mtml_documentation()


