import os

from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-p", "--path", required=False, help="Path for generate __init__.py")
    parser.add_argument("-f", "--force", required=False, help="Force replace __init__.py", default=False, action='store_true')

    args = parser.parse_args()
    
    # Prepare data
    PATH = os.getcwd()
    FULL_PATH = os.path.join(PATH, args.path or '')
    FULL_INIT = os.path.join(FULL_PATH, "__init__.py")
    COUNT = 0
    RAW_FILE = ""

    # Check file endswith is py file
    for file in os.listdir(FULL_PATH) :
        # Skip __main__ and __init__ 
        if file.endswith(".py") and os.path.isfile(os.path.join(FULL_PATH, file)):
            info = file.split(".")
            if not info[0] in ["__init__", "__main__"]:
                RAW_FILE += f"from .{info[0]} import *\n"
                COUNT += 1

    if COUNT == 0:
        print("\33[41mNot exist .py file\33[0m")
        exit(1)

    # Check if __init__.py exist
    if os.path.exists(FULL_INIT) and not args.force:
        try:
            print("\33[43m!!Warning!!\33[0m")
            print("\33[33mThere __init__.py exist in ",FULL_INIT,"\33[0m\n")
            input("Do you want process? [Press enter to continun]")
        except KeyboardInterrupt:
            print("\n\n\33[41mAbort!\33[0m")
            exit(1)
    

    with open(os.path.join(FULL_PATH, "__init__.py"), "w") as f:
        f.write(RAW_FILE)

    print("\33[42mDone", COUNT, "files\33[0m")