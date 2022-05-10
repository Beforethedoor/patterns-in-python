from abc import ABC, abstractmethod


class Bike(ABC):

    @abstractmethod
    def run_bike(self) -> None:
        ...


class SportBike(Bike):

    def run_bike(self) -> None:
        print("Run sport bike!")


class CasualBike(Bike):

    def run_bike(self) -> None:
        print("Run casual bike!")


class Human():

    def __init__(self, bike: Bike):
        self.bike = bike

    def run(self) -> None:
        self.bike.run_bike()


sport_bike = SportBike()
casual_bike = CasualBike()

h = Human(bike=sport_bike)
h.run()

h.bike = casual_bike
h.run()
