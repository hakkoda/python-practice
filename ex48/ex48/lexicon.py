DIRECTION_WORDS = [
    "north",
    "south",
    "east",
    "west",
    "up",
    "down",
    "left",
    "right",
    "back"
]

VERBS = [ "go", "stop", "kill", "eat" ]
STOP_WORDS = [ "the", "in", "of", "from", "at", "it" ]
NOUNS = [ "door", "bear", "princess", "cabinet" ]

def scan(text):
    result = []

    scanned_directions = scan_words(text, DIRECTION_WORDS, "direction")
    result = result + scanned_directions

    scanned_verbs = scan_words(text, VERBS, "verb")
    result = result + scanned_verbs

    scanned_stops = scan_words(text, STOP_WORDS, "stop")
    result = result + scanned_stops

    scanned_nouns = scan_words(text, NOUNS, "noun")
    result = result + scanned_nouns

    scanned_numbers = scan_numbers(text)
    result = result + scanned_numbers

    return result

def scan_words(text, word_list, target):
    result = []

    tokens = text.split()
    for token in tokens:
        for word in word_list:
            if token == word:
                result.append((target, token))
                break

    return result

def scan_numbers(text):
    result = []

    tokens = text.split()
    for token in tokens:
        num = convert_number(token)
        if num != None:
            result.append(("number", num))

    return result

def convert_number(text):
    try:
        return int(text)
    except ValueError:
        return None
