# MOJIZA/engine/server.py

import sys
import os
import importlib
import logging
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from http.server import BaseHTTPRequestHandler
from inspect import signature
import logging
import traceback



logger = logging.getLogger("MOJIZA")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HTMLElement:
    def __init__(self, tag, **attrs):
        self.tag = tag
        self.attrs = {k[2:]: v for k, v in attrs.items() if k.startswith('h_')}
        self.children = []
        self.content = ''
        for k, v in attrs.items():
            if not k.startswith('h_'):
                self.attrs[k] = v

    def __call__(self, *args):
        for c in args:
            if isinstance(c, (HTMLElement, str)):
                self.children.append(c)
        return self

    def __getattr__(self, tag):
        def create(*args, **attrs):
            el = HTMLElement(tag, **attrs)
            self.children.append(el)
            for c in args:
                if isinstance(c, (HTMLElement, str)):
                    el.children.append(c)
            return el
        return create

    def set_content(self, text):
        self.content = text
        return self

    def render(self, indent=0):
        sp = '    ' * indent
        attrs = ' '.join(f'{k}="{v}"' for k, v in self.attrs.items())
        if self.tag in ('meta', 'link', 'img', 'input', 'br', 'hr'):
            return f"{sp}<{self.tag} {attrs}/>\n"
        open_tag = f"<{self.tag}{' '+attrs if attrs else ''}>"
        html = f"{sp}{open_tag}\n"
        if self.content:
            html += f"{sp}    {self.content}\n"
        for c in self.children:
            html += c.render(indent+1) if isinstance(c, HTMLElement) else f"{sp}    {c}\n"
        html += f"{sp}</{self.tag}>\n"
        return html

class HTML:
    def __init__(self, title_document, lang="en", **attrs):
        self.doctype = "<!DOCTYPE html>"
        self.html = HTMLElement('html', h_lang=lang, **attrs)

        self.head = HTMLElement('head')
        self.html.children.append(self.head)

        meta_charset = HTMLElement('meta', h_charset="UTF-8")
        self.head.children.append(meta_charset)

        meta_viewport = HTMLElement('meta', h_name="viewport", h_content="width=device-width, initial-scale=1.0")
        self.head.children.append(meta_viewport)

        title = HTMLElement('title').set_content(title_document)
        self.head.children.append(title)

        self.body = HTMLElement('body')
        self.html.children.append(self.body)

        # self._initialize_elements()

    def __getattr__(self, tag_name):
        # Allow dynamic creation of any HTML tag
        def create_element(*args, **attrs):
            element = HTMLElement(tag_name, **attrs)
            self.body.children.append(element)
            for child in args:
                if isinstance(child, HTMLElement) or isinstance(child, str):
                    element.children.append(child)
            return element
        return create_element

    # Standart HTML elementlari uchun alohida metodlar
    def a(self, *args, **attrs):
        a = HTMLElement('a', **attrs)
        self.body.children.append(a)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                a.children.append(child)
        return a

    def abbr(self, *args, **attrs):
        abbr = HTMLElement('abbr', **attrs)
        self.body.children.append(abbr)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                abbr.children.append(child)
        return abbr

    def address(self, *args, **attrs):
        address = HTMLElement('address', **attrs)
        self.body.children.append(address)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                address.children.append(child)
        return address

    def area(self, *args, **attrs):
        area = HTMLElement('area', **attrs)
        self.body.children.append(area)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                area.children.append(child)
        return area

    def article(self, *args, **attrs):
        article = HTMLElement('article', **attrs)
        self.body.children.append(article)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                article.children.append(child)
        return article

    def aside(self, *args, **attrs):
        aside = HTMLElement('aside', **attrs)
        self.body.children.append(aside)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                aside.children.append(child)
        return aside

    def audio(self, *args, **attrs):
        audio = HTMLElement('audio', **attrs)
        self.body.children.append(audio)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                audio.children.append(child)
        return audio

    def b(self, *args, **attrs):
        b = HTMLElement('b', **attrs)
        self.body.children.append(b)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                b.children.append(child)
        return b

    def base(self, *args, **attrs):
        base = HTMLElement('base', **attrs)
        self.head.children.append(base)
        return base

    def bdi(self, *args, **attrs):
        bdi = HTMLElement('bdi', **attrs)
        self.body.children.append(bdi)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                bdi.children.append(child)
        return bdi

    def bdo(self, *args, **attrs):
        bdo = HTMLElement('bdo', **attrs)
        self.body.children.append(bdo)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                bdo.children.append(child)
        return bdo

    def blockquote(self, *args, **attrs):
        blockquote = HTMLElement('blockquote', **attrs)
        self.body.children.append(blockquote)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                blockquote.children.append(child)
        return blockquote

    def body(self, *args, **attrs):
        body = HTMLElement('body', **attrs)
        self.html.children.append(body)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                body.children.append(child)
        return body

    def br(self, *args, **attrs):
        br = HTMLElement('br', **attrs)
        self.body.children.append(br)
        return br

    def button(self, *args, **attrs):
        button = HTMLElement('button', **attrs)
        self.body.children.append(button)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                button.children.append(child)
        return button

    def canvas(self, *args, **attrs):
        canvas = HTMLElement('canvas', **attrs)
        self.body.children.append(canvas)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                canvas.children.append(child)
        return canvas

    def caption(self, *args, **attrs):
        caption = HTMLElement('caption', **attrs)
        self.body.children.append(caption)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                caption.children.append(child)
        return caption

    def cite(self, *args, **attrs):
        cite = HTMLElement('cite', **attrs)
        self.body.children.append(cite)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                cite.children.append(child)
        return cite

    def code(self, *args, **attrs):
        code = HTMLElement('code', **attrs)
        self.body.children.append(code)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                code.children.append(child)
        return code

    def col(self, *args, **attrs):
        col = HTMLElement('col', **attrs)
        self.body.children.append(col)
        return col

    def colgroup(self, *args, **attrs):
        colgroup = HTMLElement('colgroup', **attrs)
        self.body.children.append(colgroup)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                colgroup.children.append(child)
        return colgroup

    def data(self, *args, **attrs):
        data = HTMLElement('data', **attrs)
        self.body.children.append(data)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                data.children.append(child)
        return data

    def datalist(self, *args, **attrs):
        datalist = HTMLElement('datalist', **attrs)
        self.body.children.append(datalist)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                datalist.children.append(child)
        return datalist

    def dd(self, *args, **attrs):
        dd = HTMLElement('dd', **attrs)
        self.body.children.append(dd)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                dd.children.append(child)
        return dd

    def del_(self, *args, **attrs):
        del_elem = HTMLElement('del', **attrs)
        self.body.children.append(del_elem)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                del_elem.children.append(child)
        return del_elem

    def details(self, *args, **attrs):
        details = HTMLElement('details', **attrs)
        self.body.children.append(details)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                details.children.append(child)
        return details

    def dfn(self, *args, **attrs):
        dfn = HTMLElement('dfn', **attrs)
        self.body.children.append(dfn)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                dfn.children.append(child)
        return dfn

    def dialog(self, *args, **attrs):
        dialog = HTMLElement('dialog', **attrs)
        self.body.children.append(dialog)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                dialog.children.append(child)
        return dialog

    def div(self, *args, **attrs):
        div = HTMLElement('div', **attrs)
        self.body.children.append(div)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                div.children.append(child)
        return div

    def dl(self, *args, **attrs):
        dl = HTMLElement('dl', **attrs)
        self.body.children.append(dl)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                dl.children.append(child)
        return dl

    def dt(self, *args, **attrs):
        dt = HTMLElement('dt', **attrs)
        self.body.children.append(dt)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                dt.children.append(child)
        return dt

    def em(self, *args, **attrs):
        em = HTMLElement('em', **attrs)
        self.body.children.append(em)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                em.children.append(child)
        return em

    def embed(self, *args, **attrs):
        embed = HTMLElement('embed', **attrs)
        self.body.children.append(embed)
        return embed

    def fieldset(self, *args, **attrs):
        fieldset = HTMLElement('fieldset', **attrs)
        self.body.children.append(fieldset)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                fieldset.children.append(child)
        return fieldset

    def figcaption(self, *args, **attrs):
        figcaption = HTMLElement('figcaption', **attrs)
        self.body.children.append(figcaption)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                figcaption.children.append(child)
        return figcaption

    def figure(self, *args, **attrs):
        figure = HTMLElement('figure', **attrs)
        self.body.children.append(figure)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                figure.children.append(child)
        return figure

    def footer(self, *args, **attrs):
        footer = HTMLElement('footer', **attrs)
        self.body.children.append(footer)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                footer.children.append(child)
        return footer

    def form(self, *args, **attrs):
        form = HTMLElement('form', **attrs)
        self.body.children.append(form)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                form.children.append(child)
        return form

    def h1(self, text="", **attrs):
        h1 = HTMLElement('h1', **attrs).set_content(text)
        self.body.children.append(h1)
        return h1

    def h2(self, text="", **attrs):
        h2 = HTMLElement('h2', **attrs).set_content(text)
        self.body.children.append(h2)
        return h2

    def h3(self, text="", **attrs):
        h3 = HTMLElement('h3', **attrs).set_content(text)
        self.body.children.append(h3)
        return h3

    def h4(self, text="", **attrs):
        h4 = HTMLElement('h4', **attrs).set_content(text)
        self.body.children.append(h4)
        return h4

    def h5(self, text="", **attrs):
        h5 = HTMLElement('h5', **attrs).set_content(text)
        self.body.children.append(h5)
        return h5

    def h6(self, text="", **attrs):
        h6 = HTMLElement('h6', **attrs).set_content(text)
        self.body.children.append(h6)
        return h6

    def head(self, *args, **attrs):
        head = HTMLElement('head', **attrs)
        self.html.children.append(head)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                head.children.append(child)
        return head

    def hr(self, *args, **attrs):
        hr = HTMLElement('hr', **attrs)
        self.body.children.append(hr)
        return hr

    def html(self, *args, **attrs):
        html = HTMLElement('html', **attrs)
        self.html.children.append(html)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                html.children.append(child)
        return html

    def i(self, *args, **attrs):
        i = HTMLElement('i', **attrs)
        self.body.children.append(i)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                i.children.append(child)
        return i

    def iframe(self, *args, **attrs):
        iframe = HTMLElement('iframe', **attrs)
        self.body.children.append(iframe)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                iframe.children.append(child)
        return iframe

    def img(self, *args, **attrs):
        img = HTMLElement('img', **attrs)
        self.body.children.append(img)
        return img

    def input(self, *args, **attrs):
        input_elem = HTMLElement('input', **attrs)
        self.body.children.append(input_elem)
        return input_elem

    def ins(self, *args, **attrs):
        ins = HTMLElement('ins', **attrs)
        self.body.children.append(ins)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                ins.children.append(child)
        return ins

    def kbd(self, *args, **attrs):
        kbd = HTMLElement('kbd', **attrs)
        self.body.children.append(kbd)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                kbd.children.append(child)
        return kbd

    def label(self, *args, **attrs):
        label = HTMLElement('label', **attrs)
        self.body.children.append(label)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                label.children.append(child)
        return label

    def legend(self, *args, **attrs):
        legend = HTMLElement('legend', **attrs)
        self.body.children.append(legend)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                legend.children.append(child)
        return legend

    def li(self, *args, **attrs):
        li = HTMLElement('li', **attrs)
        self.body.children.append(li)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                li.children.append(child)
        return li

    def link(self, *args, **attrs):
        link = HTMLElement('link', **attrs)
        self.head.children.append(link)
        return link

    def main(self, *args, **attrs):
        main = HTMLElement('main', **attrs)
        self.body.children.append(main)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                main.children.append(child)
        return main

    def map(self, *args, **attrs):
        map_elem = HTMLElement('map', **attrs)
        self.body.children.append(map_elem)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                map_elem.children.append(child)
        return map_elem

    def mark(self, *args, **attrs):
        mark = HTMLElement('mark', **attrs)
        self.body.children.append(mark)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                mark.children.append(child)
        return mark

    def meta(self, *args, **attrs):
        meta = HTMLElement('meta', **attrs)
        self.head.children.append(meta)
        return meta

    def meter(self, *args, **attrs):
        meter = HTMLElement('meter', **attrs)
        self.body.children.append(meter)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                meter.children.append(child)
        return meter

    def nav(self, *args, **attrs):
        nav = HTMLElement('nav', **attrs)
        self.body.children.append(nav)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                nav.children.append(child)
        return nav

    def noscript(self, *args, **attrs):
        noscript = HTMLElement('noscript', **attrs)
        self.body.children.append(noscript)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                noscript.children.append(child)
        return noscript

    def object(self, *args, **attrs):
        object_elem = HTMLElement('object', **attrs)
        self.body.children.append(object_elem)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                object_elem.children.append(child)
        return object_elem

    def ol(self, *args, **attrs):
        ol = HTMLElement('ol', **attrs)
        self.body.children.append(ol)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                ol.children.append(child)
        return ol

    def optgroup(self, *args, **attrs):
        optgroup = HTMLElement('optgroup', **attrs)
        self.body.children.append(optgroup)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                optgroup.children.append(child)
        return optgroup

    def option(self, *args, **attrs):
        option = HTMLElement('option', **attrs)
        self.body.children.append(option)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                option.children.append(child)
        return option

    def output(self, *args, **attrs):
        output = HTMLElement('output', **attrs)
        self.body.children.append(output)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                output.children.append(child)
        return output

    def p(self, text="", **attrs):
        p = HTMLElement('p', **attrs).set_content(text)
        self.body.children.append(p)
        return p

    def param(self, *args, **attrs):
        param = HTMLElement('param', **attrs)
        self.body.children.append(param)
        return param

    def picture(self, *args, **attrs):
        picture = HTMLElement('picture', **attrs)
        self.body.children.append(picture)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                picture.children.append(child)
        return picture

    def pre(self, *args, **attrs):
        pre = HTMLElement('pre', **attrs)
        self.body.children.append(pre)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                pre.children.append(child)
        return pre

    def progress(self, *args, **attrs):
        progress = HTMLElement('progress', **attrs)
        self.body.children.append(progress)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                progress.children.append(child)
        return progress

    def q(self, *args, **attrs):
        q = HTMLElement('q', **attrs)
        self.body.children.append(q)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                q.children.append(child)
        return q

    def rp(self, *args, **attrs):
        rp = HTMLElement('rp', **attrs)
        self.body.children.append(rp)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                rp.children.append(child)
        return rp

    def rt(self, *args, **attrs):
        rt = HTMLElement('rt', **attrs)
        self.body.children.append(rt)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                rt.children.append(child)
        return rt

    def ruby(self, *args, **attrs):
        ruby = HTMLElement('ruby', **attrs)
        self.body.children.append(ruby)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                ruby.children.append(child)
        return ruby

    def s(self, *args, **attrs):
        s = HTMLElement('s', **attrs)
        self.body.children.append(s)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                s.children.append(child)
        return s

    def samp(self, *args, **attrs):
        samp = HTMLElement('samp', **attrs)
        self.body.children.append(samp)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                samp.children.append(child)
        return samp

    def script(self, text="", **attrs):
        script = HTMLElement('script', **attrs).set_content(text)
        self.body.children.append(script)
        return script

    def section(self, *args, **attrs):
        section = HTMLElement('section', **attrs)
        self.body.children.append(section)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                section.children.append(child)
        return section

    def select(self, *args, **attrs):
        select = HTMLElement('select', **attrs)
        self.body.children.append(select)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                select.children.append(child)
        return select

    def small(self, *args, **attrs):
        small = HTMLElement('small', **attrs)
        self.body.children.append(small)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                small.children.append(child)
        return small

    def source(self, *args, **attrs):
        source = HTMLElement('source', **attrs)
        self.body.children.append(source)
        return source

    def span(self, *args, **attrs):
        span = HTMLElement('span', **attrs)
        self.body.children.append(span)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                span.children.append(child)
        return span

    def strong(self, *args, **attrs):
        strong = HTMLElement('strong', **attrs)
        self.body.children.append(strong)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                strong.children.append(child)
        return strong

    def style(self, text="", **attrs):
        style = HTMLElement('style', **attrs).set_content(text)
        self.head.children.append(style)
        return style

    def sub(self, *args, **attrs):
        sub = HTMLElement('sub', **attrs)
        self.body.children.append(sub)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                sub.children.append(child)
        return sub

    def summary(self, *args, **attrs):
        summary = HTMLElement('summary', **attrs)
        self.body.children.append(summary)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                summary.children.append(child)
        return summary

    def sup(self, *args, **attrs):
        sup = HTMLElement('sup', **attrs)
        self.body.children.append(sup)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                sup.children.append(child)
        return sup

    def table(self, *args, **attrs):
        table = HTMLElement('table', **attrs)
        self.body.children.append(table)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                table.children.append(child)
        return table

    def tbody(self, *args, **attrs):
        tbody = HTMLElement('tbody', **attrs)
        self.body.children.append(tbody)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                tbody.children.append(child)
        return tbody

    def td(self, text="", **attrs):
        td = HTMLElement('td', **attrs).set_content(text)
        self.body.children.append(td)
        return td

    def template(self, *args, **attrs):
        template = HTMLElement('template', **attrs)
        self.body.children.append(template)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                template.children.append(child)
        return template

    def textarea(self, *args, **attrs):
        textarea = HTMLElement('textarea', **attrs)
        self.body.children.append(textarea)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                textarea.children.append(child)
        return textarea

    def tfoot(self, *args, **attrs):
        tfoot = HTMLElement('tfoot', **attrs)
        self.body.children.append(tfoot)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                tfoot.children.append(child)
        return tfoot

    def th(self, text="", **attrs):
        th = HTMLElement('th', **attrs).set_content(text)
        self.body.children.append(th)
        return th

    def thead(self, *args, **attrs):
        thead = HTMLElement('thead', **attrs)
        self.body.children.append(thead)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                thead.children.append(child)
        return thead

    def time(self, *args, **attrs):
        time = HTMLElement('time', **attrs)
        self.body.children.append(time)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                time.children.append(child)
        return time

    def title(self, text="", **attrs):
        title = HTMLElement('title', **attrs).set_content(text)
        self.head.children.append(title)
        return title

    def tr(self, *args, **attrs):
        tr = HTMLElement('tr', **attrs)
        self.body.children.append(tr)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                tr.children.append(child)
        return tr

    def track(self, *args, **attrs):
        track = HTMLElement('track', **attrs)
        self.body.children.append(track)
        return track

    def u(self, *args, **attrs):
        u = HTMLElement('u', **attrs)
        self.body.children.append(u)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                u.children.append(child)
        return u

    def ul(self, *args, **attrs):
        ul = HTMLElement('ul', **attrs)
        self.body.children.append(ul)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                ul.children.append(child)
        return ul

    def var(self, *args, **attrs):
        var = HTMLElement('var', **attrs)
        self.body.children.append(var)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                var.children.append(child)
        return var

    def video(self, *args, **attrs):
        video = HTMLElement('video', **attrs)
        self.body.children.append(video)
        for child in args:
            if isinstance(child, HTMLElement) or isinstance(child, str):
                video.children.append(child)
        return video

    def wbr(self, *args, **attrs):
        wbr = HTMLElement('wbr', **attrs)
        self.body.children.append(wbr)
        return wbr

    # Qo'shimcha HTML teglarini yaratish uchun metodlar
    # (Div, Span, Ul, Li, Form, Button, Table, Tr, Td allaqachon standart tags ichida)

    def add_styles(self, css):
        style = HTMLElement('style').set_content(css)
        self.head.children.append(style)
        return self

    def add_script(self, script_content):
        script = HTMLElement('script').set_content(script_content)
        self.body.children.append(script)
        return self

    def end(self, sleep=0, LOGGER=False, DEBUGS=True, AUTHOR="", others=0):
        if AUTHOR:
            script_content = f'''
const INFORMATION = `
THIS SITE CREATED BY {AUTHOR}!
:_________FRAMEWORK__INFO_________:
: VERSION: 1.0.0                  :
: FRAMEWORK NAME: MOJIZA          :
: AUTHOR: {AUTHOR}   :
: USING WITH PYTHON               :
:_________FRAMEWORK__INFO_________:
`;
console.log(INFORMATION);
'''
            self.add_script(script_content)

        return self.doctype + "\n" + self.html.render()


def get_generated_apps():


    current_dir = Path(__file__).parent.parent.parent  # project root
    apps = []

    for item in current_dir.iterdir():
        if item.is_dir():
            views_file = item / "views.py"
            urls_file = item / "urls.py"
            if views_file.exists() and urls_file.exists():
                apps.append(item.name)

    return apps




class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):  self._handle()
    def do_POST(self): self._handle()
    def _handle(self):
        from MOJIZA.engine.routing import router
        from inspect import signature
        from urllib.parse import parse_qs
        import logging

        path = self.path.split("?", 1)[0]
        view = router.get_view(path)

        if view is None:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found")
            return

        # ✅ GET yoki POST parametrlari
        try:
            if self.command == "POST":
                content_length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(content_length).decode("utf-8")
                params = parse_qs(body)  # {'guess': ['22']}
            else:
                params = {}
                if "?" in self.path:
                    query = self.path.split("?", 1)[1]
                    params = parse_qs(query)

            # ✅ STATIC FILES
            if path.startswith("/static/"):
                result = view(self)

            else:
                # ✅ View funksiyasini aniqlash
                sig = signature(view)
                names = list(sig.parameters.keys())

                if names == ["request"]:
                    result = view(self)
                elif names == ["method", "params"]:
                    result = view(method=self.command, params=params)
                else:
                    raise Exception(f"View funksiyasi noto‘g‘ri formatda! Parametrlar: {names}")

            # ✅ Javobni formatlash
            if isinstance(result, tuple) and len(result) == 3:
                status, content_type, content = result
                if isinstance(content, str):
                    content = content.encode()
                elif not isinstance(content, bytes):
                    content = str(content).encode()
            else:
                status, content_type, content = 200, "text/html", str(result).encode()

            # ✅ Yuborish
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)

        except Exception as e:
            logging.getLogger("MOJIZA.engine.server").exception("Error during request handling")
            self.send_response(500)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(f"500 Internal Server Error\n\n{e}".encode())


def run_server(port=8000):
    httpd = HTTPServer(('', port), RequestHandler)
    logger.info(f'Server running on port {port}')

    def reload_views():
        project_dir = os.path.join(os.getcwd(), 'projectpapca')
        if not os.path.exists(project_dir):
            logger.warning("projectpapca papkasi topilmadi!")
            return

        for item in os.listdir(project_dir):
            app_path = os.path.join(project_dir, item)
            views_file = os.path.join(app_path, 'views.py')
            urls_file = os.path.join(app_path, 'urls.py')

            if os.path.isfile(views_file) and os.path.isfile(urls_file):
                try:
                    # views modulini reload qilish
                    module_path = f'projectpapca.{item}.views'
                    if module_path in sys.modules:
                        importlib.reload(sys.modules[module_path])
                        logger.info(f'{module_path} qayta yuklandi.')
                    else:
                        __import__(module_path)
                        logger.info(f'{module_path} yuklandi.')

                    # base_url_name ni olish
                    urls_module = importlib.import_module(f'projectpapca.{item}.urls')
                    base_url = getattr(urls_module, 'base_url_name', None)
                    if base_url:
                        logger.info(f"App `{item}` uchun URL path: '{base_url}/'")
                    else:
                        logger.warning(f"{item}.urls ichida `base_url_name` topilmadi.")

                except Exception as e:
                    logger.error(f"{item} moduli reload qilinmadi: {e}")

    threading.Thread(target=reload_views, daemon=True).start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logger.info('Server stopped')


class ReloadHandler(FileSystemEventHandler):
    def __init__(self, cb):
        super().__init__()
        self.cb = cb

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            logger.info(f'Reloading due to change in: {event.src_path}')
            self.cb()

def start_auto_reload(callback, path='.'):
    observer = Observer()
    observer.schedule(ReloadHandler(callback), path=path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# --- Server run function ---
def run_server(port=8000):
    server = HTTPServer(('', port), RequestHandler)
    logger.info(f"Server running on port {port}")
    server.serve_forever()
