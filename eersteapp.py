import openai
from sklearn.metrics.pairwise import cosine_similarity


MODEL="text-embedding-ada-002"

openai.api_key = OPEN_AI_KEY

def createEmbedding(input):
    response = openai.Embedding.create(engine=MODEL, input=input)
    return (response.data[0].embedding)

text = "Johnny went to town on foot to buy a pizza and a beer"
search = ["animal", "food", "person"]

### Embeddings ophalen voor de search-array
needles = []
for t in search: needles.append(createEmbedding(t))

### Embeddings ophalen voor de tekst waarin gezocht moet worden
haystack = []
haystack.append(createEmbedding(text))


### Cosine similarities berekenen
similarities = cosine_similarity(haystack, needles)
print(similarities)

### Index vinden voor de meest overeenkomende
most_similar_index = similarities.argmax()
print(search[most_similar_index])