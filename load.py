import argparse
import os

def load():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder",help="nama_folder", nargs='?')

    args = parser.parse_args()
    folder = args.folder

    if folder is None:
        print("No folder name provided!")
        return
    
    if not os.path.exists(folder):
        print(f"folder {folder} not found.")
        return None

    print("Loading data from folder",folder)

    return folder

if __name__ == "__main__":
    load()