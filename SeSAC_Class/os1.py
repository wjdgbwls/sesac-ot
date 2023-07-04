import os

current_dir=os.getcwd()
print("내 현재 폴더(디렉토리):",current_dir)


#for i in range(0,10):
#  os.rmdir('sesac_'+str(i)) 폴더 지우기

#python_path = os.getenv('PATH')
#print("윈도우 내의 PYTHONPATH 환경변수값 :" ,python_path) 환경변수 찾기

#os.system(dir)
my_commands=["crome","calc"]
for com in my_commands:
    os.system(com)