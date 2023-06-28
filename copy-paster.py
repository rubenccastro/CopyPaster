import os

filepath = os.getcwd()
file_name = ''
path_file_from = ''
path_file_to = ''

while file_name == '':
    print("File name:")
    file_name = input()
while path_file_from == '':
    print("Path to copy from:")
    path_file_from = input()
while path_file_to == '':
    print("Path to copy to:")
    path_file_to = input()    

def GenerateFile(file_name):
    temp_path = os.path.join(filepath, file_name + '.bat')
    with open(temp_path, 'w') as f:
        f.write('''\
Xcopy {0} {1} /E /H /C /I /Y
'''.format(path_file_from, path_file_to))

GenerateFile(file_name)

print('.bat file generated.')
