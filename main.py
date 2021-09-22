from Ninja import Ninja
from Pet import Pet


treats= ["ball", "toy", "toy2"]
petfood= ["DogChow", "FastFood"]

snoopy= Pet("Snoopy", "Dog", ["jumps", "hides"], "pssstt") 

Marco= Ninja("Marco", "Villegas", treats, petfood, snoopy)


Marco.feed()
Marco.walk()
Marco.bathe()

