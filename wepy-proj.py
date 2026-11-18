#lexical analyzer
def scanner(code.wepy):
    state=0
    keywords = {"let","show","for","while","input"}
    ch = code.wepy.read(1)
    x=[]
    while True :
        switch(state)
            case 0:
                for keyword in keywords:
                    if len(ch) == len(keyword):
                        for j in range(len(keyword)):
                            for i in range(len(ch)):
                                if ch[i]==keyword[j]:
                                    continue
                                else:
                                    break
                                i+=1
                            j+=1
                        if word==keyword: 
                            x.append(keyword) 
                    continue
                if len(x)> 0 :
                    state=1
                    print(f"word is keyword: {x}")
                else:
                    print("No keyword")
                    state=2
            case 2:
                if 'a'<= ch <= 'z' or 'A'<= ch <= 'Z':
                    state =3
                else:
                    state=4
            case 3:
                if 'a'<= ch <= 'z' or 'A'<= ch <= 'Z'or 0<= ch <=9:
                    state=3
                    print (f"identifier:{ch}")
                else:
                    state=4
                    return 1
            case 4:
                if (0<= ch <=9):
                    state=4 
                else:
                    state = 5
                    return 1
            case 4:
                for i in ch:
                    if 0<= ch <=9 :
                        state=4
                        continue
                        print("intiger:")
                else :
                    state=5
            case 5:
                if (ch=='+' or  ch=='*'or ch=='/' or ch=='-' or ch=='='):
                    if (ch=='+' or  ch=='*'or ch=='-' or ch=='='):
                        state=6
                        print("operator:")
                    print("operator:")
                else:
                    state=6
                    return 1
            case 6 :
                if (ch=='+' or  ch=='*' or ch=='-' or ch=='=')

            if state==7:
                if (ch=='{','}',')','(',':',';',',',)

            
            
                    
                    
            
            
