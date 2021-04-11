# coding=utf8
mojesi_dict = {'🕛' : 0, '🕐' : 1, '🕑' : 2, '🕒' : 3, '🕓' : 4, '🕔' : 5, '🕕' : 6, '🕖' : 7, '🕗' : 8, '🕘' : 9, '🕙' : 10, '🕚' : 11, '☝' : 20, '👇' : 21, '🤞' : 22, '🤙' : 23}
number_dict = {0 : '🕛', 1 : '🕐', 2 : '🕑', 3 : '🕒', 4 : '🕓', 5 : '🕔', 6 : '🕕', 7 : '🕖', 8 : '🕗', 9 : '🕘', 10 : '🕙', 11 : '🕚',  20 : '☝', 21 : '👇', 22 : '🤞', 23 : '🤙'}

# We are reading the Mojesi number from the stdin
mojesi_bytecode = "8173\n"
mojesi_bytecode = int(mojesi_bytecode[:-1])

def compute_to_number(my_string):
    my_list = [char for char in my_string]
    my_list = my_list[:-1]
    
    result = 0

    for emoji in my_list:
        if emoji != '☝':
            result += mojesi_dict[emoji]
    return result


def compute_to_emoji(my_int):
    addition = 0
    multiplication = 0
    if 0 <= my_int <=11:
        return number_dict[my_int]

    sign = -1 if my_int < 0 else 1
    my_int = abs(my_int)

    emoji = ""
    while my_int != 0:
        for i in range(11, 0, -1):
            for j in range(11, 0, -1):
                for k in range(11, 0, -1):
                    for l in range(11, 0, -1):
                        for m in range(11, 0, -1):
                                if i*j*k*l*m <= my_int:
                                    addition += 1
                                    multiplication = 4
                                    emoji += number_dict[i] + number_dict[j] + number_dict[k] + number_dict[l]+ number_dict[m] + number_dict[22]*multiplication
                                    my_int -= i*j*k*l*m
                    if i*j*k*l <= my_int:
                        addition += 1
                        multiplication = 3
                        emoji += number_dict[i] + number_dict[j] + number_dict[k] + number_dict[l] + number_dict[22]*multiplication
                        my_int -= i*j*k*l
                if i*j*k <= my_int:
                    addition += 1
                    multiplication = 2
                    emoji += number_dict[i] + number_dict[j] + number_dict[k] + number_dict[22]*multiplication
                    my_int -= i*j*k
            if i*j <= my_int:
                addition += 1
                multiplication = 1
                emoji += number_dict[i] + number_dict[j] + number_dict[22]*multiplication
                my_int -= i*j
    emoji += number_dict[20]*(addition-1)
    
    if sign == 1:
        return emoji
    else:
        emoji += number_dict[2] + emoji + number_dict[22] + number_dict[21]
        return emoji

print(compute_to_emoji(mojesi_bytecode))


#exo 6 
# 🕙🕙☝🕙🕙☝🕙🕓☝☝☝
# 👀
# 🕗
# 🐶
# 🚀
# 🕚🕙☝🕙🕙☝🕙🕙☝🕙🕙☝🕙☝☝☝☝📺
# 🕚🕙☝ 📺
# 🕙🕙☝🕙🕙☝🕙🕙☝🕙🕕☝☝☝☝
# 🕐
# 🚀
# 🕙🕙☝🕙🕙☝🕙🕙☝🕙🕙☝🕙☝☝☝☝📺
# 🕙🕙☝ 📺
# 🙃