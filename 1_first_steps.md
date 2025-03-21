# **Beginner Python Tutorial for Medical Students (Cardiology example)**  

This tutorial is designed for **medical students with no prior programming experience**. You’ll learn how to:  

✅ Load patient data into Python  
✅ Perform simple calculations on health metrics  
✅ Visualize data with a histogram  

---

## **1. Setting Up Python**  

First, make sure you have Python installed. The easiest way is to use [Anaconda](https://www.anaconda.com/products/distribution) (see [installation guide](anaconda_basics.md)).  

To check if Python is installed, open a terminal and type:  

```bash
python --version
```

If you see something like `Python 3.x.x`, you’re good to go!  

---

## **2. Creating a Virtual Dataset**  

We will create a small dataset of **5 virtual patients** with:  
- **Blood pressure (systolic/diastolic)**  
- **Diabetes status**  
- **Weight (kg) & height (m)**  

**Open a Python script** (in a text editor such as Visual Studio Code and save it as cardiology.py) and copy this code:

```python
import pandas as pd

# Creating a simple dataset
data = {
    "Patient": ["A", "B", "C", "D", "E"],
    "Systolic_BP": [120, 140, 130, 150, 110],  # mmHg
    "Diastolic_BP": [80, 90, 85, 95, 75],      # mmHg
    "Diabetes": [0, 1, 0, 1, 0],               # 0 = No, 1 = Yes
    "Weight": [70, 85, 65, 90, 75],            # kg
    "Height": [1.75, 1.80, 1.65, 1.85, 1.70]   # meters
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate BMI
df["BMI"] = df["Weight"] / (df["Height"] ** 2)

# Show the dataset
print(df)
```

## **Understanding Functions and Arguments in Python**  

If you’ve studied mathematics, you’ve seen functions like this before:

`f(x) = x^2`

This function takes an input \( x \) and returns \( x^2 \). For example, if you input \( f(3) \), you get \( 9 \).

In Python, functions work in the same way. They take inputs (called **arguments**) and return outputs. For example, consider the following line:

```python
df = pd.read_csv(filename)
```

Just like how `f(3) = 9`, calling pd.read_csv("patients.csv") will give us a table of patient data that we can use in Python.
This idea applies to many functions in Python. For example, in our script:

```python
df["BMI"] = df["Weight"] / (df["Height"] ** 2)
```

By understanding functions and arguments, you’ll be able to read and write Python code more easily!

## **Understanding Assignment (=)**  

In Python, `=` is the assignment operator. It does not mean equality (like in math, where x = 3 means "x is equal to 3"). Instead, it means:

"Take the value on the right and store it in the variable on the left."

For example:

```python
x = 5
```

This means: "Store the number 5 in the variable x." Now, whenever we use x, Python knows it refers to 5.
Similarly, in our case:

```python
df = pd.read_csv(filename)
```

* pd.read_csv(filename) reads the file and returns a table of data.
* = assigns this table to the variable df, so we can use it later in the program.


**Run the script**:  
```bash
python cardiology.py
```

---

## **3. Basic Analysis**  

Let’s find out:  
1. The **average BMI** of our patients  
2. How many patients have **hypertension** (BP > 140/90)  

Add these lines **after the previous code**:  

```python
# Calculate average BMI
avg_bmi = df["BMI"].mean()
print(f"\nAverage BMI: {avg_bmi:.2f}")

# Count patients with high BP
hypertension_count = df[(df["Systolic_BP"] > 140) | (df["Diastolic_BP"] > 90)].shape[0]
print(f"Patients with hypertension: {hypertension_count}")
```

**Run the script again**:  
```bash
python cardiology.py
```

You should see output like this:  
```
  Patient  Systolic_BP  Diastolic_BP  Diabetes  Weight  Height    BMI
0       A         120           80        0      70    1.75  22.86
1       B         140           90        1      85    1.80  26.23
2       C         130           85        0      65    1.65  23.88
3       D         150           95        1      90    1.85  26.30
4       E         110           75        0      75    1.70  25.95

Average BMI: 25.44
Patients with hypertension: 2
```

---

## **4. Visualizing BMI Distribution**  

Now, let’s **plot a histogram** of the patients’ BMI using **Seaborn**.

**Install Seaborn** (only once):  
```bash
pip install seaborn
```

Add this code **after the previous code**:  

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Create a histogram of BMI
sns.histplot(df["BMI"], bins=5, kde=True)
plt.xlabel("BMI")
plt.ylabel("Number of Patients")
plt.title("BMI Distribution in Patients")
plt.show()
```

**Run the script again**:  
```bash
python cardiology.py
```

You should see a **BMI distribution plot**! 📊  

---

## **5. What’s Next?**  
🔹 Try adding more patients!  
🔹 Modify the hypertension threshold and observe changes.  
🔹 Explore **correlation** between diabetes and BMI.  

You now have a **basic** understanding of handling medical data in Python.
