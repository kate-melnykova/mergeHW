import os

# Q: How to find files on user PC?
FOLDER_NAME = '/storage/'

filenames = []
# get all files whose extension is .def
for file in os.listdir(FOLDER_NAME):
    if file.endswith(".def"):
        filenames.append(file)

print(f'Found files {filenames}')

# concatenate all files
output = open('/output/output.def', 'w')
for file in filenames:
    with open(os.path.join(FOLDER_NAME, file)) as hw:
        output.write(hw.read())

output.close()

