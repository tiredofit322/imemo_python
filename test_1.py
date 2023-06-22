def check_1(func):
    if func.__name__ == 'circle_square':
        pass
    else:
        raise NameError('The name of the function must be \'circle_square\'')
    if func.__code__.co_argcount == 1:
        pass
    else:
        raise NameError('You passed too much arguments to the function')    
    if func.__code__.co_varnames[0] == 'radius':
        pass
    else:
        raise NameError('Is the function argument equal to \'radius\'?')
    if func(4) == 3.14 * (4 ** 2):
        print('All tests are passed. That\'s right')
    else:
        raise ValueError('Check you formula, something\'s not right with it')
    

def check_2(func):
    if func.__name__ == 'power_list':
        pass
    else:
        raise NameError('The name of the function must be \'power_list\'')
    if func.__code__.co_argcount == 2:
        pass
    else:
        raise NameError('Did you pass exactly 2 arguments?')  
    if 'num_list' in func.__code__.co_varnames and 'power' in func.__code__.co_varnames:
        pass
    else:
        raise NameError('Check the name of parameters')
    if type(func([1, 2], power=2)) == list:
        pass
    else:
        raise ValueError('Does your function return a list?')
    if func(num_list=[1, 2, 3], power=3) == [1, 8, 27]:
        pass
    else:
        raise ValueError('Check you formula, something\'s not right with it')
    if func(num_list=[1, 2, 3]) == [1, 4, 9]:
        print('All tests are passed. That\'s right')
    else:
        raise ValueError('Check you formula, something\'s not right with it. Did you pass default parameter for \'power\' argument?')
        
    
def check_3(func):
    if func.__name__ == 'zip_':
        pass
    else:
        raise NameError('The name of the function must be \'zip_\'')
    if func.__code__.co_argcount == 2:
        pass
    else:
        raise NameError('Did you pass exactly 2 arguments?')  
    if 'list_1' in func.__code__.co_varnames and 'list_2' in func.__code__.co_varnames:
        pass
    else:
        raise NameError('Check the name of parameters')
    if type(func(list_1=[1,2,3], list_2=[1,2,3,4])) == dict:
        pass
    else:
        raise ValueError('The function must return dict')
    if func(list_1=[11,21,32], list_2=[1,2,3,4]) == {11:1, 21:2, 32:3}:
        pass
    else:
        raise ValueError('Your function doesn\'t work as it supposed to')
    if func(list_1=[1,2,3,4], list_2=[10,21,32]) == {1:10, 2:21, 3:32}:
        pass
    else:
        raise ValueError('Your function doesn\'t work as it supposed to')
    if func(list_1=[1,2,3], list_2=[11,22,33]) == {1:11, 2:22, 3:33}:
        pass
    else:
        raise ValueError('Your function doesn\'t work as it supposed to')
    if func(list_1=[1,2,3], list_2=['a','b','v']) == {1:'a', 2:'b', 3:'v'}:
        print('All tests are passed. That\'s right')
    else:
        raise ValueError('Your function doesn\'t work as it supposed to')
        

def check_4(func):
    if func.__name__ == 'words_counter':
        pass
    else:
        raise NameError('The name of the function must be \'words_counter\'')
    if func.__code__.co_argcount == 1:
        pass
    else:
        raise NameError('Did you pass exactly 1 argument1?')  
    if 'string' in func.__code__.co_varnames:
        pass
    else:
        raise NameError('Check the name of parameters')
    if func(string='Aa, aA, aa, bB. BB') == {'aa':3, 'bb':2}:
        print('All tests are passed. That\'s right')
    else:
        raise ValueError('Your function doesn\'t work as it supposed to')
        
        
def check_5(func):
    if func.__name__ == 'prime_numbers':
        pass
    else:
        raise NameError('The name of the function must be \'prime_numbers\'')
    if func.__code__.co_argcount == 2:
        pass
    else:
        raise NameError('Did you pass exactly 2 arguments?')  
    if 'start' in func.__code__.co_varnames and 'end' in func.__code__.co_varnames:
        pass
    else:
        raise NameError('Check the name of parameters')
    if func(start=1, end=10) == [2,3,5,7]:
        pass
    else:
        raise ValueError('Your function doesn\'t work as it supposed to')
    if func(start=3, end=10) == [3,5,7]:
        pass
    else:
        raise ValueError('Your function doesn\'t work as it supposed to')
    if func(start=25, end=50) == [29, 31, 37, 41, 43, 47]:
        pass
    else:
        raise ValueError('Your function doesn\'t work as it supposed to')
    if func(start=25, end=47) == [29, 31, 37, 41, 43]:
        print('All tests are passed. That\'s right')
    else:
        raise ValueError('Did you exclude value at the \'end\' parameter')
        
