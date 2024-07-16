class Emotion(Character, Skill):
    def __init__(self, name, age, title, level, color):
        super().__init__(name, age)
        super().__init__(title, level)
        self.__color = color

    def introduce(self):
        return f"{super().introduce()} and I am Emotion"

    """def introduce(self):
        return f'Hi I am {self.name} and i am an emotion'

    def get_color(self):
    return self.__color
"""
#hacer otro archivo Human.py

class Human:
    def __init__(self, name, age, gender, rol):
        self.name = name
        self.age = age
        self.gender = gender
        self.rol = rol

    def introduce(self):
        return f"Hi, I am {self.name} "


#hacer otro archivo Character.py
class Character:
    def __init__(self, name, age):
        self.__name= name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

#hacer otro archivo Skill.py
class Skill:
    def __init__(self, title, level):
        self.__title = title
        self.__level = level


#print(Emotion.mro()) para ver el orden de las jerarquias de las clases

