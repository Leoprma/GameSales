import pandas as pd
import rawgpy
import streamlit as st

st.title("Game Recommendation")
st.header('This is a platform that suggests games based on the one input by the user')

user_input = st.text_input("Game Title", "Search")
rawg = rawgpy.RAWG("User-Agent, this should identify your app")
results=rawg.search(user_input)
slug=results[0].slug
suggestions=pd.json_normalize(list(rawg.game_suggestions(slug))[0:3])
#st.dataframe(suggestions)

for i in range(3):
	st.write(f'**- Suggestion {i+1}:**\n')
	st.write('**Name:**\n')
	st.write(f"{suggestions['name'][i]}\n")
	st.image(suggestions['background_image'][i],use_column_width=True)
	st.write('**About:**\n')
	st.write(suggestions['short_description'][i])
	genres=[]
	for j in range(len(suggestions['genres'][i])):
		genres.append(suggestions['genres'][i][j]['name'])
	st.write('**Genres:**\n')
	st.write(f"{genres}\n")
	st.write('**Release date:**\n')
	st.write(f"{suggestions['released'][i]}\n")
	st.write('**Metacritic score:**\n')
	st.write(f"{suggestions['metacritic'][i]}\n")
	parent_platform=[]
	for k in range(len(suggestions['parent_platforms'][i])):
		parent_platform.append(suggestions['parent_platforms'][i][k]['platform']['name'])
	st.write("**Platforms:**\n")
	st.write(f'{parent_platform}\n')
	st.write("**Estimated time to beat the game:**\n")
	st.write(f"{suggestions['playtime'][i]} hours\n")