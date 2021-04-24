# GameSales

![PSButtons](https://github.com/Leoprma/GameSales/blob/main/Images/Ps_logo3.jpg)

This project has two aims: the first is to study the Playstation Store sales and the second is to create an app capable of recommend some game based on one given by the user.
The study of sales in psstore comprehends questions such as: 
- Which variables are more related with the price drop?
- What kind of games are on sale?
- Is there any difference in discounts/prices for games well-rated?
- The genre is a variable that has influence in discounts/price?
- How frequent are the sales?

# Tools
- Python
- Jupyter Notebook
  - Libraries: pandas, requests, re, BeautifulSoup, math, datetime, fuzzywuzzy, seaborn, matplotlib.pyplot
- Rawgpy API
- Tableau
- Streamlit

# Data Source 
- [Psndeals](https://psndeals.com/ps4-store-br-all-deals/)
  - Games on sale and prices obtained via web scrapping
- [Rawgpy API](https://rawgpy.readthedocs.io/en/latest/quickstart.html)
  - General information about the games (e.g. genre, metacritic score, release date) obtained via Rawg API

# Data Cleaning
- String matching

The data in psndeals website generated three dataframes: one that contained all games on sale, their original price and price with discount; one with the price historic; and one with the psplus price historic.
For getting the complementary data, it was necessary to search in the API using the game titles and the main challenge in this step was to tackle the differences between the string used to search and the string returned by the API, e.g. searching by "God of War Digital Deluxe" to get the God of War data.

The API always returned the 5 best matches and using the fuzzywuzzy library, I was able to compare which string had the higher percentage of similarity under distict metrics (Ratio, Partial Ratio, Token Sort Ratio and Token Set Ratio - for further details, I recommend this [explanation](https://www.datacamp.com/community/tutorials/fuzzy-string-python) about the library)

- Dataframe column type

After obtaining a dataframe with the API and Web Scrapping info together, te next step was to ensure that the data was in the right format/type.
In this step, all the data that came in the form of a single element list has been transformed in single strings and all date were converted to the desired format

- Adding information from the price historic dataframes

The last step was to extract data, such as: average weighted % discount, days on sale, average weighted price and to add them to the main dataframe.

# Analysis

In Jupyter notebook, the correlation between the variables was calculated seeking to give hints about what to explore on Tableau.
As a result, it was possible to notice that time since release and metacritic score were the two variables which have some correlation (although not strong). Besides that, the only genre that showed a consistent correlation with prices and discounts was the Indie genre.

Taking it into account, the main analysis made in Tableau were:

- How maximum discount varies with the time since release, metacritic score and ratings counter;
- How the maximum and minimum prices vary with the time since release, metacritic score;
- What is the relationship between the prices and the game being or not indie
- What is the average discount that the games had in the last year;
- How many times a game is on sale during a year and how much time it spend on sale;

# Results

All results and details can be accessed on [Tableau](https://public.tableau.com/profile/leonardo.prata.maciel#!/vizhome/GameSale_v4/Histria1?publish=yes)

# Conclusions

- The most important variable when talking about sales and prices is the time since release, the older the game is, the higher is the chance of having more discounts.
- However, if the game has been released in less than 2 years, the metacritic score is also a relevant variable. If the public's reception was not good, it increases the chance of a sale; and the opposite is also true.
- Indie game, in general, are much cheaper than non-indie games
- It is common to a game to enter several times on sale during the year. They stay on sale from 22% to 55% of the year (depending on how old is the game)

# Main Files
[Jupyter Notebook](https://github.com/Leoprma/GameSales/blob/main/Final_Project_Game_Sale.ipynb)
[Recommendation system](https://github.com/Leoprma/GameSales/blob/main/Game_recommendation.py)
