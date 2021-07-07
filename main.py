import json

#imports PersonalAssistant.py file
from PersonalAssistant import PersonalAssistant

#ADD CODE: open JSON file and pass data to PersonalAssistant class
with open("todo.json", "r") as todos, open("birthdays.json", "r") as birthdays, open("contacts.json", "r") as contacts:
  todo_list = json.load(todos)
  birthday_list = json.load(birthdays)
  contact_list = json.load(contacts)
  assistant = PersonalAssistant(todo_list, birthday_list, contact_list)

done = False

while not done:
  user_command = input("""
  How can I help you?

    **** To-Do *****
    1: Add a to-do
    2: Remove a to-do 
    3: Get to-do list
    **** Birthdays *****
    4: Get Birthday
    5: Add Birthday
    6: Remove Birthday
    **** Contacts *****
    7: Get A Contact
    8: Add Contact
    9: Remove Contact

    Select a number or type 'Exit' to quit:
    
    """)
  #Add Todo
  if user_command == "1":
    user_input = input("Item to add to to-do list: ")
    assistant.add_todo(user_input)
  #Remove Todo
  elif user_command == "2":
    user_input = input("Item to remove from to-do list: ")
    assistant.remove_todo(user_input)
  #Get Todo
  elif user_command == "3":
    print("Your to-do list")
    print(assistant.get_todo())
  #Get Birthdays
  elif user_command == "4":
    print("Birthday Contacts: \n")
    for name in assistant.get_birthdays():
      print(name)
    user_input = input("\nEnter a name: ")
    print(f"\n{assistant.get_birthday(user_input)}")
  #Add Birthdays
  elif user_command == "5":
    print("Add a birthday: \n")
    name = input("Name of the person: ")
    birthday = input("Their birthday (ex: 08/18/2000): ")
    print(f"\n{assistant.add_birthday(name, birthday)}")
  #Remove Birthdays
  elif user_command == "6":
    print("Birthday Contacts: \n")
    for name in assistant.get_birthdays():
      print(name)
    user_input = input("\nWhich birthday would you like removed? ")
    print(f"\n{assistant.remove_birthday(user_input)}")
  #Get Contacts
  elif user_command == "7":
    print("Contacts: \n")
    for name in assistant.get_contacts():
      print(name)
    user_input = input("\nEnter a name: ")
    print(f"\n{assistant.get_contact(user_input)}")
  #Add Contact
  elif user_command == "8":
    print("Add a contact: \n")
    name = input("Name of the person: ")
    occupation = input("Their occupation: ")
    print(f"\n{assistant.add_contact(name, occupation)}")
  #Remove Contact
  elif user_command == "9":
    print("Contacts: \n")
    for name in assistant.get_contacts():
      print(name)
    user_input = input("\nWhich contact would you like removed? ")
    print(f"\n{assistant.remove_contact(user_input)}")
  #Exit
  elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":
    done = True
    print("\nThank you for using the program")
  else:
    print("\nNot a valid command.")

#ADD CODE: write data to JSON file
with open("todo.json", "w") as write_todos, open("birthdays.json", "w") as write_birthdays, open("contacts.json", "w") as write_contacts:
  json.dump(assistant.get_todo(), write_todos)
  json.dump(assistant.get_birthdays(), write_birthdays)
  json.dump(assistant.get_contacts(), write_contacts)