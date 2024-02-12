def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Name not found"
        except IndexError:
            return "Not found"
        except Exception as e:
            return f"Error : {e}"

    return inner 

@input_error 
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args    

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact already exists."
    else:
        contacts[name] = phone
        return "Contact added."

@input_error
def show_phone(name, contacts):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found"

@input_error     
def show_all(args,contacts):
    s = ''
    for key in contacts:
        s+=(f"{key:10} : {contacts[key]}\n")
    return s

@input_error        
def change_contact(args, contacts):
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            return "Contact not found."
    else:
        return "Invalid format. Please use: change [name] [new phone]"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
            
        elif command == "phone":
            if args:
                result = show_phone(args[0], contacts)
                print(result)
            else:
                print("Please provide a contact name.")
            
        elif command == "add":
            print(add_contact(args, contacts))
                
        elif command == "all":
            print(show_all(args,contacts))
            
        elif command == "change":
            print(change_contact(args, contacts))
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
