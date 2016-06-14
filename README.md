# PoorlyTrained
### A Markov chain Twitter bot that can be trained on various source texts.

#### Installation
###### Download
Clone the repository:
`git clone https://github.com/nanovad/poorlytrained.git`  
Change to the repo directory:  
`cd poorlytrained`  
###### Initialize
Install the requirements:  
`sudo pip3 install -r requirements.txt`  
Set the API keys in poorlytrained.ini to your Twitter API keys.

#### Training
Training is accomplished by feeding the Markov chain a source text (reffered to as a 'corpus').  
The chain compiles the corpus into a 'model' (in JSON format) that can be used to generate text in the future.  
Create a model from "corpus.txt" and save to "model.json":

`python3 poorlytrained.py train corpus.txt model.json`

#### Running
First, you need to have set your API keys (See Installation) and trained a model (see Training).  
Generation requires both a corpus and a model.  
To generate some text using 'corpus.txt' and 'model.json':

`python3 poorlytrained.py tweet corpus.txt model.json`

PoorlyTrained also supports running without posting to Twitter. Simply add `--no-post` anywhere in the arguments, for example:

`python3 poorlytrained.py tweet --no-post corpus.txt model.json`
