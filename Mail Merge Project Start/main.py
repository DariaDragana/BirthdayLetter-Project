with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    text = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = text.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
