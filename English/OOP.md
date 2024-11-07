Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to model real-world entities. Objects combine data and behavior, making code modular, reusable, and easier to understand and maintain. OOP is organized around four main concepts: **Encapsulation**, **Abstraction**, **Inheritance**, and **Polymorphism**.

### 1. Encapsulation

Encapsulation is the practice of bundling data (attributes) and methods (functions) that operate on the data into a single unit, or **class**. This hides the internal state of the object from the outside world and only allows controlled access.

**Example:**

```python
class Car:
    def __init__(self, color, model):
        self.color = color      # public attribute
        self.__engine_on = False  # private attribute

    def start_engine(self):
        self.__engine_on = True
        print("Engine started.")

    def stop_engine(self):
        self.__engine_on = False
        print("Engine stopped.")
```

Here, `Car` encapsulates attributes and methods. The attribute `__engine_on` is private, meaning it can’t be accessed directly outside the class, which helps control how `engine_on` is modified.

### 2. Abstraction

Abstraction means hiding complex implementation details and showing only the necessary parts to the user. In OOP, classes and methods provide an abstraction layer.

**Example:**

```python
class Car:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print(f"The {self.model} is driving.")
```

The `Car` class provides a simple interface (`drive` method) without needing to explain how the driving works internally. The user of the class only needs to know they can call `drive()` to make the car "drive."

### 3. Inheritance

Inheritance allows a class to inherit attributes and methods from another class, enabling code reuse and creating a hierarchy.

**Example:**

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle starting.")

class Car(Vehicle):  # Car inherits from Vehicle
    def __init__(self, brand, model):
        super().__init__(brand)  # Call the constructor of Vehicle
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving.")
```

In this example, `Car` inherits from `Vehicle`, so it gains the `start` method and `brand` attribute. `Car` also has its own `drive` method.

### 4. Polymorphism

Polymorphism allows objects to be treated as instances of their parent class, even if they behave differently. It enables functions or methods to operate on objects of different types.

**Example:**

```python
class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting.")

class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle is starting.")

def start_vehicle(vehicle: Vehicle):
    vehicle.start()

car = Car()
motorcycle = Motorcycle()

start_vehicle(car)         # Output: "Car is starting."
start_vehicle(motorcycle)   # Output: "Motorcycle is starting."
```

Here, the `start_vehicle` function can take any `Vehicle` type, whether it’s a `Car` or `Motorcycle`, and will call the appropriate `start` method based on the object passed.

---

Together, these concepts make OOP a powerful tool for building modular, reusable, and maintainable software systems.
