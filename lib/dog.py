APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="DefaultName", breed=None):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            return

        if breed is not None and breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            return

        self.name = name
        self.breed = breed

# Example usage:
fido = Dog(name="Fido", breed="Pug")
