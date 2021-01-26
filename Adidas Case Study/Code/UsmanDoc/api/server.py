
import pandas as pd
import numpy as np
import json as json
patients_df = pd.read_json('https://s3-eu-west-1.amazonaws.com/csparkdata/ol_cdump.json',lines=True)



######################TASK  1 Data Cleaning###########################

df1 = patients_df.dropna(subset=['title'])
df1['publish_date'] = df1['publish_date'].str.strip().str[-4:].str.extract('(\d+)').fillna(0).astype(int)
df2 = df1.query("number_of_pages > 20 and publish_date > 1950")
df2.to_json('./json_clean.json')




######################TASK 2 Selection###########################

#Harry Potter Filter

df3=df2[df2['title'].str.contains("Harry Potter")]
df3.to_json('./json_hp.json')
df3.to_csv('./json_clean.csv',index=False)

print('Task 1 Done')

#Book with Most pages

df4=df2[df2['number_of_pages']==df2['number_of_pages'].max()]
df4.to_json('./json_MaxPage.json')

print('Task 2 Done')

#Top 5 authors 


df2['authors']=df2['authors'].astype(str)
df5=df2.groupby(["authors"]).size().nlargest(5)
                             
df5.to_json('./json_Author.json')

print('Task 3 Done')

#Top 5 genres 


df2['genres']=df2['genres'].astype(str)
df6=df2.groupby(["genres"]).size().nlargest(5)
df6.to_json('./json_genres.json')

print('Task 4 Done')

#Calculate Mean

df7=df2["number_of_pages"].mean()
with open('./json_avgpages.json', "w") as out_file:
    json.dump(df7, out_file)

print('Task 5 Done')
    
#Per Year Publish

df2['authors']=df2['authors'].astype(str)
df8=df2.groupby(['publish_date'])['authors'].count()
df8.to_json('./json_pub.json')

print('Task 6 Done')





