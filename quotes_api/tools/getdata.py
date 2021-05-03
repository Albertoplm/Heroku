from configuration import db, collection

def quotes():
    """
    Function that returns all quotes from an author
    """
    query = {}
    quotes = list(collection.find(query,{"_id": 0, "sentiment_compound":0}))
    return quotes

def authors():
    """
    Function that returns all authors from the database
    """
    query = {}
    quotes = list(collection.distinct("author"))
    return quotes

def tags():
    """
    Function that returns all authors from the database
    """
    query = {}
    quotes = list(collection.distinct("tag1") + collection.distinct("tag2") + collection.distinct("tag3") + collection.distinct("tag4") + collection.distinct("tag5") + collection.distinct("tag6"))
     #"tag2" and 'tag3' and 'tag4' and 'tag5' and 'tag6'))
    quotes = set(quotes)
    quotes = list(quotes)
    return quotes

def quotes_author(author):
    """
    Function that returns all quotes from an author
    """
    query = {"author": f"{author}"}
    quotes = list(collection.find(query,{"_id": 0, "sentiment_compound": 0}))
    return quotes


def quotes_tag(tag):
    """
    Function that returns all quotes from a tag
    """

    query = {'$or' : [{"tag1": f"{tag}"},
            {"tag2": f"{tag}"},
            {"tag3": f"{tag}"},
            {"tag4": f"{tag}"},
            {"tag5": f"{tag}"},
            {"tag6": f"{tag}"}]
            }
    tags = list(collection.find(query,{"_id": 0, "sentiment_compound":0}))
    return tags

def quotes_sentiment_gte(sentiment_compound):
    """
    Function that returns all quotes from an author
    """
    query = {"sentiment_compound": {"$gte": float(sentiment_compound)}}
    quotes = list(collection.find(query,{"_id": 0}))
    return quotes

def quotes_sentiment_lte(sentiment_compound):
    """
    Function that returns all quotes from an author
    """
    query = {"sentiment_compound": {"$lte": float(sentiment_compound)}}
    quotes = list(collection.find(query,{"_id": 0}))
    return quotes
