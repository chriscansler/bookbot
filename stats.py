def get_num_words(text):
    num_words = 0
    num_words = len(text.split())
    return num_words

def get_chars_dict(text):
    chars = {}

    for c in text:
        lowered = c.lower() 
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars

def sort_on(items):
    return items["num"]

def get_sorted_list(chars_dict):
    out = []
    for (key, value) in chars_dict.items():
        out.append({"char": key, "num": value})

    out.sort(reverse=True, key=sort_on)
    return out