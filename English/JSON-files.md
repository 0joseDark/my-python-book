JSON (JavaScript Object Notation) is a widely used format for storing and exchanging data. It's particularly popular in web applications due to its lightweight and easy-to-read structure. In Python, handling JSON files is straightforward thanks to the built-in `json` library.

Here’s an explanation and examples to help you work with JSON files in Python.

### 1. Loading JSON Data

To load JSON data from a file, use the `json.load()` method. This method reads the JSON file and parses it into a Python dictionary.

#### Example: Loading JSON from a File

Suppose we have a file `data.json`:

```json
{
  "name": "Alice",
  "age": 30,
  "city": "Lisbon",
  "languages": ["English", "Portuguese", "Spanish"]
}
```

Here’s how to read this file in Python:

```python
import json

# Open and load JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

print(data)
# Output: {'name': 'Alice', 'age': 30, 'city': 'Lisbon', 'languages': ['English', 'Portuguese', 'Spanish']}
```

### 2. Accessing JSON Data

After loading JSON data, you can access the values just like with a Python dictionary.

#### Example: Accessing JSON Data

```python
print(data['name'])        # Output: Alice
print(data['languages'])   # Output: ['English', 'Portuguese', 'Spanish']
```

### 3. Writing JSON Data

To write data to a JSON file, use the `json.dump()` method, which serializes a Python dictionary and writes it to a file.

#### Example: Writing JSON to a File

```python
data_to_save = {
    "name": "Bob",
    "age": 25,
    "city": "Porto",
    "languages": ["English", "Portuguese"]
}

# Write data to JSON file
with open('output.json', 'w') as file:
    json.dump(data_to_save, file, indent=4)
```

The `indent` parameter is optional but helps format the JSON for readability.

#### Resulting `output.json` File

```json
{
    "name": "Bob",
    "age": 25,
    "city": "Porto",
    "languages": [
        "English",
        "Portuguese"
    ]
}
```

### 4. Converting JSON Strings

If the JSON data comes as a string (e.g., from an API), you can use `json.loads()` to convert it to a Python dictionary.

#### Example: Loading JSON from a String

```python
json_string = '{"name": "Charlie", "age": 28, "city": "Coimbra"}'
data = json.loads(json_string)

print(data)
# Output: {'name': 'Charlie', 'age': 28, 'city': 'Coimbra'}
```

### 5. Converting a Python Dictionary to JSON String

To convert a Python dictionary back to a JSON-formatted string, use `json.dumps()`.

#### Example: Converting Dictionary to JSON String

```python
data_dict = {
    "name": "Diana",
    "age": 22,
    "city": "Faro"
}

json_string = json.dumps(data_dict, indent=4)
print(json_string)
```

### 6. Practical Example: Merging JSON Data

Imagine you have two JSON files and want to combine them.

File `file1.json`:
```json
{
  "name": "Alice",
  "age": 30
}
```

File `file2.json`:
```json
{
  "city": "Lisbon",
  "languages": ["English", "Portuguese"]
}
```

#### Code to Merge JSON Files

```python
with open('file1.json', 'r') as file1, open('file2.json', 'r') as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)

# Merging the dictionaries
merged_data = {**data1, **data2}

with open('merged_output.json', 'w') as outfile:
    json.dump(merged_data, outfile, indent=4)
```

#### Resulting `merged_output.json`:

```json
{
    "name": "Alice",
    "age": 30,
    "city": "Lisbon",
    "languages": [
        "English",
        "Portuguese"
    ]
}
```

### Summary of Key Functions

- **`json.load(file)`**: Load JSON data from a file.
- **`json.dump(data, file)`**: Write Python data to a JSON file.
- **`json.loads(string)`**: Parse JSON from a string.
- **`json.dumps(data)`**: Convert Python data to a JSON string.

These methods make handling JSON data in Python efficient, whether you’re reading from files, writing to them, or manipulating JSON structures.
