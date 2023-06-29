from collections import defaultdict


def printAnagramsTogether(words):
    groupedWords = defaultdict(list)

    # Put all anagram words together in a dictionary
    # where key is sorted word
    for word in words:
        groupedWords["".join(sorted(word))].append(word)

    print(groupedWords)
    # Print all anagrams together
    res = []
    for group in groupedWords.values():
        print(res.append(sorted(group)))

    r

if __name__ == "__main__":
    arr = ["cat", "dog", "tac", "god", "act"]
    printAnagramsTogether(arr)
