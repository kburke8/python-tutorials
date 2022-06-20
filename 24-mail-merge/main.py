with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as template_file:
    template = template_file.read()

for name in names:
    name = name.strip()
    letter = template.replace("[name]", name)
    with open(f"./Output/ReadyToSend/{name}.txt", "w") as new_letter:
        new_letter.write(letter)
