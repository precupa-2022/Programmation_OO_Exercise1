"""
Programme fait par Alexander Precup
Groupe: 402
Description: Objets orientées
Exercise 1 - Écrire une classe StringFoo avec un attribut message et deux méthodes set_string et print_string
"""

class StringFoo:
    message = ""

    def set_string(self,message):
        self.message = input("Entrez un mot ou une phrase : ")

    def print_string(self,message):
        self.message = message
        print(message.upper())

s = StringFoo()
s.set_string(s.message)
s.print_string(s.message)