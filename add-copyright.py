import os
import sys

def add_copyright_comment(directory_path):
    comment = "// Copyright (c) Microsoft Corporation.  All rights reserved."
    for subdir, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".cs"):
                file_path = os.path.join(subdir, file)
                with open(file_path, "r") as f:
                    lines = f.readlines()
                updated_lines = [line.strip() for line in lines]
                if not updated_lines or comment not in updated_lines:
                    with open(file_path, "w") as f:
                        f.write(comment + "\n")
                        f.writelines(lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/your/directory")
        sys.exit(1)

    directory_to_process = sys.argv[1]
    add_copyright_comment(directory_to_process)
    print(f"Copyright line added to .cs files in {directory_to_process}")
