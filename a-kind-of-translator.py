while True:
    def translate(phrase):

        translation = ""
        for letter in phrase:
            if letter.lower() in "a":
                if letter.isupper():
                    translation = translation + "4"
                else:
                    translation = translation + "4"
            elif letter.lower() in "e":
                if letter.isupper():
                    translation = translation + "3"
                else:
                    translation = translation + "3"
            elif letter.lower() in "ıi":
                if letter.isupper():
                    translation = translation + "1"
                else:
                    translation = translation + "1"
            elif letter.lower() in "oö":
                if letter.isupper():
                    translation = translation + "0"
                else:
                    translation = translation + "0"
            elif letter.lower() in "uü":
                if letter.isupper():
                    translation = translation + "W"
                else:
                    translation = translation + "w"
            else:
                translation = translation + letter
        return translation


    given_phrase = input("give me a phrase : ")
    if given_phrase == "quit":
        break
    else:
        print(translate(given_phrase))
