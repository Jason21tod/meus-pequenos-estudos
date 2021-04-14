class Mapper:
    def __init__(self, name):
        self.name = name
        self._map = []
        self._pre_map = []
    
    def pre_map_func(self, func):
        self._pre_map.append(f'pre mapped function >>> {func}')
        return func
    
    def map_run(self, mapped):
        self._map.append(f'\033[31;1m{"{"}\033[m\nrunning >>> {mapped} ')
    
    def map_inp(self, func, *inp):
        for item in inp:
            self._map.append(f'\033[33m input <<<\033[m {item}: {type(item)}\n \033[32m em {func}\033[m')
        return inp
        
    def map_out(self, func, out):
        self._map.append(f'\033[35m output >>> \033[m {out}: {type(out)}\n \033[32m em {func}\033[m \033[31;1m{"}"}\033[m')
        return out
        
    def show_map(self):
        print ('='*36)
        print(f'{"MAP":^36} ==⟩ \033[32;1m{self.name}\033[m')
        print ()
        for item in self._map:
            print(f'\033[32m>>>Mapeado\n — {item}\033[m')
            print()
            
    def show_pre_map(self):
        print ('='*36)
        print(f'{"PRE MAP":^36} ==⟩ \033[32;1m{self.name}\033[m')
        print ()
        for item in self._pre_map:
            print(f'\033[32m>>>Pré Mapeado\n — {item}\033[m')
            print()



class UnitTest:
    def __init__ (self, name):
        self.name = name
        self.__tests_runned = 0
        self.__tests_failed_logs = []
        self.__tests_failed = 0
    
    def is_equal(self, func_name, value, expected):
        self.__tests_runned += 1
        veredict = value == expected
        if veredict == False:
            self.create_fail_log(func_name, (f'VALOR DIFERENTE DO ESPERADO:\n {value} != {expected}'))
        return value

    def is_low(self, func_name, value, expected):
        self.__tests_runned += 1
        veredict = value < expected
        if veredict == False:
            self.create_fail_log(func_name, (f'VALOR MAIOR OU IGUAL AO ESPERADO:\n {value} >= {expected}'))
        return value
    
    def is_higher(self, func_name, value, expected):
        self.__tests_runned += 1
        veredict = value > expected
        if veredict == False:
            self.create_fail_log(func_name, (f'VALOR MAIOR OU IGUAL AO ESPERADO:\n {value} != {expected}'))
        return value
        
    def not_equal(self, func_name, value, expected):
        self.__tests_runned += 1
        veredict = value != expected
        if veredict == False:
            self.create_fail_log(func_name, (f'VALOR IGUAL AO ESPERADO:\n {value} == {expected}'))
        return value
        
    def is_in(self, func_name, value, expected):
        self.__tests_runned += 1
        veredict = value in expected
        if veredict == False:
            self.create_fail_log(func_name, (f'VALOR NÃO ESTÁ NO ARRAY:\n {value} not in {expected}'))
        return value
        
    def not_in(self, func_name, value, expected):
        self.__tests_runned += 1
        veredict = value not in expected
        if veredict == False:
            self.create_fail_log(func_name, (f'VALOR ESTÁ NO ARRAY:\n {value} in {expected}'))
        return value
        
    def is_type(self, func_name, value, expected):
        self.__tests_runned += 1
        veredict = type(value) == expected
        if veredict == False:
            self.create_fail_log(func_name, (f'TIPO DIFERENTE DO ESPERADO:\n {type(value)} != {expected}'))
        return value

    def not_type(self, func_name, value, expected):
        self.__tests_runned += 1
        veredict = type(value) != expected
        if veredict == False:
            self.create_fail_log(func_name, (f'TIPO IGUAL AO ESPERADO:\n {type(value)} == {expected}'))
        return value

    def create_fail_log(self, func_name, msg):
        self.__tests_failed_logs.append(f'\033[31mErro em {func_name}\033[m \n>>> {msg}\n')
        self.__tests_failed += 1
        
    def show_fails(self):
        for test in self.__tests_failed_logs:
            print(test)
        
    def run_mocked_function(self, func):
        try:
            func()
        except:
            raise Exception(f'\nA função {func} não possui mocks \n')
            
    def show_resum(self):
        print(f'\033[4m{self.name:_^36}\033[m')
        print(f'\nTestes rodados: {self.__tests_runned}')
        print(f'Testes falhos: {self.__tests_failed}')
        print('='*36)
        self.show_fails()
        

if __name__ == '__main__':
    tdu = UnitTest('testador teste')
    mp = Mapper('mapeador teste')
    
    @mp.pre_map_func
    def soma(n1= 3, n2= 3):
        mp.map_inp(soma, n1, n2)
        value = n1+n2
        tdu.not_equal(soma, value, 5)
        tdu.is_equal(soma, value, 2)
        return mp.map_out(soma, value)
    
    soma()
    tdu.show_resum()
    mp.show_map()
    
