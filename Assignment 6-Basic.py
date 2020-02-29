# Assignment 6 - Basic Question


# Import librairies

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


def load_file(path):
    """Accepts a file path (str), loads file in the path to a Dataframe object and return the object."""
    return pd.read_csv(path)


# Main()

path = '/home/user/PycharmProjects/visualization-homework/insurance.csv'

insurance_data = load_file(path)

insurance_data.info()
print(insurance_data.to_string())


# Question 1: plot the chart for charges and save it as charges_plot.png

plt.plot(insurance_data['charges'])
plt.title('Insurance Charges per Insured Person')
plt.xlabel('Insured Persons')
plt.ylabel('Insurance Charges')

os.makedirs('plots/', exist_ok=True)
plt.savefig('plots/charges_plot.png', dpi=300)
plt.show()
plt.close()

# Question 2: plot the histogram for bmi and save it as bmi_hist.png

fig, axes = plt.subplots(1,1, figsize=(8,8))
axes.hist(insurance_data['bmi'], bins=37, density=1, color='grey')

axes.set_title('BMI Distribution for Insured Persons')
axes.set_xlabel('BMI Index')
axes.set_ylabel('Distribution')

os.makedirs('plots/', exist_ok=True)
fig.savefig('plots/bmi_hist.png', dpi=300)
plt.show()
plt.close()


# Question 3: plot the scatterplot for age vs charges and save it as age_charge_scatter.png

plt.scatter(insurance_data['age'], insurance_data['charges'])
plt.title('Insurance Charges by Age of Insured Persons')
plt.xlabel('Age')
plt.ylabel('Charges')

os.makedirs('plots/', exist_ok=True)
plt.savefig('plots/age_charge_scatter.png', dpi=300)
plt.show()
plt.close()

# Question 5: Re-do the previous items, adding the title, x label and y label for each item.
# Answer: questions 2,3,4 contain titles and x-y axis labels.

# Question 6: Think about the exercise 12 from the previous section. Do the plots match what we saw with the correlation
# function?

print(insurance_data.corr())

# Answer: we can see from the scatter plot that charges tend to rise with age and bmi, with coefficients of 0.29
# and 0.19 respectively indicating moderate positive linear relationship.


