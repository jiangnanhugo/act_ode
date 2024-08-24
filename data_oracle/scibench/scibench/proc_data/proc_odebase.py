import pandas as pd
import numpy as np
import os
from sympy import Symbol, parse_expr, simplify, symbols

prefix = """import numpy as np
from scibench.data.base import KnownEquation, register_eq_class
from scibench.symbolic_data_generator import LogUniformSampling
"""

template = """@register_eq_class
class {}(KnownEquation):
    _eq_name = '{}'
    _operator_set = {}
    _description = "{}"
    def __init__(self):
        
        self.vars_range_and_types = [{}]
        super().__init__(num_vars={}, vars_range_and_types=self.vars_range_and_types)
        x= self.x
        self.sympy_eq = {}
    
    def np_eq(self, t, x):
        return np.array([{}])
"""


def fill_template(expressions, class_name, name, nvars, description, function_set):
    element = 'LogUniformSampling((1e-2, 10.0), only_positive=True)'
    elements = ", ".join([element for _ in range(int(nvars))])
    return template.format(class_name, name, function_set, description, elements, nvars,
                           expressions,
                           ", \n".join(expressions))


def detect_function_set(one_ode):
    function_set_base = ['add', 'sub', 'mul', 'div', 'const']
    if 'sin' in one_ode:
        function_set_base.append('sin')
    if 'cos' in one_ode:
        function_set_base.append('cos')
    if 'exp' in one_ode:
        function_set_base.append('exp')
    if 'log' in one_ode:
        function_set_base.append('log')
    if 'cot' in one_ode:
        function_set_base.append('cot')
    if '**' in one_ode:
        function_set_base.append('pow')
    if 'abs' in one_ode or 'Abs' in one_ode > 0:
        function_set_base.append('abs')
    return function_set_base


def main(verbose=False):
    file_name_list = []

    for root, dirs, files in os.walk("odebase/", topdown=False):

        for name in dirs:
            file_name_list.append(os.path.join(root, name))
    all_equations = dict()
    content = open(os.path.join("odebase/odebase-description.csv"), 'r').readlines()
    description = dict()
    for line in content:
        spl = line.split(",")
        description[spl[0]] = spl[1:]

    for fi in file_name_list:
        eq_name = fi[8:]
        cont = open(os.path.join(fi, 'parameters.txt'), 'r').readlines()
        equation_cont = open(os.path.join(fi, 'odes.txt'), 'r').readlines()
        # print(equation_cont)
        for ki in cont:
            ki_splited = ki.split("=")
            key = ki_splited[0].strip()
            val = "({:.3f})".format(eval(ki_splited[1].strip()))
            equation_cont = [one_eq.replace(key, val) for one_eq in equation_cont]

        one_ode = np.zeros(int(description[eq_name][1])).tolist()
        for line in equation_cont:

            one_eq = line[1:-2].split("=")
            if len(one_eq) != 2:
                continue
            ith = int(one_eq[0].strip()[7:-5]) - 1
            one_ode[ith] = one_eq[1].strip()

        expressions = " | ".join(one_ode).replace("[", "_").replace("]", '')
        for i in range(int(description[eq_name][1])+1):
            if f'x_{i}' in expressions:
                expressions = expressions.replace(f'x_{i}', f'x_{i - 1}')
        descrpt = description[eq_name][0].replace("_", "-")
        if descrpt[0] == '"' or descrpt[0] == "'":
            descrpt = descrpt[1:-1]
        all_equations[eq_name] = {
            'eq_description': descrpt,
            'nvars': int(description[eq_name][1]),
            'ncoeffs': int(description[eq_name][2].strip()),
            'eq': expressions
        }

    idx_dicts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    text_line_dict = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}}
    mode = 2
    for key in all_equations:
        one_eq = all_equations[key]
        expressions = one_eq['eq']

        if verbose:
            if mode == one_eq['nvars']:
                if one_eq['nvars'] == 1:
                    print(idx_dicts[one_eq['nvars']] + 1, " & ", one_eq['eq_description'] + " \\\\")
                else:
                    print(idx_dicts[one_eq['nvars']] + 1, "&", one_eq['eq_description'] + " \\\\")
                for i, ei in enumerate(expressions.split(' | ')):
                    print(" & $\dot{x}_", end="")
                    ei = str(parse_expr(ei.replace('^', '**')).expand().evalf(n=4)).replace('**', '^')
                    ei = ei.replace(
                        'sin', '\sin').replace(
                        'cos', '\cos').replace(
                        'exp', '\exp').replace(
                        'log', '\log').replace(
                        'cot', '\cot').replace(
                        "*", "")
                    print("{} = {}$ \\\\".format(i, ei), end="\n")
                print("  \hline")
        expressions = expressions.replace('^', '**')
        expressions = expressions.split(' | ')
        expressions = [parse_expr(eq).evalf(n=4).expand() for eq in expressions]

        expressions = " | ".join([str(ei) for ei in expressions])
        expressions = expressions.replace('x_0', 'x[0]')
        expressions = expressions.replace('x_1', 'x[1]')
        expressions = expressions.replace('x_2', 'x[2]')
        expressions = expressions.replace('x_3', 'x[3]')
        expressions = expressions.replace('x_4', 'x[4]')
        expressions = expressions.replace('x_5', 'x[5]')
        expressions = expressions.replace('exp', 'np.exp')
        expressions = expressions.replace('log', 'np.log')
        expressions = expressions.replace('sin', 'np.sin')
        expressions = expressions.replace('cos', 'np.cos')
        expressions = expressions.replace('cot', 'np.cot')
        expressions = expressions.replace('abs', 'np.abs')
        expressions = expressions.replace('Abs', 'np.abs')
        function_set = detect_function_set(expressions)
        for i in range(one_eq['nvars']+1):
            if f'x_{i}' in expressions:
                expressions = expressions.replace(f'x_{i}', f'x[{i}]')
            if f'x{i}' in expressions:
                expressions = expressions.replace(f'x{i}', f'x[{i}]')
        expressions = expressions.split(' | ')
        description = one_eq['eq_description']
        idx_dicts[one_eq['nvars']] += 1
        name = "odebase_vars{}_prog{}".format(one_eq['nvars'], idx_dicts[one_eq['nvars']])

        class_name = key
        class_name = class_name.replace('.', "_")
        class_name = class_name.replace(' ', '_')
        class_name = class_name.replace('-', '_')
        class_name = class_name.upper()

        line = fill_template(expressions, class_name, name, one_eq['nvars'], description, function_set)
        print(line)
        text_line_dict[one_eq['nvars']][idx_dicts[one_eq['nvars']]] = line
    fw = open("../data/equation_odes_odebase.py", 'w')
    fw.write(prefix)
    for i in range(1, 6):
        for j in range(1, idx_dicts[i] + 1):
            print(text_line_dict[i][j])
            fw.write(text_line_dict[i][j] + '\n')
    fw.close()
    print(idx_dicts)


if __name__ == '__main__':
    main()
