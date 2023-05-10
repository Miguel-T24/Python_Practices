# 24. Write a python program to extract year, month, and date from an url

from re import search

def extract_date(string):
    return search(r"\d{4}/\d{2}/\d{2}", string).group()

print(extract_date("https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"))