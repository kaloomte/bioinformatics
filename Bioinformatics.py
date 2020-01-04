#!/usr/bin/env python
# coding: utf-8

# In[8]:


# sequence of ori region of Vibrio cholerae
# Copy your updated FrequentWords function (along with all required subroutines) below this line
def FrequentWords(Text, k):
    # your code here
    words = []
    freq = FrequencyMap(Text,k)
    m = max(freq.values())
    for key in freq:
          if freq[key] == m:
            pattern = key
            words.append(pattern)
    return words
def FrequencyMap(Text, k):
    # your code here.
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for i in range(n-k+1):
            if Text[i:i+k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq

# Now set Text equal to the Vibrio cholerae oriC and k equal to 10
Text= "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
k = 10

# Finally, print the result of calling FrequentWords on Text and k.
print(FrequentWords(Text,k))


# In[ ]:




