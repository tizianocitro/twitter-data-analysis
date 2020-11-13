import twitter
import graphic

# Set the time interval
date_since = "2020-11-12"
date_until = "2020-11-13"

# Set source folders
csv_with_duplicate = "CSVWithDuplicate/"
csv_without_duplicate = "CSVWithoutDuplicate/"

# Obtain tweets for each team in case of no event
# catch_no_event = True
catch_no_event = False
if catch_no_event:
    twitter.obtain_tweets(date_since,
                          date_until,
                          csv_with_duplicate + "NoEvent/",
                          csv_without_duplicate + "NoEvent/")

# Obtain tweets for each team in case of event
# catch_event = True
catch_event = False
if catch_event:
    twitter.obtain_tweets(date_since,
                          date_until,
                          csv_with_duplicate + "Event/",
                          csv_without_duplicate + "Event/")

# Get and show total tweets statistics
print("\nNumber of total tweets:")
total_tweets_counts = twitter.count_total_tweets(twitter.get_teams(), csv_with_duplicate + "NoEvent/")

graphic.create_graph(total_tweets_counts, ["Team", "Count"])

# Get and show unique users' tweets statistics
print("\nNumber of tweets created by unique users:")
total_tweets_per_unique_user_counts = twitter.count_tweets_per_unique_user(twitter.get_teams(),
                                                                           csv_without_duplicate + "NoEvent/")

graphic.create_graph(total_tweets_per_unique_user_counts, ["Team", "Count"])

# Get and show tweets per users statistics
print("\nAverage number of tweets created per users:")
tweets_per_user_per_team_counts = twitter.count_tweet_per_user(twitter.get_teams(),
                                                               csv_with_duplicate + "NoEvent/",
                                                               csv_without_duplicate + "NoEvent/")

graphic.create_graph(tweets_per_user_per_team_counts, ["Team", "Count"])