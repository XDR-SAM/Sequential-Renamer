# SequentialRenamer

SequentialRenamer is a lightweight and user-friendly GUI tool designed to help users organize and rename files in a folder. By sorting files based on their creation time, it renames them sequentially (e.g., `1`, `2`, `3`, etc.), making file organization simple and efficient.



## Features

- **Graphical User Interface (GUI)**:  
  Powered by `tkinter`, the GUI provides an intuitive and user-friendly experience for selecting folders and processing files.

- **Time-Based Sorting**:  
  Files are renamed in order of their creation date, from the oldest to the newest.

- **Sequential Renaming**:  
  Files are renamed in numerical order while retaining their original file extensions.

- **Error Handling**:  
  Any issues during the renaming process are displayed in detailed error messages.

- **Reusable Tool**:  
  Easily select new folders and process files multiple times without restarting the program.



## Installation

### Prerequisites
- **Python 3.7 or newer**  
  Ensure Python is installed on your system. Download it from [python.org](https://www.python.org/).

### Install Dependencies
SequentialRenamer uses standard libraries (`os`, `pathlib`, and `tkinter`), so no additional packages are required. These libraries come pre-installed with Python.


## Usage

1. Clone the repository:  
  
   git clone https://github.com/XDR-SAM/Sequential-Renamer.git

2. Run the program:  
  
   python sequential_renamer.py
 

3. A GUI window will open. Click the **"Select Folder and Rename"** button.

4. Browse and select the folder containing the files to rename.

5. The program will process the files and rename them sequentially. A success message will be displayed upon completion.


## Example

**Before Renaming**:  

randomfile123.jpg  
anotherfile456.png  
example789.txt  


**After Renaming**:  

1.jpg  
2.png  
3.txt  




## Author

**Name**: Sami  
**Date**: January 3, 2025  
**Email**: [tdxfarhan@gmail.com] 
**Description**:  
Sami is a passionate programmer and problem-solver, creating tools to simplify everyday tasks. SequentialRenamer is one such project designed to streamline file organization.  



## Contributing

Contributions are welcome! To contribute:  
1. Fork the repository.  
2. Create a new branch:  
  
   git checkout -b feature-name
  
3. Commit your changes:  
 
   git commit -m "Add feature-name"
  
4. Push to the branch:  
  
   git push origin feature-name
   
5. Open a pull request.



## License

MIT License

Copyright (c) 2025 Sami

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.




