def input_error(func):
    '''Декоратор, обробляє винятки, що виникають у функціях (KeyError, ValueError, IndexError)'''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter the argument for the command"
        except ValueError:
            return "Enter the argument for the command: [command] [name] [phone_numder]"
        except IndexError:
            return "Enter the argument for the command: [command] [name]"
        
    return inner


def parse_input(user_input):
    ''' Функція отримання команди і значення з командної строки'''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    '''Функція зберігає у пам'яті, (словнику), новий контакт'''
    name, phone = args
    if name in contacts:
        return f"Contact [{name}] is present. You can change it by command 'change'"
    else:
        contacts[name] = phone
        return f"Contact [{name}] [{phone}] added."


@input_error
def change_contact(args, contacts):
    '''Функція змінює у пам'яті, (словнику), новий контакт'''
    name, phone = args
    if contacts.get(name) == None:
        return f"No name in phone books. You can added name by command 'add'"
    else:
        y_n_input = None
        while y_n_input != "y" and "n":
            y_n_input = input(f"A you realy want change Phone number '{name}': '{contacts.get(name)}' on '{phone}'?  (Y/N)\n>>> ").lower()
            if y_n_input == "y":
                contacts[name] = phone
                return f"Contact [{name}] [{phone}] changed."
            elif y_n_input.lower() == "n":
                return f"Addition contact [{name}] [{phone}] canceled."

@input_error        
def show_phone(args, contacts):
    '''Виводить у консоль номер телефону для зазначеного контакту'''
    name = args[0]
    if contacts.get(name) == None:
        return "This name is not in the phone books"
    else:
        return f"Phone number '{name}'\t is: '{contacts.get(name)}'"

@input_error
def show_all(contacts):
    '''Виводить у консоль всі телефони зі словника'''
    all_text = "All numbers is:\n"
    for name, phone in contacts.items():
        all_text = all_text + f"Phone number '{name}'\t is: '{phone}\n"
    return all_text

  
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    commands = ["hello", "add", "change", "phone", "all", "close", "exit"]
    while True:
        user_input = input(f"Enter a command ({commands}): \n>>> ")
        command, *args = parse_input(user_input)

        if command in [commands [5], commands [6]]: #["close", "exit"]:
            print("Good bye!")
            break

        elif command == commands [0]: # "hello":
            print("How can I help you?")
        
        elif command == commands [1]: # "add":
            print(add_contact(args, contacts))
             
        elif command == commands [2]: # "change":
            print(change_contact(args, contacts))
        
        elif command == commands [3]: # "phone":
            print(show_phone(args, contacts))

        elif command == commands [4]: # "all":
            print(show_all(contacts))
                    
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
