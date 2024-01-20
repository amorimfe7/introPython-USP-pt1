def soma (x,y):
    return x+y

print(soma(10,20))
print(soma(50,27))

def multiplica (x,y,z):
    return x*y*z

print(soma(10,40))
multiplica(soma(10,40),multiplica(10,20,30), soma(10,20)) #utilizei como parametro p/ função multiplica 3 funções
#1 função soma = x; 1 função multiplica =y; 1 função soma =z

#função sem parametro
def nome_do_time ():
    return "SPFC"

#função c/ print (sem return)
def timida ():
    x = 10 + 20
    print("O valor calculado é", x)

#função sem return
def silenciosa ():
    x = 10 + 20

