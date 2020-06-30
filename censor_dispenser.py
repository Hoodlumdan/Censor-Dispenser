# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "herself", "her"]

negative_words = ["concerned", "behind", "dangerous", "danger", "alarming", "alarmed", "alarmingly", "out of control", "help", "unhappy", "bad", "upset",
"awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]

punctuation = [",", "!", "?", ".", "%", "/", "(", ")", " "]

# Match censor length to original word length and check for punctuation
def blank_out(word):
    blank = ''
    b = ''
    for c in word:
        for p in punctuation:
            if c == p:
                b = c
                break
            else:
                b = '*'
        blank += b
    
    return blank

def censor(document, terms):
    censored = document
    for t in terms:
        # Find returns -1 if not found since indexes start at 0       
        while censored.lower().find(t) >= 0:
            blank = blank_out(t)
            # New string is equal to old string split around censored word
            censored = censored[:censored.lower().find(t)] + blank + censored[censored.lower().find(t) + len(t):]
    return censored


def tone_down(document, terms, negatives):
    toned_down = censor(document, terms)
    first = toned_down
    for n in negatives:
        # Set variable equal to input string up to first occurrence of a blacklisted word
        if toned_down.lower().find(n) > 0 and toned_down.lower().find(n) < len(first):
            first = toned_down[:toned_down.lower().find(n) + len(n) + 1]
    for n in negatives:
        while toned_down[len(first):].lower().find(n) >= 0:
            blank = blank_out(n)
            toned_down = first + toned_down[len(first):toned_down.lower().find(n)] + blank + toned_down[toned_down.lower().find(n) + len(n):]
    return toned_down


def super_censor(document, terms, negatives, extra):
    # Checking and editing a list is much easier. Leaving split() blank removed newlines "\n" as well as spaces.
    super_censored = document.split(' ')    
    
    for c in super_censored:
        index = super_censored.index(c)
        w = c.strip(''.join(punctuation)).lower()
        
        for t in terms:
            # Split the bad term into individual words otherwise multi-word terms don't get caught
            for p in t.split():
                # If the word isn't part of a blacklisted term we don't need to change the list entry and can end the loop
                if w != p:
                    break
                else:
                    super_censored[index] = blank_out(c)
                    
                    # Added a customisable amount of surrounding words to remove
                    for r in range(extra):                    
                        super_censored[index - extra ] = blank_out(super_censored[index - extra ])
                        super_censored[index + extra ] = blank_out(super_censored[index + extra ])
        
        for n in negatives:
            for p in n.split():
                if w != n:
                    break
                else:
                    super_censored[index] = blank_out(c)
                    
                    for r in range(extra):                    
                        super_censored[index - extra ] = blank_out(super_censored[index - extra ])
                        super_censored[index + extra ] = blank_out(super_censored[index + extra ])
    # Combines all elements in list with a space in-between
    return ' '.join(super_censored)
             
print(email_one.replace("learning algorithm", '*****'))
print(censor(email_two, proprietary_terms))
print(tone_down(email_three, proprietary_terms, negative_words))
print(super_censor(email_four, proprietary_terms, negative_words, 1))