def convert(msg):
    link = 'https://twitter.com'
    list = msg.split(' ')
    for word in list:
        if link in word:
            var = word
            
    list1=[]
    list1[:0] = var
    list1.insert(8, 'f')
    list1.insert(9, 'x')
    list1 = ''.join(list1)

    return list1
 