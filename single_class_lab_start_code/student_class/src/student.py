
class Student:
    def __init__(self, name, cohort): 
        self.name = name
        self.cohort = cohort

    def talk(self):
        return "I can talk!"

    def say_favourite_language(self,language):
        return f"I love {language}"

# I've created a class Student with the properties of name and cohort - hint, could be bananas. Self is a need, also technically we
# don't need to look at it. 
# created a talk method which returns the string "I can talk!"
# Then created a method called say_favourite_language with the language property. This returns "I love Python/Bananas" becase
# of the f in front of the string which formats the return with the {language}inside

