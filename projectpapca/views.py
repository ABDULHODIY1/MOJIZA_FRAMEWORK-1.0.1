# projectpapca/views.py

from MOJIZA.engine.server import HTML


def fullpage():
    page = HTML(title_document="Full HTML Elements Example")

    # CSS yaratish va qo'shish
    css = """
    body { font-family: Arial, sans-serif; }
    header, footer { background-color: #f1f1f1; padding: 20px; text-align: center; }
    nav ul { list-style-type: none; padding: 0; }
    nav ul li { display: inline; margin-right: 10px; }
    main { margin: 20px; }
    section, article, aside { margin-bottom: 20px; }
    table { width: 100%; border-collapse: collapse; }
    table, th, td { border: 1px solid black; }
    th, td { padding: 10px; text-align: left; }

    """
    page.add_styles(css)

    # Header
    header = page.header(h_id="main-header", h_class="header")
    header.h1("Full HTML Elements Example")
    header.nav(
        header.ul(
            header.li(header.a("Home", href="/")),
            header.li(header.a("About", href="/about")),
            header.li(header.a("FAQ", href="/faq")),
            header.li(header.a("Full Page", href="/fullpage"))
        )
    )

    # Main Content
    main = page.main()

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

