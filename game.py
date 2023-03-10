import sys
from termcolor import cprint

from player import Player
from settings import *
from messages import *


# класс Game, отвечающий за игру
class Game:
    def __init__(self):
        self.room_number = 0
        self.player = Player()
        print(messages["start_messages"])

    # метод отвечающий за начало игры
    def start_game(self):
        self.print_text()

    # метод отвечающий за написание текста комнаты, вывод и сбор данных
    def print_text(self):
        print(room_description[room_names[self.room_number]])
        if self.room_number in room_with_objects and rooms_objects[
            room_names[self.room_number]] not in self.player.get_inventory():
            print(messages[rooms_objects[room_names[self.room_number]]])
            cprint(messages["item_question"] + rooms_objects[room_names[self.room_number]] + "? (Да/Нет)", "light_green")
            answer = input().strip().lower()
            while answer not in ["да", "нет"]:
                cprint(messages["error"], "red")
                answer = input().strip().lower()
            if answer == "да":
                self.set_item_to_player()
        cprint(messages["question"], "light_blue")
        if "фонарик" in self.player.get_inventory():
            possible_rooms = room_connections[self.room_number]
        else:
            possible_rooms = [room for room in room_connections[self.room_number] if room in room_without_light]
        choice = self.print_possible_rooms(possible_rooms)
        self.room_number = room_connections[self.room_number][int(choice) - 1]
        print()
        if self.room_number in ending_rooms:
            self.end()
        self.print_text()

    # метод отвечающий за вывод комнат, в которые можно пойти
    def print_possible_rooms(self, possible_rooms):
        possible_variants = list()
        for number, room in enumerate(possible_rooms):
            cprint(f"{number + 1}. {room_names[room]}", "cyan")
            possible_variants.append(number + 1)
        choice = input()
        while not choice.isdigit() or int(choice) not in possible_variants:
            cprint(messages["error"], "red")
            choice = input()
        return choice

    # метод отвечающий за добавление вещи в инвентарь игрока
    def set_item_to_player(self):
        if not self.player.set_item(rooms_objects[room_names[self.room_number]]):
            cprint(messages["inventory_error"] + self.player.get_inventory()[-1] + "? (Да/Нет)", "light_green")
            answer = input().strip().lower()
            while answer not in ["да", "нет"]:
                cprint(messages["error"], "red")
                answer = input().strip().lower()
            if answer == "да":
                self.player.get_inventory()[-1] = rooms_objects[room_names[self.room_number]]
        cprint(messages["update_inventory"] + ", ".join(self.player.get_inventory()), "light_blue")

    # метод отвечающий за битву с финальным боссом
    def fight(self, stage):
        stage_name = stages[stage]
        cprint(fight_messages[f"{stage_name}_hit"], "light_green")
        answer = input().strip().lower()
        while (answer not in ["влево", "вправо"] and stage in [1, 3]) and (
                answer not in ["да", "нет"] and stage in [2]):
            cprint(messages["error"], "red")
            answer = input().strip().lower()
        if stage != 4:
            if answer == "влево" or answer == "нет":
                print(fight_messages[f"{stage_name}_hit_to_left"])
            else:
                print(fight_messages[f"{stage_name}_hit_to_right"])
            self.fight(stage + 1)
        else:
            if len(self.player.get_inventory()) == 2:
                if answer == "да":
                    if "огнетушитель" in self.player.get_inventory():
                        print(endings["ending_yes_with_extinguisher"])
                    if "аптечка" in self.player.get_inventory():
                        print(endings["ending_yes_with_kit"])
                else:
                    if "огнетушитель" in self.player.get_inventory():
                        print(endings["ending_no_with_extinguisher"])
                    if "аптечка" in self.player.get_inventory():
                        print(endings["ending_no_with_kit"])
            else:
                print(endings["ending_with_nothing"])
            input()
            sys.exit(0)

    # метод отвечающий за конец игры
    def end(self):
        if self.room_number == 10:
            print(endings["ending_without_fight"])
        else:
            self.fight(1)
