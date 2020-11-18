import twitter
import graphic
import result

# Set the time interval
date_since = "2020-11-18"
date_until = "2020-11-13"

# Set source folders
csv_with_duplicate = "CSVWithDuplicate/"
csv_without_duplicate = "CSVWithoutDuplicate/"
csv_result = "Result/"

# Set variable date
date = "2020-11-18/"
print("\nThe date is " + date)

##### No Event #####
no_event_folder = "NoEvent/"

# Obtain tweets for each team in case of no event
# catch_no_event = True
catch_no_event = False
if catch_no_event:
    twitter.obtain_tweets(date_since,
                          date_until,
                          csv_with_duplicate + no_event_folder + date,
                          csv_without_duplicate + no_event_folder + date)

# Get and show total tweets statistics
print("\nGet number of total tweets.")
total_tweets_counts = twitter.count_total_tweets(twitter.get_teams(), csv_with_duplicate + no_event_folder + date)

# graphic.create_graph(total_tweets_counts, ["Team", "Count"])

# Save results in CSV file
print("\nSave results -> Total tweets")
result.save_result(total_tweets_counts,
                   ["Position", "Team", "Total tweets"],
                   csv_result + no_event_folder + date,
                   "ResultTotalTweets")

# Get and show unique users' tweets statistics
print("\nGet number of tweets created by unique users.")
total_tweets_per_unique_user_counts = twitter.count_tweets_per_unique_user(twitter.get_teams(),
                                                                           csv_without_duplicate + no_event_folder + date)

# graphic.create_graph(total_tweets_per_unique_user_counts, ["Team", "Count"])

# Save results in CSV file
print("\nSave results -> Total tweets per unique user")
result.save_result(total_tweets_per_unique_user_counts,
                   ["Position", "Team", "Total tweets per unique user"],
                   csv_result + no_event_folder + date,
                   "ResultTweetsPerUniqueUser")

# Get and show tweets per users statistics
print("\nGet average number of tweets created per users.")
tweets_per_user_per_team_counts = twitter.count_tweet_per_user(twitter.get_teams(),
                                                               csv_with_duplicate + no_event_folder + date,
                                                               csv_without_duplicate + no_event_folder + date)

# graphic.create_graph(tweets_per_user_per_team_counts, ["Team", "Count"])

# Save results in CSV file
print("\nSave results -> Tweets per user per team")
result.save_result(tweets_per_user_per_team_counts,
                   ["Position", "Team", "Tweets per user per team"],
                   csv_result + no_event_folder + date,
                   "ResultTweetsPerUserPerTeam")

##### Event #####
event_folder = "NoEvent/"

# Obtain tweets for each team in case of event
# catch_event = True
catch_event = False
if catch_event:
    twitter.obtain_tweets(date_since,
                          date_until,
                          csv_with_duplicate + "Event/2020-11-18/",
                          csv_without_duplicate + "Event/2020-11-18/")
