"""define a word"""

from wordnik import swagger, WordApi
from config import apiKeys

def DefineWord(word):
    apiUrl = 'http://api.wordnik.com/v4'
    apiKey = apiKeys.WORDNIK
    client = swagger.ApiClient(apiKey, apiUrl)

    wordApi = WordApi.WordApi(client)

    try:
        definitions = wordApi.getDefinitions(word)

        if definitions is not None:
            print definitions[0].text
        else:
            print "Word not found"
    except Exception, e:
        print "Authentication Error"

