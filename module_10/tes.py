
def s_n_f():
    print(stc.plant)


class p:
    def n_f(self):
        print("norm plant")
    
    @staticmethod
    def s_n_f():
        print("stc plant")

obj = p() #instance of plant class | object plant

obj.n_f()
obj.s_n_f()


