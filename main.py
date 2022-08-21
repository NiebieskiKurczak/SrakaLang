import interpreter
import sys

args = sys.argv
try:
    if args[2] == '--AllowPythonCode':
       #interpreter.AllowPythonCode = True
       pass
except:
    pass

interpreter.run(args[1])