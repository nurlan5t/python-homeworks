def write_to_file(line):
    new_file = open("quiz.txt", "a")
    new_file.write(f"{line}\n")
    new_file.close()

def read_from_file():
    file = open("quiz.txt", "r")
    lines = file.readlines()
    file.close()
    return lines
