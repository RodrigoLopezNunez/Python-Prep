class Tools_sec:
    def __init__(self,lis):
        self.lis=lis
    
    def check_prime(self,lis:list)->list:
        lis_of_primes=[i for i in self.lis if self.__check_prime(i)==True]
        return lis_of_primes
    def __check_prime(self,n:int)->bool:
        '''Ésta función recibe un número y verifica si es primo.
                n: Es un número entero positivo
                output: Devuelve un booleano.'''
        prime=True
        for i in range(2,n):
            if n%i==0:
                prime=False
                break
        return prime
    
    def most_common(self,lis:list,max_or_min='max')->int:
        '''Ésta función itera una lista de números y devuelve el valor modal.
                list: Una lista de números enteros.
                output: Es una str con el valor modal y el número de repeticiones.'''
        dicc={}
        for i in lis:
            if i in dicc.keys():
                dicc[i]+=1
            else:
                dicc[i]=1
        most_rep=[]
        max_rep=0
        for n,rep in dicc.items():
            if rep>max_rep:
                most_rep=[n]
                max_rep=rep
            elif rep==max_rep:
                most_rep.append(n)
        if max_or_min=='Max':
            return f'El número mayor más repetido es {max(most_rep)} con {max_rep}'
        elif max_or_min=='Min':
            return f'El número menor más repetido es {min(most_rep)} con {max_rep}'
        else:
            return TypeError
    
    def Degree_Tranformation(self,lis:list,org:str,dest:str)->list:
        sec_lis=[self.__Degree_Transformation(i,org,dest) for i in self.lis]
        return f'{lis} de {org}° a {dest}° es',sec_lis
    def __Degree_Transformation(self,val:str,orgn:str,dest:str)->int:
        '''Ésta función recibe una variable de tipo "int" representando temperatura; 
             recibe el origen de temperatura (ya sea "Celsius", "Farenheit" ó "Kelvin"; 
                de la misma manera que el destino de transformación)'''
        if orgn=='Celsius':
            if dest=='Celsius':
                return val
            elif dest=='Farenheit':
                return (val*(9/5))+32
            elif dest=='Kelvin':
                return val+273.15
            else:
                return 'Hay un error en el valor de destino'
        elif orgn=='Farenheit':
            if dest=='Celsius':
                return (val-32)*(5/9)
            elif dest=='Farenheit':
                return val
            elif dest=='Kelvin':
                return ((val-32)*(5/9))+273.15
            else:
                return 'Hay un error en el valor de destino'
        elif orgn=='Kelvin':
            if dest=='Celsius':
                return val-273.15
            elif dest=='Farenheit':
                return ((val-273.15)*(9/5))+32
            elif dest=='Kelvin':
                return val
            else:
                return 'Hay un error en el valor de destino'
        else:
            return 'Hay un error en el valor de origen'
    
    def factorial(self,lis:list)->list:
        fact_lis=[self.__factorial(i) for i in self.lis]
        return fact_lis
    def __factorial(self,n:int)->int:
        '''Ésta función devuelve el factorial de un número.
                n: Es un número entero y positivo
                output: Es un número estero y positivo'''
        if type(n)==int and n>0:
            if n==1:
                return 1
            else:
                return n*self.__factorial(n-1)
        else:
            return f'Hay un error en el valor de entrada. Por favor, revísalo.'
    