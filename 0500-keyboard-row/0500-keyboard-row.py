class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # initalize keyboards rows
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        res=[]
        for word in words:
            w=word.lower()  #change letter to lowerCase
            if len(set(row1 + w)) == len(row1) or len(set(row2+w))==len(row2) or len(set(row3+w))==len(row3):
                res.append(word)
        return res