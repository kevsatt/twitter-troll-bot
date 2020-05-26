# twitter-troll-bot

**THIS PROJECT WAS MEANT AS A FUN PROJECT TO TROLL MY FRIENDS. PLEASE DO NOT USE THIS MALICIOUSLY.**

Twitter troll bot that identifies a subject from a tweet and replies with a troll response. The bot watches a targeted Twitter user's account and replies whenever a new tweet is tweeted instantaneously. Personally, I have deployed this on a Raspberry Pi 3.

The bot will send a text message to your cellular device when a tweet has been posted, when the bot has been started, and if there are any errors.

The NLP library spaCy is utilized to tokenize tweets and identify multiple subjects in a tweet. A naive subject selector chooses the best subject by finding which subject has the max length of characters between all of the subjects and filters subjects that you would not like to reply with. A generic "SMOKING" is used as the subject whenever the subject is returned as empty due to the filter.

# Prerequisites:
1. A Twitter account and Twitter developer account. Instructions on how to get your API credentials can be found [here](https://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/).
2. A Twilio account for sending text messages. Sign up [here](https://www.twilio.com) and get your API key.
  
# Limitations:
1. The account to be followed cannot be private. If the account is private, then the user will have to allow the bot to follow them in order to allow the bot to read the user's tweets via a stream listener.
2. If the followed account has "protected tweets", the bot will not work. The stream will run but the bot will not be able to pick up any new tweets.

# IF YOU ARE DEPLOYING THIS ON A RASPBERRY PI
Most Raspbian OS are 32-bit, this causes problems with a regular spaCy package install since it is only compatible with 64-bit OS. Thankfully, a user on StackOverflow pre-compiled a 32-bit version of spaCy for us to work with. Details can be found [here](https://stackoverflow.com/questions/59927844/is-it-possible-to-install-spacy-to-raspberry-pi-4-raspbian-buster).
