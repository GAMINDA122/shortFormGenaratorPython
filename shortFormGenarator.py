print("-----------------------WELCOME TO SHORT FORM GENERATOR------------------")


def generator(sentence):
    word_list = sentence.split()
    short_form = ""
    for i in word_list:
        short_form = short_form + i[0].upper()
    print("Short Form : ",short_form)

text = input("Enter sentence : ")
generator(text)
next = int(input("Do you want to enter another word? (yes = 1 or exit = 0 ) : "))
count = 1
while count > 0:
    if next == 1:
        text = input("Enter sentence : ")
        generator(text)
        next = int(input("Do you want to enter another word? (yes = 1 or exit = 0 ) : "))
        if next == 1:
            count +=1
            continue
        else:
            print("-----------------------THANK YOU USE ME------------------")
            break
    else:
        print("-----------------------THANK YOU USE ME------------------")
        break