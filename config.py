client_id = ""
client_secret = ""
user_agent = ""

post_type = "hot" # hot, top, rising, new
subreddits = ['memes', 'funny']

# If true, the bot comments to the post in Reddit before reposting it. Some subreddit mods may not be okay with reposting their content.
comment_submission = False 
submission_comment = "Hey! I'm a bot and I reposted your post to my Instagram account ({instagram})! [Click here to see the post.]({instagram_post})"

# DO NOT USE YOUR MAIN INSTAGRAM ACCOUNT, 
# BECAUSE WHAT THIS BOT DOES IS AGAINST INSTAGRAM'S RULES.
# YOUR ACCOUNT MAY GET BANNED, SO USE ANOTHER ACCOUNT!
instagram_username = ""
instagram_password = ""
post_caption = "\"{title}\"\nThis post is posted by {author} at {subreddit}.\nScore: {score}"

wait_before_posting = 1800 # In seconds (by default it posts every 30 minute)