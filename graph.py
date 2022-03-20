import os
import matplotlib.pyplot as plt
import dataFetch    # Our custom functions to fetch the list containing the ID, likes and retweet lists

def plotGraphs(username):
    try:
        masterList = dataFetch.finalReturn(username)
        sNoList = masterList[0]
        likesList = masterList[1]
        retweetsList = masterList[2]

        fig,ax=plt.subplots()
        ax.plot(sNoList,likesList,marker = 'o',color = 'blue')
        ax.set_xlabel('n\'th tweet in the last 20 tweets')
        ax.set_ylabel('No.of likes')
        ax.set_xticks(sNoList)
        ax.set_title('@'+username)

        plt.savefig("./likes.jpeg")
        print(os.getcwd())


        fig,ax2=plt.subplots()
        ax2.plot(sNoList,retweetsList,marker = 'o',color = 'red')
        ax2.set_xlabel('n\'th tweet in the last 20 tweets')
        ax2.set_ylabel('No.of retweets')
        ax2.set_xticks(sNoList)
        ax2.set_title('@'+username)

        plt.savefig("./retweets.jpeg")

    except:
        return "User not found"




