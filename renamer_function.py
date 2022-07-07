def renamer_bot(file_name):
    file_name = file_name.lower().replace('.', '_').replace('(', '_').replace(')', '_').replace(' ', '_')
    file_name = file_name.replace('_xlxs', '.xlxs')
    return file_name

# name = 'Example.bad (file).xlxs'
# print(renamer_bot(name))

fname = input("What's the file name you want to rewrite? ")

print(renamer_bot(fname))
