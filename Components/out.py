import err_man as er

class Out:
    def Run(self, line, var_Table, addInfo=True):
        if addInfo:
            try:
                self.Code(line, var_Table)
            except:
                er.Put_Err("OUT", "Unknown error has accured")
        else:
            self.Code(line, var_Table)

    def Code(self, line, var_Table):
        self.splitLine = line.split()

        if self.splitLine[0] == 'out':
            if self.splitLine[1][0] == "'":
                print(self.splitLine[1][1:-1])
            else:
                try:
                    print(var_Table[self.splitLine[1]])
                except KeyError:
                    er.Put_Err("OUT", f"Variable '{self.splitLine[1]}' does not exist!")
