while True:
    def translate(phrase):

        translation = ""
        for letter in phrase:
            if letter.lower() in "aeıioöuü":
                if letter.isupper():
                    translation = translation + "G"
                else:
                    translation = translation + "g"
            else:
                translation = translation + letter
        return translation


    given_phrase = input("give me a phrase : ")
    if given_phrase == "quit":
        break
    else:
        print(translate(given_phrase))

