
def scanner(file):
    keywords = ["let","show","for","while","input","if","else","elif","then","end","do"]
    token = ""
    state = 0
    while True :
        pos = file.tell()  
        ch = file.read(1)
        if ch == "":
            break
        if state == 0: 
            print("state 0 running")            
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
                state = 2
        if state == 2:
            print("state 2 running")
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                state = 2
                token += ch 
                ch = file.read(1)
                while 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'or '0' <= ch <= '9':
                    state = 3
                    token += ch 
                print(f"{token}: identifier")
            else:
              state = 4
        if state == 4:
            print("state 4 running")
            if '0' <= ch <= '9':
                state = 5
                ch = file.read(1)
                token += ch
                while 0<= ch <=9:
                    state = 5
                    token += ch 
                print(f"{token}: number")
            else:
                token= ''
                state=6
        if state==6:
            if (ch=='+' or ch=='=' or ch=='*' or ch=='/'or ch=='-'or ch=='!' or ch=='%' or ch=='>'or ch=='<'):
                state = 6
        if state == 6:
            print("state 6 running")
            if (ch == '+' or ch == '=' or ch == '*' or ch == '/' or ch == '-' or ch == '%' or ch == '>' or ch == '<'):
                token += ch
                state = 7
                ch = file.read(1)
                if (ch=='+' or  ch=='*'or ch=='-' or ch=='='):
                    if token== ch:
                        state=8
                        token += ch
                        print(f"operator:{token}")
                elif (token == '+'or token== '-'or token == '!' and ch=='='):
                    state=8
                    token += ch
                    print(f"operator:{token}")
                elif token== '=' and (ch=='>' or ch=='<'):
                if (ch == '+' or  ch == '*' or ch == '-' or ch == '='):
                    if token == ch:
                        state = 8
                        token += ch
                        print(f"{token}: operator")
                elif token == '=' and (ch == '>' or ch == '<'):
                    state=8
                    token += ch
                    print(f"{token}: operator")
                print(f"{token}: operator")
            else:
                state = 10
                return 1
        if state == 10:
            print("state 10 running")
            if (ch=='{','}',')','(',':',';',','):
                state=11
                token += ch
                print(f"{token}: symbol")
        
    token=""

if __name__ == "__main__":
        with open("main.wepy", "r") as f:
            scanner(f)
    
            
                    
                    
            
            
