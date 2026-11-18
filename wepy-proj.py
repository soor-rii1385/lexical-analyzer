#lexical analyzer
def scanner(code.wepy):
    state=0
    keywords = {"let","show","for","while","input"}
    ch = code.wepy.read(1)
    while True :
        switch(state)
            case 0:
                
                for keyword in keywords:
                    for i=0 in keyword: 
                        if ch == keyword[i]:
                            i++
                        else
                            keyword++
                    state=0
                    print("keyword:" keywords[keyword])
                else:
                    state=1
            case 1:

                if 'a'<= ch <= 'z' or 'A'<= ch <= 'Z':
                    state =2
                else:
                    state=3
                    return 1
            case 2:
                if 'a'<= ch <= 'z' or 'A'<= ch <= 'Z'or 0<= ch <=9:
                    state=2
                    print ("identifier:"{ch})
                else:
                    state=3
                    return 1
            case 3:
                if (0<= ch <=9):
                    state=4
                    
                    
                else:
                    state = 5
                    return 1
            case 4:
                if 0<= ch <=9 :
                    state=4
                    print("intiger:")
                print ("int:")
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

            
            
                    
                    
            
            
