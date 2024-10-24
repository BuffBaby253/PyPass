# Author: BuffBaby253
# Title: PyPass
# Description: This is a simple password manager that generates random passwords and stores them in a text file with username and service provided.

import random
import string

# Function to generate a random string of a given length
def generate_random_string(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Main function to get user input and save the data to a file
def main():
    service = input("Enter the service name: ")
    username = input("Enter your username: ")
    password = generate_random_string()
    
    with open("user_data.txt", "a") as file:
        file.write(f"Service: {service}, Username: {username}, Password: {password}\n")
    
    print(f"Username, Password & Service saved: {service} {username}, {password}")

if __name__ == "__main__":
    main()
