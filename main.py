names = []
with open('C:/Users/Matan/PycharmProjects/name/Input/Names/invited_names.txt', "r") as file:
    for line in file:
        names.append(line.strip("\n"))
for name in names:
    with open('C:/Users/Matan/PycharmProjects/name/Input/Letters/starting_letter.txt', "r") as file:
        data = file.read()
        letter = data.replace("[name]", name)
    with open('C:/Users/Matan/PycharmProjects/name/Output/ReadyToSend/example.txt'.replace("example",
                                                                                           "letter_for_" + name),
              "a") as file:
        file.write(data.replace("[name]", name))

        
