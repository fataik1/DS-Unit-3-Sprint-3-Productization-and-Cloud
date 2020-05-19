import basilica

BASILICA_API_KEY = '45ece93b-eb6f-0ab5-cf67-cb889d63200f'

connection - Connection(BASILICA_API_KEY)
print(type(connection))



embeddings = connection.embed_sentence
print(embeddings)

sentences = [
    "This is a sentence!",
    "This is a similar sentence!",
    "I don't think this sentence is very similar at all...",
]
with basilica.Connection(BASILICA_API_KEY) as c:
    embeddings = list(c.embed_sentences(sentences))






sentences = [
    "This is a sentence!",
    "This is a similar sentence!",
    "I don't think this sentence is very similar"
]

embeddings = list(connection.embed_sentences(sent
for embedin))