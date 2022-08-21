import sys

# er.Put_Err("NUM_MAN", "ERROR HAS ACCURED")
# er.Put_Warn("APC", "Python Code is not enabled! You must add --AllowPythonCode flag to interpreter!")

def Put_Err(line, txt, ext=True):
    strn = ''

    print(f"\033[91m{line}\033[0m")

    for i in range(len(line)):
        strn = strn + '^'

    print(f"\033[91m{strn}\033[0m")
    print(f"\033[91m{txt}\033[0m")

    if ext:
        sys.exit()

def Put_Warn(line, txt):
    strn = ''

    print(f"\033[93m{line}\033[0m")

    for i in range(len(line)):
        strn = strn + '^'

    print(f"\033[93m{strn}\033[0m")
    print(f"\033[93m{txt}\033[0m")
