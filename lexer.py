
def scanner(file):
    keywords = ["let","show","for","while","input","if","else","elif","then","end","do"]
    token = ""
    state = 0
    while True :
        ch = file.read(1)
        if ch == "":
            break
        if state == 0: 
            print("state 0 running")              
            for i in range(len(keywords)):
                for j in range(len(keywords[i])):
                    print(f"cheking char {keywords[i][j]} in {keywords[i]}")
                    while ch == keywords[i][j]:  
                        print("ch matches")        
                        token += ch
                        ch = file.read(1)
                        print("reading next ch")
                        j+=1
                        state=1
                        break
                    else:
                        token = ""
                        break
            if token == keywords[i]:  
                print(f"{token}: keyword")
            else:
                state=2
        if state==2:
            if 'a'<= ch <= 'z' or 'A'<= ch <= 'Z':
                state=2
                token += ch 
                ch = file.read(1)
                while 'a'<= ch <= 'z' or 'A'<= ch <= 'Z'or 0<= ch <=9:
                    state=3
                    token += ch 
                 print(f"{token}:Identifier")
            else:
              state=4
        if state==4:
            if 0<= ch <=9:
                state=5
                ch = file.read(1)
                token +=ch
                while 0<= ch <=9:
                    state=5
                    token+= ch 
                print(f"{token}:Number")
            else:
                state=6
        if state==6:
            if (ch=='+' or ch=='=' or ch=='*' or ch=='/'or ch=='-' or ch=='%' or ch=='>'or ch=='<'):
                token += ch
                state=7
                ch = file.read(1)
                if (ch=='+' or  ch=='*'or ch=='-' or ch=='='):
                    if token== ch:
                        state=8
                        token += ch
                        print(f"operator:{token}")
                elif token== '=' and (ch=='>' or ch=='<'):
                    state=8
                    token += ch
                    print(f"operator:{token}")
                print(f"operator:{token}")
            else:
                state=10
                return 1
        if state==10:
            if (ch=='{','}',')','(',':',';',','):
                state=11
                token += ch
                print(f"symbol:{token}")
            else:
                break
        
    token=""

                


    # position = file.tell()  # ذخیرهٔ موقعیت فعلی
    # ch = file.read(1)       # خواندن یک کاراکتر
    # file.seek(position) # برگشت به موقعیت ذخیره‌شده
if __name__ == "__main__":
    with open("main.wepy", "r") as f:
        scanner(f)
    
            
                    
                    
            
            
