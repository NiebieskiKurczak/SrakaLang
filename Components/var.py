class Var:
    def __init__(self, content):
        self.content = content
        print(self.content)

        if str(self.content).isdigit():
            self.type = 'T_INT'
        elif self.content != int(self.content):
            self.type = 'T_FLOAT'
        else:
            self.type = 'T_STRING'
        
    def __repr__(self) -> str:
        return f'{self.type}={self.content}'