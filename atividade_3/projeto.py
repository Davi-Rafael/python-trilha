class agenda:
    def __init__(self):
        self.calendario = {}

    def adicionarEvento(self, evento, dia):
        if evento in self.calendario.keys():
            if dia in self.calendario[evento]:
                print('Já existe esse evento')
            else:
                self.calendario[evento].append(dia)
        else:
            self.calendario[evento] = [dia]

    def removerEvento(self, evento, dia):
        if evento in self.calendario.keys():
            if dia in self.calendario[evento]:
                self.calendario[evento].remove(dia)
                if len(self.calendario[evento]) == 0:
                    del self.calendario[evento]
            else:
                print('O evento existe, mas não nesse dia')
        else:
            print('Esse evento não existe')

    def relatorioDia(self, dia):
        relatorio = [x for x,y in self.calendario.items() if dia in y]
        print(relatorio)

    def diaEvento(self, evento):
        dia = [y for x,y in self.calendario.items() if x == evento]
        if len(dia) == 1:
            dia = dia[0]
        print(dia)

    def mostrarCalendario(self):
        print(self.calendario)

davi = agenda()

# Testando o metodo para adicionar eventos
print('-------------Testando adicionar evento')
davi.adicionarEvento('Sopa com os amigos', '16/11/2026')
davi.adicionarEvento('Prova de Matemática Discreta', '23/11/2026')
davi.adicionarEvento('Prova de Sistemas Digitais', '16/11/2026')
davi.adicionarEvento('Valorant com os amigos', '16/11/2026')
davi.adicionarEvento('Valorant com os amigos', '18/11/2026')
davi.adicionarEvento('Começo das ferias', '12/12/2026')
davi.mostrarCalendario()

# Testando o metodo para remover eventos
print('\n-------------Testando remover evento')
davi.removerEvento('Sopa com os amigos', '16/11/2026')
davi.mostrarCalendario()

# Testando o relatório por dia
print('\n-------------Testando relatório por dia')
davi.relatorioDia('16/11/2026')
davi.relatorioDia('12/12/2026')

# Testando o relatório por evento
print('\n-------------Testando relatório por evento')
davi.diaEvento('Prova de Matemática Discreta')
davi.diaEvento('Valorant com os amigos')