import streamlit as strl
import pandas as pd
import pickle as pck
import requests




dict1 = pck.load(open('file1.pkl','rb'))
list1 = pd.DataFrame(dict1)

correlation = pck.load(open('correlation.pkl','rb'))


def fetch(id):
    temp = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=b0f2982393a3c430a4b093a72986ffe6&language=en-US'.format(id))
    data = temp.json()
    str = 'https://image.tmdb.org/t/p/w500/'
    return str + data['poster_path']

def fetch1(id):
    temp = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=b0f2982393a3c430a4b093a72986ffe6&language=en-US'.format(id))
    data = temp.json()
    return data['homepage']

def recommendor(movie):
    idx = list1[movie == list1['title']].index[0]
    dist = correlation[idx]
    movie_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:7]
    sgst = []
    posters = []
    homepage = []
    for i in movie_list:
        id = list1.iloc[i[0]].movie_id
        sgst.append(list1.iloc[i[0]].title)
        posters.append(fetch(id))
        homepage.append(fetch1(id))
    return sgst,posters,homepage
strl.title("Movie Picks for you")
option_list = strl.selectbox(
'Movie name:',
list1['title'].values,

)

if (strl.button('Recommend')):
    names,poster,link = recommendor(option_list)
    c1,c2,c3,c4,c5,c6 = strl.columns(6)
    with c1:
        strl.text(names[0])
        strl.image(poster[0])
        strl.markdown(link[0], unsafe_allow_html=True)
    with c2:
        strl.text(names[1])
        strl.image(poster[1])
        strl.markdown(link[1], unsafe_allow_html=True)
    with c3:
        strl.text(names[2])
        strl.image(poster[2])
        strl.markdown(link[2], unsafe_allow_html=True)
    with c4:
        strl.text(names[3])
        strl.image(poster[3])
        strl.markdown(link[3], unsafe_allow_html=True)
    with c5:
        strl.text(names[4])
        strl.image(poster[4])
        strl.markdown(link[4], unsafe_allow_html=True)
    with c6:
        strl.text(names[5])
        strl.image(poster[5])
        strl.markdown(link[5], unsafe_allow_html=True)