import pandas as pd
import requests
from bs4 import BeautifulSoup
import streamlit as st

st.title("Game Recommendation")
st.header('This is a platform that suggests games based on the one input by the user')

try:
	user_input = st.text_input("Game Title", "Search")
	game_name = user_input.lower().replace(' ','+')
	requests.get(f'https://api.rawg.io/api/games?key=f9ffc69c548c4547bdfe188c29fa4086&search={game_name}').json()
	slug=pd.json_normalize(requests.get(f'https://api.rawg.io/api/games?key=f9ffc69c548c4547bdfe188c29fa4086&search={game_name}').json())['results'][0][0]['slug']
	soup=BeautifulSoup(requests.get(f'https://rawg.io/games/{slug}/suggestions').content)
	game_name=[]
	metacritic=[]
	release=[]
	genre=[]
	description=[]
	background_image=[]
	for i in range(3):
		game_name.append(soup.find_all('a',attrs={'class':"game-card-compact__heading game-card-compact__heading_with-link"})[i].text)
		metacritic.append(soup.find_all('div',attrs={'class':"metascore-label metascore-label_green"})[i].text)
		description.append(soup.find_all('div',attrs={'class':"truncate-block game-card__about-text"})[i].text)
	for i in range(1,13,4):
		release.append(soup.find_all('div',attrs={'class':"game-card-about__desription"})[i].text)
		genre.append(soup.find_all('div',attrs={'class':"game-card-about__desription"})[i+1].text)
	for i in range(3):
		suggestion_name=game_name[i].lower().replace(' ','+')
		game_info=requests.get(f'https://api.rawg.io/api/games?key=f9ffc69c548c4547bdfe188c29fa4086&search={suggestion_name}').json()
		background_image.append(game_info['results'][0]['background_image'])
#st.dataframe(suggestions)

	for i in range(3):
		st.write(f'**- Suggestion {i+1}:**\n')
		st.write('**Name:**\n')
		st.write(f"{game_name[i]}\n")
		st.image(background_image[i],use_column_width=True)
		st.write('**About:**\n')
		st.write(description[i])
		st.write('**Genres:**\n')
		st.write(f"{genre[i]}\n")
		st.write('**Release date:**\n')
		st.write(f"{release[i]}\n")
		st.write('**Metacritic score:**\n')
		st.write(f"{metacritic[i]}\n")
except:
	pass