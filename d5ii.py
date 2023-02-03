def revi(money):
    print("give revi the sum of",money)
revi(50*2)
revi(50+2)

var='revi'
def show():
    global var1
    var1='tall'
    print("in function var cls",var)
show()
print("outside function",var1)
print("var is",var)

def outf():
    var=10
    def innf():
        var=20
        print("inner var",var)
    innf()
    print("outer var",var)
outf()    