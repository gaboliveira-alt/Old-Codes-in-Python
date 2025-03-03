import sys

def is_dancing_sentence2(text):
    upper = True
    dancing_text = ''
    for char in text:
        if char == ' ':
            dancing_text += char
            continue
            
        dancing_text += char.upper() if upper else char.lower()
        upper = not upper
    return dancing_text

def is_dancing_sentence(text):
    upper = True
    dancing_text = ''
    for char in text:
        if not char.isspace():
            char += char.upper() if upper else char.lower()
            upper = not upper
            dancing_text += char
    return dancing_text


for text in sys.stdin:
    text = text.strip('\n')
    print(is_dancing_sentence(text))
    



