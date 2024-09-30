"""
NumTextAlchemy Library

This library provides functionality to convert numbers to their textual representations
and vice versa. It includes two main functions:

- num2text(number): Converts a numerical value to its corresponding text representation.
- text2num(text): Converts a textual representation back to its numerical form.

Limitations:
Both functions support numbers up to 10^212.

Author: Srinath Gudi

Example Usage:

# Converting a large number to text
number = 123456789012345678901234567890
text_representation = num2text(number)
print(text_representation)
# Output: "One hundred twenty-three quattuordecillion four hundred fifty-six tredecillion
# seven hundred eighty-nine duodecillion twelve undecillion three hundred forty-five decillion
# six hundred seventy-eight nonillion nine hundred twelve octillion three hundred forty-five
# septillion six hundred seventy-eight."

# Converting text to a number
text = "One hundred twenty-three quattuordecillion four hundred fifty-six tredecillion
seven hundred eighty-nine duodecillion twelve undecillion three hundred forty-five decillion
six hundred seventy-eight nonillion nine hundred twelve octillion three hundred forty-five
septillion six hundred seventy-eight."
number_representation = text2num(text)
print(number_representation)
# Output: 123456789012345678901234567890
"""







__number_upper_set = {
    "0": "",
    "1": "one",
    "2": "Twenty",
    "3": "Thirty",
    "4": "Forty",
    "5": "Fifty",
    "6": "Sixty",
    "7": "Seventy",
    "8": "Eighty",
    "9": "Ninety",
}
__numbers_lower_set = {
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
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
}

__number_units = {
    0: "",
    1: "Thousand",  # 10^3 = 10^(3*1)
    2: "Million",  # 10^6 = 10^(3*2)
    3: "Billion",  # 10^9 = 10^(3*3)
    4: "Trillion",  # 10^12 = 10^(3*4)
    5: "Quadrillion",  # 10^15 = 10^(3*5)
    6: "Quintillion",  # 10^18 = 10^(3*6)
    7: "Sextillion",  # 10^21 = 10^(3*7)
    8: "Septillion",  # 10^24 = 10^(3*8)
    9: "Octillion",  # 10^27 = 10^(3*9)
    10: "Nonillion",  # 10^30 = 10^(3*10)
    11: "Decillion",  # 10^33 = 10^(3*11)
    12: "Undecillion",  # 10^36 = 10^(3*12)
    13: "Duodecillion",  # 10^39 = 10^(3*13)
    14: "Tredecillion",  # 10^42 = 10^(3*14)
    15: "Quattuordecillion",  # 10^45 = 10^(3*15)
    16: "Quindecillion",  # 10^48 = 10^(3*16)
    17: "Sexdecillion",  # 10^51 = 10^(3*17)
    18: "Septendecillion",  # 10^54 = 10^(3*18)
    19: "Octodecillion",  # 10^57 = 10^(3*19)
    20: "Novemdecillion",  # 10^60 = 10^(3*20)
    21: "Vigintillion",  # 10^63 = 10^(3*21)
    22: "Unvigintillion",  # 10^66 = 10^(3*22)
    23: "Duovigintillion",  # 10^69 = 10^(3*23)
    24: "Trevigintillion",  # 10^72 = 10^(3*24)
    25: "Quattuorvigintillion",  # 10^75 = 10^(3*25)
    26: "Quinvigintillion",  # 10^78 = 10^(3*26)
    27: "Sexvigintillion",  # 10^81 = 10^(3*27)
    28: "Septenvigintillion",  # 10^84 = 10^(3*28)
    29: "Octovigintillion",  # 10^87 = 10^(3*29)
    30: "Novemvigintillion",  # 10^90 = 10^(3*30)
    31: "Trigintillion",  # 10^93 = 10^(3*31)
    32: "Untrigintillion",  # 10^96 = 10^(3*32)
    33: "Duotrigintillion",  # 10^99 = 10^(3*33)
    34: "Trestrigintillion",  # 10^102 = 10^(3*34)
    35: "Quattuortrigintillion",  # 10^105 = 10^(3*35)
    36: "Quintrigintillion",  # 10^108 = 10^(3*36)
    37: "Sextrigintillion",  # 10^111 = 10^(3*37)
    38: "Septentrigintillion",  # 10^114 = 10^(3*38)
    39: "Octotrigintillion",  # 10^117 = 10^(3*39)
    40: "Novemtrigintillion",  # 10^120 = 10^(3*40)
    41: "Quadragintillion",  # 10^123 = 10^(3*41)
    42: "Unquadragintillion", # 10^126 = 10^(3*42)
    43: "Duoquadragintillion", # 10^129 = 10^(3*43)
    44: "Trequadragintillion", # 10^132 = 10^(3*44)
    45: "Quattuorquadragintillion", # 10^135 = 10^(3*45)
    46: "Quinquadragintillion", # 10^138 = 10^(3*46)
    47: "Sexquadragintillion",   # 10^141 = 10^(3*47)
    48: "Septenquadragintillion",# 10^144 = 10^(3*48)
    49: "Octoquadragintillion",# 10^147 = 10^(3*49)
    50: "Novemquadragintillion",# 10^150 = 10^(3*50)
    51: "Quinquagintillion",# 10^153 = 10^(3*51)
    52: "Unquinquagintillion",# 10^156 = 10^(3*52)
    53: "Duoquinquagintillion",# 10^159 = 10^(3*53)
    54: "Trequinquagintillion",# 10^162 = 10^(3*54)
    55: "Quattuorquinquagintillion",# 10^165 = 10^(3*55)
    56: "Quinquinquagintillion",# 10^168 = 10^(3*56)
    57: "Sexquinquagintillion",# 10^171 = 10^(3*57)
    58: "Septenquinquagintillion",# 10^174 = 10^(3*58)
    59: "Octoquinquagintillion",# 10^177 = 10^(3*59)
    60: "Novemquinquagintillion",# 10^180 = 10^(3*60)
    61: "Sexagintillion",# 10^183 = 10^(3*61)
    62: "Unsexagintillion",# 10^186 = 10^(3*62)
    63: "Duosexagintillion",# 10^189 = 10^(3*63)
    64: "Tresexagintillion",# 10^192 = 10^(3*64)
    65: "Quattuorsexagintillion",# 10^195 = 10^(3*65)
    66: "Quinsexagintillion",# 10^198 = 10^(3*66)
    67: "Sexsexagintillion",# 10^201 = 10^(3*67)
    68: "Septensexagintillion",# 10^204 = 10^(3*68)
    69: "Octosexagintillion",# 10^207 = 10^(3*69)
    70: "Novemsexagintillion",# 10^210 = 10^(3*70)
}






def ___get_sub_number(number):
    number = str(int(number))
    data = ""
    for value, num in enumerate(number):
        place = len(number) - (value + 1)
        if place == 0:
            data += __numbers_lower_set.get(num)
        elif place == 1:
            if num == "1":
                data += __numbers_lower_set.get(num + number[-1])
                return data
            elif number[-1] != '0' and number[-2] != '0':
                data += __number_upper_set.get(num) + "-"
            else:
                data += __number_upper_set.get(num) + " "
        elif place == 2:
            data += __numbers_lower_set.get(num) + " hundred "
    return data


def ___extra(number):
    if len(number) % 3 == 0:
        return len(number) // 3 - 1, 0
    else:
        return len(number) // 3, len(number) % 3


def num2text(number:str):
    """
        Converts a large number (up to 10^212) into its corresponding English words representation.
    
        Args:
        - number (str): The number to be converted. It should be a string representation of the number.
    
        Returns:
        str: The English words representation of the input number.
    
        Example:
        >>> num2text('123456789012345678901234567890123456789012345678901234567890').lower()
        'one hundred twenty-three octodecillion four hundred fifty-six septendecillion seven hundred eighty-nine sexdecillion
         twelve quindecillion three hundred forty-five quattuordecillion six hundred seventy-eight tredecillion nine hundred
         one duodecillion two hundred thirty-four undecillion five hundred sixty-seven decillion eight hundred ninety nonillion
         one hundred twenty-three octillion four hundred fifty-six septillion seven hundred eighty-nine sextillion twelve quintillion
         three hundred forty-five quadrillion six hundred seventy-eight trillion nine hundred one billion two hundred thirty-four million
         five hundred sixty-seven thousand eight hundred ninety'
    """
    number = str(number)
    if len(number) > 213:
        raise ValueError(f"Input number is too large. num2text only supports 213 digit numbers but {len(number)} digit number was given.")

    output = ""
    commas, extras = ___extra(number)
    pos = commas
    if extras:
        number = (3 - extras) * "0" + number
    for i in range(commas + 1):
        if (nu := number[i * 3 : 3 * (i + 1)].strip()) != "000":
            output += (
                ___get_sub_number(nu) + " " + __number_units.get((pos + abs(pos)) / 2) + " "
            )
            pos -= 1
        else:
            output += ___get_sub_number(nu) + " "
            pos -= 1

    capitalized_text = " ".join(word.capitalize() for word in output.split())

    return capitalized_text


def __reverse_loop(num):
    
    for key, value in __numbers_lower_set.items():
        if value.lower() == num.lower():
            return (key)

    for key, value in __number_upper_set.items():
        if value.lower() == num.lower():
            return (key) + "0" 

    
    
    return None
def text2num(text:str):
    """
        Converts an English words representation of a large number (up to 10^212) into its corresponding numerical value.
    
        Args:
        - text (str): The English words representation of a number.
    
        Returns:
        int: The numerical value of the input number.
    
        Example:
        
        >>> text2num('one hundred twenty-three octodecillion four hundred fifty-six septendecillion seven hundred eighty-nine sexdecillion twelve quindecillion three hundred forty-five quattuordecillion six hundred seventy-eight tredecillion nine hundred one duodecillion two hundred thirty-four undecillion five hundred sixty-seven decillion eight hundred ninety nonillion one hundred twenty-three octillion four hundred fifty-six septillion seven hundred eighty-nine sextillion twelve quintillion three hundred forty-five quadrillion six hundred seventy-eight trillion nine hundred one billion two hundred thirty-four million five hundred sixty-seven thousand eight hundred ninety')
            123456789012345678901234567890123456789012345678901234567890

"""
    word = text.lower().split()
    num=0
    temp_num = ""
    try:
        for i in range(len(word)):
            if word[i] == 'hundred':
                if temp_num:
                    temp_num = str(int(temp_num) * 100)
                else:
                    temp_num="100"
            elif '-'  in word[i]:
                num1, num2 = word[i].split('-')
                temp_data = __reverse_loop(num1)[0] + __reverse_loop(num2)
                if temp_num:
                    temp_num= int(temp_num) + int(temp_data)
                else:
                    temp_num=int(temp_data)
            else:
                if ((data:=__reverse_loop(word[i])) == None):
                    for key, value in __number_units.items():
                        if value.lower() == word[i].lower():
                            num+=int(temp_num) * (10**(3*key))
                            temp_num=""
                else:
                    if not temp_num:
                        temp_num=data
                    else:
                        temp_num=str(int(temp_num) + int(data))
        if temp_num:
            num+=int(temp_num)
    except:
        raise Exception("Failed to convert text to number. Reason: Could not identify unit.")
    return num

if __name__ == "__main__":
    print(num2text('123456789012345678901234567890123456789012345678901234567890').lower())
    print(text2num("one hundred twenty-three octodecillion four hundred fifty-six septendecillion seven hundred eighty-nine sexdecillion twelve quindecillion three hundred forty-five quattuordecillion six hundred seventy-eight tredecillion nine hundred one duodecillion two hundred thirty-four undecillion five hundred sixty-seven decillion eight hundred ninety nonillion one hundred twenty-three octillion four hundred fifty-six septillion seven hundred eighty-nine sextillion twelve quintillion three hundred forty-five quadrillion six hundred seventy-eight trillion nine hundred one billion two hundred thirty-four million five hundred sixty-seven thousand eight hundred ninety"))