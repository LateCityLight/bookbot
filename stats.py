def num_words(text):
    words = text.split()
    return len(words)

def characters(text):
    char_counts = {}

    for character in text.lower():
        if character in char_counts:
            char_counts[character] += 1
        else:
            char_counts[character] = 1
    
    return char_counts.items()

def char_sort(touple):
    char_list = []
    for char, count in touple:
        char_list.append({"char": char, "num": count})
    char_list.sort(key=lambda d: d["num"], reverse=True)
    
    return char_list