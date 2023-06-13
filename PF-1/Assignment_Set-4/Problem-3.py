#lex_auth_01269444890062848087

"""
Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers. 
Assume that the words contain only uppercase letters and the maximum word length is 10.
"""


def find_correct(word_dict):
    
    output=[0,0,0]
    for k, v in word_dict.items():
        if k==v:
            output[0]=output[0]+1
        elif len(k)!=len(v):
            output[2]=output[2]+1
        else:
            keys=word_dict.keys()
            values=word_dict.values()
            count=0
            for i in range(len(k)):
                if k[i]!=v[i]:
                    count+=1
            if count<=2:
                output[1]=output[1]+1
            else:
                output[2]=output[2]+1
    return output
                    
                        

word_dict={'MIND': 'MUND', 'ALWAYS': 'ALLISWELL', 'RADIO': 'RADICAL', 'VENDOR': 'VENDING', 'CHECK': 'CHEK'}
print(find_correct(word_dict))
