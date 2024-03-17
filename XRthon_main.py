import os, pathlib

func_name = None
list_1_s = []
D_FilePath = 'XRthon_editor\\T_F\\TEST.XRn'
AllVariablesDelete = False

folder = pathlib.Path(__file__).parent.resolve()

class XR_func_quit(BaseException):
    def __init__(self, *args : object):
        self.args = args
        super().__init__(*self.args)

class XR_bool_():
    def __init__(self):
        pass

    def _bool(self, text : str, var : dict):
        if text in var:
            if var[text] == True:
                return True
            elif var[text] == False:
                return False
            else:
                return False
        elif text == 1:
            return True
        else:
            return False

class _XR_bool_types(type):
    def __init__(self):
        super().__init__('True' or 'False')

def _XR_bool(text : _XR_bool_types):
    if text == 'True':
        return True
    elif text == 'False':
        return False

XR_bool = XR_bool_()

class XRthon_main():
    def __init__(self):
        global func_name
        self.always_debug_after_execution = False
        self.var = {'breakpoints': []}  # 初始化 breakpoints 为空列表

    def raisess(self, text: str, types: str, code: str, file_: str, line= 0, code_=1):
        Error_table = {
                       'VariableError',
                       'InitError',
                       'CodeError',
                       'ErrortypeError',
                       'NameError',
                       'EmptyFunctionError',
                       'LogicError',
                       'ConditionError',
                       'TextError',
                       'EmptyIterableError',
                       'NotSupportError',
                       'CanNotDeleteError',
                       'PrintError',
                       'CanNotSetError',
                      }
        if types in Error_table:
            if file_ == 'text':
                pass
            else:
                file_s = os.path.join(file_)
                print(' > Backtrack (last call):')
                print(f' >   File "{file_s}", line {line}')
                print(f' >     {code}')
                print(f' >     {types}: Error: {text}, Status code: {code_}\n')
                return 0
        else:
            self.raisess(f'name {types} is not defined', 'NameError', code, file_)
            return 0
    
    def Logic(self, var, text, file_now_line, path, file_line, file_text):
        global func_name, list_1_s, AllVariablesDelete
        # breakpoint()
        if file_now_line == 1:
            if 'init' in text:
                list_ = text.split(':')
                if '#' in list_[0]:
                    self.raisess('init undefined', 'InitError', text, path, file_now_line)
                    return
                paths_ = ''.join(path)
                path_ = paths_.split('\\')
                path_len_ = len(path_) - 1
                pathss_ = path_[path_len_].split('.')
                pathss_len_ = len(pathss_) - 1
                var.update({'__name__' : pathss_[pathss_len_ -1],
                            '__path__' : path,
                            '__init__' : list_[1],
                            '__file__' : path_[path_len_],
                            '__package__' : path_[path_len_ - 1],
                            'True' : True,
                            'False' : False,
                            'None' : None,})
                return
            else:
                returns = self.raisess('init undefined', 'InitError', text, path, file_now_line)
                if returns == 0:
                    return 0
        if '    ' in text:
            return
        elif '#' in text:
            return
        elif text == '':
            return
        elif '=' in text:
            list_ = text.split('=')
            v_name_ = list_[0]
            v = list_[1]
            if '.' in v_name_:
                list_1_ = v_name_.split('.')
                names = list_1_[0]
                d_ = list_1_[1]
                if names == 'del':
                    if d_ == 'AllVariablesDelete':
                        if v == 'True' or v == 'False':
                            print(' > WARNING: ')
                            print(' > When set to \'True\', all variables are deleted, as well as special variables.')
                            print(' > Therefore, an error will be reported when printing special variables.')
                            AllVariablesDelete = _XR_bool(v) # type: ignore
                        else:
                            returns = self.raisess('Can not set AllVariablesDelete', 'CanNotSetError', text, path, file_now_line)
                            if returns == 0:
                                return 0
                    else:
                        returns = self.raisess('Can not set AllVariablesDelete', 'CanNotSetError', text, path, file_now_line)
                        if returns == 0:
                            return 0
                else:
                    returns = self.raisess('Can not set AllVariablesDelete', 'CanNotSetError', text, path, file_now_line)
                    if returns == 0:
                        return 0
            elif 'input' in v:
                v_list_ = v.split(':')
                if v_list_[0] == 'input':
                    text_2 = v_list_[1].split('\'')
                    for text_1 in text_2:
                        if text_1 in var:
                            print(' > ' + var[text_1], end='')
                        else:
                            if not text_1 == '':
                                print(' > ' + v_list_[1], end='')
                        v = input('')
            elif '{' in v and '}' in v:
                vs = set( )
                v_list_ = v.split('{')[1].split('}')
                for vars in v_list_:
                    if vars == '':
                        continue
                    vars_list_ = vars.split(',')
                    for vars_ in vars_list_:
                        vs.update({vars_})
                        var.update({v_name_ : vs})
                return
            elif '.' in v:
                v_list_ = v.split('.')
                v_names_ = v_list_[0]
                v_d_ = v_list_[1]
                if v_names_ in var:
                    if v_d_ in var[v_names_]:
                        var.update({v_name_ : var[v_names_][v_d_]})
                    else:
                        returns = self.raisess('variable undefined', 'VariableError', text, path, file_now_line)
                        if returns == 0:
                            return 0
                else:
                    returns = self.raisess('variable undefined', 'VariableError', text, path, file_now_line)
                    if returns == 0:
                        return 0
                return
            elif v == 'math' and v in var:
                var.update({v_name_ : var[v]})
                return
            var.update({v_name_ : v})
        elif ':' in text:
            list_ = text.split(':')
            f = list_[0]
            if f == 'print':
                text_2 = list_[1].split('\'')
                for text_1 in text_2:
                    if (text_1 == '__name__' or
                    text_1 == '__path__' or
                    text_1 == '__init__' or
                    text_1 == '__file__' or
                    text_1 == '__package__' or
                    text_1 == 'True' or
                    text_1 == 'False' or
                    text_1 == 'None'):
                        if not text_1 in var:
                            returns = self.raisess('special variable cannot be printed', 'PrintError', text, path, file_now_line)
                            if returns == 0:
                                return 0
                        else:
                            print(' > ' + str(var[text_1]), end='')
                    elif text_1 in var:
                        print(' > ' + str(var[text_1]), end='')
                    else:
                        if not text_1 == '':
                            print(' > ' + list_[1], end='')
                print()
            elif f == 'input':
                text_2 = list_[1].split('\'')
                for text_1 in text_2:
                    if (text_1 == '__name__' or
                        text_1 == '__path__' or
                        text_1 == '__init__' or
                        text_1 == '__file__' or
                        text_1 == '__package__'):
                        if not text_1 in var:
                            self.raisess('special variable cannot be printed', 'PrintError', text, path, file_now_line)
                        else:
                            print(' > ' + str(var[text_1]), end='')
                    elif text_1 in var:
                        print(' > ' + str(var[text_1]), end='')
                    else:
                        if not text_1 == '':
                            print(' > ' + list_[1], end='')
                    v = input('')
            elif f == 'return':
                print(' > The program has exited\n')
                return 0
            elif f == 'raise':
                text_2 = list_[1].split(',')
                if len(text_2) == 2:
                    returns = self.raisess(text_2[0], text_2[1], text, path, file_now_line)
                    if returns == 0:
                        return 0
                elif len(text_2) == 3:
                    try:
                        returns = self.raisess(text_2[0], text_2[1], text, path, file_now_line, int(text_2[2]))
                        if returns == 0:
                            return 0
                    except SystemExit:
                        pass
                    except:
                        returns = self.raisess(f'code {text} is ERROR', 'CodeError', text, path, file_now_line)
                        if returns == 0:
                            return 0
                else:
                    returns = self.raisess(f'code {text} is ERROR', 'CodeError', text, path, file_now_line)
                    if returns == 0:
                        return 0
            elif f == 'def':
                func_name = list_[1]
                args_str = ''.join(list_[2:-1]).strip('(').strip(')')
                args_list = [arg.strip() for arg in args_str.split(',') if arg.strip()]
                
                var[func_name] = {'type': 'function', 'args': args_list, 'body': []}
                
                next_file_line = file_now_line + 1
                
                try:
                    while list_1_s[next_file_line - 1] != 'end':
                        var[func_name]['body'].append(list_1_s[next_file_line - 1].split('    ')[::-1][0])
                        next_file_line += 1
                except IndexError:
                    returns = self.raisess(f'Function "{func_name}" is empty', 'EmptyFunctionError', text, path, file_now_line)
                    if returns == 0:
                        return 0
                        
                if not var[func_name]['body']:
                    returns = self.raisess(f'Function "{func_name}" is empty', 'EmptyFunctionError', text, path, file_now_line)
                    if returns == 0:
                        return 0
                return
            elif f == 'if':
                condition = text.split(':')[1].split(' ')[0]
                body_lines = [line.strip() for line in text.split(':')[1].split('\n') if line.strip() != '']
                next_file_line = file_now_line + 1
                i = 0

                def test_1(i):
                    nonlocal next_file_line, condition
                    if i == 1:
                        i += 1
                        returns = test_1(i)
                        if returns == 0:
                            return 0
                        return
                    elif i >= 2:
                        while list_1_s[next_file_line - 1] != 'end':
                            returns = self.Logic(var, list_1_s[next_file_line - 1].split('    ')[::-1][0], file_now_line, path, file_line, file_text)
                            if returns == 0:
                                return 0
                            next_file_line += 1
                            returns = self.evaluate_expression(var, condition)
                            if returns == 0:
                                return 0
                    
                returns = test_1(1)
                if returns == 0:
                    return 0

            elif f in var:
                if 'type' in var[f]:
                    if var[f]['type'] == 'function':
                        function_info = var[f]
                        
                        local_vars = {arg: None for arg in function_info['args']}
                        
                        local_vars.update(var)

                        def test_2(i):
                            if i == 1:
                                i += 1
                                returns = test_2(i)
                                if returns == 0:
                                    return 0
                                return
                            elif i >= 2:
                                for texts in function_info['body']:
                                    returns = self.Logic(local_vars, texts, file_now_line, path, file_line, file_text)
                                    if returns == 0:
                                        return 0
                        
                        returns = test_2(1)
                        if returns == 0:
                            return 0

                        var[func_name]['return_value'] = None
                    else:
                        returns = self.raisess(f'name {text} is not defined', 'NameError', text, path, file_now_line)
                        if returns == 0:
                            return 0
                else:
                    returns = self.raisess(f'name {text} is not defined', 'NameError', text, path, file_now_line)
                    if returns == 0:
                        return 0
                
            elif f == 'for':
                next_file_line = file_now_line + 1
                v_name_ = list_[1]
                v = list_[1]

                def test_3(i):
                    nonlocal next_file_line, v
                    text_l = []
                    if i == 1:
                        i += 1
                        returns = test_3(i)
                        if returns == 0:
                            return 0
                        return
                    elif i >= 2:
                        while list_1_s[next_file_line - 1] != 'end':
                            text_l.append(list_1_s[next_file_line - 1].split('    ')[::-1][0])
                            next_file_line += 1
                        ns = int(v)
                        for i in range(ns):
                            for texts__ in text_l:
                                var.update({'ln' : ns})
                                var.update({'i' : i + 1})
                                returns = self.Logic(var, texts__, file_now_line, path, file_line, file_text)
                                if returns == 0:
                                    return 0
                    
                returns = test_3(1)
                if returns == 0:
                    return 0
                
            elif f == 'while':
                returns = self.raisess(f'while loop is not supported', 'NotSupportError', text, path, file_now_line)
                if returns == 0:
                    return 0
                condition, body_lines = text.split(':')[0], text.split(':')[1].strip()
                while self.eval_condition(var, condition, body_lines, next_file_line, path, file_line, file_text):
                    next_file_line = file_now_line + 1
                    
                    for body_line in body_lines.split('\n'):
                        returns = self.Logic(var, body_line, file_now_line, path, file_line, file_text)
                        if returns == 0:
                            return 0
            elif f == 'import':
                v = list_[1]
                if v == 'math':
                    math = {'pi' : 3.14159265358979,
                            'e' : 2.71828182845905,
                            'phi' : 1.61803398874989,
                            'tau' : 6.28318530717959,
                            'inf' : float('inf'),
                            'nan' : float('nan'),}
                    var.update({'math' : math})
                else:
                    returns = self.raisess(f'name {f} is not defined', 'NameError', text, path, file_now_line)
                    if returns == 0:
                        return 0
            elif f == 'del':
                if AllVariablesDelete == True:
                    if ',' in list_[1]:
                        list_s_ = list_[1].split(',')
                        for i in list_s_:
                            if i in var:
                                var.pop(i)
                            else:
                                returns = self.raisess(f'can not delete {i}', 'CanNotDeleteError', text, path, file_now_line)
                                if returns == 0:
                                    return 0
                    else:
                        v = list_[1]
                        if v in var:
                            var.pop(v)
                elif AllVariablesDelete == False:
                    if ',' in list_[1]:
                        list_s_ = list_[1].split(',')
                        for i in list_s_:
                            if i in var:
                                if (i == '__name__' or
                                    i == '__path__' or
                                    i == '__init__' or
                                    i == '__file__' or
                                    i == '__package__' or
                                    i == 'True' or
                                    i == 'False' or
                                    i == 'None'):
                                    returns = self.raisess(f'can not delete {i}', 'CanNotDeleteError', text, path, file_now_line)
                                    if returns == 0:
                                        return 0
                                else:
                                    var.pop(i)
                            else:
                                returns = self.raisess(f'can not delete {i}', 'CanNotDeleteError', text, path, file_now_line)
                                if returns == 0:
                                    return 0
                    else:
                        v = list_[1]
                        if v in var:
                            if (v == '__name__' or
                                v == '__path__' or
                                v == '__init__' or
                                v == '__file__' or
                                v == '__package__' or
                                v == 'True' or
                                v == 'False' or
                                v == 'None'):
                                returns = self.raisess(f'can not delete {v}', 'CanNotDeleteError', text, path, file_now_line)
                                if returns == 0:
                                    return 0
                            else:
                                var.pop(v)
                        else:
                            returns = self.raisess(f'can not delete {v}', 'CanNotDeleteError', text, path, file_now_line)
                            if returns == 0:
                                return 0
            else:
                returns = self.raisess(f'name {f} is not defined', 'NameError', text, path, file_now_line)
                if returns == 0:
                    return 0
                 
        elif text == 'end':
            return

        else:
            returns = self.raisess(f'name {text} is not defined', 'NameError', text, path, file_now_line)
            if returns == 0:
                return 0

    def eval_condition(self, var, condition, body_lines, start_line, path, file_line, file_text):
        evaluated_condition = self.evaluate_expression(var, condition)
        if evaluated_condition:
            for line_num, line_text in enumerate(body_lines, start=start_line):
                file_now_line = line_num
                returns = self.Logic(var, line_text, file_now_line, path, file_line, file_text)
                if returns == 0:
                    return 0

    def evaluate_expression(self, var, expression):
        try:
            return XR_bool._bool(expression, var)
        except ValueError:
            return False

    def debug_mode(self, text, var, path, file_now_line, file_line, file_text):
        if '#' in text:
            return
        print(f'Executing line {file_now_line}, code: {text}')
        try:
            user_input = input('Enter \'s\' in step debug mode, \'p\' to print the variable, \'quit\' to quit:')
        except KeyboardInterrupt:
            return
        if user_input == 's':
            retruns = self.Logic(var, text, file_now_line, path, file_line, file_text)
            if retruns == 0:
                return 0
        elif 'p' in user_input:
            text_S_ = user_input.split(' ')
            if text_S_[0] == 'p':
                text_S__ = text_S_[1].split('\'')
            else:
                return
            if text_S__[1] in var:
                print(' > ', var[text_S__[1]])
            else:
                returns = self.raisess(f'name {text_S_[1]} is not defined', 'NameError', text, path, file_now_line)
                if returns == 0:
                    return 0
            self.debug_mode(text, var, path, file_now_line, file_line, file_text)
        elif user_input == 'quit':
            self.always_debug_after_execution = False
            retruns = self.Logic(var, text, file_now_line, path, file_line, file_text)
            if retruns == 0:
                return 0
            return
        else:
            self.debug_mode(text, var, path, file_now_line, file_line, file_text)
            return

    def XRthon_file(self, file, path=os.path.join(folder, './TEST/TEST.XRn')):
        global list_1_s, D_FilePath
        texts = ''.join(file.read())
        file_line = len(file.read().split('\n'))
        file_text = texts
        file_now_line = 0
        list_1 = texts.split('\n')
        list_1_s = [text_4 for text_4 in file_text.split('\n')]
        if 'XRthon_editor\\TEST\\TEST.XRn' in path or 'XRthon_editor\\temp\\temp.XRn':
            path = D_FilePath
        for text in list_1:
            file_now_line += 1
            if file_now_line in self.var['breakpoints']:
                self.always_debug_after_execution = True
                retruns = self.debug_mode(text, self.var, path, file_now_line, file_line, file_text)
                if retruns == 0:
                    return
            else:
                if self.always_debug_after_execution:
                    retruns = self.debug_mode(text, self.var, path, file_now_line, file_line, file_text)
                    if retruns == 0:
                        return
                else:
                    self.always_debug_after_execution = False
                    retruns = self.Logic(self.var, text, file_now_line, path, file_line, file_text)
                    if retruns == 0:
                        return

            if not (file_now_line in self.var['breakpoints'] or self.always_debug_after_execution):
                continue

_XRthon_main_ = XRthon_main()

if __name__ == '__main__':
    with open(os.path.join(folder, './TEST/', 'TEST.XRn'), 'r', encoding='UTF-8') as file:
        _XRthon_main_.XRthon_file(file, str(folder) + '\\TEST\\' + 'TEST.XRn')
