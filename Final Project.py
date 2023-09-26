
# This program will determine the BMI (Body Mass Index) of six individuals.
# The six individuals are as follows: Dan, Kelly, Trevin, Steve, Mike, and Joe.

# This defines a function that will calculate bmi for every individual
def calculate_bmi(weight, height):
    bmi = (weight * 703) / (height ** 2)
    return bmi

# This defines the three categories of weight in regards to BMI
def bmi_category(bmi):
    if bmi < 18.5:      # 18.5 or less BMI is defined as being underweight
        return 'underweight'
    elif 24.9 > bmi > 18.5:    # 18.6-24.9 BMI is defined as being a healthy weight
        return 'healthy weight'
    elif bmi > 25:      # Over 25 BMI is defined as being overweight
        return 'overweight'


# These are the subjects names as listed in an array
names = ['Dan', 'Kelly', 'Trevin', 'Steve', 'Mike', 'Joe']
bmi = [] # BMI value set for the for statement

# For statement to gather each users weight and height
for name in names:
    weight = eval(input(name + ', what is your current weight in pounds?  ')) # Variable to determine weight
    height = eval(input(name + ', What is your current height in inches?  ')) # Variable to determine height

# Appending BMI variables with the defining statement of height and weight
    bmi.append(calculate_bmi(weight, height))

    bmi.append(calculate_bmi(weight, height))


ucounter = 0    # Underweight counter for the for statement
hcounter = 0    # Healthy counter for the for statement
ocounter = 0    # Overweight counter for the for statement

# For statement taking the array values for each user and categorizing them into either underweight, healthy
# or overweight
for bmi_value in bmi:
    category = bmi_category(bmi_value)
    if category == 'underweight':
        ucounter += 1
    elif category == 'healthy weight':
        hcounter += 1
    else:
        ocounter += 1

# displaying the final result of how many individuals are in each category of BMI weight class
print(ucounter / 2, 'subjects are underweight')
print(hcounter / 2, 'subjects are a healthy weight')
print(ocounter / 2, 'subjects are overweight')