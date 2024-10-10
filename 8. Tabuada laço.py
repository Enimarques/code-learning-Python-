# TRABALHANDO COM MÓDULOS
# Formato básico: \033[<style>;<text_color>;<background_color>m
# Exemplo simples para mudar a cor do texto:

# Cores do Texto (Foreground):
print("\033[30mBlack\033[m")
print("\033[31mRed\033[m")
print("\033[32mGreen\033[m")
print("\033[33mYellow\033[m")
print("\033[34mBlue\033[m")
print("\033[35mMagenta\033[m")
print("\033[36mCyan\033[m")
print("\033[37mWhite\033[m")

# Background color example:
print("\033[41mRed Background\033[m")
print("\033[42mGreen Background\033[m")

n = int(input('Digite um numero: '))
for c in range(1, 11):
    print(f'O valor de \033[33m{n}*{c} é {n*c}')