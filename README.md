# Mini Notepad Application
This is a mini notepad application developed using Python's Tkinter library. This application provides basic functionalities of a notepad like creating new file, opening a file, saving the current file, selecting text, undo and redo, copying and pasting text, changing font style and color, and highlighting text.

# Requirements
Python 3.x
Tkinter module
math module
How to Run
To run the application, save the code in a file with extension .py and run it using Python interpreter.

# Functionality
Create a new file: This creates a new file and clears the current text area. If there are any unsaved changes in the current file, it prompts the user to save them.

Open an existing file: This opens a file dialog box and allows the user to select a file to open. If there are any unsaved changes in the current file, it prompts the user to save them.

Save the current file: This saves the current file. If there is no file name assigned to the current file, it prompts the user to save the file with a name.

Save the current file as a new file: This saves the current file with a new name.

Undo and Redo: This undoes or redoes the last action performed in the text area.

Copy, Cut, and Paste: These functions allow the user to copy, cut, and paste text respectively.

Select All: This selects all the text in the text area.

Change font style and size: This allows the user to change the font style and size.

Change font color: This allows the user to change the font color.

Highlight text: This allows the user to highlight the selected text.

About Notepad: This provides information about the Notepad application.
# The Notepad class is defined which has methods for handling various operations such as creating a new file, opening an existing file, saving a file, copying, cutting and pasting text, changing the font and font size, changing font color and highlighting text.
The class also creates the graphical user interface (GUI) for the notepad, including a text widget, a menu bar with dropdown menus, and key bindings for certain actions.
The main code creates a new instance of the Notepad class and runs the main event loop to display the GUI and handle user input.
