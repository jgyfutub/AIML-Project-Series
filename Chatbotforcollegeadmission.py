import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('punkt')
nltk.download('wordnet')

f = open('admission_prospectus_2022.txt', 'r', errors='ignore')
raw = f.read()
raw = raw.lower()


tokens = nltk.sent_tokenize(raw) #converts to list of scentences
word_tokens = nltk.word_tokenize(raw) #converts to list of words

# sentToken = sent_tokens[:4]
#print(sentToken)
wordToken = word_tokens[:4]
#print(wordToken)

#preprocessing 
lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormal(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


def response(response):
    chatbot_response = ''
    tokens.append(response)
    TfidfVec=TfidfVectorizer(tokenizer=LemNormal,stop_words="english")
    tfidf=TfidfVec.fit_transform(tokens)
    vals=cosine_similarity(tfidf[-1],tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf == 0):
        chatbot_response = chatbot_response + "I am sorry! I don't understand you"
    else:
        chatbot_response=chatbot_response+tokens[idx]

    tokens.pop()
    tokens.append("What did I asked = "+response+" What you replied = "+chatbot_response)
    return chatbot_response
    
    

flag=True
print("Hello I am your admission helping bot!!.Ask me anything related to the admission process.If you want to quit say bye!!")
while(flag):
    userinput=input("")
    if userinput.lower()!='bye':
        print(response(userinput))
        continue
    else:
        print("Ok!!Bye!!")
        break


