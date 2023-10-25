BAD_WORDS = [
    "fuck",
    "shit",
    "bullshit",
    "bastard",
    "bitch",
    "whore",
    "damn",
]

def censored(text):
    text = text.split(" ")
    new_text = []
    for i in text:
        if i.lower() in BAD_WORDS:
            i = '*' * len(i)
        new_text.append(i)

    text = " ".join(new_text)
    # print(text)
    return text


assert censored("this line should not be censored at all") == "this line should not be censored at all"
assert censored("fuck this bitch") == "**** this *****"
assert censored("This task is UTTER BULLshit") == "This task is UTTER ********", "be careful with the case!"
assert censored("") == ""
