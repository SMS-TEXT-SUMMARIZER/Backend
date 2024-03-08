import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
from spacy import displacy


async def extract_entities(text):
    nlp = spacy.load('en_core_web_md')
    doc = nlp(text)
    # print(nlp.pipe_names)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    # print(entities)
    # displacy.render(doc, style="ent", jupyter=True)
    return entities


async def summarizer(rawdocs):
    stop_words = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_md')
    doc = nlp(rawdocs)

    # Extract entities
    entities = await extract_entities(rawdocs)
    print(entities)

    # Convert entities to lowercase for easier matching
    entity_tokens = [entity[0].lower() for entity in entities]

    # Filter out stop words and punctuation
    word_freq = {}
    for word in doc:
        if word.text.lower() not in stop_words and word.text.lower() not in punctuation:
            if word.text.lower() not in entity_tokens:  # Exclude entities
                if word.text not in word_freq.keys():
                    word_freq[word.text] = 1
                else:
                    word_freq[word.text] +=1

    max_freq = max(word_freq.values())

    for word in word_freq.keys():
        word_freq[word] = word_freq[word] / max_freq

    sent_tokens = [sent for sent in doc.sents]

    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]
    # print(sent_scores)
    select_len = int(len(sent_tokens) * 0.6)
    summary = nlargest(select_len, sent_scores, key=sent_scores.get)
    print(summary)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    print(summary)
    return summary


