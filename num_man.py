import err_man as er

class Num_Man():
    def Manage(self, input, var_Table, addInfo=True):
        if addInfo:
            try:
                self.ret = self.MCode(input, var_Table)
                return self.ret
            except:
                er.Put_Err("NUM_MAN", "Unknown error has accured")
                return input
        else:
            self.ret = self.MCode(input, var_Table)
            return self.ret

    def MCode(self, input, var_Table):
        self.inputf = input.split()
        self.leng = len(self.inputf)
        
        # var_Table[self.sline[0][1:]]

        if self.leng == 1:
            return input
        elif self.leng == 2:
            er.Put_Err("NUM_MAN", "Invalid Syntax! Use: 'NUM' + '+, -, *, /' + 'NUM'")
            return 'invalid'

        if not self.inputf[0][0].isdigit():
            
            if self.inputf[1] == '-':
                self.ret = var_Table[self.inputf[0]] - int(self.inputf[2])
                return self.ret
            if self.inputf[1] == '+':
                self.ret = var_Table[self.inputf[0]] + int(self.inputf[2])
                return self.ret
            if self.inputf[1] == '*':
                self.ret = var_Table[self.inputf[0]] * int(self.inputf[2])
                return self.ret
            if self.inputf[1] == '/':
                self.ret = var_Table[self.inputf[0]] / int(self.inputf[2])
                return self.ret

        if self.inputf[1] == '-':
            self.ret = int(self.inputf[0]) - int(self.inputf[2])
            return self.ret
        if self.inputf[1] == '+':
            self.ret = int(self.inputf[0]) + int(self.inputf[2])
            return self.ret
        if self.inputf[1] == '*':
            self.ret = int(self.inputf[0]) * int(self.inputf[2])
            return self.ret
        if self.inputf[1] == '/':
            self.ret = int(self.inputf[0]) / int(self.inputf[2])
            return self.ret
