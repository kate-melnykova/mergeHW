# Merging WeBWorK assignments

You may want to create an additional
set of problems for your students to provide them
additional practice as a preparation of midterm or
final exam. You may do it by concatenating existing
WeBWorK assignments and assigning them to your students.

To do it, follow these steps.

1. Go to WeBWorK, click on "File manager" tab. Download
all source files of interest (.def - files for the
assignments in question) to a single folder.

2. Run python script via the terminal
```
$ python merge_files.py -input_folder=./storage -output_folder=./output -noweight -filename=setAssignment.def
```
Replace ./storage by a link to the folder that contains
all downloaded assignments source files. Output folder (./output)
is the folder where the output will be created. If folder
does not exist, it will be created. Add the flag ```-noweight`` if you want all
problems to have zero points.

Finally, specify
the filename. Note that WeBWorK only accepts assignments
which start from set and whose extension is .def

3. Upload the new file to the WeBWorK via the "File manager"
tool.

4. Go to "Hmwk sets editor" and Import the file.  