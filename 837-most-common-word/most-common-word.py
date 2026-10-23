class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        '''
        Cases:
        Mixed cases in paragraph
        words ending punctuation
        words ending in spaces
        '''

        banned_set=set(banned)

        normal_str="".join(ch.lower() if ch.isalnum() else ' ' for ch in paragraph)
        word_counter={}

        for n_word in normal_str.split():
            if n_word not in banned_set:
                word_counter[n_word]=word_counter.get(n_word,0)+1

        curr_max=0
        max_word=''

        for word in word_counter:
            if word_counter[word]>curr_max:
                curr_max=word_counter[word]
                max_word=word
        
        return max_word

