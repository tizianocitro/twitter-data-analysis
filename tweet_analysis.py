import twitter
import graphic

# Set the time interval
date_since = "2020-11-04"
date_until = "2020-11-05"

# Obtain tweets for each team
catch = False
if catch:
    twitter.obtain_tweets(date_since, date_until)

print("\nNumber of total tweets:")
total_tweets_counts = twitter.count_total_tweets(twitter.get_teams())

graphic.create_graph(total_tweets_counts, ["Team", "Count"])

print("\nNumber of tweets created by unique users:")
total_tweets_per_unique_user_counts = twitter.count_tweets_per_unique_user(twitter.get_teams())

graphic.create_graph(total_tweets_per_unique_user_counts, ["Team", "Count"])
