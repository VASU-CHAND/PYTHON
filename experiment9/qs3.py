class A:
    def show(self):
        print("Class A")

class B(A):
    def show2(self):
        print("Class B")

obj = B()
obj.show()
obj.show2()