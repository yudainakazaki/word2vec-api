import torch
import torchtext

def calcEmbed(word):
    glove = torchtext.vocab.GloVe(name="6B", dim=50)
    wordArray = word.split(" ")
    res = glove[""].unsqueeze(0)
    for w in wordArray:
        val = glove[w].unsqueeze(0)
        res += val
    return res

def getSimilarity(word1, word2):
    sim = torch.cosine_similarity(calcEmbed(word1), calcEmbed(word2))
    return sim.item()
