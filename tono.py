n = int(input())

lista = [1]

for x in range(n):
  if len(lista) >= n:
    pass
  else:
    value = 0 if lista[-1] == 1 or lista[-2] == 1 else 1
    lista.append(value)
lista = lista[::-1]
retorno = lista.index(1)

print("Player 1 wins!" if retorno != 0 else "Player 2 wins!")