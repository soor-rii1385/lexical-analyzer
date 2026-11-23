
def scanner(file):
    keywords = ["let","show","for","while","input","if","else","elif","then","end","do"]
    token = ""
    state = 1
    while True :
        pos = file.tell()  
        ch = file.read(1)
        if ch == "":
            break
        if ch == ' ':
            print("saw space")
        if state == 1:    
            for i in range(len(keywords)):    
                for j in range(len(keywords[i])):
                    while  ch == keywords[i][j]:    
                        token += ch
                        ch = file.read(1)
                        break
                    else:
                        token = ""
                        file.seek(pos)
                        ch = file.read(1)
                        break
                if token == keywords[i]: 
                    print(f"{token}: keyword")
                    break
            else:
                token = ''
                state = 2
        if state == 2:
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                if ch=="x":
                    print ("kn b mn bgooooooooooooooooooooooo")
                state = 3
                token += ch 
                ch = file.read(1)
                while 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'or '0' <= ch <= '9':
                    state = 3
                    token += ch
                    ch = file.read(1)
                    
                else:
                    print(f"{token}: identifier")
                    token=''
                    state=4
            else:
              token = ''
              state = 4
        if state == 4:  
            if '0' <= ch <= '9':
                state = 5
                token += ch
                ch = file.read(1)
                while '0' <= ch <= '9':
                    state = 5
                    token += ch 
                    ch = file.read(1)
                print(f"{token}: number")
            else:
                token = ''
                state = 6
        if state == 6:
            if (ch == '+' or ch == '=' or ch == '*' or ch == '/' or ch == '-' or ch == '%' or ch == '>' or ch == '<'):
                state = 7
                token+=ch
                pos = file.tell() 
                ch = file.read(1)                
                if (ch == '+' or  ch == '*' or ch == '-' or ch == '='):
                    if token == ch:
                        state = 8
                        token += ch
                        print(f"{token}: operator")
                    elif ch == '=' and token in ('+', '-', '!'):
                        state=8
                        token += ch
                        print(f"{token}: operator")
                elif token == '=' and (ch == '>' or ch == '<'):
                    state = 8
                    token += ch
                    print(f"{token}: operator")
                elif state==7:
                    if(token== '+' or token == '=' or token == '*' or token== '/' or token == '-' or token== '%' or token == '>' or token == '<'):
                        print(f"{token }: operator")
                file.seek(pos)          
            else:
                token = ''
                state = 10
        if state == 10:
            if (ch == '{' or ch=='(' or ch==':' or ch==';' or ch==','):
                state = 11
                token += ch
                print(f"{token} : symbol")
                ch = file.read(1)
                if (ch== ')'or ch == '}' ):
                    token=''
                    token+= ch
                    print(f"{token} : symbol")
            else:
                token = ''
                state = 1
        else:
            token = ''
            state = 1

if __name__ == "__main__":
        with open("main.wepy", "r") as f:
            scanner(f)
    
            
                    
                    
            
            
