sentense ="Hello,world!"

def count_char(input_char):
    count=0
    for char in sentense:
        if char.upper() == input_char.upper():
            count += 1
        elif char.lower() == input_char.lower():
            count += 1
        else:
            continue
    return count
char='H'
count=count_char(char)
print(f"글자 {char} 갯수 :{count}")