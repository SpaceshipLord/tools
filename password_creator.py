import string, random, argparse

def password_creator(length, punctuation, letters):
    characters = string.digits
    if punctuation:
        characters += string.punctuation
    if letters:
        characters += string.ascii_letters
    password = "".join(random.SystemRandom().choice(characters) for x in range(length))
    return(password)

def main():
    parser = argparse.ArgumentParser(description = "Creation of a password using random.Systemrandom. " \
            "Only digits are included, if no other optional argument is given.")
    parser.add_argument("length", type = int, help = "length of password")
    parser.add_argument("-p", "--punctuation", action = "store_true", default = False, help = "include punctuation")
    parser.add_argument("-l", "--letters", action = "store_true", default = False, help = "include letters")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action = "store_true")
    group.add_argument("-q", "--quiet", action = "store_true")
    args = parser.parse_args()
    password = password_creator(args.length, args.punctuation, args.letters)
    if args.verbose:
        print("\nnew password\n============\nlength:\t\t\t" + str(args.length) + \
                "\nincluding punctuation:\t" + str(args.punctuation) + \
                "\nincluding letters:\t" + str(args.letters) + \
                "\npassword:\t\t" + password)
    elif  args.quiet:
        print("\n" + password)
    else:
        print("\nYour new password is: " + password)

if __name__ == "__main__":
    main()