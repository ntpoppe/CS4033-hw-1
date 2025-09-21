class Counter:
    __slots__ = ("expanded") # fun thing i learned a while back that
                              # forces a class to only have whitelisted attributes
    def __init__(self): 
        self.expanded = 0