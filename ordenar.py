class ListaNum:

    #declarar constructor
    def __init__(self ) -> None: 
        self.listaNum = []

    #declarar metodos
    
    def ordenar(self):
        pares = []
        impares =[]
        tamanio = int(input("Dame la cantidad de numeros a ingresar: "))
        for i in range(tamanio):
            numeros =int(input(f"Ingresa el numero {i+1}: "))
            self.listaNum.append(numeros)
            self.listaNum.sort()
            
            if self.listaNum.count(numeros) > 1:
                repetidos = []
                repetidos.append(numeros)
                print(f"El numero {numeros} se repite {self.listaNum.count(numeros)} veces")

            if numeros%2 == 0:
                if numeros in pares:
                    pass
                else:
                    pares.append(numeros)
            else:
                if numeros in impares:
                    pass
                else:
                    impares.append(numeros)
                
        print(self.listaNum)
        print(f"Los numeros pares son: {pares}")
        print(f"Los numeros impares son: {impares}")
        
def main():
    obj = ListaNum()
    obj.ordenar()
    

if __name__ == "__main__":
    main() 

