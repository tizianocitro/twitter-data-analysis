import tweepy
import csv
import collections
import pandas as pd

# Set credentials
credentials = {"CONSUMER_KEY": "7wUxEvUfDmfav3WbpKcU8O9NQ",
               "CONSUMER_SECRET": "0jOVcLWmInwh6l8MusvvaE1UTBqfRyWrz7dibVyh6MK1e6ywaN",
               "ACCESS_TOKEN": "1290305049256775683-6pRjLmuny7CrJUnkebeWwKWIL2CFCc",
               "ACCESS_TOKEN_SECRET": "JBcFXfyAeYVJoUimhafwnWWRMZVvp2taaSFsCD3nBNZ5z"}

# Set teams
# teams = ["#RealMadrid"]
teams = ["#RealMadrid", "#Barcelona", "#ManchesterUnited", "#Chelsea", "#Juventus"]

def create_connection():
    # Establishing connection
    auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
    auth.set_access_token(credentials["ACCESS_TOKEN"], credentials["ACCESS_TOKEN_SECRET"])
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    return api

# Obtain tweets from twittter nad save them in two CSV files:
# The first file is for all tweets
# The second file is for tweets from different users, so any user will be counted one single time
def obtain_tweets(date_since, date_until):
    # Establishing connection
    api = create_connection()

    # Get teams for each of which the research should be done
    teams = get_teams()

    # Handle CSV files
    csv_file_with_duplicate = {}
    csv_file_writers_with_duplicate = {}
    for team in teams:
        csv_file_with_duplicate[team] = open("CSVWithDuplicate/" + team + ".csv", "a", encoding="UTF-8")
        csv_file_writers_with_duplicate[team] = csv.writer(csv_file_with_duplicate[team])

    # Obtain tweets for each team
    for team in teams:
        print("I'm going to search tweets for " + team)

        # search_word = team + " -filter:retweets"

        # Obtain tweets
        tweets = tweepy.Cursor(api.search,
                               q=team,
                               lang="en",
                               since=date_since,
                               until=date_until).items()

        # Save obtained tweets
        for tweet in tweets:
            tweet_user = api.get_user(tweet.user.screen_name)

            csv_file_writers_with_duplicate[team].writerow([tweet.user.screen_name, tweet_user.name, tweet.text, tweet.retweet_count, tweet.user.location])

    # Save tweets that are not from the same user in order to get the different users which have published
    for team in teams:
        df = pd.read_csv("CSVWithDuplicate/" + team + ".csv", names=["screen_name", "name", "text", "retweet_count", "location"])

        # Remove duplicated user
        df.drop_duplicates(subset=["screen_name", "name"], inplace=True)

        df.to_csv("CSVWithoutDuplicate/" + team + ".csv", index=False)

# Obtain the number of total tweets
def count_total_tweets(teams):
    total_tweets_counts = {}

    # Count
    for team in teams:
        with open("CSVWithDuplicate/" + team + ".csv") as csv_file:
            csv_file_reader = csv.reader(csv_file)
            total_tweets_count = len(list(csv_file_reader))
            total_tweets_counts.setdefault(team, total_tweets_count)

    return sort(total_tweets_counts)

# Obtain the number of total tweets
def count_tweets_per_unique_user(teams):
    total_tweets_per_unique_user_counts = {}

    # Count
    for team in teams:
        with open("CSVWithoutDuplicate/" + team + ".csv") as csv_file:
            csv_file_reader = csv.reader(csv_file)
            total_tweets_per_unique_user_count = len(list(csv_file_reader))
            total_tweets_per_unique_user_counts.setdefault(team, total_tweets_per_unique_user_count)

    return sort(total_tweets_per_unique_user_counts)

# Obtain the number of tweets per user
def tweet_per_user(team):
    # Open CSV file with duplicate and get the list of tweet in a list of objects
    # with open("CSVWithoutDuplicate/#" + team + ".csv") as csv_file:
        # csv_file_reader = csv.reader(csv_file)
        # next(csv_file_reader) to get a new line

    tweet_data_list = ()
    tweet_dictionary = {}
    for tweet_data in tweet_data_list:
        # Check if the usern<me is in the list of keys of the dictionary
        if tweet_data.screen_name not in tweet_dictionary:
            nothing = "if"
            # Add tweet_data.screen_name to tweet_dictionary with count = 1
        else:
            nothing = "else"
            # Increment count of tweet_data.screen_name

def sort(dictionary):
    sorted_tuples = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

    # Get them in form of dictionary
    sorted_dictionary = collections.OrderedDict(sorted_tuples)

    return sorted_dictionary

def get_credentials():
    return credentials

def get_teams():
    return teams