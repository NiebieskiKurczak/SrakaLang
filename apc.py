import err_man as er

class Apc:
    def Run(self, line, apcB, addInfo=True):
        if addInfo:
            try:
                self.Code(line, apcB)
            except:
                er.Put_Err("APC", "Unknown error has accured")
        else:
            self.Code(line, apcB)

    def Code(self, line, apcB):
        self.splitLine = line.split(' ', 1)

        if self.splitLine[0] == 'apc':
            if apcB:
                exec(self.splitLine[1])
            else:
                er.Put_Warn("APC", "Python Code is not enabled! To enable it, add --AllowPythonCode flag to interpreter!")
