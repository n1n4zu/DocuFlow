from DocuFlow.docuflow import comment

@comment('''
Test class of dog''')
class Dog:

    @comment("constructor of dog class")
    def __init__(self):
        pass

    @comment("Dog's noise")
    def noise(self):
        print("Woof woof")