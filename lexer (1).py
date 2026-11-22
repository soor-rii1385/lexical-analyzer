"""
تحلیل‌گر لغوی زبان Wepy (مبتنی بر DFA)

انواع توکن: keyword, identifier, number, string, operator, symbol
قالب خروجی هر توکن:   مقدار: نوع

حالت‌ها:
  0  : شروع
  1  : شناسه / کلیدواژه                (final)
  2  : عدد صحیح                        (final)
  3  : =                               (final, operator)
  4  : ==                              (final, operator)
  5  : !                               (غیر final، فقط با = معتبر است)
  6  : !=                              (final, operator)
  7  : + - * / < >                     (final, operator)
  8  : ; , ( ) :                       (final, symbol)
  9  : داخل رشته (بعد از " باز)        (غیر final)
  10 : رشته‌ی بسته‌شده                  (final, string)

انتقال‌ها:
  0 --فاصله/تب/خط جدید--> 0
  0 --حرف--> 1            1 --حرف یا رقم--> 1
  0 --رقم--> 2            2 --رقم--> 2
  0 --'='--> 3            3 --'='--> 4
  0 --'!'--> 5            5 --'='--> 6
  0 --'+' '-' '*' '/' '<' '>'--> 7
  0 --'; , ( ) :'--> 8
  0 --'"'--> 9            9 --هر کاراکتر جز " و خط جدید--> 9
                          9 --'"'--> 10
  بقیه‌ی انتقال‌ها وجود ندارند:
    - حالت final  : توکن چاپ می‌شود، به حالت 0 می‌رویم و کاراکتر فعلی دوباره بررسی می‌شود
    - حالت 5      : خطای لغوی (! به‌تنهایی مجاز نیست)
    - حالت 9      : خطای لغوی (رشته‌ی بسته‌نشده)
    - حالت 0      : خطای لغوی (کاراکتر غیرمجاز)
"""

import sys


def lexer(file):
    # فقط کلیدواژه‌ها حق استفاده از لیست دارند
    keywords = ["let", "show", "for", "while", "input", "if", "else", "elif", "then", "end", "do"]

    state = 0
    token = ""
    line = 1            # شماره‌ی خط کاراکتر فعلی
    token_line = 1      # شماره‌ی خط شروع توکن (برای گزارش خطا)
    has_error = False

    ch = file.read(1)   # lookahead: کاراکتری که هنوز پردازش نشده

    while True:
        nxt = -1        # -1 یعنی انتقالی وجود ندارد (dead)

        # ---------- تابع انتقال ----------
        if state == 0:
            if ch == ' ' or ch == '\t' or ch == '\n' or ch == '\r':
                nxt = 0
            elif 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                nxt = 1
            elif '0' <= ch <= '9':
                nxt = 2
            elif ch == '=':
                nxt = 3
            elif ch == '!':
                nxt = 5
            elif ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '<' or ch == '>':
                nxt = 7
            elif ch == ';' or ch == ',' or ch == '(' or ch == ')' or ch == ':':
                nxt = 8
            elif ch == '"':
                nxt = 9
        elif state == 1:
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' or '0' <= ch <= '9':
                nxt = 1
        elif state == 2:
            if '0' <= ch <= '9':
                nxt = 2
        elif state == 3:
            if ch == '=':
                nxt = 4
        elif state == 5:
            if ch == '=':
                nxt = 6
        elif state == 9:
            if ch == '"':
                nxt = 10
            elif ch != "" and ch != '\n' and ch != '\r':
                nxt = 9
        # حالت‌های 4، 6، 7، 8 و 10 انتقال خروجی ندارند

        # ---------- اجرای انتقال ----------
        if nxt != -1:
            if state == 0 and nxt != 0:
                token_line = line               # شروع یک توکن جدید
            if not (state == 0 and nxt == 0):   # فاصله وارد توکن نمی‌شود
                token += ch
            if ch == '\n':
                line += 1
            state = nxt
            ch = file.read(1)

        else:
            if state == 0:
                if ch == "":                    # پایان فایل
                    break
                print(f"Lexical error at line {line}: invalid character '{ch}'")
                has_error = True
                ch = file.read(1)

            elif state == 5:
                print(f"Lexical error at line {token_line}: '!' must be followed by '='")
                has_error = True
                token = ""
                state = 0

            elif state == 9:
                print(f"Lexical error at line {token_line}: unclosed string {token}")
                has_error = True
                token = ""
                state = 0

            else:
                # حالت پایانی: توکن را گزارش می‌کنیم (ch مصرف نمی‌شود)
                if state == 1:
                    if token in keywords:
                        print(f"{token}: keyword")
                    else:
                        print(f"{token}: identifier")
                elif state == 2:
                    print(f"{token}: number")
                elif state == 8:
                    print(f"{token}: symbol")
                elif state == 10:
                    print(f"{token}: string")
                else:                           # حالت‌های 3، 4، 6، 7
                    print(f"{token}: operator")
                token = ""
                state = 0

    return not has_error


def main():
    path = "main.wepy"
    if len(sys.argv) > 1:
        path = sys.argv[1]

    if not path.endswith(".wepy"):
        print("Error: input file must have the .wepy extension")
        sys.exit(1)

    try:
        with open(path, "r", encoding="utf-8") as f:
            lexer(f)
    except FileNotFoundError:
        print(f"Error: file '{path}' not found")
        sys.exit(1)


if __name__ == "__main__":
    main()
