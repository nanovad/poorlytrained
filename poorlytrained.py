import markovify
import sys
import argparse
import configparser
import twitter

def main():
	arg_parser = argparse.ArgumentParser(description="Generate text with Markov chains based on a source corpus.")
	subparser = arg_parser.add_subparsers(dest="subparser_name")

	subparser_train = subparser.add_parser("train")
	subparser_train.add_argument("corpus", help="Path to a corpus to train with.")
	subparser_train.add_argument("savepath", help="Path to where to save the model, in JSON format.")

	subparser_tweet = subparser.add_parser("tweet")
	subparser_tweet.add_argument("corpus", help="Path to a corpus.")
	subparser_tweet.add_argument("modelpath", help="Path to a model built with \"train\"")

	args = arg_parser.parse_args()

	config = configparser.ConfigParser()
	config.read("poorlytrained.ini")
	twitter_consumer_key = config["keys"]["consumerkey"]
	twitter_consumer_secret = config["keys"]["consumersecret"]
	twitter_access_token = config["keys"]["accesstoken"]
	twitter_access_token_secret = config["keys"]["accesstokensecret"]

	if(args.subparser_name == "train"):
		with open(args.corpus) as f:
			text = f.read()

		text_model = markovify.Text(text)

		with open(args.savepath, "w") as f:
			f.write(text_model.chain.to_json())

	elif(args.subparser_name == "tweet"):
		with open(args.corpus) as corpus:
			with open(args.modelpath) as model:
				model_chain = markovify.Chain.from_json(model.read())
				text_model = markovify.Text(corpus.read(), 2, model_chain)

		tweet_message = text_model.make_short_sentence(140)
		print(tweet_message)
if __name__ == "__main__":
	main()
