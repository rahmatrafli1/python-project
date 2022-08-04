class Kucing():
    def suara(self):
        print("Meow")

    def warna_tubuh(self):
        print("Warna tubuh kucing pada umumnya adalah kuning")


class Anjing():
    def suara(self):
        print("Woof")

    def harapan_hidup(self):
        print("Harapan hidup anjing adalah 15 tahun.")


obj1 = Kucing()
obj2 = Anjing()
for type in (obj1, obj2):
    type.suara()
