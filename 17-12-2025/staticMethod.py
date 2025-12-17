class staticExample:
    @staticmethod
    def add(a,b):
        print("the addition is :",a+b)

st = staticExample()
st.add(10,20)
staticExample.add(30,40)