# "match" nos permite organizar bloques de codigo de forma que se ejecuten cuando se cumpla "x" condicion/caso.

tamaño_de_pija = int(input("Cuanto te mide la pija? : "))

match tamaño_de_pija:
    case 1:
        print("Pobre pibe")
    case 15:
        print("Muy bien nene, ya casi")
    case 18:
        print("Ufffff")
    case 20:
        print("El diablo...")
    case _:
        print("Me dio paja poner tantos tamaños, elegi los que hay papi") # _ vendria a ser "otro"