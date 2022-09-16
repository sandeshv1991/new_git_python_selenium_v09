class Point:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __len__self():
        return 2

    def __contains__(self,value):
        if value in self.__dict__.values():
            return True
        return False

    def __getitem__(self,index):
        if index == 0:
            return self.a
        elif index == 1:
            return self.b
        else:
            raise IndexError("no value in this index")

    def __setitem__(self,index,value):
        if index == 0:
            self.a = value
        elif index == 1:
            self.b = value

p1 = Point(1,2)
p1.__getitem__(0)
