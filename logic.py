from random import randint
import requests
from datetime import datetime, timedelta

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(150,250)
        self.power = randint(5,15)
        self.last_feed_time = datetime.now
        Pokemon.pokemons[pokemon_trainer] = self


    def feed(self, feed_interval = 10, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time-delta_time}"




    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']["other"]["official-artwork"]["front_shiny"])
        else:
            return "https://upload.wikimedia.org/wikipedia/ru/7/77/Pikachu.png"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    def plus_age(self,age=1):
            plus = randint(1,3)
            age += plus
            # Определяем правильную форму слова
            last_two_digits = age % 100
            last_digit = age % 10
            
            if 11 <= last_two_digits <= 14:
                form = "лет"
            elif last_digit == 1:
                form = "год"
            elif last_digit in [2, 3, 4]:
                form = "года"
            else:
                form = "лет"
            return f"Ваш покемон вырос на {plus} {form}"\
            f"\nему {age} {form}"
            

    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

    # Метод класса для получения информации 
    def info(self):
        if self.pokemon_number == 42 or self.pokemon_number ==666 or self.pokemon_number ==52 or self.pokemon_number ==67 or self.pokemon_number ==555 or self.pokemon_number ==444 or self.pokemon_number ==777 or self.pokemon_number ==888 or self.pokemon_number ==999 or self.pokemon_number ==1001:
            return "Поздравляю вам попался редкий покемон:"\
            f"Имя твоего покеомона: {self.name}"\
            f"\nНомер твоего покеомона: {self.pokemon_number}"\
            f"\nСила: {self.power+5}, здоровье: {self.hp+50}"
        else:
            return f"Имя твоего покеомона: {self.name}"\
            f"\nНомер твоего покеомона: {self.pokemon_number}"\
            f"\nСила: {self.power}, здоровье: {self.hp}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img


class Wizard(Pokemon):
    
    def feed(self, feed_interval = 20, hp_increase = 20 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time-delta_time}"

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power} "