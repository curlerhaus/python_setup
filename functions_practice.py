def hello():
    print(f"Greetings User!")


hello()


def pack(item1, item2, item3):
    items = [item1, item2, item3]
    print(items)


pack('bacon', 'pizza', 'beer')


def eat_lunch(my_lunch):
    if len(my_lunch) == 0:
        print('My lunch box is empty')
    else:
        for i in range(len(my_lunch)):
            if i == 0:
                print(f"First I will eat {my_lunch[0]}.")
            else:
                print(f"Next I will eat {my_lunch[i]}.")


eat_lunch(['sandwich', 'chips', 'granola bar', 'candy'])
