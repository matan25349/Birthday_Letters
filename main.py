# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

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

        