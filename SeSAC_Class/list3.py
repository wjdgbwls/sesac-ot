print('hello')
words= ["apple","banana","cherry",'dragonfruit','egg']
short_words=[]
short_words=[word for word in words if len(word) <= 3]
print(short_words)