'''
Common functions and definitions.

---
'''


version = 'v0.5.0'
'''Package version, using semantic versioning to indicate breaking changes, as in v<MAJOR>.<MINOR>.<PATCH>.'''


def welcome(submodule_str:str='') -> str:
    '''Returns the welcome message as a string.'''
    for_submodule_str = ''
    if submodule_str:
        for_submodule_str = ' for ' + submodule_str + ' inputs.'
    string = '\n-------------------------------------------------------------\n'
    string +='Welcome to InputMaker' + version + for_submodule_str + '\n'
    string += 'You should already have cif2cell installed on your system.\n'
    string += '-------------------------------------------------------------\n'
    string += 'This is free software, and you are welcome to\n'
    string += 'redistribute it under GNU General Public License.\n'
    string += 'If you find this code useful, a citation would be awesome :D\n'
    string += 'Pablo Gila-Herranz, InputMaker ' + version + ', 2024.\n'
    string += 'https://github.com/pablogila/InputMaker\n'
    string += '-------------------------------------------------------------\n'
    return string
