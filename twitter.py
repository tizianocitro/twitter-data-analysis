import tweepy
import csv
import pandas as pd

# Set credentials
credentials = {"CONSUMER_KEY": "7wUxEvUfDmfav3WbpKcU8O9NQ",
               "CONSUMER_SECRET": "0jOVcLWmInwh6l8MusvvaE1UTBqfRyWrz7dibVyh6MK1e6ywaN",
               "ACCESS_TOKEN": "1290305049256775683-6pRjLmuny7CrJUnkebeWwKWIL2CFCc",
               "ACCESS_TOKEN_SECRET": "JBcFXfyAeYVJoUimhafwnWWRMZVvp2taaSFsCD3nBNZ5z"}

# Set teams
teams = ["#Arsenal"]
teams2 = ["#RealMadrid", "#Barcelona", "#ManchesterUnited", "#Chelsea", "#Juventus"]

def create_connection():
    # Establishing connection
    auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
    auth.set_access_token(credentials["ACCESS_TOKEN"], credentials["ACCESS_TOKEN_SECRET"])
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    return api

def obtainTweet(date_since, date_until):
    # Establishing connection
    api = create_connection()

    # Get teams for each of which the research should be done
    teams = getTeams()

    # Handle CSV files
    csvFileWithDuplicate = {}
    csvFileWritersWithDuplicate = {}
    for team in teams:
        csvFileWithDuplicate[team] = open("CSVWithDuplicate/" + team + ".csv", "a", encoding="UTF-8")
        csvFileWritersWithDuplicate[team] = csv.writer(csvFileWithDuplicate[team])

    # Obtain tweets for each team
    for team in teams:
        print("I'm going to search tweets for " + team)

        # search_word = team + " -filter:retweets"

        #Obtain tweets
        tweets = tweepy.Cursor(api.search,
                               q=team,
                               lang="en",
                               since=date_since,
                               until=date_until).items()

        # Save obtained tweets
        for tweet in tweets:
            tweet_user = api.get_user(tweet.user.screen_name)

            csvFileWritersWithDuplicate[team].writerow([tweet.user.screen_name, tweet_user.name, tweet.text, tweet.retweet_count, tweet.user.location])

    # Save tweets that are not from the same user in order to get the different users which have published
    for team in teams:
        df = pd.read_csv("CSVWithDuplicate/" + team + ".csv", names=["screen_name", "name", "text", "retweet_count", "location"])

        # remove duplicates
        df.drop_duplicates(subset=["screen_name", "name"], inplace=True)

        df.to_csv("CSVWithoutDuplicate/" + team + ".csv", index=False)

def tweet_per_user():
    # Open CSV file with duplicate and get the list of tweet in a list of objects

    tweet_data_list = ()
    tweet_dictionary = {}
    for tweet_data in tweet_data_list:
        #Check if the usern<me is in the list of keys of the dictionary
        if tweet_data.screen_name not in tweet_dictionary:
            nothing = "if"
            # Add tweet_data.screen_name to tweet_dictionary with count = 1
        else:
            nothing = "else"
            # Increment count of tweet_data.screen_name

    return tweet_dictionary

def getTeams():
    return teams