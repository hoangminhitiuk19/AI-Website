import spacy
from textblob import TextBlob
import logging
# from py2neo import Graph

nlp = spacy.load("en_core_web_sm")

# Comment out Neo4j related parts if not in use
# graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

def extract_entities(text):
    try:
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities
    except Exception as e:
        logging.error(f"Error extracting entities: {e}")
        raise RuntimeError(f"Error extracting entities: {e}")

def analyze_sentiment(text):
    try:
        blob = TextBlob(text)
        sentiment = blob.sentiment
        return sentiment
    except Exception as e:
        logging.error(f"Error analyzing sentiment: {e}")
        raise RuntimeError(f"Error analyzing sentiment: {e}")

def summarize_text(text):
    try:
        blob = TextBlob(text)
        sentences = blob.sentences
        summary = ' '.join(str(sent) for sent in sentences[:2])
        return summary
    except Exception as e:
        logging.error(f"Error summarizing text: {e}")
        raise RuntimeError(f"Error summarizing text: {e}")

def analyze_text(text):
    try:
        entities = extract_entities(text)
        sentiment = analyze_sentiment(text)
        summary = summarize_text(text)
        result = {
            "entities": entities,
            "sentiment": {
                "polarity": sentiment.polarity,
                "subjectivity": sentiment.subjectivity
            },
            "summary": summary
        }
        logging.info(f"Text analysis result: {result}")
        return result
    except Exception as e:
        logging.error(f"Error in text analysis: {e}")
        raise RuntimeError(f"Error in text analysis: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python text_analysis.py <text>")
        sys.exit(1)

    text = sys.argv[1]
    result = analyze_text(text)
    print(result)
