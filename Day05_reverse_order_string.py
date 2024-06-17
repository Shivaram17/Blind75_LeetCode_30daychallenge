# reverse order string
sentence = "This is Coders"

def reverse_string(sentence):
  list_sort = []
  sentence = sentence.split(" ")
  while (len(sentence)) > 0:
    word = sentence.pop()
    list_sort.append(word)

  return " ".join(list_sort)

reverse_string(sentence)
