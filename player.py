# класс Player, который отвечает заигрока
class Player:
    def __init__(self):
        self.inventory = list()

    # метод для получения вещей в инветоре
    def get_inventory(self):
        return self.inventory

    # метод для добавления вещей в инвентарь
    def set_item(self, item):
        if len(self.inventory) < 2:
            self.inventory.append(item)
            return True
        return False
