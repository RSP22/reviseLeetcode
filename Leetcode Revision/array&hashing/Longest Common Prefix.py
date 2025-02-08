class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        firstString = strs[0]
        result = "" # empty string

        for i in range(len(firstString)):
            for s in strs:
                if i == len(s) or s[i] != firstString[i]: 
                #if str length 0 to n-1, if i reaches n, stop to avoid outofbound
                #so if index is at len(s) dont compare the 2 part
                    return result

            result += strs[0][i]

        return result
        '''
take the first string, flower, iterate to each of its characters and compare with
other string characters, f matched -> store in result, l matched -> append in result
i not matched -> return the result till now, which is "fl"

so idea is to iterate on the first string: which is strs[0]
strs[0][0] is 'f'
strs[0][1] is 'l'

while comparing, flower is larger in length than flow, so we can access out of bound character in shorter length string, so add condition to avoid. like index 4 of flower is e, but accessing s[4] in flow gives out of bound.
'''




    




