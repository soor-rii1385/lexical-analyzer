#lexical analyzer
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
                        i=0
                        j+=1
                        break
                    else:
                        token = ""
                        break
            if token == keywords[i]:  
                print(f"{token}: keyword")
            else:
                state=1
                    # case 1:
                    #     if 'a'<= ch <= 'z' or 'A'<= ch <= 'Z':
                    #         state =3
                    #     else:
                    #         state=4
                    # case 2:
                    #     if 'a'<= ch <= 'z' or 'A'<= ch <= 'Z'or 0<= ch <=9:
                    #         state=3
                    #         print (f"identifier:{ch}")
                    #     else:
                    #         state=4
                    #         return 1
                    # case 3:
                    #     if (0<= ch <=9):
                    #         state=4 
                    #     else:
                    #         state = 5
                    #         return 1
                    # case 4:
                    #     for i in ch:
                    #         if 0<= ch <=9 :
                    #             state=4
                    #             continue
                    #             print("intiger:")
                    #     else :
                    #         state=5
                    # case 5:
                    #     if (ch=='+' or  ch=='*'or ch=='/' or ch=='-' or ch=='='):
                    #         if (ch=='+' or  ch=='*'or ch=='-' or ch=='='):
                    #             state=6
                    #             print("operator:")
                    #         print("operator:")
                    #     else:
                    #         state=6
                    #         return 1
                    # case 6 :
                    #     if (ch=='+' or  ch=='*' or ch=='-' or ch=='=')

                    # if state==7:
                    #     if (ch=='{','}',')','(',':',';',',',)


    # position = file.tell()  # ذخیرهٔ موقعیت فعلی
    # ch = file.read(1)       # خواندن یک کاراکتر
    # file.seek(position) # برگشت به موقعیت ذخیره‌شده
if __name__ == "__main__":
    with open("main.wepy", "r") as f:
        scanner(f)
    
            
                    
                    
            
            
