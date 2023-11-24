import re
def to_list(text):
    template = "<li>{}</li>"
    split = text.split("\n")
    line1 = split.pop(0)
    for line in split:
        formatted = template.format(line)
        line1 += formatted
    return line1

def to_slug(text):
    return "-".join(text.split())

def to_text(slug):
    return " ".join(slug.split("-"))
    

            
        