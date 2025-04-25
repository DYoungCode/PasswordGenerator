import random
import string

count = 0
total = 0
char_dict = {}      #key: type of char (lower, upper, digit, special), value: how many user selected
random_list = []    #store randomly generated characters in list

### Todo ###
# optional - add a "just surprise me option"

print("This program will generate a random password based on your inputs.")

char_types = ["lowercase characters", "uppercase characters", "digits", "special characters"]

# this function takes in 3 prompts (2 strings, 1 list) to ask the user
# a question and variable created to store users response
def get_user_input(prompt1, prompt2, prompt3, data_type=int):
    prompt = prompt1 + " " + prompt2 + " " + prompt3
    while True:
        try:
            value = data_type(input(prompt))
            return value
        except ValueError: 
            print("Invalid input.")

# call get_user_input func, return value to a dictionary and capture total characters in password
for x in char_types:
    return_value = get_user_input("How many", x, "do you want in your password?")
    char_dict[x] = return_value
    total += return_value

print(char_dict)
print("The total number of characters is", total)

for key in char_dict:
    value = char_dict[key]
    for x in range(value):
        if key == 'lowercase characters':
            random_lower = random.choice(string.ascii_lowercase)
            random_list.append(random_lower)
        elif key == 'uppercase characters':
            random_upper = random.choice(string.ascii_uppercase)
            random_list.append(random_upper)
        elif key == 'digits':
            random_digits = random.choice(string.digits)
            random_list.append(random_digits)
        elif key == 'special characters':
            random_special = random.choice(string.punctuation)
            random_list.append(random_special)
        #print(x)
    #print(f"Key: {key} Value: {value}")   #Debugging

random.shuffle(random_list)
combined_string = ''.join(random_list)
print("\nYour randomly generated password is:", combined_string)
# type: ignore