# **Measure TV Show Addictiveness**

# You're building a system to measure how addictive a TV show is. Implement two functions:

# - `process_log(show, episode, user_id)` — called continuously to log each viewing event
# - `print_results()` — after all logs processed, for each show find the earliest 
# episode `n` where at least 70% of viewers who watched episode `n` went on to watch the final 
# episode (episode 10)

# ```python
# process_log("Breaking Bad", 1, 1001)
# process_log("Breaking Bad", 2, 1001)
# process_log("Breaking Bad", 10, 1001)  # 1001 finished
# process_log("Breaking Bad", 1, 1002)
# process_log("Breaking Bad", 2, 1002)   # 1002 did NOT finish

# print_results()
# # Episode 1: 1 of 2 viewers finished = 50% → No
# # Episode 2: 1 of 2 viewers finished = 50% → No
# # No episode found for Breaking Bad
# ```


def process_log(movie, episode, user_id):
    users_who_watched_curr_episode = set()# Set of users who watched that episode   
    users_who_watched_final_episode = set() # Set of users who watched episode 10
    
    
    pass

def print_results():
    pass