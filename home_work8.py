# Общий класс - животные
class Animals():
    voice = None
    limb = None
    skin = None
    nose = None

    def cry(self):
        print(self.voise)


# Классы домашней скотины и птицы наследуют от предка общие свойства с уникальными значениями
class Livestock(Animals):
    # уникальное свойство - есть рога
    horns = True

    def __init__(self):
        self.limb = 'hooves'
        self.skin = 'wool'
        self.nose = 'normal nose)'


class Fowl(Animals):
    def __init__(self):
        self.limb = 'paws and wings'
        self.skin = 'plumage'
        self.nose = 'beak'

    # уникальный метод - могут летать
    def fly(self):
        print('I FLY!')


class Cow(Livestock):
    def __init__(self):
        super().__init__()
        self.voise = 'мууу мууу'


class Goat(Livestock):
    def __init__(self):
        super().__init__()
        self.voise = 'меее меее'


class Sheep(Livestock):
    def __init__(self):
        super().__init__()
        self.voise = 'беее беее'


# у свиньи переопределяем переменные родительского класса
class Pig(Livestock):
    def __init__(self):
        super().__init__()
        self.skin = 'pigskin'
        self.nose = 'piglet'
        self.voise = 'хрю хрю'


class Duck(Fowl):
    def __init__(self):
        super().__init__()
        self.voise = 'кря кря'


class Goose(Fowl):
    def __init__(self):
        super().__init__()
        self.voise = 'га га га'


# у курицы переопределяем методы родительского класса
class Chicken(Fowl):
    def __init__(self):
        super().__init__()
        self.voise = 'кудах кудах)'

    def fly(self):
        print('I forgot to fly(')


# перекличка на скотном дворе
animals = [Cow(), Goat(), Sheep(), Pig(), Duck(), Goose(), Chicken()]
for animal in animals:
    animal.cry()

