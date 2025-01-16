#!/usr/bin/env python3

import datetime
import os
import platform
import shutil
import subprocess
import tempfile


def main():
    # Get the project name from the current directory
    project_name = os.path.basename(os.getcwd())

    # Create target directory with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    target_dir = os.path.join(tempfile.gettempdir(), f"{project_name}_{timestamp}")
    os.makedirs(target_dir, exist_ok=True)

    try:
        # Read .aixtract file
        with open(".aixtract") as file:
            for filepath in file:
                filepath = filepath.strip()

                if not filepath or filepath.startswith("#"):
                    continue

                try:
                    if os.path.exists(filepath):
                        # Convert path separators to double underscores
                        new_filename = filepath.replace("/", "__")
                        # Copy the file to the target directory with the new name
                        shutil.copy2(filepath, os.path.join(target_dir, new_filename))
                        print(f"Copied: {filepath} -> {new_filename}")
                    else:
                        print(f"Warning: File not found: {filepath}")
                except Exception as e:
                    print(f"Error processing {filepath}: {str(e)}")

        print(f"\nFiles extracted to: {target_dir}")

        # Open the target directory
        if platform.system() == "Darwin":  # macOS
            subprocess.run(["open", target_dir])
        elif platform.system() == "Linux":
            subprocess.run(["xdg-open", target_dir])

    except FileNotFoundError:
        print("Error: .aixtract file not found in current directory")
        exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
