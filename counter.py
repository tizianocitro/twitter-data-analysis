import twitter
import result

# No event day dates
no_event_dates = ["2020-11-10",
                  "2020-11-11",
                  "2020-11-12",
                  "2020-11-13",
                  "2020-11-14",
                  "2020-11-15",
                  "2020-11-16",
                  "2020-11-17",
                  "2020-11-18",
                  "2020-11-19"]

# Event day dates
event_dates = ["2020-11-20",
               "2020-11-21",
               "2020-11-22",
               "2020-11-28"]

# Experiments number
experiments = len(no_event_dates) + len(event_dates)

# Total amount of tweets obtained
total = twitter.get_total_stats(no_event_dates, event_dates)

# Average of tweets obtained
average = total / experiments

# Save stats
result.save_stats(experiments, total, average,
                 ["Experiments", "Total", "Average"],
                 "Result/Stats/",
                 "Stats")