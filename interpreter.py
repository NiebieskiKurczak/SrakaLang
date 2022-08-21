import Components.token as token
import Components.err_man as er
import Components.num_man
import Components.var as var
# VERSION 0.1

AllowPythonCode = False

def run(fileOrg):
    with open(fileOrg, "r") as f:
        code = f.readlines()

    var_Table = {}
    fun_Table = {}

    for line in code:
        splitLine = line.split()
        t = []

        for u in splitLine:
            t.append(token.Token(u))
        
        if t[0].type == 'T_VAR':
            try:
                if not t[1].type == 'T_STRING' or not t[2].type == 'T_SET':
                    er.Put_Err(line, "Invalid Syntax! Use: 'VAR' + 'STR' + '=' + 'STR, INT'")
            except Exception:
                er.Put_Err(line, "Invalid Syntax! Use: 'VAR' + 'STR' + '=' + 'STR, INT'")
            
            nm = Components.num_man.Num_Man()
            strn = ''

            for n in range(len(splitLine)):
                if n >= 3:
                    strn += (splitLine[n] + ' ')

            l = nm.Manage(strn, var_Table)
            tvar = var.Var(l)

            var_Table[t[1].content] = tvar
    
    print(var_Table)

            
