"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values,
will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. 
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.



"""

def rgb(r, g, b):    
    rgb_list = [r, g, b]
    final_value = ""
    for value in rgb_list:
        if value > 255:
            value = 255
        elif value < 0:
            value = 0 
        final_value += ("0" + str(hex(value)[2:]))[-2:]
    return final_value.upper()

print(rgb(0, 12, 500))

