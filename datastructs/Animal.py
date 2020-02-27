class Animal:
    def __init__(self, age, name=None):
        self.age = age
        self.name = name
        
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age
        
    def __str__(self):
        return f'animal: {self.name} {self.age}'
   

def main():
    cat = Animal(20, "ogobo")
    print(cat)
    
if __name__ == "__main__":
    main()
    
    
    
