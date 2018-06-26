class Dog:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return "Arf!"

class Poodle(Dog):
    def speak(self):
        return "Yip!" 

if __name__ == "__main__":
    s=set()
    s.add(Dog("Rex"))
    s.add(Poodle("Fifi"))
    s.add(Dog("Spot"))
    s.add(Poodle("Spike"))
    for dog in s:
        print(dog.name,"says",dog.speak())

print(__name__)
