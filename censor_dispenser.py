# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "herself", "her"]

def censor(document, terms):
    censored = document
    for t in terms:
        blank_out = ''
        for c in t:
            if c != ' ':
                blank_out += '*'
            else:
                blank_out += ' '
        while censored.lower().find(t) >= 0:
            censored = censored[:censored.lower().find(t)] + blank_out + censored[censored.lower().find(t) + len(t):]
    return censored

negative_words = ["concerned", "behind", "dangerous", "danger", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset",
"awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]

print(email_three)

def tone_down(document, terms, negatives):
    toned_down = censor(document, terms)
    first = toned_down
    for n in negatives:
        if toned_down.lower().find(n) > 0 and toned_down.lower().find(n) < len(first):
            first = toned_down[:toned_down.lower().find(n) + len(n) + 1]
    for n in negatives:
        blank_out = ''
        for c in n:
            if c == ' ':
                blank_out += c
            else:
                blank_out += '*'
        while toned_down[len(first):].lower().find(n) >= 0:
            toned_down = first + toned_down[len(first):toned_down.lower().find(n)] + blank_out + toned_down[toned_down.lower().find(n) + len(n):]
        
    return toned_down
 
print(censor(email_one, proprietary_terms))
print(censor(email_two, proprietary_terms))
print(tone_down(email_three, proprietary_terms, negative_words))