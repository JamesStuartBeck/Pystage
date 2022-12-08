# Pystage

### What is this Project
This is a sample project to demonstrate game programming basics using [Pystage](https://github.com/pystage/pystage), a Python API for [Scratch](https://scratch.mit.edu/).

### Set Up

This guide is meant to walk you through setting up this project, on the assumption that you start with nothing.
If one of these steps does not apply to you, simply skip it.

#### Installing Python

Navigate to the [Python website](https://www.python.org/downloads/release/python-3109/) and install the proper version for your operating system.
This is an older version of Python, but we have found that the most recent version of Python is incompatible with Pystage.
Once installation is complete, test that you have properly installed Python by opening one of the following:
- A `Command Prompt` window for Windows users
- A `Terminal` window for Mac users

And running the command `python -V`.
It should print out your version of Python.

#### Installing Pycharm

In order to be able to work on this code, you need an IDE, and I am recommending [Pycharm](https://www.jetbrains.com/pycharm/) for that.
On the Pycharm website, click on the `Download` button in the middle of the screen.
On the new page it takes you to, click on the `Download` button for the free Community version, on the right-hand side of the screen.

Once it is installed, open up Pycharm.

#### Cloning in this GitHub Repository

Now that you have an IDE installed, you have to clone in the code for this project to be able to modify and run it.

Select `Import Project from VCS` and paste in this link: https://github.com/JamesStuartBeck/Pystage.git.

If you see the words `Git not installed` appear in red, then you need to install Git.
Pycharm should give you the option to install it, and if you click the button, it will do it for you.

This should copy in all the files for this project.

#### Adding an Interpreter

Click on `File > Settings` to open up the `Settings` window.
Within the search bar, type in `Python Interpreter` and press enter; this will take you to the `Python Interpreter` page.
Click on `Add Interpreter > Add Local Interpreter` and in the new window that appears, click `Okay`.
This will take you back to the `Python Interpreter` page. Click `Apply` at the bottom.

#### Installing Pystage

Open up a new `Termianl` window closing your current one and clicking the button on the bottom, and run the following command: `pip install pystage`.

### Running the Game

To run the game, run the command `python gamy.py`.
