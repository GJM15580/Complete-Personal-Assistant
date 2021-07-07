class PersonalAssistant:
  def __init__(self, todos, birthdays, contacts):
      self.contacts = contacts
      self.todos = todos
      self.birthdays = birthdays

  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "No contact with that name"

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      index = self.todos.index(todo_item)
      self.todos.pop(index)
    else:
      print("Todo is not in list!")

  def get_todo(self):
    return self.todos

  def get_birthdays(self):
    return self.birthdays

  def get_birthday(self, name):
    if name in self.birthdays:
      return f"{name}'s birthday is on {self.birthdays[name]}."
    else:
      return "Can't find a birthday for this person"

  def add_birthday(self, name, date):
    if name in self.birthdays:
      return f"There is already a birthday for {name}"
    else:
      self.birthdays[name] = date
      return f"{name}'s birthday has been added"
  
  def remove_birthday(self, name):
    if name in self.birthdays:
      self.birthdays.pop(name)
      return f"{name}'s birthday has been removed"
    else:
      return "There is no birthday listed for that person"

  def get_contacts(self):
    return self.contacts

  def get_contact(self, name):
    if name in self.contacts:
      return f"{name}'s job is {self.contacts[name]}."
    else:
      return "Can't find an entry for this person"

  def add_contact(self, name, job):
    if name in self.contacts:
      return f"There is already an entry for {name}"
    else:
      self.contacts[name] = job
      return f"{name} has been added"

  def remove_contact(self, name):
    if name in self.contacts:
      self.contacts.pop(name)
      return f"{name} has been removed"
    else:
      return "There is no entry listed for that person"
      
#assistant = PersonalAssistant()
#assistant.add_todo("Pick up groceries")

#print(assistant.get_contact("Chelsea"))
#print(assistant.get_todo())
#print(assistant.get_birthday("Melanie O'Connor"))