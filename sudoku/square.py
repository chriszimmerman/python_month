class Square(object):
    def __init__(self, number, row, column, block):
        self.number = number
        self.row = row 
        self.column = column 
        self.block = block

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)
