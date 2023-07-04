'''with open("names.txt", "r") as file: #r=read ,w = write ,a = append  whit as 는 내가 연파일을 =file이라고 부르겠다
    names= file.read()
    print(names)
'''
with open("names.txt", "r") as file: #r=read ,w = write ,a = append  whit as 는 내가 연파일을 =file이라고 부르겠다
    names= file.readlines()
    for item in names:
        print(item)

