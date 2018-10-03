# Write a program to read an integer from 1 to 999 and print the integer in
# words.  For example, if 437 is read, the output should be:
#     four hundred and thirty-seven

# what about:
#   10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, etc...
def convert_ones(text):
    ones_dict = {
        "0": "",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
    }

    return ones_dict.get(text, "")

def convert_tens(text):
    tens_dict = {
        "0": "",
        "1": "",
        "2": "twenty",
        "3": "thirty",
        "4": "forty",
        "5": "fifty",
        "6": "sixty",
        "7": "seventy",
        "8": "eighty",
        "9": "ninety"
    }

    return tens_dict(text, "")

def convert(text):
    for x in text:
        print(x)

convert("123")
