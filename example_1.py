
a = [1,2,3,4,4,5,5,6,7]
b = ['abc','xtz','aba','1212','zava']
data =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def sumaDatos(listNumbers):
    sumData = 0
    for i in range(0, len(listNumbers)):
        sumData += i
    return sumData

def multData(listNumbers):
    multData = 1
    for k in range(0, len(listNumbers)):
        multData *= listNumbers[k]
    return multData

def matchWords(words):
    counter = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            counter += 1
    return counter



sorted_list = sorted(
    data,
    key=lambda t: t[1]
)

print(sorted_list)
        
  
            



            
