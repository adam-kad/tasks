text = "How can mirrors be real if our eyes aren't real"

list_text = list(text)


for index, letter in enumerate(list_text):
    if letter == ' ':
        list_text[index+1] = list_text[index+1].upper()
        #letter[index+1].upper()


print("".join(list_text))