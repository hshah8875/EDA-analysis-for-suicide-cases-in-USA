# Final project EM 624
# Author: Harsh Shah
# This program performs analysis on Suicides using guns from year 2012 to 2014
# It presents output in form of graphs and stats to have clear idea of data
import pandas as pd
import matplotlib.pyplot as plt
import csv
import bs4 as bs
import requests
import nltk
import string
from wordcloud import WordCloud     # importing all the necessary libraries

df = pd.read_csv('full_data.csv')     # opening of our data file
cases_distribution = df['intent'].values.tolist()     # to plot suicides cases so require only intent column
count_cases = [0, 0, 0, 0]                           # and converting values to list
for i in cases_distribution:
    if i == 'Suicide':                # conditions and store in variable list
        count_cases[0] += 1
    elif i == 'Homicide':
        count_cases[1] += 1
    elif i == 'Accidental':
        count_cases[2] += 1
    elif i == 'Undetermined':
        count_cases[3] += 1
    else:
        continue
print("\n*Suicide analysis report*")
print("\nQue :- How are cases of death between 2012 and 2014 involving guns are distributed?")
print("\nThe number of suicides are " + str(count_cases[0]))
print("The number of homicides are " + str(count_cases[1]))
print("The number of accidental are " + str(count_cases[2]))    # printing the necessary stats

w = df.loc[df['intent'] == "Suicide"]
column_year = w['year'].values.tolist()       # finding columns for year and intent with suicides
count_years = [0, 0, 0]                # variable to store values
for i in column_year:
    if i == 2012:                   # conditions for distribution of suicides over years
        count_years[0] += 1
    elif i == 2013:
        count_years[1] += 1
    elif i == 2014:
        count_years[2] += 1
    else:
        continue
print("\nQue :- Year wise distribution of suicide cases")
print("\nThere were total " + str(count_years[0]) + " suicide cases in 2012.")
print("There were total " + str(count_years[1]) + " suicide cases in 2013.")
print("There were total " + str(count_years[2]) + " suicide cases in 2014")   # printing necessary stats
x_year1 = ['2012', '2013', '2014']      # values store as years
y = count_years
plt.pie(y, labels=x_year1, autopct='%2.1f%%')      # plotting pie graph for better visualization
plt.title("Pie chart- Suicide cases distribution over 3 years")
plt.show()

column_gender = w['sex'].values.tolist()     # creating the column for gender as to plot graph
count_gender_suicides = [0, 0]
for i in column_gender:
    if i == 'M':      # getting condition
        count_gender_suicides[0] += 1
    elif i == 'F':
        count_gender_suicides[1] += 1
    else:
        continue
print("\nGender wise distribution")
print("\nThere were total " + str(count_gender_suicides[0]) + " males who committed suicides.")
print("There were total " + str(count_gender_suicides[1]) + " females who committed suicides.")
x_sex = ['Male', 'Female']
y = count_gender_suicides
plt.pie(y, labels=x_sex, autopct='%2.1f%%')     # printing pie chart
plt.title("Pie chart - Distribution over gender")
plt.show()

column_race = w['race'].values.tolist()   # column for race
count_race_suicides = [0, 0, 0, 0, 0]
for i in column_race:
    if i == "Asian/Pacific Islander":
        count_race_suicides[0] += 1
    elif i == "White":
        count_race_suicides[1] += 1
    elif i == "Native American/Native Alaskan":
        count_race_suicides[2] += 1
    elif i == "Black":
        count_race_suicides[3] += 1
    elif i == "Hispanic":
        count_race_suicides[4] += 1
    else:
        continue
print("\nQue :- Race wise distribution of cases")
print("\nThere were total " + str(count_race_suicides[0]) + " suicide cases for Asian/Pacific Islander race.")
print("There were total " + str(count_race_suicides[1]) + " suicide cases for White race.")
print("There were total " + str(count_race_suicides[2]) + " suicide cases for Native American/Native Alaskan race.")
print("There were total " + str(count_race_suicides[3]) + " suicide cases for Black race. ")
print("There were total " + str(count_race_suicides[4]) + " suicide cases for Hispanic race. ")
x = ['Asian/Pacific Islander', 'White', 'Native American/Native Alaskan race', 'Black', 'Hispanic']
y = count_race_suicides
plt.pie(y, labels=x, autopct='%2.1f%%')
plt.title("Pie chart- Suicide case distribution over race")
plt.show()

column_education = w['education'].values.tolist()    # for education
count_education_suicides = [0, 0, 0, 0]
for i in column_education:
    if i == 'BA+':
        count_education_suicides[0] += 1
    elif i == 'Some college':
        count_education_suicides[1] += 1
    elif i == 'HS/GED':
        count_education_suicides[2] += 1
    elif i == 'Less than HS':
        count_education_suicides[3] += 1
    else:
        continue
column_nan = w['education']
nan = column_nan.isnull().sum()      # condition for nan
count_education_suicides.append(nan)
print("\nQue :- Education wise distribution of suicide cases")
print("\nThere were total " + str(count_education_suicides[0]) + " suicide cases with BA+ as their education.")
print("There were total " + str(count_education_suicides[1]) +
      " suicide cases went to some college for their education.")
print("There were total " + str(count_education_suicides[2]) + " suicide cases with HS/GED as their education.")
print("There were total " + str(count_education_suicides[3]) + " suicide cases with Less than HS as their education.")
print("There were total " + str(count_education_suicides[4]) + " suicide cases where education is not stated.")
x_edu = ['BA+', 'Some college', 'HS/GED', 'Less than HS', 'Not stated']
y = count_education_suicides
plt.pie(y, labels=x_edu, autopct='%2.1f%%')
plt.title("Pie chart- Suicide case distribution over education")
plt.show()

column_age = w['age'].values.tolist()
count_ages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def get_ages(parts, age_list):    # defining function to get index of age
    for i in parts:
        if i in range(0, 10):
            age_list[0] += 1
        elif i in range(10, 20):
            age_list[1] += 1
        elif i in range(20, 30):
            age_list[2] += 1
        elif i in range(30, 40):
            age_list[3] += 1
        elif i in range(40, 50):
            age_list[4] += 1
        elif i in range(50, 60):
            age_list[5] += 1
        elif i in range(60, 70):
            age_list[6] += 1
        elif i in range(70, 80):
            age_list[7] += 1
        elif i in range(80, 90):
            age_list[8] += 1
        elif i in range(90, 100):
            age_list[9] += 1
        elif i in range(100, 110):
            age_list[10] += 1
        else:
            continue
    return age_list


age_list_update = get_ages(column_age, count_ages)
column_nan_age = w['age']
nan_age = column_nan_age.isnull().sum()
age_list_update.append(nan_age)
print('\nAge wise analysis')
print("\n Four highest age groups with highest number of cases:")
print("\nIt seems maximum cases were " + str(age_list_update[5]) + " and between 50-60 age group.")
print("Second most number cases were " + str(age_list_update[4]) + " and between 40-50 age group.")
print("Third most number of cases were " + str(age_list_update[6]) + " and between 60-70 age group.")
print("Fourth most number of cases were " + str(age_list_update[2]) + " and between 20-30 age group.")
print("Fifth most number of cases were " + str(age_list_update[3]) + " and between 30-40 age group.")
x = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100', '100-110', 'Not stated']
y = age_list_update
plt.bar(x, y, width=0.4)
plt.title("Bar chart- Distribution over ages")
plt.xticks(rotation='vertical')
plt.xlabel("Age group")
plt.ylabel("Count")
plt.show()

comparison_age_race = w.loc[w['race'] == "White"]      # getting column for race
comparison_age_race_list = comparison_age_race['age'].values.tolist()
comparison_age_race_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
comparison_age_race_list_update = get_ages(comparison_age_race_list, comparison_age_race_counts)
column_nan_age_race = comparison_age_race['age']
nan_age_race = column_nan_age_race.isnull().sum()
comparison_age_race_list_update.append(nan_age_race)

comparison_age_race_black = w.loc[w['race'] == "Black"]
comparison_age_race_list_black = comparison_age_race_black['age'].values.tolist()
comparison_age_race_counts_black = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
comparison_age_race_list_update_black = get_ages(comparison_age_race_list_black, comparison_age_race_counts_black)
column_nan_age_race_black = comparison_age_race_black['age']
nan_age_race_black = column_nan_age_race_black.isnull().sum()
comparison_age_race_list_update_black.append(nan_age_race_black)
print("\nAge versus Race comparison")
print("\nIt seems for white race maximum cases are between 50-60: " + str(comparison_age_race_list_update[5]))
print("Also for age group 40-50 and 60-70 are almost same which are: " + str(comparison_age_race_list_update[4])
      + " and " + str(comparison_age_race_list_update[6]) + " respectively.")
print("In age group 20-40 there are total: " + str(comparison_age_race_list_update[2] +
                                                   comparison_age_race_list_update[3]) + " cases.")

x1 = x
y1 = comparison_age_race_list_update
y2 = comparison_age_race_list_update_black
plt.bar(x1, y1, width=0.4, label='White')
plt.bar(x1, y2, width=0.4, label='Black')
plt.title("Bar chart- Comparison of age versus race(White, Black)")
plt.xticks(rotation='vertical')
plt.xlabel("Age group")
plt.ylabel("Count")
plt.legend()
plt.show()

comparison_gender_race_list = comparison_age_race['sex'].values.tolist()
com_sex_race_counts = [0, 0]
for i in comparison_gender_race_list:
    if i == 'M':
        com_sex_race_counts[0] += 1
    elif i == 'F':
        com_sex_race_counts[1] += 1
    else:
        continue

x5 = x_sex
y5 = com_sex_race_counts
plt.pie(y5,  labels=x5, autopct='%2.1f%%')
plt.title('Distribution: White Race vs Gender')
plt.show()

comparison_education = comparison_age_race['education'].values.tolist()
com_edu_counts = [0, 0, 0, 0]
for i in comparison_education:
    if i == 'BA+':
        com_edu_counts[0] += 1
    elif i == 'Some college':
        com_edu_counts[1] += 1
    elif i == 'HS/GED':
        com_edu_counts[2] += 1
    elif i == 'Less than HS':
        com_edu_counts[3] += 1
    else:
        continue
column_nan_edu = comparison_age_race['education']
nan_edu = column_nan_edu.isnull().sum()
com_edu_counts.append(nan_edu)
x2 = x_edu
y_edu = com_edu_counts
plt.pie(y_edu, labels=x2, autopct='%2.1f%%')
plt.title('Pie chart: Education of White race people')
plt.show()

com_year_race = comparison_age_race['year'].values.tolist()
com_year_race_counts = [0, 0, 0]
for i in com_year_race:
    if i == 2012:
        com_year_race_counts[0] += 1
    if i == 2013:
        com_year_race_counts[1] += 1
    if i == 2014:
        com_year_race_counts[2] += 1
    else:
        continue
x_year = x_year1
y_year = com_year_race_counts
plt.plot(x_year, y_year)
plt.title('White race cases over years')
plt.xlabel('Years')
plt.ylabel('Counts')
plt.show()

file = open('who_suicide_statistics.csv', 'r')
reader = csv.reader(file)
next(reader)


def get_index_total(parts):      # defining the function fro index
    if parts[0] == 'United States of America' and parts[1] == '2012':
        return 0
    if parts[0] == 'United States of America' and parts[1] == '2013':
        return 1
    if parts[0] == 'United States of America' and parts[1] == '2014':
        return 2
    else:
        return 3


def get_index_male(parts):
    if parts[0] == 'United States of America' and parts[1] == '2005' and parts[2] == 'male':
        return 0
    if parts[0] == 'United States of America' and parts[1] == '2006' and parts[2] == 'male':
        return 1
    if parts[0] == 'United States of America' and parts[1] == '2007' and parts[2] == 'male':
        return 2
    if parts[0] == 'United States of America' and parts[1] == '2008' and parts[2] == 'male':
        return 3
    if parts[0] == 'United States of America' and parts[1] == '2009' and parts[2] == 'male':
        return 4
    if parts[0] == 'United States of America' and parts[1] == '2010' and parts[2] == 'male':
        return 5
    if parts[0] == 'United States of America' and parts[1] == '2011' and parts[2] == 'male':
        return 6
    else:
        return 7


def get_index_female(parts):
    if parts[0] == 'United States of America' and parts[1] == '2005' and parts[2] == 'female':
        return 0
    if parts[0] == 'United States of America' and parts[1] == '2006' and parts[2] == 'female':
        return 1
    if parts[0] == 'United States of America' and parts[1] == '2007' and parts[2] == 'female':
        return 2
    if parts[0] == 'United States of America' and parts[1] == '2008' and parts[2] == 'female':
        return 3
    if parts[0] == 'United States of America' and parts[1] == '2009' and parts[2] == 'female':
        return 4
    if parts[0] == 'United States of America' and parts[1] == '2010' and parts[2] == 'female':
        return 5
    if parts[0] == 'United States of America' and parts[1] == '2011' and parts[2] == 'female':
        return 6
    else:
        return 7


male_count = [0, 0, 0, 0, 0, 0, 0]
for row in reader:
    index = get_index_male(row)
    if index == 7:
        continue
    male_count[index] += int(row[4])
file1 = open('who_suicide_statistics.csv', 'r')
reader1 = csv.reader(file1)
next(reader1)
female_count = [0, 0, 0, 0, 0, 0, 0]
for row1 in reader1:
    index1 = get_index_female(row1)
    if index1 == 7:
        continue
    female_count[index1] += int(row1[4])

x = ['2005', '2006', '2007', '2008', '2009', '2010', '2011']
y1 = male_count
y2 = female_count
plt.plot(x, y1, label='Male')
plt.plot(x, y2, label='Female')
plt.legend()
plt.show()

file2 = open('who_suicide_statistics.csv', 'r')     # opening this file
reader2 = csv.reader(file2)
next(reader2)
total_count = [0, 0, 0]
for row2 in reader2:
    index2 = get_index_total(row2)
    if index2 == 3:
        continue
    total_count[index2] += int(row2[4])
x_comparison = x_year1
y_comparison_1 = total_count
y_comparison_2 = count_years
plt.figure(figsize=(15, 6))
plt.bar(x_comparison, y_comparison_1, label='Total cases')
plt.bar(x_comparison, y_comparison_2, label='Suicides with guns')
plt.title('Total Suicide Cases vs Suicides with Guns')
plt.legend()
plt.show()

# Washington post Article Analysis through Wordcloud
body = requests.get('https://www.washingtonpost.com/graphics/business/wonkblog/suicide-rates/')
soup = bs.BeautifulSoup(body.content, 'html.parser')  # requesting content from website
para_1 = ''
for paragraph in soup.find_all('p'):
    text = paragraph.text.replace("\n", " ").strip()
    para_1 += ' ' + text
para_clean = []      # cleaning the text
for word in para_1:
    if word not in string.digits:
        if word not in string.punctuation:
            word1 = word.lower()
            para_clean.append(word1)
para = ''.join(para_clean)
para_tokens = nltk.word_tokenize(para)
stopwords_file = open('stopwords_en (1).txt', 'r')       # opening stopwords file
stopwords = []
for words in stopwords_file:
    stopwords.append(words.rstrip('\n'))
para_update = []
for word2 in para_tokens:
    if len(word2) > 2:
        if word2 not in stopwords:
            para_update.append(word2)
para_common_words = nltk.FreqDist(para_update).most_common(15)
stopwords.extend(['percent', 'people', 'states', 'suicides', 'suicide', 'rates', 'gun', 'guns', 'women',
                  'access', 'americans', 'attempt', 'die', 'firearm', 'countries'])
# removing words that are not in need
para_update_final = []
for word3 in para_update:
    if word3 not in stopwords:
        para_update_final.append(word3)
para_word_cloud = ' '.join(para_update_final)
plt.figure(figsize=(9, 7))       # deciding parameters
wc = WordCloud(background_color="white", max_words=200)
wc.generate(para_word_cloud)     # printing the Wordcloud
wc.to_file('Headlines.png')
plt.title("Wordcloud for article")
plt.imshow(wc)
plt.axis('off')
plt.show()

print("\n* This is end of processing *")