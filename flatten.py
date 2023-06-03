import os
import sys
import shutil
import itertools


def flatten_folders(directory, only_images=False):
    result_files = []

    for root, dirs, files in itertools.islice(os.walk(directory), 1, None):
        for filename in files:
            if filename.endswith((".jpg", ".jpeg", ".png")) or not only_images:
                result_files.append((root, filename))

    # Move files to new destination
    for folder, file in result_files:
        parent_folder = os.path.basename(folder)
        new_file_name = f"{parent_folder}-{file}"
        src_path = os.path.join(folder, file)
        dst_path = os.path.join(directory, new_file_name)
        shutil.move(src_path, dst_path)

    # Delete original folders
    for root, dirs, _ in os.walk(directory, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            shutil.rmtree(folder_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python flatten.py <directory> <only_images>")
        sys.exit(1)
    
    directory_to_flatten = sys.argv[1]
    only_images = sys.argv[2].lower() in ["true", "yes", "1"] if len(sys.argv) > 2 else False
    
    if not os.path.isdir(directory_to_flatten):
        print(f"Error: {directory_to_flatten} is not a valid directory.")
        sys.exit(1)
    
    flatten_folders(directory_to_flatten, only_images)
