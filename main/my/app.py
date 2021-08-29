def main():
    user_name = input("user name: ")
    password = input("password: ")
    result = login(user_name, password)
    print(result)


def login(user_name: str, password: str) -> str:
    print("login by {}....".format(user_name))
    return "done."


if __name__ == "__main__":
    main()
