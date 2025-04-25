#The long and winding road

#dun dun

#you use to be....

#user_input = input("Password length(integer):")

#try:
#    number = int(user_input)
#    print("Success!")
#except:
#    print("That's not an integer")

count = 0
total = 0

char_types = ["lowercase characters", "uppercase characters", "digits", "special characters"]
char_dict = {}
def get_user_input(prompt1, prompt2, prompt3, data_type=int):
    prompt = prompt1 + " " + prompt2 + " " + prompt3
    while True:
        try:
            value = data_type(input(prompt))
            return value
        except ValueError: 
            print("Invalid input.")

for x in char_types:
    return_value = get_user_input("How many", x, "do you want in your password?")
    char_dict[x] = return_value
    total += return_value

print(char_dict)
print("The total number of characters is", total)

#lcase = get_user_input("How many lowercase characters do you want in your password?")
#ucase = get_user_input("How many uppercase characters do you want in your password?")
#digit = get_user_input("How many digits do you want in your password?")
#special = get_user_input("How many special characters do you want in your password?")

