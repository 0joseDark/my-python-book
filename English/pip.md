**Using `pip` to Manage Packages** and **Running Your First Python Program** are essential steps in getting started with Python. Here’s how to do both effectively.

---

### **Using `pip` to Manage Packages**

`pip` is Python's package manager. It allows you to install, update, and manage third-party libraries and tools, which you can use to extend Python's capabilities.

1. **Installing a Package**
   - To install a package, simply use the command:
     ```shell
     pip install <package_name>
     ```
   - **Example**: Install the popular `requests` library for handling HTTP requests.
     ```shell
     pip install requests
     ```

2. **Listing Installed Packages**
   - You can see all installed packages and their versions with:
     ```shell
     pip list
     ```
   - **Example**:
     ```
     Package    Version
     ---------- -------
     requests   2.26.0
     numpy      1.21.2
     ```

3. **Upgrading a Package**
   - To update a package to the latest version, use:
     ```shell
     pip install --upgrade <package_name>
     ```
   - **Example**: Upgrade `requests` to the latest version.
     ```shell
     pip install --upgrade requests
     ```

4. **Uninstalling a Package**
   - If you no longer need a package, you can uninstall it with:
     ```shell
     pip uninstall <package_name>
     ```
   - **Example**: Uninstall the `requests` package.
     ```shell
     pip uninstall requests
     ```

5. **Requirements File**:
   - If you have a list of packages needed for a project, you can create a `requirements.txt` file, which contains all the packages and their versions.
   - To install packages from this file, use:
     ```shell
     pip install -r requirements.txt
     ```
   - **Example** of `requirements.txt`:
     ```
     requests==2.26.0
     numpy>=1.21
     ```

---

### **Running Your First Python Program**

1. **Write a Simple Python Program**
   - Open your code editor (or a text editor) and create a new file named `hello.py`.
   - Type the following code:
     ```python
     print("Hello, World!")
     ```
   - This is a simple program that prints “Hello, World!” to the screen.

2. **Run the Program**
   - Save the file and open a terminal or command prompt.
   - Navigate to the directory where `hello.py` is saved. For example:
     ```shell
     cd path/to/your/file
     ```
   - Run the Python program by typing:
     ```shell
     python hello.py
     ```
   - **Output**:
     ```
     Hello, World!
     ```

3. **Running a Python Program with Input**
   - Modify `hello.py` to ask for user input:
     ```python
     name = input("What's your name? ")
     print(f"Hello, {name}!")
     ```
   - Run the program again:
     ```shell
     python hello.py
     ```
   - **Example Interaction**:
     ```
     What's your name? Alice
     Hello, Alice!
     ```

4. **Using an Installed Package in Your Program**
   - Let’s use the `requests` package we installed to make a simple HTTP request.
   - Update `hello.py`:
     ```python
     import requests

     response = requests.get("https://api.github.com")
     print(response.status_code)
     ```
   - Run the program:
     ```shell
     python hello.py
     ```
   - **Output**:
     ```
     200
     ```
     (This indicates that the request was successful.)

With these basics, you can now manage packages with `pip` and run simple programs in Python!
