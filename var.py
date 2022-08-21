from num_man import Num_Man
import err_man as er

class VarManager:
    def Run(self, line, var_Table, addInfo=True):
        if addInfo:
            try:
                self.Code(line, var_Table)
            except:
                er.Put_Err("VAR_MANAGER", "Unknown error has accured")
        else:
            self.Code(line, var_Table)

    def Code(self, line, var_Table):
        self.splitLine = line.split()

        if self.splitLine[0] == 'var':
            self.nm = Num_Man()
            self.strn = ''

            for n in range(len(self.splitLine)):
                if n >= 3:
                    self.strn += (self.splitLine[n] + ' ')

            self.l = self.nm.Manage(self.strn, var_Table)

            var_Table[self.splitLine[1]] = self.l

class Var:
    def __init__(self, content, type):
        self.content = content
        self.type = type
    
    def _setType(self):
        pass