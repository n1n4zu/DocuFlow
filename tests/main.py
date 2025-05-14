from DocuFlow.docuflow import comment, args, returns

@comment('''
Test file
second line line
''')
@returns('test text')
@returns('second test text')
def main():
    return "Test file", "second line"
