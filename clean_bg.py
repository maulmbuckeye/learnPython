import bs4
import re

print("Loading "+ __file__)

HTML_DOC =  """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

HTML_SMALL_CAPS = '<span><span class="small-caps">Lord</span> and <span class="small-caps">Lord</span></span>'
HTML_SMALL_CAPS = '<span class="small-caps">Lord</span> and <span class="small-caps">Lord</span>'

def make_soup(html) :
    return bs4.BeautifulSoup(html,"html.parser")

def clean_bg(html) :
    soup = make_soup(html)
    for small_caps_item in soup.select(".small-caps") :
        old_text = small_caps_item.string
        small_caps_item.replace_with(old_text.upper())
    for indent_item in soup.select(".indent-1") :
        indent_item.unwrap()
    for selector_to_remove in [".versenum","sup.crossreference",".indent-1-breaks"] :
        for verse_number_item in soup.select(selector_to_remove) :
            verse_number_item.decompose()
    return soup

verse_address_re = re.compile("(\S+)+-(\d+)+-(\d+)")
def get_verse_address(html) :
    soup = make_soup(html) 
    verse_tag = soup.select(".text")[0]
    for class_label in verse_tag["class"] :
        res = verse_address_re.match(class_label)
        if res :
            return (res.group(1),res.group(2),res.group(3))

def verses(html) :
    soup = make_soup(html)
    list_of_verses = soup.select(".text")
    for verse in soup.select(".text") :
        yield verse
        
def print_text(html) :
    soup = make_soup(html)
    print(soup.get_text())
    
def print_pretty(html) :
    soup = make_soup(html) 
    print(soup.prettify())

if __name__ == "__main__" :
    print(clean_bg(HTML_SMALL_CAPS))
    html = '<span class="text">initial</span>'
    e =get_next_verse(html)
    print(next(e))
    for verse in get_next_verse(html) :
        print(verse.text)

