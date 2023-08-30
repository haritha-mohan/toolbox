import sys
import glob
import re
import os
import subprocess

def modify_second_line(filename, new_line_text):
    with open(filename, 'r') as file:
        lines = file.readlines()

    if len(lines) >= 2 and lines[1].startswith("##"):
        # alr added name to binding, updating status with PR link
        lines[1] = new_line_text + '\n'
    else:
        # adding name to binding
        lines.insert(1, new_line_text + '\n')

    with open(filename, 'w') as file:
        file.writelines(lines)

def modify_files_in_directory(directory, pattern, new_line_text):
    file_list = glob.glob(os.path.join(directory, pattern))
    count = 0
    
    for filename in file_list:
        modify_second_line(filename, new_line_text)
        print(f"Second line modified in {filename}")
        count += 1
    
    return count

def run_make_command(directory_path):
    original_directory = os.getcwd()

    try:
        os.chdir(directory_path)
        subprocess.run(["make", "all"], check=True)
    except Exception as e:
        print("Error occurred with running make all:", e)
    finally:
        os.chdir(original_directory)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 wiki-catalyst.py <directory> <file_pattern> <new_line_text>")
        sys.exit(1)

    directory_path = sys.argv[1]
    file_pattern = sys.argv[2]
    new_line_text = sys.argv[3]

    count = modify_files_in_directory(directory_path, file_pattern, new_line_text)

    print("Modification completed!")
    print(f"Total files modified: {count}")
    run_make_command(directory_path)
