# Write a program to read an integer from 1 to 999 and print the integer in
# words.  For example, if 437 is read, the output should be:
#     four hundred and thirty-seven

# what about:
#   10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, etc...

# TODO: handle the teens

def convert_ones(num):
    ones_dict = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }

    return ones_dict.get(num, "")

def convert_tens(num):
    tens_dict = {
        0: "",
        1: "",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }

    return tens_dict.get(num, "")

def convert_hundreds(num):
    hundreds_dict = {
        0: "",
        1: "one hundred",
        2: "two hundred",
        3: "three hundred",
        4: "four hundred",
        5: "five hundred",
        6: "six hundred",
        7: "seven hundred",
        8: "eight hundred",
        9: "nine hundred"
    }

    return hundreds_dict.get(num, "")

def convert(text):
    num = int(text)
    if num > 0 and num < 1000:
        hundreds = int((num % 1000) / 100)
        hundreds_converted = convert_hundreds(hundreds)
        tens = int(num % 100 / 10)
        tens_converted = convert_tens(tens)
        ones = int(num % 10)
        ones_converted = convert_ones(ones)
        print(f"{text} : {hundreds} {tens} {ones}")
        print(f"{text} : {hundreds_converted} {tens_converted} {ones_converted}")

convert("123")
convert("321")
convert("21")
convert("1")
convert(10)
convert(11)
convert(12)
convert(13)
convert(14)
convert(15)
convert(16)
convert(17)
convert(18)
convert(19)
convert(20)
convert(30)
convert(40)
