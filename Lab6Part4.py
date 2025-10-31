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
    
#1-2    
sns.relplot(data=data, x="GNI per capita", y="Life expectancy, female", hue="Region")

#3
sns.relplot(data=data, x="GNI per capita", y="Life expectancy, female", hue="Region", kind= "line", errorbar="sd")

#4
sns.lmplot(data=data, x="GNI per capita", y="Life expectancy, female", hue="Region")

#5
#Is there any association between Physicians and Life expectancy, female?
sns.relplot(data=data, x="Physicians", y="Life expectancy, female", size ="Population", col="Region")
#In every region as the number of physicians increases, so does the life expectency for women (linear)

#Is there any association between Tertiary education, female and Life expectancy, female?
sns.relplot(data=data, x="Tertiary education, female", y="Life expectancy, female", col="Region")
#In Asia, Africa and Oceania, as the tertiary education for female increases so does the life expectancy for women. However, in Europe and america, the life expectancy is constant

#Is there any association between Women in natinal parliement and Life expectancy, female?
sns.relplot(data=data, x="Women in national parliament", y="Life expectancy, female", col="Region")
#In every region, there is no association between women in natinal parliement and life expectancy for womn.

#Is there any association between Greenhouse gas emissions and Life expectancy, female?
sns.relplot(data=data, x="Greenhouse gas emissions", y="Life expectancy, female", col="Region")
#In every region, the greenhouse gas emisions are constant despite the fluctuation of women's life expectancy.

#Is there any association between Internet use and Life expectancy, female?
sns.relplot(data=data, x="Internet use", y="Life expectancy, female", col="Region")
#In every region, the association between internet use and fife expectancy for women is linear.

#6
#a)Is there any association between Internet use and emissions per capita?
data['emissions per capita'] =(data['Greenhouse gas emissions'] / data['Population'])

sns.relplot(data=data, x="Internet use", y="emissions per capita", hue="Region")
# The association between Internet use and emissions per capita is linear.

#b) Which are the countries with high emissions? (> 0.03)
Filtered_emissions_data=  data[data['Greenhouse gas emissions']> 0.03]
print(Filtered_emissions_data)
for i in Filtered_emissions_data['Country Name']:  
   print(i)
   
#c)Is there much variation by region (with respect to high emissions vs Internet use)?
data["High emissions"]= data[data['Greenhouse gas emissions']> 0.03]
sns.relplot(data=data, x= Filtered_emissions_data["Internet use"], y= Filtered_emissions_data["Greenhouse gas emissions"], hue="Region")

#d) Do all high income economies have high emissions?
High_income= data[data['High Income Economy']==1]
print(High_income)
High_emissions_income= data[(data['Greenhouse gas emissions']> 0.03) & (data['High Income Economy']==1)]
print(High_emissions_income)
#No because there are 67 countries with high income economies but only 61 countries with both high income economies and high greenhouse gas emissions.
#Therefore, not all high income countries have high emissions