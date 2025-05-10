class compu:
    def __init__(self, marca, procesador, memoria, sistema_operativo):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.sistema_operativo = sistema_operativo

    def imprimir(self):
        print(
            f"computador marca {self.marca} y su procesador es {self.procesador} y su capacidad de memoria es {self.memoria} y con sistema operativo{self.sistema_operativo}"
        )


compu1 = compu("hp", "intel core 5", "250", "windows")
compu2 = compu("lenovo", "intel core 3", "250", "linux")
compu3 = compu("macbook", "ryzen", "250", "iOs")

compu2.imprimir()
