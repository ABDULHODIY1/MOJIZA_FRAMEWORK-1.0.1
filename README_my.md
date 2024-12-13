
# MOJIZA Framework Example: Full HTML Page

This README explains how to use the MOJIZA Framework to create a fully functional HTML page using Python. Below is a step-by-step guide to the framework's capabilities and usage.

---

## Overview

The **MOJIZA Framework** simplifies web development by enabling developers to create full HTML pages programmatically with Python code. This example demonstrates how to build a web page containing various HTML elements such as headers, footers, tables, forms, multimedia, and semantic elements.

---

## Requirements

To use this framework, ensure you have the following:

- Python 3.7 or higher.
- MOJIZA Framework installed.

Install MOJIZA Framework:

```bash
pip install mojiza-framework
```

---

## Project Structure

### File Location

The main functionality resides in the `views.py` file located in the `projectpapca/` directory.

### Code Description

The file defines a `fullpage()` function that generates an HTML page with the following sections:

1. **Header**
   - Contains the site title and navigation links.
2. **Main Content**
   - Articles with images and captions.
   - Sidebar with navigational links.
   - Forms for user input.
   - Tables displaying user data.
   - Multimedia elements (videos and audio).
   - Lists (ordered and unordered).
   - Definitions and abbreviations.
   - Interactive elements like dialogs and details.
   - Semantic elements (article, section, aside).
3. **Footer**
   - Contains copyright and author information.
4. **Styles and Scripts**
   - Inline CSS for styling and JavaScript for interactivity.

---

## Code Breakdown

### Importing Dependencies

The MOJIZA framework's `HTML` class is imported to build the web page:

```python
from MOJIZA.engine.server import HTML
```

### Generating the Web Page

The `fullpage()` function builds the entire HTML document using the following steps:

1. **Initialize the Page**

   ```python
   page = HTML(title_document="Full HTML Elements Example")
   ```

2. **Add CSS Styles**

   ```python
   css = """CSS content here"""
   page.add_styles(css)
   ```

3. **Create Header**

   ```python
   header = page.header(h_id="main-header", h_class="header")
   header.h1("Full HTML Elements Example")
   header.nav(
       header.ul(
           header.li(header.a("Home", href="/")),
           header.li(header.a("About", href="/about"))
       )
   )
   ```

4. **Main Content Sections**
   Example for creating an article section:

   ```python
   section_article = main.section(h_id="article-section", h_class="section")
   section_article.h2("Article Section")
   section_article.article(
       section_article.h3("Understanding MOJIZA Framework"),
       section_article.p("Explanation text here..."),
   )
   ```

5. **Footer**

   ```python
   footer = page.footer(h_id="main-footer", h_class="footer")
   footer.p("© 2024 MOJIZA Framework. All rights reserved.")
   ```

6. **Add Scripts**

   ```python
   page.add_script("""
   console.log('Full Page Loaded');
   """)
   ```

7. **Render the Page**

   ```python
   return page.end(AUTHOR="Muhiddinov Abdulhodiy")
   ```

---

## Example Output

The generated HTML page includes:

- Navigation with links.
- A contact form.
- A styled table with user data.
- Multimedia elements (video and audio).
- Semantic HTML5 elements (section, article, aside).
- Interactive features (details and dialog).

---

## Running the Code

1. Place the `views.py` file in your project.
2. Use your web server (e.g., Flask, Django) to call the `fullpage()` function.
3. Open the page in your browser.

---

## Author

Created by **Muhiddinov Abdulhodiy**.

---

**For more details, visit the** [MOJIZA Framework Documentation](#).
