passphrase = {"Joseph":"W@12"}

name = input("Please enter your name..:").title()

if name == "Joseph":
    print(f"Hello\033[1m {name}\033[0m! The password is: {passphrase[name]}")
else:
    print(f"Hello\033[1m {name}\033[0m! See you later.")
