class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
            anagrams = {}
            for word in strs:
                 form = ''.join(sorted(word))
                 if form in anagrams:
                    anagrams[form].append(word)
                 else:
                     anagrams[form] = [word]
       

        
            return list(anagrams.values())

       
           




    
    