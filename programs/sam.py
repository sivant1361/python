class dog:
    def __init__(self,breed):
        self.breed=breed
my_dog=dog(breed="lab")
print(my_dog.breed)

class animal(dog):
    pass

c=cat("dobour man")
print(c.breed)