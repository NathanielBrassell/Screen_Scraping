import google, urllib
from bs4 import BeautifulSoup, SoupStrainer


def search_query(question):
    question_word= (question.split(" ")[0]).lower()
    print question
    content_words=" ".join(question.split(" ")[1:])
    g= google.search(content_words,num=5, stop=5)
    search_results=""
    only_p= SoupStrainer("p")
    for result in g:
        search_results += BeautifulSoup(urllib.urlopen(result),parse_only=only_p).get_text()
    print search_results
    response=""
    if question_word == "who":
        response = "who"#who(search_results)
    elif question_word == "where":
        response = "where"#where(search_results)
    elif question_word == "when":
        response = "when"#when(search_results)
    
    print question_word
    print content_words
    return response
        
        
