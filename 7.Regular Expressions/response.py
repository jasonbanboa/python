from validator_collection import validators


def validate():
    try:
        if email := validators.email(input("What's your email address? ")):
            print("Valid")
    except ValueError:
        print("Invalid")


if __name__ == "__main__":
    validate()


