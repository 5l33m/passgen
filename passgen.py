import itertools
import string
import subprocess

def generate_permutations(word):
    # Capitalization permutations
    cap_permutations = list(map(''.join, itertools.product(*((c.upper(), c.lower()) for c in word))))

    # Numbers and special characters
    numbers = [str(i) for i in range(10)]
    special_chars = '!@#$%^&*()-=_+[]{}|;:,.<>?/`~'
    chars_to_add = numbers + list(special_chars)

    # Create password combinations
    passwords = []
    for perm in cap_permutations:
        passwords.append(perm)
        for i in range(1, 3):  # Limit the additional characters to a maximum of 2
            for combination in itertools.product(chars_to_add, repeat=i):
                passwords.append(perm + ''.join(combination))
    return passwords

def save_passwords_to_file(passwords, file_path):
    with open(file_path, 'w') as f:
        for password in passwords:
            f.write(password + '\n')

def run_john_the_ripper(password_file, target_file):
    command = f"john --wordlist={password_file} {target_file}"
    subprocess.run(command, shell=True, check=True)

def main():
    word = input("Enter the base word: ")
    passwords = generate_permutations(word)
    password_file = "passwords.txt"
    save_passwords_to_file(passwords, password_file)

    target_file = input("Enter the path to the target file (e.g., shadow file): ")
    run_john_the_ripper(password_file, target_file)

if __name__ == "__main__":
    main()
