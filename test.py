import os
import time
questions = [
    "1.) Euclidean algorithm",
    "2.) Tegsh untsugtiin talbai",
    "3.) Ugsun 2 toonii ihiig hewle",
    "4.) Ugsun 3 toonii ihiig hewle",
    "5.) Ugsun n toonii ihiig hewle",
    "6.) 1 + x/1! + x^2/2! + x^3/3! + ... + x^n / n!",
    "7.) A ^ k (A-ийн k зэрэгт) бодох.",
    "8.) Ugsun too 3d huwaagdah esehig shalga",
    "9.) 100 hurtelh toonii niilberig ol",
    "10.)Гараас өгсөн N тоо хүртэл тоонуудын нийлбэрийг олно.",
    "11.)Massive iin hamgiin ih gishuunig ol",
    "________garah bol 0________"
]
def _1():
    print(questions[1-1])
    a = int(input("ehnii toogoo oruulna uu\n"))
    b = int(input("2dahi toogoo oruulna uu\n"))
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    print("gcd ni ",max(a,b),"\n")
    time.sleep(2.8)
    print_questions()
def _2():
    print(questions[2-1])
    a = int(input("tegsh untsugtiin urt\n"))
    b = int(input("tegsh untsugtiin urgun\n"))
    print("tegsh untsugtiin talbai ni ",a*b,"\n")
    time.sleep(2.8)
def _3():
    print(questions[3-1])
    a = int(input("Ehnii too ni\n"))
    b = int(input("2dahi too ni\n"))
    print("ih too ni ", a*(a>b)+b*(b>=a), "\n")
    time.sleep(2.8)
    print_questions()
def _4():
    print(questions[4-1])
    a = int(input("Ehnii too ni\n"))
    b = int(input("2dahi too ni\n"))
    c = int(input("3dahi too ni\n"))
    b = a*(a>b)+b*(b>=a)
    print("ih too ni ", c*(c>b)+b*(b>=c), "\n")
    time.sleep(2.8)
    print_questions()
def _5():
    print(questions[5-1])
    n = int(input("heden too oruulah we ?\n"))
    m = 0
    for k in range (0, n, 1):
        print(k+1, "deh gishuunee oruulna uu")
        x = int(input())
        if m < x:
            m = x
    print("hamgiin ih too ni ",m,"\n")
    time.sleep(2.8)
    print_questions()
def _6():
    print(questions[6-1])
    print("hello6")
    time.sleep(2.8)
    print_questions()
def _7():
    print(questions[7-1])
    print("hello7")
    time.sleep(2.8)
    print_questions()
def _8():
    print(questions[8-1])
    print("hello8")
    time.sleep(2.8)
    print_questions()
def _9():
    print(questions[9-1])
    print("hello9")
    time.sleep(2.8)
    print_questions()
def _10():
    print(questions[10-1])
    print("hello10")
    time.sleep(2.8)
    print_questions()
def _11():
    print(questions[11-1])
    print("hello11")
    time.sleep(2.8)
    print_questions()

def print_questions():
    for i in range (0, len(questions),1):
        print(questions[i])
    n = input("\nBodlogiin dugaaraa oruulna uu\n")
    solver(n)
def xit():
    print("Duuslaa")
def solver(t):
    os.system('clear')
    if t == "0":
        xit()
    elif t=="1":
        _1()
    elif t=="2":
        _2()
    elif t=="3":
        _3()
    elif t=="4":
        _4()                           
    elif t=="5":
        _5()
    elif t=="6":
        _6()
    elif t=="7":
        _7()
    elif t=="8":
        _8()
    elif t=="9":
        _9()
    elif t=="10":
        _10()
    elif t=="11":
        _11()
    else:
        print("buruu utga")
        print("0-ees 11 hurtelh too oruulna uu")
        time.sleep(2.8)
        print_questions()
print_questions()