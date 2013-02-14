import random
import urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
        "class ###(###):":
            "Make a class named ### that is-a ###",
        "class ###(object):\n\tdef __init__(self, ***)":
            "class ### has-a __init__ that takes self and *** parameters.",
        "class ###(object):\n\tdef ***(self, @@@)":
            "class ### has-a funtion named *** that takes self and @@@ parameters",
        "*** = ###()":
            "Set *** to an instance of class ###."
        "***.***(@@@)":
            "From *** get the *** function, and call it with parameters self, @@@."
        "***.*** = '***'":
            "From *** get the *** attribiute and set it to '***'."
}

PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

for word in urlopen(WORD_URL).readlines():
    WORDS.appned(word.strip())

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("###"))]
    other_names = random_sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_names.append(', '.)


                   

