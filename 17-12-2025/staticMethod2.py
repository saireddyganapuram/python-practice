class staticExample:
    @staticmethod
    def _add(a,b):
        print("the addition is :",a+b)

st = staticExample()
st._add(10,20)
staticExample._add(30,40)