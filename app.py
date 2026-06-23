import os
import pickle

# ==============================================================================
# PASSO 1 — A classe que representa um item (image_b7e000.png, image_b7e32e.png)
# ==============================================================================
class Agendamento:
    """Classe que representa UM item do seu sistema (um agendamento)."""
    
    def __init__(self, id, nome_cliente, servico, valor):
        self.id = id
        self.nome = nome_cliente  
        self.servico = servico
        self.valor = valor
        self.status = "Pendente"

    def __str__(self):
        return f"ID #{self.id} | Cliente: {self.nome} - Serviço: {self.servico} (R$ {self.valor:.2f}) | Status: [{self.status}]"

    def concluir(self):
        self.status = "Concluído"


# ==============================================================================
# PASSO 2 — A classe gerenciadora (image_b7e32e.png, image_b7e388.png)
# ==============================================================================
class GerenciadorBarbearia:
    """Classe que gerencia a lista de objetos e cuida da persistência com pickle."""
    
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.itens = []
        self.proximo_id = 1
        self.carregar() # Tenta carregar dados existentes ao iniciar o programa

    def adicionar(self, nome_cliente, servico, valor):
        # Cria o objeto usando o self.proximo_id automático
        novo = Agendamento(self.proximo_id, nome_cliente, servico, valor)
        self.itens.append(novo)
        self.proximo_id += 1

    def listar(self):
        return self.itens

    def buscar(self, id):
        # Percorre a lista e retorna o agendamento com o id correspondente ou None
        for item in self.itens:
            if item.id == id:
                return item
        return None

    def remover(self, id):
        # Procura o item pelo id, se achar, remove da lista e retorna True
        item = self.buscar(id)
        if item:
            self.itens.remove(item)
            return True
        return False

    # 🌟 FUNCIONALIDADE EXTRA EXIGIDA (image_b7e32e.png, image_b7e364.png)
    def calcular_faturamento(self):
        """Soma o valor de todos os serviços que mudaram de status para Concluído."""
        total = 0.0
        for item in self.itens:
            if item.status == "Concluído":
                total += item.valor
        return total

    # MÉTODOS DE PERSISTÊNCIA COMPATÍVEIS COM O MODELO DO PROFESSOR
    def salvar(self):
        # Salva a lista de agendamentos e o contador de IDs usando pickle
        with open(self.arquivo, 'wb') as f:
            dados = {
                'itens': self.itens,
                'proximo_id': self.proximo_id
            }
            pickle.dump(dados, f)

    def carregar(self):
        # Se o arquivo .pkl já existir, lê as informações salvas anteriormente
        if os.path.exists(self.arquivo):
            try:
                with open(self.arquivo, 'rb') as f:
                    dados = pickle.load(f)
                    self.itens = dados.get('itens', [])
                    self.proximo_id = dados.get('proximo_id', 1)
            except Exception:
                # Caso ocorra erro de leitura, inicializa as variáveis vazias
                self.itens = []
                self.proximo_id = 1


# ==============================================================================
# PASSO 3 — A função menu (image_b7e3a7.png)
# ==============================================================================
def menu():
    # Cria o arquivo de dados local para persistência consistente
    g = GerenciadorBarbearia('barbearia_sistema.pkl')
    
    while True:
        print('\n=== SISTEMA GERENCIADOR BARBEARIA ===')
        print('1 - Adicionar Agendamento')
        print('2 - Listar Todos')
        print('3 - Buscar por ID')
        print('4 - Remover Agendamento')
        print('5 - Concluir Serviço (Dar Baixa)')  # Opção útil para mudar status
        print('6 - Ver Faturamento Total')         # Ativando a nossa função extra
        print('0 - Sair')
        
        op = input('Escolha: ').strip()
        
        if op == '1':
            nome = input('Nome do Cliente: ')
            servico = input('Serviço (Ex: Cabelo, Barba): ')
            try:
                valor = float(input('Valor cobrado (R$): '))
                g.adicionar(nome, servico, valor)
                g.salvar()
                print('Adicionado!')
            except ValueError:
                print('Erro: O valor deve ser um número decimal válido (ex: 35.00).')
                
        elif op == '2':
            lista_atual = g.listar()
            if len(lista_atual) == 0:
                print('Nenhum agendamento registrado.')
            else:
                for item in lista_atual:
                    print(item) # O Python chama automaticamente o __str__ aqui!
                    
        elif op == '3':
            try:
                id_busca = int(input('ID: '))
            except ValueError:
                print('ID inválido.')
                continue
            item = g.buscar(id_busca)
            print(item if item else 'Não encontrado')
            
        elif op == '4':
            try:
                id_busca = int(input('ID: '))
            except ValueError:
                print('ID inválido.')
                continue
            ok = g.remover(id_busca)
            g.salvar()
            print('Removido!' if ok else 'Não encontrado')
            
        elif op == '5':
            try:
                id_busca = int(input('ID do atendimento concluído: '))
            except ValueError:
                print('ID inválido.')
                continue
            item = g.buscar(id_busca)
            if item:
                item.concluir()
                g.salvar()
                print(f'Status do ID #{id_busca} atualizado para Concluído!')
            else:
                print('Não encontrado')
                
        elif op == '6':
            total = g.calcular_faturamento()
            print(f'\n====================================')
            print(f' Faturamento (Serviços Concluídos): R$ {total:.2f}')
            print(f'====================================')
            
        elif op == '0':
            g.salvar()
            print('Até mais!')
            break
        else:
            print('Opção inválida.')

# Para executar o menu, descomente a linha abaixo:
menu()