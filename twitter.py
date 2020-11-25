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
# teams_to_catch = ["#RealMadrid"]
teams_to_catch = ["#RealMadrid", "#Barcelona", "#ManchesterUnited", "#Chelsea", "#Juventus"]


def create_connection():
    # Establishing connection
    auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
    auth.set_access_token(credentials["ACCESS_TOKEN"], credentials["ACCESS_TOKEN_SECRET"])
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    return api


# Obtain tweets from twitter nad save them in two CSV files:
# The first file is for all tweets
# The second file is for tweets from different users, so any user will be counted one single time
def obtain_tweets(date_since, date_until, with_duplicate_path, without_duplicate_path):
    # Establishing connection
    api = create_connection()

    # Get teams for each of which the research should be done
    teams = get_teams()

    # Handle CSV files
    csv_file_with_duplicate = {}
    csv_file_writers_with_duplicate = {}
    for team in teams:
        csv_file_with_duplicate[team] = open(with_duplicate_path + team + ".csv", "a", encoding="UTF-8")
        csv_file_writers_with_duplicate[team] = csv.writer(csv_file_with_duplicate[team])

    # Obtain tweets for each team
    for team in teams:
        print("I'm going to search tweets for " + team)

        # search_word = team + " -filter:retweets"

        # Obtain tweets
        tweets = tweepy.Cursor(api.search,
                               q=team,
                               # lang="en",
                               since=date_since,
                               until=date_until).items()

        # Save obtained tweets
        for tweet in tweets:
            tweet_user = api.get_user(tweet.user.screen_name)

            csv_file_writers_with_duplicate[team].writerow(
                [tweet.user.screen_name, tweet_user.name, tweet.user.location, str(tweet.created_at)[:10]])

    # Save tweets that are not from the same user in order to get the different users which have published
    for team in teams:
        df = pd.read_csv(with_duplicate_path + team + ".csv",
                         names=["screen_name", "name", "location", "created"])

        # Remove duplicated user
        df.drop_duplicates(subset=["screen_name", "name"], inplace=True)

        df.to_csv(without_duplicate_path + team + ".csv", index=False)


# Obtain the number of total tweets for each teams
def count_total_tweets(teams, path):
    total_tweets_counts = {}

    # Count
    for team in teams:
        with open(path + team + ".csv") as csv_file:
            csv_file_reader = csv.reader(csv_file)
            total_tweets_count = len(list(csv_file_reader))
            total_tweets_counts.setdefault(team, total_tweets_count)

    return sort(total_tweets_counts)


# Obtain the number of tweets per unique user for each teams
def count_tweets_per_unique_user(teams, path):
    total_tweets_per_unique_user_counts = {}

    # Count
    for team in teams:
        with open(path + team + ".csv") as csv_file:
            csv_file_reader = csv.reader(csv_file)
            total_tweets_per_unique_user_count = len(list(csv_file_reader))
            total_tweets_per_unique_user_counts.setdefault(team, total_tweets_per_unique_user_count)

    return sort(total_tweets_per_unique_user_counts)


# Obtain the number of tweets per unique user for the given team
def count_tweets_per_unique_user_per_team(team, path):
    with open(path + team + ".csv") as csv_file:
        csv_file_reader = csv.reader(csv_file)
        total_tweets_per_unique_user_per_team = len(list(csv_file_reader))

    return total_tweets_per_unique_user_per_team


# Obtain the average number of tweets per user for each team
def count_tweet_per_user(teams, total_path, unique_user_path):
    tweet_per_user_count = {}

    for team in teams:
        tweet_per_user_per_team = count_total_tweets_per_team(team, total_path) / count_tweets_per_unique_user_per_team(
            team, unique_user_path)
        tweet_per_user_count.setdefault(team, tweet_per_user_per_team)

    return sort(tweet_per_user_count)


def sort(dictionary):
    sorted_tuples = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

    # Get them in form of dictionary
    sorted_dictionary = collections.OrderedDict(sorted_tuples)

    return sorted_dictionary


# Get the number of all the tweets obtained during the analysis
def get_total_stats(no_event_dates, event_dates):
    stats = 0

    csv_with_duplicate = "CSVWithDuplicate/"
    csv_without_duplicate = "CSVWithoutDuplicate/"

    no_event_folder = "NoEvent/"
    event_folder = "Event/"

    # Count all tweets for no_event analysis
    stats += count_all_obtained_tweets(no_event_dates, get_teams(), csv_with_duplicate, no_event_folder)
    stats += count_all_obtained_tweets(no_event_dates, get_teams(), csv_without_duplicate, no_event_folder)

    # Count all tweets for event analysis
    stats += count_all_obtained_tweets(event_dates, get_teams(), csv_with_duplicate, event_folder)
    stats += count_all_obtained_tweets(event_dates, get_teams(), csv_without_duplicate, event_folder)

    return stats


def count_all_obtained_tweets(dates, teams, duplicate_folder, event_folder):
    count = 0

    for date in dates:
        for team in teams:
            count += count_total_tweets_per_team(team, duplicate_folder + event_folder + date)

    return count


# Obtain the number of total tweets for the given team
def count_total_tweets_per_team(team, path):
    with open(path + team + ".csv") as csv_file:
        csv_file_reader = csv.reader(csv_file)
        total_tweets_per_team = len(list(csv_file_reader))

    return total_tweets_per_team


def get_credentials():
    return credentials


def get_teams():
    return teams_to_catch
