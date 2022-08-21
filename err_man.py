import sys

# er.Put_Err("NUM_MAN", "ERROR HAS ACCURED")
# er.Put_Warn("APC", "Python Code is not enabled! You must add --AllowPythonCode flag to interpreter!")

def Put_Err(seg, txt, ext=True):
    print(f"\033[91mComponent: '{seg}' Puts Error: '{txt}'\033[0m")

    if ext:
        sys.exit()

def Put_Warn(seg, txt):
    print(f"\033[93mComponent: '{seg}' Puts Warning: '{txt}'\033[0m")
