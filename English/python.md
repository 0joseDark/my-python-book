![douctor](https://github.com/0joseDark/0joseDark/blob/main/assets/douctor-inteiro-trabalhando.jpg)
1.1 What is Python?

Python is a high-level, interpreted programming language created by Guido van Rossum and released in 1991. It stands out for its simplicity and readability, making it an excellent choice for both beginners and experienced programmers. Python is widely used in many areas, such as web development, automation, data analysis, artificial intelligence, machine learning, and much more. Its simple and clean syntax allows developers to focus on solving problems without getting lost in complex language details.
Advantages of Python:

 Readable and maintainable code.
 Large community and extensive library of packages and modules.
 Multi-paradigm: supports object-oriented, functional and procedural programming.
 Portability: works on different operating systems, such as Windows, macOS and Linux.
 Excellent integration with other languages ​​and technologies.

1.2 Installation and Configuration

To start programming in Python, you need to install the Python interpreter on your system. Python is compatible with major operating systems such as Windows, macOS and Linux.
1.2.1 Installing Python on Windows, macOS and Linux

Windows:

 Go to the official Python website (python.org) and download the installer for Windows.
 You run the installer and check the "Add Python to PATH" option to ensure that Python will be accessible from the terminal.
 Complete the installation by following the on-screen instructions.

macOS:

 Python is already pre-installed on macOS, but it may be an old version. To install the latest version, you use Homebrew:

 bash

 brew install python

 Homebrew will install Python and pip (Python package manager).

Linux:

 On most Linux distributions, Python is already pre-installed. To ensure you have the latest version, use the following command:

 bash

sudo apt update
sudo apt install python3

To verify that Python was installed correctly, he runs:

bash

 python3 --version

1.2.2 Using pip to manage packages

pip is Python's package manager, allowing you to install, update, and uninstall third-party libraries and modules. These packages are essential for expanding Python's functionality.

Verify pip installation:

 After installing Python, pip is usually installed automatically. To check:

 bash

 pip --version

Installing a package:

 To install a package using pip, use the command:

 bash

pip install package-name

For example, to install the request library, which facilitates HTTP communication:

bash

 pip install requests

Updating a package:

bash

pip install --upgrade package-name

Uninstalling a package:

bash

pip uninstall package-name

1.3 Running the First Program in Python

After installing Python, it's time to run your first program. A classic program to start with is “Hello, World!”.
Steps to create the program:

 Create a Python file:
 Open a text editor (such as Notepad on Windows, TextEdit on macOS, or Nano editor on Linux).
 Write the following code:

 python

 print("Hello, World!")

Save the file:

 Saves the file with the .py extension, for example, ola_mundo.py.

Running the program:

 Opens the terminal or command prompt.
 Navigate to the directory where you saved the file.
 Execute the following command:

 bash

python file_name.py

In the case of the example, the command would be:

bash

 python hello_world.py

If everything goes well, the output will be:

css

Hello World!

With this, you will already have Python installed on your system and will be able to write and run your first programs. Python is a very flexible and powerful language, and these first steps will pave the way for you to explore more features and libraries that the language offers.
