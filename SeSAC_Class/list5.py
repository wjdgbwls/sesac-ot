
#대문자로변환하시오p
text=input()

def convert_case(text):
    result=""
    
    for c in text:
      if c.isupper(): 
        result += c.lower()
      elif c.lower():
        result += c.upper()
      else:
         result += c


    return result

result=convert_case(text)



print("변환된 문장: ",result)