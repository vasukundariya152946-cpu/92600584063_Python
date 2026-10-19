# Write a program to demonstrate method
# overriding and polymorphism.
class teacher:
    def event(self):
        print("Say all the student participant in event")
class boys(teacher):
    def event(self):
        print("Participant of all boys")
class girs(teacher):
    def event(self):
        print("Participant of all girls")
t=teacher()
b=boys()
g=girs()

t.event()
b.event()
g.event()
# output :-
# Say all the student participant in event
# Participant of all boys
# Participant of all girls