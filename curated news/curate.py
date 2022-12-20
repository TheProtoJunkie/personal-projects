from web_scrape7 import *
import pandas as pd
# pip install pywin32
import win32com.client

# imports an excel list of 'bad words' that headlines commonly use that may hint at negative news.
bad_words_df = pd.read_excel(
    r'C:\Users\guerr\Desktop\NucampFolder\Python\1-Fundamentals\project\bad_word_list.xlsx')
bad_words_read = pd.DataFrame(bad_words_df, columns=['words'])

# Turn bad words dataframe into a list
bad_words_list = bad_words_read.values.tolist()

# turns dataframe import from list of lists to a list of strings


def string_list():
    num = 0
    just_bad_words_list = []
    while num < (len(bad_words_list)):
        just_text = (str(bad_words_list[num]))
        parsed_text = just_text[2:-2]
        just_bad_words_list.append(parsed_text)
        num += 1
    return just_bad_words_list


bw = string_list()
curated_headlines = list_of_stories[:15]
curated_urls = list_of_links[:15]


for i in range(len(bw)-1):
    for j in range(len(curated_headlines)-1):
        if str(bw[i]) in str(curated_headlines[j]):
            # curated_headlines.pop(j)
            curated_headlines[j] = ""
            curated_urls[j] = ""
            i = 0
else:
    i = 0

# -----email-----#
email = input('Where would you like to send your curated news?')
outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = str(email)
mail.Subject = 'Curated News!'
mail.Body = '1'+str(curated_headlines[0])+'\n'+str(curated_urls[0])+'\n' + '\n' + \
    '2'+str(curated_headlines[1])+'\n'+str(curated_urls[1])+'\n'+'\n' +\
    '3'+str(curated_headlines[2])+'\n'+str(curated_urls[2])+'\n'+'\n' +\
    '4'+str(curated_headlines[3])+'\n'+str(curated_urls[3])+'\n'+'\n' +\
    '5'+str(curated_headlines[4])+'\n'+str(curated_urls[4])+'\n'+'\n' +\
    '6'+str(curated_headlines[5])+'\n'+str(curated_urls[5])+'\n'+'\n' +\
    '7'+str(curated_headlines[6])+'\n'+str(curated_urls[6])+'\n'+'\n' +\
    '8'+str(curated_headlines[7])+'\n'+str(curated_urls[7])+'\n'+'\n' +\
    '9'+str(curated_headlines[8])+'\n'+str(curated_urls[8])+'\n'+'\n' +\
    '10'+str(curated_headlines[9])+'\n'+str(curated_urls[9])+'\n'+'\n' +\
    '11'+str(curated_headlines[10])+'\n'+str(curated_urls[10])+'\n'+'\n' +\
    '12'+str(curated_headlines[11])+'\n'+str(curated_urls[11])+'\n'+'\n' +\
    '13'+str(curated_headlines[12])+'\n'+str(curated_urls[12])+'\n'+'\n' +\
    '14'+str(curated_headlines[13])+'\n'+str(curated_urls[13])+'\n'+'\n' +\
    '15'+str(curated_headlines[14])+'\n'+str(curated_urls[14])+'\n'+'\n'
mail.send
