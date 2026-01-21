
def mostWordsFound(sentences: list[str]) -> int:
    res = 0
    for w in sentences:
        res = max(len([s for s in w.split(' ')]), res)
    return res
            
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(mostWordsFound(sentences))