import praw
reddit = praw.Reddit(client_id = 'Lq6zlWlS7RaVOQ', client_secret = 'yIZAzKj5JCEZCfhUQ-NTOirVVNY', username = 'mbkt8', password ='enter8898', user_agent = 'me')
subreddit_news = reddit.subreddit('news')
subreddit_nba = reddit.subreddit('nba')

hot_news = subreddit_news.hot(limit = 20)
hot_nba = subreddit_nba.hot(limit = 20)
print('NEWS:')
for submission in hot_news:
 	if not submission.stickied:
 		print(submission.title)
print('NBA:')
for submission in hot_nba:
	if not submission.stickied:
		print(submission.title)

