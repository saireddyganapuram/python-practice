class staticExample:
    @staticmethod
    def add(a,b):
        print("the addition is :",a+b)
    def add(self,a,b):
        print("the sum is :",a+b)
    
st = staticExample()
st.add(10,20)
staticExample.add(st,30,40)