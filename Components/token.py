class Token:
    def __init__(self, content):
        self.content = content

        if self.content == 'var':
            self.type = 'T_VAR'
        elif self.content == 'out':
            self.type = 'T_OUT'
        elif self.content == 'if':
            self.type = 'T_IF'
        elif self.content == 'func':
            self.type = 'T_FUNC'
        elif self.content == '=':
            self.type = 'T_SET'
        elif self.content == '==':
            self.type = 'T_EQUAL'
        elif self.content == '>=':
            self.type = 'T_BIGGEROREQUAL'
        elif self.content == '<=':
            self.type = 'T_SMALLEROREQUAL'
        elif self.content == '>':
            self.type = 'T_BIGGER'
        elif self.content == '<':
            self.type = 'T_SMALLER'
        elif self.content == '+':
            self.type = 'T_PLUS'
        elif self.content == '-':
            self.type = 'T_MINUS'
        elif self.content == '*':
            self.type = 'T_MULTIPLY'
        elif self.content == '/':
            self.type = 'T_DIVIDE'
        elif self.content.isdigit():
            self.type = 'T_INT'
        elif not self.content.isdigit():
            self.type = 'T_STRING'
    
    def __repr__(self) -> str:
        return self.type

