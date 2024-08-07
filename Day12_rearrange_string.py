# Question:-2
# Given a string S with repeated characters. The task is to rearrange characters in a string such that no two adjacent characters are the same.

string = 'aaabc'
string = list(string)
print(string)
# Expected answer: acaba

def rearrange_str(arr):

    for i in range(len(arr)-1):
        print(arr[i])
        if arr[i] == arr[i+1]:
            for j in range(i+2,len(arr)):
                if arr[i] != arr[j]:
                    temp = arr[j]
                    arr[j] = arr[i+1]
                    arr[i+1] = temp
    output = arr
    output = ''.join(output)
    return output

print(rearrange_str(string))
