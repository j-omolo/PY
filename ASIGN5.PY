# Base class: Superhero
class Superhero:
    def __init__(self, name, alias, power_level, origin):
        self.name = name
        self.alias = alias
        self.power_level = power_level
        self.origin = origin

    def display_identity(self):
        return f"Hero Name: {self.name}, Alias: {self.alias}"

    def fight_crime(self):
        return f"{self.alias} fights crime with a power level of {self.power_level}!"

# Subclass 1: FlyingHero
class FlyingHero(Superhero):
    def __init__(self, name, alias, power_level, origin, flight_speed):
        super().__init__(name, alias, power_level, origin)
        self.flight_speed = flight_speed

    def fight_crime(self):
        return f"{self.alias} soars through the skies at {self.flight_speed} mph to fight crime!"

# Subclass 2: StrengthHero
class StrengthHero(Superhero):
    def __init__(self, name, alias, power_level, origin, strength_level):
        super().__init__(name, alias, power_level, origin)
        self.strength_level = strength_level

    def fight_crime(self):
        return f"{self.alias} uses superhuman strength (Level: {self.strength_level}) to protect the city!"


if __name__ == "__main__":
    # Creating objects for each class
    general_hero = Superhero("Diana Prince", "Wonder Woman", 95, "Amazon")
    flying_hero = FlyingHero("Clark Kent", "Superman", 100, "Krypton", 500)
    strength_hero = StrengthHero("Bruce Banner", "Hulk", 90, "Earth", "Massive")

    # Display identity
    print(general_hero.display_identity())
    print(flying_hero.display_identity())
    print(strength_hero.display_identity())

    # Fight crime with unique behavior (polymorphism)
    print(general_hero.fight_crime())
    print(flying_hero.fight_crime())
    print(strength_hero.fight_crime())