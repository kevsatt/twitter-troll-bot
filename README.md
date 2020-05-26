# twitter-troll-bot
Twitter troll bot that identifies a subject from a tweet and replies with a troll response.

The bot will send a text message to your cellular device when a tweet has been posted, when the bot has been started, and if there are any errors.

The NLP library spaCy is utilized to tokenize tweets and identify multiple subjects in a tweet. A naive subject selector chooses the best subject by finding which subject has the max length of characters between all of the subjects and filters subjects that you would not like to reply with. A generic "SMOKING" is used as the subject whenever the subject is returned as empty due to the filter.

# Prerequisites:
### A Twitter developer account. Instructions on how to get your API credentials can be found here:
  https://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/
### A Twilio account for sending text messages. Sign up here and get your API key:
  https://www.twilio.com/
