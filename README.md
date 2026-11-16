# O que é:
É um repositório com todas as minhas resoluções do módulo: Python Básico, da trilha UFPE.

## As pastas:
Cada pasta tem uma das três atividades e dentro tem a resolução de cada exercício em arquivos separados.

## O Projetinho:
Fiz uma agenda simples usando POO, com os seguintes métodos: adicionarEvento, removerEvento, relatorioDia, diaEvento, mostrarCalendario.

### O que cada método faz:
1. O adicionarEvento: segue o padrão a seguir, no qual 'evento' e 'dia' são strings:

``` python
self.adicionarEvento(evento, dia)
```

Ele adiciona um evento no seu calendário, a não ser que já exista um evento com mesmo nome no mesmo dia.

2. O removerEvento: segue o padrão a seguir, no qual 'evento' e 'dia' são strings:

``` python
self.removerEvento(evento, dia)
```

Ele remove um evento que ocorreria naquele dia, a não ser que não exista o evento, ou ele não exista naquele dia específico.

3. O relatorioDia: segue o padrão a seguir, no qual 'dia' é uma string:

``` python
self.relatorioDia(evento)
```

Printa uma lista com os eventos que ocorrem naquele dia