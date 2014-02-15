"""define a word"""

from wordnik import swagger, WordApi

def DefineWord(word):
    apiUrl = 'http://api.wordnik.com/v4'
    apiKey = 'YOUR_WORDNIK_API_KEY'
    client = swagger.ApiClient(apiKey, apiUrl)

    wordApi = WordApi.WordApi(client)

    try:
        definitions = wordApi.getDefinitions(word)
        print definitions[0].text
    except Exception, e:
        print "Could not find word"

