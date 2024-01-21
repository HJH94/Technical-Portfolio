import random
import string

def generate_random_password(length=8):
    # Combine letters and digits
    characters = string.ascii_letters + string.digits

    # Generate a random password with the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

user_file = open('generated_passwords.txt', 'w')
pass_count = int(input("Please enter the number of passwords you want to generate: \n"))

print(f"You have entered {pass_count} passwords to generate.")

for pass_gen in range(pass_count):
    # Generate a random password with default length (8 characters)
    random_password = generate_random_password()
    user_file.write('.........................................................................\n')
    user_file.write(random_password + '\n')

user_file.write('...........................END OF REGISTER...............................\n')

user_file.close()
