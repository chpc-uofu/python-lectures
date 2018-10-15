class Dog:
    "Class Dog defines a generic dog."
    def __init__(self,name):
        self.name=name
    def speak(self):
        return "Arf!"

class Poodle(Dog):
    """Class Poodle defines a special kind of dog, and is derived from
    the Dog class."""
    def speak(self):
        return "Yip!" 

# This code gets run only if this module is executed, not if it is imported:
if __name__ == "__main__":
    # Create a set.
    s=set()
    # Add some dogs to the set.
    s.add(Dog("Rex"))
    s.add(Poodle("Fifi"))
    s.add(Dog("Spot"))
    s.add(Poodle("Spike"))
    # For each dog ...
    for dog in s:
    	# ... print the dogs name and what it says.
        print(dog.name,"says",dog.speak())

print(__name__)
