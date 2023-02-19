class Player:
    def __init__(self):
        self.inventory = list()

    def get_inventory(self):
        return self.inventory

    def set_item(self, item):
        if len(self.inventory) < 2:
            self.inventory.append(item)
            return True
        return False
