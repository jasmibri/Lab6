# Team members: Anahita Niavarani and Jasmine Duong Brisebois
import pandas as pd
import seaborn as sns

# Uploading the dataset
data= pd.read_csv("wdi_wide.csv")

# Using info() function
print(data.info()) # Using this funtion we get the non-null count for each column the we substracte it from the total number of values which ois 217

# Question 3: for Population: 217-217= 0 missing values and for Physicians: 217-207= 10 missing values
print(data.columns)
print(data.isnull())

# Using nunique() function

print(data.nunique())

# Using describe()

print(data.describe()) # this fucntion provides  some statistical values for each column with numerical data.


# Creating a new column wih rounded GNI data

data['GNI per capita'] = round(data['GNI'] / data['Population'],2) # Rounding to the nearest cent= 2


#Using value_count function

region_count= data['Region'].value_counts()
print(region_count)

income_count= data['High Income Economy'].value_counts()
print(income_count)

# using the crosstab() function

cross_tab = pd.crosstab(data['Region'], data['High Income Economy'])
print(cross_tab)

# Filtering data 
Filtered_women_data=  data[data['Life expectancy, female']> 80]

print(Filtered_women_data)



for i in Filtered_women_data['Country Name']:  
   print(i)
   
   
#part 4

#1) “Is there any association between GNI per capita and life expectancy?”
# Life expendancy of male

sns.relplot( data= data, x= "GNI", y= "Life expectancy, male" )

#2) “Does the association between GNI per capita and life expectancy vary by region?”
# data of the male

sns.relplot( data= data, x= "GNI", y= "Life expectancy, male", hue= "Region" )

#3) Linear plot with standard deviation

sns.relplot( data= data, x= "GNI", y= "Life expectancy, male", hue= "Region" , kind= "line" , )
