import random

def generar_pass():
    
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z',]
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z',]  
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',]
    chars = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = mayus + minus + nums + chars

    contra = []

    for i in range(15):
        caracteres_random = random.choice(caracteres)
        contra.append(caracteres_random)
    contra = "".join(contra)
    return contra

def run():
    contra = generar_pass()
    print("tu nueva contraseña es  :  " + contra)





if __name__ == "__main__":
    run()