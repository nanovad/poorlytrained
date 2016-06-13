import markovify
import sys
import argparse

def main():
	arg_parser = argparse.ArgumentParser(description="Generate text with Markov chains based on a source corpus.")
	subparser = arg_parser.add_subparsers(dest="subparser_name")

	subparser_train = subparser.add_parser("train")
	subparser_train.add_argument("corpus", help="Path to a corpus to train with.")
	subparser_train.add_argument("savepath", help="Path to where to save the model, in JSON format.")

	subparser_tweet = subparser.add_parser("tweet")
	subparser_tweet.add_argument("modelpath", help="Path to a model built with \"train\"")

	args = arg_parser.parse_args()

	if(args.subparser_name == "train"):
		with open(args.corpus) as f:
			text = f.read()

		text_model = markovify.Text(text)

		with open(args.savepath, "w") as f:
			f.write(text_model.chain.to_json())

	elif(args.subparser_name == "tweet"):
		pass
if __name__ == "__main__":
	main()