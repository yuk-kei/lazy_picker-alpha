import sys

from data import Algorithm, MapData
from entities import Item, Shelf, Worker
from service import Map, print_banner, refresh


def read_map_data(filename):
    """Reads the map data from the given file.
    It first generates a list of items by reading the file line by line.
    Then it generates a list of shelves by calling the gen_shelves function.

    :param filename: A string representing the name of the file to read from.
    :return: items and shelves generated from the data in the file.
    """

    items = []
    with open(filename, 'r') as file:
        # Skip the first line of the file

        next(file)
        # Read the file line by line
        for line in file:
            data = line.strip().split()
            item = Item(int(data[0]), float(data[1]), float(data[2]))

            items.append(item)

    shelves = gen_shelves(items)

    return items, shelves


def gen_shelves(items):
    """
    The gen_shelves function takes in a list of items and returns a list of shelves.
    The function first sorts the items by their position (x-coordinate, y-coordinate).
    It then iterates through the sorted list, if the current item has the same position as the previous item,
    it adds the item to the existing shelf. Otherwise, it creates a new shelf and adds the item to the shelf.

    :param items: A list of items read from the database file(from read_map_data function)
    :return: A list of shelves generated from the list of items
    """

    temp = list(items)
    # Sort the items by their position
    temp.sort(key=lambda item: item.pos)
    index = 0

    pre = temp[0]
    shelf = Shelf(index, pre.pos[0], pre.pos[1])
    shelf.add_item(pre)
    shelves = [shelf]
    # Iterate through the sorted list of items
    for i in range(1, len(temp)):

        curr = temp[i]
        # If the current item has the same position as the previous item, add the item to the existing shelf
        if curr.pos == pre.pos:
            i += 1
            shelf.add_item(curr)
        # Otherwise, create a new shelf and add the item to the shelf
        else:
            pre = curr
            index += 1

            shelf = Shelf(index, pre.pos[0], pre.pos[1])
            shelf.add_item(pre)
            shelves.append(shelf)

    return shelves


def get_worker_pos():
    """
    The get_worker_pos function base on the user's input to create a worker.
    If the user wants to use the default position, the function returns a worker with the default position.
    If the user wants to enter a custom position, the function prompts the user to enter the position
    The function then returns a worker with the custom position.


    :return: A worker object, which is used to create a worker
    :author:
    """

    while True:
        print()
        print("please enter the worker's starting position")
        is_default = input("Do you want to use the default position(0,0)? (y/n)")
        # If the user wants to use the default position, return a worker with the default position
        if is_default == "y":
            return Worker(0, 0)
        # If the user wants to enter a custom position, prompt the user to enter the x-coordinate and y-coordinate
        elif is_default == "n":
            print("worker's x-coordinate is:")
            worker_x = input()
            # Check if the input is numeric
            if worker_x.isnumeric():
                # Convert the input to an integer
                converted_x = int(worker_x)
                print("worker's y-coordinate is:")
                worker_y = input()
                # Check if the input is numeric
                if worker_y.isnumeric():
                    # Convert the input to an integer
                    converted_y = int(worker_y)
                    # Create a worker with the given position
                    worker_pos = (converted_x, converted_y)
                    # Display the worker's position(Let the user confirm the position)
                    print("worker's position is:", worker_pos)
                    print("Press any key to continue")
                    input()
                    return Worker(worker_pos[0], worker_pos[1])  # return the worker's position
                else:
                    print("must be number")
            else:
                print("must be number")
        else:
            print("invalid input")


def peek_items(items):
    """ Prints the items in the list.
        :param items: The list of all items
    """
    for item in items:
        print(item)

    input("Press any key to continue:")
    print()


def set_target_item(items):
    """
    The set_target_item function takes in a list of items and prompts the user to enter an item id.
    If the input is not numeric, it will prompt again until a valid number is entered.
    It then checks if that number matches any of the item ids in the list, and returns that item if so.

    :param items: Pass the list of items to the function
    :return: The target item
    """

    print()
    print("Please enter the target item's id:")
    print("(If you forgot the id, you can press 'p' to see all the items' information)")
    target_id = input()
    if target_id.isnumeric():
        converted_id = int(target_id)
        for item in items:
            if item.item_id == converted_id:
                print("Target item is:", item)
                return item
            else:
                continue
        print()
        print("Cannot find item with that id, please try again!")

        return set_target_item(items)

    elif target_id == "p":
        peek_items(items)
        return set_target_item(items)
    else:
        print("Invalid input")
        return set_target_item(items)


def initialize_data():
    """
    The initialize_data function reads the data from the database file to get the items and shelves,
    It first calls the read_map_data function to read the data from the file,
    then calls the get_worker_pos function to get the worker's starting position,
    then calls the set_target_item function to get the target item.
    finally, it generates a MapData object with the data it got from the previous functions.

    :return: A MapData object, which contains all the data needed to create a map
    """

    items, shelves = read_map_data('qvBox-warehouse-data-s23-v01.txt')
    worker = get_worker_pos()
    target = set_target_item(items)
    map_data = MapData(worker, shelves, items, target)

    return map_data


def display_welcome():
    """ Displays the welcome screen for the program.

    :return: None
    """

    refresh()
    print_banner()
    print('------------------------------------------------------------------------------------')
    print()
    print('Welcome to Lazy Warehouse Picker!')
    print("Before we start, please make sure you file is in the same directory as this program.")
    print()
    print('------------------------------------------------------------------------------------')
    print("Press 'space' then enter to continue...")
    while True:
        # wait for space key to be pressed
        key = input()
        if key == ' ':
            break
        elif key == 'q':
            sys.exit(0)
        else:
            print("Invalid input")


def find_path(map_data):
    """
    The find_path function takes in a MapData object and prompts the user to select an algorithm.
    It then calls the corresponding function in the Map class.
    If the user input 1, it calls the a_star function in the Map class.
    If the user input 2, it calls the bfs function in the Map class.
    If the user input 3, it calls the dijkstra function in the Map class.
    If the user input 4, it calls the dfs function in the Map class.

    :param map_data: Pass the MapData object to the function
    """

    refresh()
    grid = Map(map_data)
    grid.visualize(False)
    while True:
        print('-------------------------------------------------------------------------------------------------------')
        print()
        print("Welcome to the lazy picker for warehouse!")
        print("Press '1' to find path faster(using A *), '2' to find the shortest path(using BFS),")
        print("'3' to find the shortest path in another way(using Dijkstra), '4' to find a longer path(using DFS).")
        print("Press 'r' to return to the main menu")
        print()
        print('-------------------------------------------------------------------------------------------------------')

        choice = input('Press the corresponding number and enter to continue: ')

        if choice == '1':
            grid.a_star()

        elif choice == '2':
            grid.bfs()

        elif choice == '3':
            grid.dijkstra()

        elif choice == '4':
            grid.dfs()

        elif choice == 'r':
            display_menu(map_data)

        else:
            print('Invalid input')

        grid = Map(map_data)


def setting(map_data):
    """
    The setting function prompts the user to enter a new target item or algorithm.
    It then returns the new map data.

    :param map_data: Pass the map data to the function
    :return: The new map data
    """

    print()

    while True:
        print("Welcome to the setting menu!")
        print("Please enter '1' to set a new target item, '2' to set a new start point, or 'r' to return to the main "
              "menu")
        choice = input()
        if choice == "1":
            new_target = set_target_item(map_data.items)
            map_data.target = new_target

        elif choice == "2":
            new_worker = get_worker_pos()
            map_data.worker = new_worker

        elif choice == "r":
            return display_menu(map_data)

        else:
            print("Invalid input")
            return setting(map_data)


def display_menu(map_data):
    """
    Displays the menu for the user to choose from.
    The function will display a list of options and then prompt the user to enter their choice.

    :return: The chosen screen
    """

    print('------------------------------------')
    print()
    print('Menu:')
    print('1. Find your target item')
    print('2. Settings')
    print('3. Exit')
    print()
    print('------------------------------------')
    while True:
        choice = input('Press the corresponding number and enter to continue: ')

        if choice == '1':
            return find_path(map_data)

        elif choice == '2':
            return setting(map_data)

        elif choice == '3':
            print('Exiting program...')
            sys.exit(0)

        else:
            print('Invalid choice. Please try again.')


def main():
    """
    The main function is the entry point of the program.
    """

    display_welcome()
    map_data = initialize_data()
    display_menu(map_data)


if __name__ == '__main__':
    main()

"""
----------------------------------------------
NOT USED, save for future development
----------------------------------------------
"""


def get_algorithm():
    """
    The get_algorithm function prompts the user to select an algorithm from a list of options.
    The function returns the selected algorithm as a string.

    :return: An algorithm enum
    """
    print("Please select the algorithm you want to use:")
    print("1. Greedy")
    print("2. BFS")
    print("3. DFS")
    print("4. A*")
    algorithm = input()
    if algorithm == "1":
        return Algorithm.GREEDY
    elif algorithm == "2":
        return Algorithm.BFS
    elif algorithm == "3":
        return Algorithm.DFS
    elif algorithm == "4":
        return Algorithm.A_STAR
    else:
        print("Invalid input")
        return get_algorithm()
