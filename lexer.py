
def scanner(file):
    keywords = ["let","show","for","while","input","if","else","elif","then","end","do"]
    token = ""
    state = 1
    while True :
        pos = file.tell()  
        ch = file.read(1)
        if ch == "":
            break
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
                    print(f"{token} : keyword")
                    break
            else:
                token = ''
                state = 2
        if state == 2:
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                state = 2
                token += ch 
                ch = file.read(1)
                while 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'or '0' <= ch <= '9':
                    state = 3
                    token += ch
                    ch = file.read(1) 
                print(f"{token}: identifier")
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
                token += ch
                ch = file.read(1)
                if (ch == '+' or  ch == '*' or ch == '-' or ch == '='):
                    if token == ch:
                        state = 8
                        token += ch
                        print(f"{token}: operator")
                elif (token == '+' or token == '-' or token == '!' and ch == '='):
                    state=8
                    token += ch
                    print(f"{token}: operator")
                elif token == '=' and (ch == '>' or ch == '<'):
                        state = 8
                        token += ch
                        print(f"{token}: operator")
                else:
                    print(f"{token } : operator")
                
            else:
                token = ''
                state = 10

                
        if state == 10:
            if (ch == '{' , '}' , ')' , '(' , ':' , ';' , ','):
                state = 11
                token += ch
                print(f"{token} : symbol")
            
            

        else:
            token=''
            state=1

if __name__ == "__main__":
        with open("main.wepy", "r") as f:
            scanner(f)
    
            
                    
                    
            
            
