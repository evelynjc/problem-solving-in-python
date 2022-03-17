class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re, collections

        # filter non-word chars
        p = re.findall(r'\w+', paragraph.lower())
        # retrieve counts of each word in the list using Counter
        counted = collections.Counter([word for word in p if word not in banned])
        # reverse sort the result to get the most frequent word
        result = sorted(list(counted.items()), key = lambda x: x[1], reverse=True)

        return result[0][0]