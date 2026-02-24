#!/usr/local/bin/python3

# Function cosine_similarity
def cosine_similarity(a,b):
    ## Inline function dot calculation
    def dot(A,B): return (sum(a*b for a,b in zip(A,B)))
    return dot(a,b) / ( (dot(a,a) ** .5) * (dot(b,b) ** .5) )

hans = [0.45, 0.8]
piet = [-0.1, -0.3]
anna = [0.6, 0.2]

print("Hans - Piet  :", cosine_similarity(hans,piet))
print("Hans - Anna  :", cosine_similarity(hans,anna))
