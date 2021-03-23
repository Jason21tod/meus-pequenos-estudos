from time import sleep

"""
NOTA! Em todos os métodos que pedem um argumento 'func',
ele se refere somente a uma função sem chamá-la, sendo que
a existência desse argumento serve para um mapeamento de onde
tais testes serão executados, com exceção apenas do método
'run_function, que roda uma função que argumentos pré estabelecidos
e todos os testes dentro dela.
"""

class TestDroidFunctional:
    log_list = []
    tests_concluded = 0
    functions_mapped = 0
    functions_runned = 0
    tests_failed = 0
    
    @classmethod
    def receive_msg(cls, msg: str) -> None:
        """
        Método que gera uma mensagem, adicionando-a ao resumo
        de testes.
        """
        cls.log_list.append(msg)
        
    @classmethod
    def map_functions(cls, func) -> None:
        """
        Mapeia funções, de modo a exibir as mesmas no resultado dos testes.
        Este método não roda as funções.
        """
        cls.log_list.append(f'\033[32m>>> Mapeando {func}\033[m')
        cls.functions_mapped += 1
        
    @classmethod
    def emit_all_logs(cls) -> None:
        """
        Gera uma representação sistemática ( em ordem de execução ), de funções/métodos mapeados,
        funções/métodos rodados, mensagens importantes, testes bem sucedidos e falhos, além de dar
        a localização de tais funções ou métodos. 
        """
        print(34*'_')
        print('EMITIR TODOS OS LOGS')
        for msg in cls.log_list:
            print(msg)
            print()
            sleep(0.3)
            
    @classmethod
    def show_resum(cls) -> None:
        """
        Exibe um resumo de testes feitos, quantos destes são falhos e quantas funções do código foram mapeadas e rodadas.
        """
        print(f'Testes realizados >>> {cls.tests_concluded}')
        print(f'Testes falhos >>> {cls.tests_failed}')
        print(f'Funções/métodos mapeados >>> {cls.functions_mapped}')
        print(f'funções/métodos rodados >>> {cls.functions_runned}')
        print('TESTES CONCLUÍDOS...')
     
    @classmethod
    def run_function(cls, func) -> None:
        """
        Recebe como argumento uma função sem chamá-la diretamente. A função/método chamado,
        deverá possuir argumentos pré-estabelecidos, afim de não criar erros.
        """
        cls.log_list.append(f'>>>\033[32mIniciando... {func}\033[m')
        cls.tests_concluded += 1
        cls.functions_runned += 1
        func()
   
    @classmethod
    def testing_upper(cls, func, val: float, expected: float) -> None:
        """
        Verifica se o valor (val) é maior que o esperado(expected).
        """
        value = val
        cls.tests_concluded += 1
        if value >= expected:
            cls.log_list.append(f'TESTE higher-> <"{value}" >= {expected}> em {func}>>> \033[32mOK\033[m')
        else:
            cls.log_list.append(f'TESTE higher-> <"{value}" >= {expected}> em {func}>>> \033[31mFAIL-> o valor é menor que o experado\033[m')
            cls.tests_failed += 1

    @classmethod
    def testing_lower(cls, func, val= float, expected= float) -> None:
        """
        Verifica se o valor (val) é menor que o esperado(expected).
        """
        value = val
        cls.tests_concluded += 1
        if value <= expected:
            cls.log_list.append(f'TESTE lower-> <"{value}" <= {expected}> em {func}>>> \033[32mOK\033[m')
        else:
            cls.log_list.append(f'TESTE lower-> <"{value}" <= {expected}> em {func}>>> \033[31mFAIL-> o valor é maior que o experado\033[m')
            cls.tests_failed += 1
            
    @classmethod
    def testing_equal(cls, func, val, expected) -> None:
        """
        Verifica se o valor (val) é igual que o esperado(expected).
        """
        value = val
        cls.tests_concluded += 1
        if value == expected:
            cls.log_list.append(f'TESTE equal-> <"{value}" == {expected}> em {func}>>> \033[32mOK\033[m')
        else:
            cls.log_list.append(f'TESTE equal-> <"{value}" != {expected}> em {func}>>> \033[31mFAIL-> o diferente é maior que o experado\033[m')
            cls.tests_failed += 1

    @classmethod
    def testing_type(cls, func, val, expected) -> None:
        """
        Verifica se o valor (val) é do mesmo tipo que o tipo de expected.
        """
        value = val
        cls.tests_concluded += 1
        if type(value) == type(expected):
            cls.log_list.append(f'TESTE type -> <{type(value)} == {type(expected)}> em {func}>>> \033[32mOK\033[m')
        else:
            cls.log_list.append(f'TESTE type -> <{type(value)} == {type(expected)}> em {func}>>> \033[31mFail-> o Objeto não coincide com o esperado\033[m')
            cls.tests_failed += 1
            
    @classmethod
    def testing_in(cls, func, val, container) -> None:
        """
        Verifica se o valor (val) está num container específico(container).
        """
        value = val
        cls.tests_concluded += 1
        if value in container:
            cls.log_list.append(f'TESTE in -> <{value} in {container}> em {func}>>> \033[32mOK\033[m')
        else:
            cls.log_list.append(f'TESTE in -> <{value} NOT IN {expected}> em {func}>>> \033[31mFail-> O item não esta no container\033[m')
            cls.tests_failed += 1
            
    @classmethod
    def testing_not_in(cls, func, val, container) -> None:
        """
        Verifica se o valor (val) não está num container específico(container).
        """
        value = val
        cls.tests_concluded += 1
        if value not in container:
            cls.log_list.append(f'TESTE not in -> <{value} not in {container}> em {func}>>> \033[32mOK\033[m')
        else:
            cls.log_list.append(f'TESTE not in -> <{value} in {expected}> em {func}>>> \033[31mFail-> O item esta no container\033[m')
            cls.tests_failed += 1


#As funções a baixo serão usadas na representação de testes. Simulando a utilização de TestDroidFuncional
def is_number(num: float) -> bool:
    try:
        float(num)
        return True
    except:
        pass
    return False

def value_assign(value_field= 'testando value assign') -> int:
    """
    Gera uma mensagem de input garantindo que o valor escrito seja um número.
    retornando um número inteiro.
    """
    value = input(f'{value_field}: ').strip()
    evaluation = is_number(value)
    while evaluation != True:
        value = input ('Insira um valor válido (int): ').strip()
        evaluation = is_number(value)    
    
    value = int(value)
    TestDroidFunctional.testing_type(value_assign, value, 1)
    return value


if __name__ == '__main__':
    #CASO VOCÊ RODE NESSA PASTA:
    """
    O arquivo sera executado, mostrando essa área.
    """
    print('TESTES')

    """    
    na função abaixo, são posicionados por padrão dois
    números 1 caso você não dê os argumentos pra função.
    """
    def soma_dois(n1 = 1, n2 = 1):
        #soma dois números
        soma = n1 + n2

        #testando se soma é maior q 1
        TestDroidFunctional.testing_upper(soma_dois, soma, 1)
        
        #testando se a soma é menor que 3
        TestDroidFunctional.testing_lower(soma_dois, soma, 3)
        
        #testando se soma é igual a 2
        TestDroidFunctional.testing_equal(soma_dois, soma, 2)
        
        #testando se o tipo é o mesmo de 0
        TestDroidFunctional.testing_type(soma_dois, soma, 0)
        
        return soma

    """
    com essa função, você ve todos os logs do testdroid,
    mapeando a função.
    """
    
    TestDroidFunctional.run_function(value_assign)
    
    #rode essa função
    TestDroidFunctional.run_function(soma_dois)
    
    #diz pra mim todos os seus logs
    TestDroidFunctional.emit_all_logs()
    
    #diz pra mim um resumo
    TestDroidFunctional.show_resum()
    
    
