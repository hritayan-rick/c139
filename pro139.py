import pandas as pd
import numpy as np

df1 = pd.read_csv("shared_articles.csv") 
df2 = pd.read_csv("users_interactions.csv") 



df1 = df1[df1["eventType"] == "CONTENT SHARED"]
print(df1.shape)
print(df2.shape)

def totalEvents(df1_row):
  total_likes = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "LIKE")].shape[0]
  total_views = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "VIEW")].shape[0]
  total_bookmark = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "BOOKMARK")].shape[0]
  total_comment = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "COMMENT CREATED")].shape[0]
  total_follow = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "FOLLOW")].shape[0]

  return total_likes + total_views + total_bookmark + total_comment + total_follow

df1["total_events"] = df1.apply(totalEvents, axis = 1)

df1 = df1.sort_values(["total_events"], ascending = [False])
print(df1.head())