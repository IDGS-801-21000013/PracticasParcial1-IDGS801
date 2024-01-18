class piramide:
    #declarar propiedades
    x=0
    y=0
    #declarar constructor
    def __init__(self, a, b) -> None:
        self.x=a
        self.y=b
    #declarar metodos
    def crearPiramide(self):
        for i in range(self.x):
            for j in range(i+1):
                print(self.y, end="")
            print("")

def main():
    obj=piramide(5, "*")
    obj.crearPiramide() 

if __name__ == "__main__":
    main()           