#! /usr/bin/python3.6

def add_to_list(items, your_choice, choice_count=1):
    find_result = find_in_list(items, your_choice)
    if find_result[0]:
        items[find_result[1]][1] += choice_count

    else:
        items.append([your_choice, choice_count])


def remove_from_list(items, your_victim):
    find_result = find_in_list(items, your_victim)
    if find_result[0]:
        victim_item = items[find_result[1]]
        items.remove(victim_item)
        return True
    return False


def find_in_list(items, your_choice):
    for item in items:
        if item[0] == your_choice:
            return [True, items.index(item)]
    return [False, -1]


def shopping_list_help():
    print("""
    Enter (help) for giving help to you(usage:help)
    Enter (add) for adding item to list remind that you can't add items contain any numbers to the list(usage: add item_name count(default=1)) 
    Enter (find) for check your item's count and availability(usage: find item_name)
    Enter (remove) for removing your victim from the list(usage: remove item_name)
    Enter (done) for finalizing your shopping list (usage:done)
    Enter (show) for print your shopping list (usage:show)    
    """)


def show_shopping_list(items):
    if not len(items):
        print("Your shopping list is empty.")
    for item in items:
        print("{item}:{count}".format(item=item[0], count=item[1]))



def shopping_list():
    items = []
    shopping_list_help()

    while True:
        input_error = False
        your_choice = input(">").lower().split()

        if not len(your_choice):
            continue
        if not your_choice[0].isalpha():
            print("Wrong input, please read our help again.")
            continue

        if your_choice[0] == "add":
            count = 1
            if len(your_choice) == 3:
                if not your_choice[1].isalpha() or not your_choice[2].isnumeric():
                    input_error = True
                else:
                    count = int(your_choice[2])
            elif len(your_choice) == 2:
                if not your_choice[1].isalpha():
                    input_error = True
            elif len(your_choice) > 3 or len(your_choice) == 1:
                input_error = True

            if not input_error:
                add_to_list(items, your_choice=your_choice[1], choice_count=count)
                print("Your item added to the list successfully.")
                continue

        elif your_choice[0] == "find":
            if len(your_choice) == 2:
                if not your_choice[1].isalpha():
                    input_error = True
            elif len(your_choice) > 2 or len(your_choice) == 1:
                input_error = True
            if not input_error:
                result = find_in_list(items, your_choice=your_choice[1])
                if result[0]:
                    item = items[result[1]]
                    print("You have {count} {item}(s) in your list.".format(count=item[1], item=item[0]))
                else:
                    print("You don't have any {item} in your list.".format(item=your_choice[1]))
                continue

        elif your_choice[0] == "remove":
            if len(your_choice) == 2:
                if not your_choice[1].isalpha():
                    input_error = True
            elif len(your_choice) > 2 or len(your_choice) == 1:
                input_error = True

            if not input_error:
                result = remove_from_list(items, your_victim=your_choice[1])
                if result:
                    print("You victim({item}) removed successfully.".format(item=your_choice[1]))
                else:
                    print("You don't have any {item} in your list.".format(item=your_choice[1]))
                continue

        elif your_choice[0] == "done":
            if not len(your_choice) == 1:
                input_error = True
            else:
                break

        elif your_choice[0] == "help":
            if not len(your_choice) == 1:
                input_error = True
            else:
                shopping_list_help()

        elif your_choice[0] == "show":
            if not len(your_choice) == 1:
                input_error = True
            else:
                show_shopping_list(items)

        if input_error:
            print("Wrong input, please read our help again.")

    if len(items):
        print("Hoora, your list are ready")
        show_shopping_list(items)

def main():
    answer = input("Are you ready to prepare your shopping list?(press y to continue)\n>")

    if answer.lower() != "y":
        print("Come back as soon as possible.")
        exit(0)

    print("Let's Go.")

    shopping_list()

if __name__ == "__main__":
    main()
