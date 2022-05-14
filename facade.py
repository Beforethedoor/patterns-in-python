class Inverstor:
    def invest(self):
        print("Inverstor is investing money...")


class Vendor:
    def give(self):
        print("Vendor is giving materials...")


class Builder:
    def build(self):
        print("Builder is building build...")


class Facade:
    def __init__(self):
        self.investor = Inverstor()
        self.vendor = Vendor()
        self.builder = Builder()

    def start_project(self):
        self.investor.invest()
        self.vendor.give()
        self.builder.build()


worka = Facade()
worka.start_project()
