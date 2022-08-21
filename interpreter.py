from var import Var, VarManager
from out import Out
from func import FuncManager
from apc import Apc

# VERSION 0.1

AllowPythonCode = False

def run(fileOrg):
    with open(fileOrg, "r") as f:
        code = f.readlines()

    var_Table = {}
    fun_Table = {}

    for line in code:
        var = VarManager()
        out = Out()
        fun = FuncManager()
        apc = Apc()
        fun.Run(line, fun_Table, False)
        var.Run(line, var_Table)
        out.Run(line, var_Table)
        apc.Run(line, AllowPythonCode)