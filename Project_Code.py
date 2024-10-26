# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:54:16 2024

@author: Priscilla
"""
import pandas as pd
from collections import Counter


 
file_path = 'movie_dataset.csv'  
movies_df = pd.read_csv(file_path)
movies_df.columns = movies_df.columns.str.replace(' ', '_')

#Question 1:What is the highest rated movie in the dataset?
highest_rated_movie = movies_df.loc[movies_df['Rating'].idxmax(), 'Title']
print(highest_rated_movie)


#Question 2: What is the average revenue of all movies in the dataset? 
movies_df['Revenue_(Millions)'] = movies_df['Revenue_(Millions)'].fillna(movies_df['Revenue_(Millions)'].median())
movies_df['Metascore'] = movies_df['Metascore'].fillna(movies_df['Metascore'].median())
print(movies_df['Metascore'])
average_revenue = movies_df['Revenue_(Millions)'].mean()
print(average_revenue)


#Question 3:What is the average revenue of movies from 2015 to 2017 in the dataset?
average_revenue_2015_2017 = movies_df[(movies_df['Year'] >= 2015) & (movies_df['Year'] <= 2017)]['Revenue_(Millions)'].mean()
print(average_revenue_2015_2017)


#Question 4:How many movies were released in the year 2016?
movies_2016_count = movies_df[movies_df['Year'] == 2016].shape[0]
print(movies_2016_count)


#Question 5:How many movies were directed by Christopher Nolan?
nolan_movies_count = movies_df[movies_df['Director'] == 'Christopher Nolan'].shape[0]
print(nolan_movies_count)



#Question 6:How many movies in the dataset have a rating of at least 8.0?
movies_above_8_count =movies_df[movies_df["Rating"]>=8].shape[0]
print(movies_above_8_count)


#Question 7:What is the median rating of movies directed by Christopher Nolan?
median_rating_by_Nolan = movies_df[movies_df['Director']=='Christopher Nolan']['Rating'].median()
print(median_rating_by_Nolan)



#Question 8:Find the year with the highest average rating?
highest_avg_rating = movies_df.groupby('Year')['Rating'].mean().idxmax()
print(highest_avg_rating)      



#Question 9:What is the percentage increase in number of movies made between 2006 and 2016?
#Making the actors column an array on individual names that can be iterated through
movies_2006_count = movies_df[movies_df['Year'] == 2006].shape[0]
percentage_increase_2006_2016 = ((movies_2016_count - movies_2006_count) / movies_2006_count) * 100
print(movies_2006_count)
print(percentage_increase_2006_2016)         



#Question 10:Find the most common actor in all the movies?
#this is remove any inconsistencies such as anything seperating the actors other than semicolon
actors_list = movies_df['Actors'].str.split(',').explode().str.strip().str.lower()
most_common_actor = Counter(actors_list).most_common(1)[0][0]
print(most_common_actor)
unusual_delimiters = movies_df['Actors'].str.contains(';|\|')
print(movies_df[unusual_delimiters])


#Question 11:How many unique genres are there in the dataset?
genres_list = movies_df['Genre'].str.split(',').explode()
print(genres_list)
unique_genres_count = genres_list.nunique()
print(unique_genres_count)













