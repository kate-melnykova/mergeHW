import os
import sys


# Q: How to find files on user PC?
FOLDER_NAME = './storage/'
OUTPUT_FOLDER = './output/'
title = 'setMerged.def'

args = sys.argv[1:]
noweight = False
for entry in args:
    if entry.startswith('-input_folder='):
        FOLDER_NAME = entry.lstrip('-input_folder=')
    elif entry.startswith('-output_folder='):
        OUTPUT_FOLDER = entry.lstrip('-output_folder=')
    elif entry.startswith('-filename='):
        title = entry.lstrip('-filename=')
    elif entry == '-noweight':
        noweight = True

# create output folder if needed
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

full_address = os.path.join(OUTPUT_FOLDER, title)

filenames = []
# get all files whose extension is .def
for file in os.listdir(FOLDER_NAME):
    if file.endswith(".def"):
        filenames.append(file)
filenames = sorted(filenames)
print('====================================================================================')
print(f'Found files {filenames}')


def concat_and_enumerate(filenames, folder=FOLDER_NAME):
    """
    concatenate all files and include enumeration of problems
    Returns file with name 'output.def'
    :param filenames: list of all files to concatenate
    :param folder: the folder where all files are located
    """
    problem_id = 1
    output = open(full_address, 'w+')
    # write a header
    with open(os.path.join(folder, filenames[0])) as hw:
        for line in hw:
            output.write(line)
            if line.startswith('problemListV2'):
                break

    for file in filenames:
        with open(os.path.join(folder, file)) as hw:
            header = True
            for line in hw:
                if not header:
                    if line.startswith('problem_id = '):
                        line = 'problem_id = ' + str(problem_id) + '\n'
                        problem_id += 1
                    if line.startswith('max_attempts = '):
                        line = 'max_attempts = ' + str(1000) + '\n'
                    if noweight and line.startswith('value ='):
                        line = 'value = 0\n'
                    output.write(line)

                if line.startswith('problemListV2'):
                    header = False

    output.close()

concat_and_enumerate(filenames)
print('========================================================================')
print('Merging is completed.')

