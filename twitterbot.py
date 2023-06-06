import tweepy
import openai

AI_KEY = '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'
quote_key = 'X7TVTxa71QtTIfvrtaEUUg==IcJ5BldVQ0r6OvYg'
api_key = "Kbac48DDrpOyD02en72ELZL7z"
api_secret = "Tnu10IIzpGPSJ7PKUmY43sRBzbC9e1D3j0QMh4fZen0SqYv3im"
access_token = "1624851913345994753-96411rQhCbtICx3U0GFrsPaV2Da7BY"
access_token_secret = "aE2pW1TEJIjRXU2marMx1f2kn8PAFRmLqCz6qxvh89zoi"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAD1fnAEAAAAAe3GNoV5R9IxdAvVz%2Fszjtetu5bU%3DWAPm72xaY8r5Cac6IWGECrVhMCPkeYMQ7AqDS0IozHkQtdQCSz"

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

auth = tweepy.OAuth1UserHandler(api_key, api_secret,access_token, access_token_secret)
api = tweepy.API(auth)

openai.api_key = AI_KEY

# Define your prompt
prompt = "write a melancholic tweet about life, don't add any hashtags and try writing in no-caps"

# Call the API
response = openai.Completion.create(
  engine='text-davinci-003',
  prompt=prompt,
  max_tokens=100,
  n=1,
  stop=None,
  temperature=0.7
)

# Extract the generated text from the API response
generated_text = response.choices[0].text.strip()

print(generated_text)

tweet = client.create_tweet(
            text=generated_text
            )