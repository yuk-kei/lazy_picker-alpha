class Entity:
    """Act like a basic class or abstract class """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = (x, y)


class Item:
    """ A class to represent an item in the warehouse. """

    def __init__(self, item_id, x, y):
        self.x = x
        self.y = y
        self.item_id = item_id
        self.pos = (int(float(self.x)), int(float(self.y)))

    def __str__(self):
        return "Item ID: " + str(self.item_id) + " \t" + "X: " + str(self.x) + "\t" + "Y: " + str(self.y) + "\t"\
            + "position: " + str(self.pos)

    def toJSON(self):
        return {
            "item_id": self.item_id,
            "x": self.x,
            "y": self.y
        }


class Shelf(Entity):
    """ A class to represent a shelf in the warehouse.
    """

    def __init__(self, shelf_id, x, y):
        super().__init__(x, y)
        self.shelf_id = shelf_id
        self.items = []

    def add_item(self, item):
        """
        The add_item function adds an item to the list of items in a given order.

        :param self: Refer to the current instance of a class
        :param item: Add an item to the list of items

        """
        self.items.append(item)

    def remove_item(self, item):
        """
        The remove_item function removes an item from the list of items in a room.
        Args:
            item (str): The name of the item to be removed.

        :param self: Refer to the instance of the class
        :param item: Specify the item that is being removed from the list

        """
        self.items.remove(item)

    def get_item(self, item_id):
        """ Return the item with the given name.

        :param self: Refer to the instance of the class
        :param item_id: Specify the item that is being returned
        :return: The wanted item
        """
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def get_item_count(self):

        """
        The get_item_count function returns the number of items in the list.

        :param self: Represent the instance of the class
        :return: The number of items in the list

        """
        return len(self.items)

    def __str__(self):
        item_str = ""
        for item in self.items:
            item_str += str(item) + "\n"
        return "Shelf ID: " + str(self.shelf_id) + "\n" + "X: " + str(self.x) + "\n" + "Y: " + str(
            self.y) + "\n" + "Items: " + item_str

    def toJSON(self):
        """ Return a JSON representation of the shelf."""
        return {
            "shelf_id": self.shelf_id,
            "x": self.x,
            "y": self.y,
            "items": self.items
        }


class Worker(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_carrying = False
        self.carrying_item = None

    def pick_up_item(self, item):
        """
        The pick_up_item function takes an item as a parameter and sets the player's is_carrying attribute to True.
        It also sets the carrying_item attribute to the item that was passed in.

        :param self: Refer to the object itself
        :param item: Set the carrying_item attribute to the item
        :return: The carrying_item

        """
        self.is_carrying = True
        self.carrying_item = item

    def drop_off_item(self):
        """
        The drop_off_item function sets the is_carrying attribute to False and the carrying_item attribute to None.
        This means that after this function is called, the robot will no longer be carrying an item.

        :param self: Refer to the instance of the class
        :return: A boolean value of false and a none object

        """
        self.is_carrying = False
        self.carrying_item = None

    def __str__(self):
        return "Worker X: " + str(self.x) + "\n" + "Worker Y: " + str(self.y) + "\n" + "Is Carrying: " + str(
            self.is_carrying) + "\n" + "Carrying Item: " + str(self.carrying_item)

    def toJSON(self):
        return {
            "x": self.x,
            "y": self.y,
            "is_carrying": self.is_carrying,
            "carrying_item": self.carrying_item
        }
