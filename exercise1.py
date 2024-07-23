def get_string_to_file(word):

    y = input("Do you want to enter another string? ")
    try:
        while True:
            if y == "Yes":
                word = input("Enter another string: ")
                print("You additionally entered: ", word)
                break #this not works proper
            elif y == "No":
                print("Ok")
                break

        with open("file.txt", "w") as file:
            file.write(word)

        with open("file.txt", "r") as file:
            content = file.read()

        words = content.split()
        print(words)

    except SyntaxError:
        print("write properly")
    except UnboundLocalError:
        print("'file' not associated with a value")

    finally:
        file.close()
        print("Done")


# name_of_file = input("Enter a file name: ")
# with open("file.txt") as f:
#     f.name(name_of_file)

get_string_to_file(word=input("Enter a string: "))