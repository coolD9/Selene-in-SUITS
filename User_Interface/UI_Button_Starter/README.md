## UI_Button_Starter
The following is copy and paste from Issue #4, so if you've already read that, don't waste your time. Alternatively, don't waste your time reading Issue #4 if this is what you read first.

For week 2, I would like to officially get everybody integrated with our development language of choice. We will be using **Python** as the main language as well as the **QML** and **PyQt5** frameworks for frontend and backend work/management. Subsequently, I would love for everybody to familiarize themselves with Python and the frameworks. I think in order to successfully develop a functioning and robust interface, it's crucial for everybody to start small and work our way up to the bigger picture. To achieve this level of learning while also practicing using GitHub for version control I want the end goal of this project to be a singular window with everybody's button that introduces themselves. More details on that at the end of this issue.

## Hello World Starter

First, I want each of you to create a simple `Hello world!` window on your own, meaning you do **NOT** push it to this GitHub. Of course, there is a huge learning curve with every new language/framework you're trying to learn, so please don't hesitate to get aid from someone or something else. Not to be too much of a pedagogical teacher, but I think it will be best if you don't outright cheat, making your whole program via ChatGPT would only get it done, and you likely will have learned very little. With that being said, I'll lay out some of the steps for a `Hello world!` window.

**Note:** I made these steps using WSL for VS Code as I believe everyone should be familiar with that, please let me know if not.

### 1.  If you do not have Python and `pip` installed, install it using the following
```
sudo apt update
sudo apt upgrade
```
```
sudo apt install python3
```
This installs `pip` for Python3, which is a package manager
```
sudo apt install python3-pip
```
### 2.  Install PyQt5
```
pip3 install PyQt5
```
At this point, it may give you a warning, saying some scripts were not installed on your path. After tinkering around with it, I could not resolve this issue, but the simple program still seems to work, so we'll just cross our fingers and hope this doesn't become a bigger issue.

### 3. Create your program file

### 4.  Create your `Hello World!` window
The following starter code introduces a basic PyQt5 window. To effectively familiarize yourself with what's going on, I recommend reading and understanding the code thoroughly before tweaking it. 
```py
import sys
from PyQt5.QtWidgets import QApplication, QWidget

def main():
    # Create an instance of QApplication
    app = QApplication(sys.argv)

    # Create a QWidget (the main window)
    window = QWidget()
    window.setWindowTitle('Hello PyQt5')
    window.resize(400, 300)  # Set the window size
    window.show()  # Show the window

    # Run the application's event loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```
Once you understand the code, feel free to attempt adding your `Hello World!` statement. I recommend trying this on your own first, but if you get stuck, you may need to utilize the following code:
```py
from PyQt5.QtWidgets import QLabel

# Create a QLabel to display "Hello, World!"
hello_label = QLabel("Hello, World!", window)
```

### 5. Explore possibilities
Before moving on, I highly encourage you to see all of the neat things you can do with a simple window like this one. Some guiding steps are below.
* Did you notice that the starting position of the window is random? I didn't at first until I was messing around with another feature. Try to solve this issue. 
* Using the `PyQt5.QtGui` library, import `QFont` and experiment with all of the different things you can do with font sizes/features, primarly look into resizing it so it's more readable.
* Mess around with the window attributes to see how scaling works.


 
## Button Project
With a solid foundational program, I would like to expand upon this as a team. We will be creating a sole application with button functionality for each individual team member. The goal is still to start small, but gradually scale up our efforts. We'll be making a window with a button for each team member. Each team member is responsible for their own button. The general idea is for the screen to be blank with buttons that will display the team member's name once clicked. 

This is to help familiarize us not only with the button functionality of the PyQt library, but to also help facilitate working as a group on this project. I have no idea what potential challenges we may face while collaborating on this project, but that's why we're doing it. The following steps outline how I personally imagine it will go.

### 1. I will create the initial document with outlines for the window and some classes/libraries already included
### 2. Each team member will create a branch and code their own version of the button. *Communication is key here!* We don't want to pick a spot on the window where somebody else's button will already be. (For instance, I'm choosing the top left slot)
### 3. We will practice good project management skills and submit a pull request with reviewers, preferably myself as the reviewer. 
### 4. Once the pull request is recieved, I will approve it and send a message in the slack so people can update their branches if need be.

Sorry to be all pedagogical again, but remember, this is a learning experience. I don't mean to belittle your development skills by making you do trivial stuff. I just want to get the ball rolling on level ground for everyone so we're ready when we come up on the cliff so to speak. This is a brand new experience for myself and several of you, so we'll take it as it comes.
