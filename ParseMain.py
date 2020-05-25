import requests
import bs4
import json

def getInfo(name):

    info  = requests.get("https://www.instagram.com/{}/?__a=1".format(name));
    try:
        j = json.loads(info.content)
    except:
        return {
            "Biography":"",
        "Followers":0,
        "Follow":0,
        "Full_name": "",
        "Is_business_account":False,
        "Business_category_name": "",
        "Likes":0,
        "Comments":0,
        "Is_error":True
        }

    #Check if acoount is private!!!

    #Count of comments
    try:
        total_comments = 0
        max_comments = 0
        max_comments_pic =""
        min_comments=10000000
        min_comments_pic = ""
        commentsList=[]
        for i in j["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]:
            total_comments+=int(i["node"]["edge_media_to_comment"]["count"])
            commentsList.append(int(i["node"]["edge_media_to_comment"]["count"]))
            if int(i["node"]["edge_media_to_comment"]["count"])>max_comments :
                max_comments = int(i["node"]["edge_media_to_comment"]["count"])
                max_comments_pic = i["node"]["display_url"]
            if(int(i["node"]["edge_media_to_comment"]["count"])<min_comments):
                min_comments = int(i["node"]["edge_media_to_comment"]["count"])
                min_comments_pic = i["node"]["display_url"]

    #count of likes
        total_likes = 0
        max_likes = 0
        max_likes_pic = ""
        min_likes = 10000000
        min_likes_pic = ""
        likesList=[]
        for i in j["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]:
            total_likes+=int(i["node"]["edge_liked_by"]["count"])
            likesList.append(int(i["node"]["edge_liked_by"]["count"]))
            if(int(i["node"]["edge_liked_by"]["count"])>max_likes):
                max_likes = int(i["node"]["edge_liked_by"]["count"])
                max_likes_pic = i["node"]["display_url"]
            if(int(i["node"]["edge_liked_by"]["count"])<min_likes):
                min_likes=int(i["node"]["edge_liked_by"]["count"])
                min_likes_pic=i["node"]["display_url"]

        return {
            "Pic": j["graphql"]["user"]["profile_pic_url"],
            "Biography":j["graphql"]["user"]["biography"],
            "Followers":j["graphql"]["user"]["edge_followed_by"]["count"],
            "Follow":j["graphql"]["user"]["edge_follow"]["count"],
            "Full_name": j["graphql"]["user"]["full_name"],
            "Is_business_account":j["graphql"]["user"]["is_business_account"],
            "Business_category_name": j["graphql"]["user"]["business_category_name"],
            "Likes":total_likes,
            "Comments":total_comments,
            "Is_error": False,
            "max_comments" : max_comments,
            "max_comments_pic" : max_comments_pic,
            "min_comments": min_comments,
            "min_comments_pic" : min_comments_pic,
            "max_likes" : max_likes,
            "max_likes_pic" : max_likes_pic,
            "min_likes" : min_likes,
            "min_likes_pic" : min_likes_pic,
            "likesList": likesList,
            "commentsList":commentsList
            }
    except KeyError:
        return {
        "Pic":"",
        "Biography":"",
        "Followers":0,
        "Follow":0,
        "Full_name": "",
        "Is_business_account":False,
        "Business_category_name": "",
        "Likes":0,
        "Comments":0,
        "Is_error":True,
        "max_comments":0,
        "max_comments_pic": "",
        "min_comments": 0,
        "min_comments_pic": "",
        "max_likes": 0,
        "max_likes_pic": "",
        "min_likes": 0,
        "min_likes_pic": "",
        "likesList": [],
        "commentsList": []
        }

