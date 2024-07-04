# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

strs = 'abc'

def reverse_str(strs):
    reversed_str = ''
    # iterate over the string
    for i in range(len(strs)-1,-1,-1):
        reversed_str = reversed_str + strs[i]
    
    reversed_str = strs[::-1]
    
    return reversed_str

print(reverse_str(strs))
    
print("Try programiz.pro")

#
