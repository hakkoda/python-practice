# Write a program to read an integer from 1 to 999 and print the integer in
# words.  For example, if 437 is read, the output should be:
#     four hundred and thirty-seven

# TODO: now that I've brute forced this to work, how can this be made a little
# more readable and maintainable (maybe using recursion?)

def convert_ones(num, hundreds_value, tens_value):
    if tens_value == 1:
        ones_dict = {
            0: "ten",
            1: "eleven",
            2: "twelve",
            3: "thirteen",
            4: "fourteen",
            5: "fifteen",
            6: "sixteen",
            7: "seventeen",
            8: "eighteen",
            9: "nineteen",
        }
    else:
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

    if tens_value > 1 and num > 0:
        return  "-" + ones_dict.get(num, "")
    elif hundreds_value > 0 and tens_value < 1 and num > 0:
        return  "and " + ones_dict.get(num, "")
    else:
        return ones_dict.get(num, "")

def convert_tens(num, is_hundreds):
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

    if is_hundreds and num > 0:
        return "and " + tens_dict.get(num, "")
    else:
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
        tens_converted = convert_tens(tens, hundreds != 0)
        ones = int(num % 10)
        ones_converted = convert_ones(ones, hundreds, tens)
        final_num_str = ""
        final_num_str += hundreds_converted + " " if hundreds_converted != "" else ""
        final_num_str += tens_converted if tens_converted != "" else ""
        final_num_str += ones_converted + " " if ones_converted != "" else ""
        #print(f"{text} : {hundreds} {tens} {ones}")
        print(f"{text} : {final_num_str}")

for x in range(0, 200):
#for x in range(90, 110):
    convert(str(x))
