from instabot import Bot
print("http://thisiswhereidostuff.com")
print("http://github.com/DylanAlloy")
print("Please make sure you have hashtags.txt and comments.txt filled out and in the same directory!\n\n")
bot = Bot(
            max_likes_per_day=1000,
            max_unlikes_per_day=1000,
            max_follows_per_day=350,
            max_unfollows_per_day=350,
            max_comments_per_day=100,
            max_likes_to_like=100,
            filter_users=True,
            max_followers_to_follow=2000,
            min_followers_to_follow=10,
            max_following_to_follow=7500,
            min_following_to_follow=10,
            max_followers_to_following_ratio=10,
            max_following_to_followers_ratio=2,
            max_following_to_block=2000,
            min_media_count_to_follow=3,
            like_delay=10,
            unlike_delay=10,
            follow_delay=30,
            unfollow_delay=30,
            comment_delay=60,
            whitelist=False,
            blacklist=False,
            comments_file="comments.txt",
            stop_words=['shop', 'store', 'free']
)
print("---Initialize---")
user = input("\n\nWhat is your username?: ")
passw = input("\n\nWhat is your password?: ")
bot.login(username=user,password=passw)

while True:

    print("\n\n---OPTIONS---\n\n")
    print("1. Follow")
    print("2. Like")
    print("3. Comment\n\n")
    x = input("What would you like to do?: ")

    if x == "1":
        print("\n\nFollowing based on what is in hashtags.txt file!\n\n")
        with open("hashtags.txt", "r") as f:
            for line in f:
                user = bot.get_hashtag_users(line)
                bot.follow_users(user)

    elif x == "2":
        print("\n\nLiking based on what is in hashtags.txt file!\n\n")
        with open("hashtags.txt", "r") as f:
            for line in f:
                bot.like_hashtag(line)

    elif x == "3":
        print("\n\nCommenting based on what is in hashtags.txt file!\n\n")
        with open("hashtags.txt", "r") as f:
            for line in f:
                l = bot.get_hashtag_medias(line)
                for each in l:
                    if bot.is_commented(each)==True:
                        print("\n\nSkipping one we've already commented on!\n\n")
                    else:
                        bot.comment_medias(each)
                bot.comment_hashtag(line)

    else:
        print("\n\nYou didn't enter a valid number...\n\n")
