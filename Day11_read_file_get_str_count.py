

text = "string what is what in the text file, what, if, there, comma,"
text = text.replace(',', '')
text_list = text.split(" ")
print(text_list)
def count_str(text_list):
    count = 0
    for i in text_list:
        # print(i)
        if i == 'what':
            count +=1
    return count


print(count_str(text_list))
