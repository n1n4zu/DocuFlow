from DocuFlow.docuflow import comment, args, returns

@comment('''
Test class of dog''')
class Dog:

    @comment("constructor of dog class")
    def __init__(self):
        pass

    @comment("Dog's noise")
    @args("name - name of dog")
    @args("noise - noise of dog")
    @returns("string of name and noise")
    def noise(self, name: str, noise: str):
        return f"{name}: {noise}"
