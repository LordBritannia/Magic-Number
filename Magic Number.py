
num_character_list = ["zero", "one", "two,", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                      "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                      "nineteen", "twenty", "twentyone", "twentytwo", "twentythree", "twentyfour", "twentyfive",
                      "twentysix", "twentyseven", "twentyeight", "twentynine"]

#   num = number, on = Old number


def magic_number(num):
    on = 0
    while on != num_character_list[num]:
        on = num_character_list[num]
        num = len(on)
    print(num)


magic_number(0)
