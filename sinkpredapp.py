from sklearn.tree import DecisionTreeClassifier

# Collecting input from the user
age = int(input("Enter age: "))
gender = input("Enter gender (male/female): ")
weight = float(input("Enter weight (in kg): "))
height = float(input("Enter height (in cm): "))

# Converting gender to numerical value (0 = male, 1 = female)
gender = 0 if gender == 'male' else 1

# Sample data: age, gender, weight, height, and safe (0 = not safe, 1 = safe)
data = [
    [25, 0, 70, 175, 1],
    [30, 1, 60, 160, 1],
    [45, 0, 85, 180, 0],
    [20, 1, 55, 150, 1],
    # ... more data
]

# Splitting data into features and labels
X = [entry[:-1] for entry in data]
y = [entry[-1] for entry in data]

# Creating a Decision Tree classifier
classifier = DecisionTreeClassifier()

# Training the classifier on the data
classifier.fit(X, y)

# Making prediction for the input data
input_data = [age, gender, weight, height]
prediction = classifier.predict([input_data])

if prediction[0] == 1:
    print("The person is predicted to be safe from sinking.")
else:
    print("The person is predicted not to be safe from sinking.")
