# Write functions is always a good idea because it allows us to encapsulate 
#the code which is good for better understanding, clarification, code reutilzation, etc.

def generate_dict(value1, value2, value3, value4):
    new_dict = {'first_field':{'second_field':{'val2':value2,'val3':value3}}}
    return new_dict



if __name__ == "__main__":
    new_dict = generate_dict(1, 2,3, 4)
    print new_dict


