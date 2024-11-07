File handling in Python is about managing files on your system to read or write data. Python provides built-in functions to open, read, write, and close files, making it efficient for data storage and retrieval.

### Opening a File

To start working with a file, it must be opened using the `open()` function, which returns a file object. You can specify the file path and the mode in which you want to open the file:

- `"r"`: Read mode (default) – Opens a file for reading; error if the file doesn’t exist.
- `"w"`: Write mode – Opens a file for writing; creates a new file if it doesn’t exist or truncates the existing file.
- `"a"`: Append mode – Opens a file for appending; creates a new file if it doesn’t exist.
- `"r+"`: Read and write mode – Opens a file for both reading and writing.

Example:
```python
file = open("example.txt", "r")  # Opens file in read mode
```

### Reading from a File

Python provides multiple methods for reading files, depending on how you want to access the data:

1. **`read()`**: Reads the entire file.
2. **`readline()`**: Reads a single line from the file.
3. **`readlines()`**: Reads all lines as a list of strings.

#### Example of reading a file:
```python
# Reading the entire file content
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Reading line by line
file = open("example.txt", "r")
for line in file:
    print(line.strip())  # Remove newline character
file.close()
```

### Writing to a File

When writing to a file, you can use:
- **`write()`**: Writes a string to the file.
- **`writelines()`**: Writes a list of strings to the file.

#### Example of writing to a file:
```python
# Writing a single line to a file
file = open("example.txt", "w")
file.write("Hello, world!\n")
file.close()

# Writing multiple lines
lines = ["This is line 1.\n", "This is line 2.\n"]
file = open("example.txt", "w")
file.writelines(lines)
file.close()
```

### Appending to a File

Using append mode (`"a"`) allows you to add content without overwriting existing data.

#### Example of appending to a file:
```python
file = open("example.txt", "a")
file.write("This is a new line added to the file.\n")
file.close()
```

### Using `with` Statement for File Handling

The `with` statement is the preferred way to handle files as it ensures the file is properly closed after its suite finishes, even if an exception is raised.

```python
# Reading with 'with' statement
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Writing with 'with' statement
with open("example.txt", "w") as file:
    file.write("Using 'with' to handle files in Python.\n")
```

### Example: Reading and Writing Data to a File

Here’s a practical example where we read a list of names from a file, process them, and write them to another file:

```python
# Read names from 'input.txt' and write each name in uppercase to 'output.txt'
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.strip().upper() + "\n")
```

In this example:
1. The `input.txt` file is read line-by-line.
2. Each line is converted to uppercase and written to `output.txt`.

File handling is powerful and flexible, letting you easily manage persistent data in Python scripts.
