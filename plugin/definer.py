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
        print definitions[0].text
    except Exception, e:
        print "Wordnik authentication error"

