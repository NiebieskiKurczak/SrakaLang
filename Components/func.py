import err_man as er

class FuncManager:
    def Run(self, line, fun_Table, addInfo=True):
        if addInfo:
            try:
                self.Code(line, fun_Table)
            except:
                er.Put_Err("FUNC_MANAGER", "Unknown error has accured")
        else:
            self.Code(line, fun_Table)

    def Code(self, line, fun_Table):
        self.cline = line.split('#')
        self.mline = line.split(':')

        if self.cline[0] == 'fun ':
            fun_Table[self.cline[0][1:]] = self.cline
