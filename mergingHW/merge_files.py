import os
from typing import List

# Q: How to find files on user PC?
FOLDER_NAME = './storage/'


def get_all_files(folder: str = FOLDER_NAME):
    filenames = []
    # get all files whose extension is .def
    for file in os.listdir(folder):
        if file.endswith(".def"):
            filenames.append(file)
    filenames = sorted(filenames)
    print(f'Found files {filenames}')
    return filenames


def concat_and_enumerate(filenames: List[str], folder=FOLDER_NAME):
    """
    concatenate all files and include enumeration of problems
    Returns file with name 'output.def'
    :param filenames: list of all files to concatenate
    :param folder: the folder where all files are located
    """
    problem_id = 1
    output = open('./output/output.def', 'w+')
    with open(os.path.join(folder, filenames[0])) as hw:
        output.write(hw.read())

    for file in filenames[1:]:
        with open(os.path.join(folder, file)) as hw:
            header = True
            for line in hw:
                if not header:
                    if line.startswith('problem_id = '):
                        line = 'problem_id = ' + str(problem_id) + '\n'
                        problem_id += 1
                    output.write(line)

                if line.startswith('problemListV2'):
                    header = False

    output.close()

