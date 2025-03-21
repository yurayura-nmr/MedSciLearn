# **Basic Python Commands You Should Know**  

Before diving deeper into Python, it’s important to understand some fundamental commands and syntax. These are essential for working with **bioinformatics tools, data visualization libraries, and general scripting**.  

---

## **1. Importing Libraries**  

Many Python tools come in the form of **libraries** (collections of pre-written functions). You can import them using `import`:  

```python
import pandas as pd  # Import pandas for data handling
import numpy as np   # Import numpy for numerical operations
import matplotlib.pyplot as plt  # Import matplotlib for plotting
```

This allows you to use the tools inside these libraries. For example, pd.read_csv("data.csv") reads a file using pandas.

## **2. Printing Output**  

The print() function displays text or values:

```python
print("Hello, world!")  # Prints text
print(5 + 3)  # Prints the result of a calculation (8)
```

This is useful for checking your code or debugging.

## **3. Strings**  

A string is a piece of text inside quotes:

```python
name = "Kyodai Taro"
print(name)  # Prints: Kyodai Taro
```

Strings are important for handling labels, file names, or textual data.

## **4. Comments**  

A # symbol creates a comment—text that Python ignores. 

Comments are like a memo that help explain your code:

```python
# This calculates BMI
bmi = weight / (height ** 2)
```

Use comments to make your code clearer for yourself and others.

## **5. Using the Dot (.) for Methods**  

A . (dot) lets you use functions that belong to an object. This is common when working with data analysis tools:

```python
data.head()  # Show the first 5 rows of a dataset
data.tail()  # Show the last 5 rows
```

Here, .head() and .tail() are methods that belong to the data object (a DataFrame).

Think of data.head() as saying:

"Take the object data and apply the head() function to it."

Other examples:

```python
text = "kyodai igakubu"
print(text.upper())  # Converts text to uppercase: "KYODAI IGAKUBU"
```

## **6. Assigning Values with = **  

The = sign assigns values to variables:

```python
x = 10
y = x + 5
print(y)  # Prints: 15
```

Important: = does not mean equality (like in math). It stores a value in a variable.
So, you might wonder if there is also a normal equal sign in Python ...

## **7. Checking Equality with == **  

If you want to check if two things are equal, use == instead of =:

```python
print(5 == 5)  # True
print(5 == 3)  # False
```

This is useful in filtering data or decision-making.

These basic commands will help you understand Python’s structure. By learning how to import libraries, print output, use strings, write comments, apply methods, assign variables, and check equality, you’ll be well-prepared to work with bioinformatics tools and data analysis libraries.
