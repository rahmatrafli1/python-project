class Orang:
    def __init__(self, name, age=0):
        self.name = name
        self._age = age


org_obj = Orang('Budi')
print(org_obj._age)
