class Votante:

    def __init__(self, sexo, num_cuenta):
        self.__votos = 5
        self.__sexo = sexo
        self.__ya_voto = False
        self.__num_cuenta = num_cuenta

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def puede_votar(self):
        if self.get_ya_voto():
            print("Ya no tienes votos disponibles")

        else:
            print(f"Dispones de {self.__votos} votos todavia")

    def votar(self, cantidad_votos):
        if self.__ya_voto:
            print("Esta persona ya voto")
            return

        if cantidad_votos > self.__votos:
            print("No dispones de los votos necesarios")

        elif cantidad_votos <= self.__votos:
            self.__votos -= cantidad_votos
        else:
            self.set_ya_voto()
            print("Ya no tienes votos disponibles")
        if self.__votos <= 0:
            self.set_ya_voto(True)

    def set_ya_voto(self, voto):
        self.__ya_voto = voto

    def get_ya_voto(self):
        return self.__ya_voto

    def get_votos(self):
        return self.__votos

    def get_sexo(self):
        return self.__sexo

    def get_num_cuenta(self):
        return self.__num_cuenta

    def __str__(self):
        return f"""
        Votos restantes {self.__votos}
        Sexo {self.__sexo}
        Ya voto {self.__ya_voto}"""


def menu_principal():
    print("ENCUESTA PREFERENCIA ELECCIONES")
    print("Elige la opcion que prefieras")
    print("1 - Iniciar una votacion")
    print("2 - Salir")


def menu_partidos():
    print("Elige el partido al que quieres votar preferencia")
    print("1 - Rojo")
    print("2 - Naranja")
    print("3 - Verde")


def verificar_opcion(opcion):
    match opcion:
        case "1":
            print("\tElegiste rojo")
            return 1
        case "2":
            print("\tElegiste naranja")
            return 2
        case "3":
            print("\tElegiste verde")
            return 3
        case _:
            print("\t\tOpcion no valida")
            return 4


def ver_opc_menu_princ(opcion):
    match opcion:
        case "1":
            print("Iniciando Votacion...")
            return 1
        case "2":
            print("Saliendo...")
            return 2
        case _:
            print("Opcion no valida")
            return 4


def ganador(rojo, verde, naranja):
    max_valor = max(rojo, naranja, verde)

    ganadores = [color for color in ['Rojo', 'Naranja', 'Verde'] if eval(color.lower()) == max_valor]

    if len(ganadores) == 1:
        return f"{ganadores[0]} es el ganador"
    else:
        return f"Empate entre: {', '.join(ganadores)}"


def porcentaje_aparicion_letras_m_f(lista):
    if not lista:
        return 0, 0

    total_letras = len(lista)

    conteo_m = lista.count('H')
    conteo_f = lista.count('M')

    porcentaje_H = (conteo_m / total_letras) * 100
    porcentaje_M = (conteo_f / total_letras) * 100

    return porcentaje_H, porcentaje_M


def es_numerico(entrada):
    if entrada.isdigit():
        return True
    else:
        try:
            float(entrada)
            return True
        except ValueError:
            return False


def main():
    while True:
        menu_principal()
        opcion_m_p = input("Introduce tu opcion: ")
        op_ver = ver_opc_menu_princ(opcion_m_p)
        while op_ver == 4:
            op_ve = input("Introduce tu opcion: ")
            op_ver = ver_opc_menu_princ(op_ve)
        if op_ver == 2:
            break
        rojo = 0
        naranja = 0
        verde = 0
        sexos = []
        lista_votantes = []
        print("¿Cuantas personas van a ser encuestadas?")
        print("La encuesta solo permite un minimo de 5 participantes y un maximo de 100")
        numero_personas = input("Numero de personas: ")
        while True:
            if es_numerico(numero_personas):
                if 5 <= int(numero_personas) <= 100:
                    break
                else:
                    print("Introduce un valor correcto")
                    print("La encuesta solo permite un minimo de 5 participantes y un maximo de 100")
                    numero_personas = input("Numero de personas: ")
            else:
                print("Introduce un valor numerico correcto")
                numero_personas = input("Numero de personas: ")

        personas = int(numero_personas)
        turno = 1
        while personas > 0:
            print(f"Eres el encuestado numero {turno}")
            num_cuenta = input("Ingresa tu numero de cuenta: ")
            while True:
                if es_numerico(num_cuenta):
                    if len(num_cuenta) == 4:
                        int(num_cuenta)
                        break
                    else:
                        print("La entrada no es valida")
                        print("El numero de cuenta son 4 digitos")
                        num_cuenta = input("Ingresa tu numero de cuenta: ")
                else:
                    print("La entrada no es valida")
                    print("El numero de cuenta son 4 digitos")
                    num_cuenta = input("Ingresa tu numero de cuenta: ")

            if num_cuenta in lista_votantes:
                print(f"El usuario con el numero de cuenta {num_cuenta} ya voto")
                print("Pase el siguiente usuario")
            else:
                print("Ingresa tu sexo")
                sexo = input("M -> Mujer , H -> Hombre : ").upper()
                while sexo != "M" and sexo != "H":
                    print("Dato no valido, intenta nuevamente")
                    print("Ingresa tu sexo")
                    sexo = input(" M -> Mujer , H -> Hombre : ").upper()

                votante = Votante(sexo, num_cuenta)
                sexos.append(votante.get_sexo())
                menu_partidos()
                while votante.get_votos() > 0:
                    print(f"Tienes {votante.get_votos()} votos restantes")
                    opcion = input("Introduce tu opcion: ")
                    voto = verificar_opcion(opcion)
                    match voto:
                        case 1:
                            rojo += 1
                            votante.votar(1)
                        case 2:
                            naranja += 1
                            votante.votar(1)
                        case 3:
                            verde += 1
                            votante.votar(1)
                        case 4:
                            print("Revisa las opciones")
                personas -= 1
                lista_votantes.append(votante.get_num_cuenta())
                turno += 1

        print("\t###------------### Resultados de la Encuesta ###------------###\n")
        resultado = ganador(rojo, verde, naranja)
        print(f"\t\t\t######### {resultado.upper()} #########")

        print(f"""Los votos fueron
            Rojo:       {rojo}
            Naranja:    {naranja}
            Verde       {verde}\n""")

        hombres, mujeres = porcentaje_aparicion_letras_m_f(sexos)
        print("\t###------------### Participacion en la Encuesta ###------------###\n")
        print(f"\t\t\tNumero total de participantes: {len(lista_votantes)}")
        print(f"""
            -----------------------------------------------------
            Hombres: {hombres} % con {sexos.count("H")} participantes
            Mujeres: {mujeres} % con {sexos.count("M")} participantes
            -----------------------------------------------------\n\n""")


if __name__ == '__main__':
    main()
