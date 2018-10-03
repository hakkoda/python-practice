LEGAL_WORDS_DICT = {
    "direction": [
        "north",
        "south",
        "east",
        "west",
        "up",
        "down",
        "left",
        "right",
        "back"
    ],
    "verb": [ "go", "stop", "kill", "eat" ],
    "stop": [ "the", "in", "of", "from", "at", "it" ],
    "noun": [ "door", "bear", "princess", "cabinet" ],
}

def scan(text):
    result = []

    for token in text.split():
        match = parse_token(token)
        if match != None:
            result.append(match)
            continue

        num = convert_number(token)
        if num != None:
            result.append(num)
            continue

        result.append(("error", token))

    return result

def parse_token(token):
    for category, word_list in LEGAL_WORDS_DICT.items():
        for word in word_list:
            if token == word:
                return (category, token)

    return None

def convert_number(text):
    try:
        return ("number", int(text))
    except ValueError:
        return None
