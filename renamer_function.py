def renamer_bot(file_name):
    specialchars = """.,!@#$%^&*() -=+<>?'"/\|[]{}"""
    file_name = file_name.lower()
    for i in specialchars:
        file_name = file_name.replace(i, '_')
    file_name = file_name.replace('_xlsx', '.xlsx')
    return file_name

while True:
    name = input("What's the file name you want to rewrite? ")
    print(renamer_bot(name))
