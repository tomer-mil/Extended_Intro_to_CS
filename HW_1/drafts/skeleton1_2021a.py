#Skeleton file for HW1 - Winter 2021 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.

#Change the name of the file to include the ID number of the student submitting the solution (hw1_ID.py).

#Enter all IDs of participating students as strings, separated by commas.
#The first ID should be the ID of the student submitting the solution
#For example: SUBMISSION_IDS = ["123456000", "987654000"]
SUBMISSION_IDS = []

#Question 4a
def max_word_len(text):
    pass #replace with your implementation    

#Question 4b
def frequent_word(text):
    pass #replace with your implementation    

#Question 4c
def vc_ratio(text):
    pass #replace with your implementation    

#Question 5
def calc(expression):
    pass #replace with your implementation


#Question 6
def max_div_seq(n, k):
    pass #replace with your implementation


########
# Tester
########

def test():
    #testing Q4
    st = "the quick brown fox jumps over the lazy dog"
    if max_word_len(st) != 5:
        print("Error in max_word_len")
    if frequent_word(st) != "the":
        print("Error in frequent_word")
    if vc_ratio(st) != 11/24:
        print("Error in vc_ratio")

    #testing Q5
    if calc("2 ** 2 ** 2 ** 2") != 256:
        print("Error in calc")
    if calc("20 // 3") != 6:
        print("Error in calc")
        
    #testing Q6
    l = max_div_seq(23300247524689, 2)
    if l != 4:
        print("Error in max_div_seq")

    if not SUBMISSION_IDS:
        print("The list of IDs is empty")
        
    if not type(SUBMISSION_IDS) == list:
        print("The list of IDs is not a list type")

    if SUBMISSION_IDS and not all(type(x)==str for x in SUBMISSION_IDS):
        print("The list of IDs contains elments that are not strings")

   
