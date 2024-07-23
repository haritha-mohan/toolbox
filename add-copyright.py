import os
import sys

def add_or_update_copyright_comment(directory_path):
    comment = "// Copyright (c) Microsoft Corporation. All rights reserved."
    for subdir, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".cs"):
                file_path = os.path.join(subdir, file)
                with open(file_path, "r") as f:
                    lines = f.readlines()

                # Remove any existing copyright line
                lines = [line for line in lines if not line.strip().startswith("// Copyright (c) Microsoft")]

                # Ensure no extra empty line at the beginning
                if lines and lines[0].strip() == "":
                    lines = lines[1:]

                # Add the copyright line and a new line at the beginning
                updated_lines = [comment + "\n", "\n"] + lines

                with open(file_path, "w") as f:
                    f.writelines(updated_lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/your/directory")
        sys.exit(1)

    directory_to_process = sys.argv[1]
    add_or_update_copyright_comment(directory_to_process)
    print(f"Copyright line added or updated in .cs files in {directory_to_process}")
