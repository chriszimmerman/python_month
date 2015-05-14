class Square(object):
    def __init__(self, number, row, column, block):
        self.number = number
        self.row = row 
        self.column = column 
        self.block = block

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)

    def __hash__(self):
        return int(str(self.number) + str(self.row) + str(self.column) + str(self.block))
