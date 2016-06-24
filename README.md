# PoorlyTrained
### A Markov chain Twitter bot that can be trained on various source texts.

#### Installation
###### Download
Clone the repository:
`git clone https://github.com/nanovad/poorlytrained.git`  
Change to the repo directory:  
`cd poorlytrained`  
###### Initialize
Install virtualenv:  
`sudo pip3 install virtualenv`

Create a new virtual environment for the bot, using Python3:  
`virtualenv --python=python3 env`

Activate the environment:  
`source env/bin/activate`

Install the requirements:  
`pip install -r requirements.txt`  

Deactivate the environment:  
`deactivate`
#### Configuration
A few different settings can be tweaked in the configuration file (poorlytrained.ini).  
The most important of these are the Twitter API keys. Without them, the bot will not be able to post to Twitter.  
These values **must** be set before you attempt to tweet. You can find these after creating an app at https://apps.twitter.com.  
Just fill these values in in the \[keys\] section of poorlytrained.ini.  

There are also values that can tweak Markov chain behavior (these are stored in a section titled \[markov\].)  
Currently, the only value in this section is `modeldepth`, which configures the Markov chain model depth.

#### Training
Training is accomplished by feeding the Markov chain a source text (reffered to as a 'corpus').  
The chain compiles the corpus into a 'model' (in JSON format) that can be used to generate text in the future.  
Create a model from "corpus.txt" and save to "model.json":

`env/bin/python poorlytrained.py train corpus.txt model.json`

#### Running
First, you need to have set your API keys (See Installation) and trained a model (see Training).  
Generation requires both a corpus and a model.  
To generate some text using 'corpus.txt' and 'model.json':

`env/bin/python poorlytrained.py tweet corpus.txt model.json`

PoorlyTrained also supports running without posting to Twitter. Simply add `--no-post` anywhere in the arguments, for example:

`env/bin/python poorlytrained.py tweet --no-post corpus.txt model.json`
