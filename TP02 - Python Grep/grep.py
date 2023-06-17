import sys
import os

def scan_file(root, target_directory, target_string, option=""):
    try:
        old_target_directory = target_directory
        target_directory = os.path.join(os.getcwd(), target_directory)

        if os.path.exists(target_directory):
            if os.path.isfile(target_directory):
                with open(target_directory, "r") as file:
                    for line_num, line_text in enumerate(file, 1):
                        if is_match(line_text, target_string, option):
                            print_line(str(target_directory).replace(root, ""), line_num, line_text)
            else:
                os.chdir(target_directory)
                for main_directory, _, files in os.walk(os.getcwd()):
                    for filename in files:
                        current_file = os.path.join(main_directory, filename)
                        with open(current_file, "r") as file:
                            for line_num, line_text in enumerate(file, 1):
                                if is_match(line_text, target_string, option):
                                    print_line(str(current_file).replace(root, ""), line_num, line_text)
        else:
            raise Exception(f"Path {old_target_directory} tidak ditemukan")
    except Exception as invalid:
        print(invalid)

def is_match(line_text, target_string, option):
    if option == "-i":
        return is_match_case_insensitive(line_text, target_string)
    elif option == "-w":
        return is_match_whole_word(line_text, target_string)
    else:
        return is_match_case_sensitive(line_text, target_string)

def is_match_case_insensitive(line_text, target_string):
    if "*" in target_string:
        stringX, stringY = get_wildcard_strings(target_string)
        return stringX.upper() in line_text.upper() and stringY.upper() in line_text.upper()
    else:
        return target_string.upper() in line_text.upper()

def is_match_whole_word(line_text, target_string):
    if "*" in target_string:
        stringX, stringY = get_wildcard_strings(target_string)
        list_line_text = line_text.strip().split(" ")
        for word in list_line_text:
            if stringX in word and stringY in word:
                return True
        return False
    else:
        return target_string in line_text.strip().split(" ")

def is_match_case_sensitive(line_text, target_string):
    if "*" in target_string:
        stringX, stringY = get_wildcard_strings(target_string)
        return stringX in line_text and stringY in line_text
    else:
        return target_string in line_text

def get_wildcard_strings(target_string):
    new_target_string = target_string.split("*")
    if len(new_target_string) > 2:
        raise Exception("Argumen program tidak benar")
    else:
        stringX = new_target_string[0]
        stringY = new_target_string[1]
    return stringX, stringY

def print_line(filedir, line_num, line_text):
    print("{:<40} line {:<3} {:<.40}".format(filedir[1:], line_num, line_text.strip()))

def main():
    root = os.getcwd()
    if len(sys.argv) == 3:
        target_string = sys.argv[1]
        target_directory = sys.argv[2]
        scan_file(root, target_directory, target_string)
    elif len(sys.argv) == 4 and (sys.argv[1] == "-i" or sys.argv[1] == "-w"):
        target_string = sys.argv[2]
        target_directory = sys.argv[3]
        scan_file(root, target_directory, target_string, sys.argv[1])
    else:
        print("Argumen program tidak benar")

if __name__ == "__main__":
    main()
