from controladorElevador import ControladorElevador

controlador = ControladorElevador()

controlador.inicializarElevador('erro', 10, 6, 1)
controlador.subir()
print(controlador.elevador.andarAtual)
