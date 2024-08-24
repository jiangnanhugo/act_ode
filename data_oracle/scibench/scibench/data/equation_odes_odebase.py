import numpy as np
from scibench.data.base import KnownEquation, register_eq_class
from scibench.symbolic_data_generator import LogUniformSampling


@register_eq_class
class BIOMD0000000425(KnownEquation):
    _eq_name = 'odebase_vars1_prog1'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Tan2012 - Antibiotic Treatment Inoculum Effect"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=1, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-1.0*x[0] + 1.0*x[0]/(x[0] + 2.0) - 0.05*x[0]/(0.1*x[0] + 0.1) + 0.1']

    def np_eq(self, t, x):
        return np.array([-1.0 * x[0] + 1.0 * x[0] / (x[0] + 2.0) - 0.05 * x[0] / (0.1 * x[0] + 0.1) + 0.1])


@register_eq_class
class BIOMD0000000414(KnownEquation):
    _eq_name = 'odebase_vars1_prog2'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Band2012-DII-Venus-ReducedModel"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=1, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.0026*x[0] - 0.005*x[0]/(0.056*x[0] + 0.16) + 0.005']

    def np_eq(self, t, x):
        return np.array([-0.0026 * x[0] - 0.005 * x[0] / (0.056 * x[0] + 0.16) + 0.005])


@register_eq_class
class BIOMD0000000728(KnownEquation):
    _eq_name = 'odebase_vars2_prog1'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Norel1990 - MPF and Cyclin Oscillations"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['1.0*x[0]**2*x[1] - 10.0*x[0]/(x[0] + 1.0) + 3.466*x[1]', '1.2 - 1.0*x[0]']

    def np_eq(self, t, x):
        return np.array([1.0 * x[0] ** 2 * x[1] - 10.0 * x[0] / (x[0] + 1.0) + 3.466 * x[1],
                         1.2 - 1.0 * x[0]])


@register_eq_class
class BIOMD0000000815(KnownEquation):
    _eq_name = 'odebase_vars2_prog2'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Chrobak2011 - A mathematical model of induced cancer-adaptive immune system competition"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.03125*x[0]**2 - 0.125*x[0]*x[1] + 0.0625*x[0]',
                         '-0.08594*x[0]*x[1] - 0.03125*x[1]**2 + 0.03125*x[1]']

    def np_eq(self, t, x):
        return np.array([-0.03125 * x[0] ** 2 - 0.125 * x[0] * x[1] + 0.0625 * x[0],
                         -0.08594 * x[0] * x[1] - 0.03125 * x[1] ** 2 + 0.03125 * x[1]])


@register_eq_class
class BIOMD0000000346(KnownEquation):
    _eq_name = 'odebase_vars2_prog3'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "FitzHugh1961-NerveMembrane"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-1.0*x[0]**3 + 3.0*x[0] + 3.0*x[1] - 1.2', '-0.3333*x[0] - 0.2667*x[1] + 0.2333']

    def np_eq(self, t, x):
        return np.array([-1.0 * x[0] ** 3 + 3.0 * x[0] + 3.0 * x[1] - 1.2,
                         -0.3333 * x[0] - 0.2667 * x[1] + 0.2333])


@register_eq_class
class BIOMD0000000678(KnownEquation):
    _eq_name = 'odebase_vars2_prog4'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Tomida2003 - Calcium Oscillatory-induced translocation of nuclear factor of activated T cells"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.359*x[0]*x[4] + 0.147*x[1] + 0.035*x[3]', '0.359*x[0]*x[4] - 0.207*x[1]']

    def np_eq(self, t, x):
        return np.array([-0.359 * x[0] * x[4] + 0.147 * x[1] + 0.035 * x[3],
                         0.359 * x[0] * x[4] - 0.207 * x[1]])


@register_eq_class
class BIOMD0000000538(KnownEquation):
    _eq_name = 'odebase_vars2_prog5'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Clarke2000 - One-hit model of cell death in neuronal degenerations"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.278*x[0]', '-0.223*x[1]']

    def np_eq(self, t, x):
        return np.array([-0.278 * x[0],
                         -0.223 * x[1]])


@register_eq_class
class BIOMD0000000774(KnownEquation):
    _eq_name = 'odebase_vars2_prog6'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Wodarz2018/1 - simple model"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0.004*x[0] + 0.004*x[1]/(0.01*x[0]**1.0 + 1.0)',
                         '0.006*x[0] - 0.003*x[1] - 0.004*x[1]/(0.01*x[0]**1.0 + 1.0)']

    def np_eq(self, t, x):
        return np.array([0.004 * x[0] + 0.004 * x[1] / (0.01 * x[0] ** 1.0 + 1.0),
                         0.006 * x[0] - 0.003 * x[1] - 0.004 * x[1] / (0.01 * x[0] ** 1.0 + 1.0)])


@register_eq_class
class BIOMD0000000552(KnownEquation):
    _eq_name = 'odebase_vars2_prog7'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Ehrenstein2000 - Positive-Feedback model for the loss of acetylcholine in Alzheimer's disease"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.007*x[0]*x[1]', '-0.004*x[0] - 0.01*x[1] + 0.33']

    def np_eq(self, t, x):
        return np.array([-0.007 * x[0] * x[1],
                         -0.004 * x[0] - 0.01 * x[1] + 0.33])


@register_eq_class
class BIOMD0000000485(KnownEquation):
    _eq_name = 'odebase_vars2_prog8'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Cao2013 - Application of ABSIS method in the bistable Schlagl model"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.00096*x[0]**3 + 0.1229*x[0]**2 - 3.072*x[0] + 12.5',
                         '0.00096*x[0]**3 - 0.1229*x[0]**2 + 3.072*x[0] - 12.5']

    def np_eq(self, t, x):
        return np.array([-0.00096 * x[0] ** 3 + 0.1229 * x[0] ** 2 - 3.072 * x[0] + 12.5,
                         0.00096 * x[0] ** 3 - 0.1229 * x[0] ** 2 + 3.072 * x[0] - 12.5])


@register_eq_class
class BIOMD0000001024(KnownEquation):
    _eq_name = 'odebase_vars2_prog9'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Chaudhury2020 - Lotka-Volterra mathematical model of CAR-T cell and tumour kinetics"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0.002*x[0]*x[1] - 0.16*x[0]', '0.15*x[1]']

    def np_eq(self, t, x):
        return np.array([0.002 * x[0] * x[1] - 0.16 * x[0],
                         0.15 * x[1]])


@register_eq_class
class BIOMD0000000550(KnownEquation):
    _eq_name = 'odebase_vars2_prog10'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Baker2013 - Cytokine Mediated Inflammation in Rheumatoid Arthritis"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-x[0] + 3.5*x[1]**2/(x[1]**2 + 0.25)',
                         '1.0*x[1]**2/(x[0]**2*x[1]**2 + 1.0*x[0]**2 + 1.0*x[1]**2 + 1.0) - 1.25*x[1] + 0.025/(x[0]**2 + 1.0)']

    def np_eq(self, t, x):
        return np.array([-x[0] + 3.5 * x[1] ** 2 / (x[1] ** 2 + 0.25),
                         1.0 * x[1] ** 2 / (x[0] ** 2 * x[1] ** 2 + 1.0 * x[0] ** 2 + 1.0 * x[1] ** 2 + 1.0) - 1.25 * x[
                             1] + 0.025 / (x[0] ** 2 + 1.0)])


@register_eq_class
class BIOMD0000000114(KnownEquation):
    _eq_name = 'odebase_vars2_prog11'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Somogyi1990-CaOscillations"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-5.0*x[0]*x[1]**4.0/(x[1]**4.0 + 81.0) - 0.01*x[0] + 2.0*x[1]',
                         '5.0*x[0]*x[1]**4.0/(x[1]**4.0 + 81.0) + 0.01*x[0] - 3.0*x[1] + 1.0']

    def np_eq(self, t, x):
        return np.array([-5.0 * x[0] * x[1] ** 4.0 / (x[1] ** 4.0 + 81.0) - 0.01 * x[0] + 2.0 * x[1],
                         5.0 * x[0] * x[1] ** 4.0 / (x[1] ** 4.0 + 81.0) + 0.01 * x[0] - 3.0 * x[1] + 1.0])


@register_eq_class
class BIOMD0000000799(KnownEquation):
    _eq_name = 'odebase_vars2_prog12'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Cucuianu2010 - A hypothetical-mathematical model of acute myeloid leukaemia pathogenesis"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.1*x[0] + 0.3*x[0]/(0.5*x[0] + 0.5*x[1] + 1.0)',
                         '-0.1*x[1] + 0.3*x[1]/(0.5*x[0] + 0.5*x[1] + 1.0)']

    def np_eq(self, t, x):
        return np.array([-0.1 * x[0] + 0.3 * x[0] / (0.5 * x[0] + 0.5 * x[1] + 1.0),
                         -0.1 * x[1] + 0.3 * x[1] / (0.5 * x[0] + 0.5 * x[1] + 1.0)])


@register_eq_class
class BIOMD0000000782(KnownEquation):
    _eq_name = 'odebase_vars2_prog13'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Wang2016/3 - oncolytic efficacy of M1 virus-SN model"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.2*x[0]*x[1] - 0.02*x[0] + 0.02', '0.16*x[0]*x[1] - 0.03*x[1]']

    def np_eq(self, t, x):
        return np.array([-0.2 * x[0] * x[1] - 0.02 * x[0] + 0.02,
                         0.16 * x[0] * x[1] - 0.03 * x[1]])


@register_eq_class
class BIOMD0000000793(KnownEquation):
    _eq_name = 'odebase_vars2_prog14'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Chen2011/1 - bone marrow invasion absolute model"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.2*x[0]**2 + 0.1*x[0]', '-1.0*x[0]*x[1] - 0.8*x[1]**2 + 0.7*x[1]']

    def np_eq(self, t, x):
        return np.array([-0.2 * x[0] ** 2 + 0.1 * x[0],
                         -1.0 * x[0] * x[1] - 0.8 * x[1] ** 2 + 0.7 * x[1]])


@register_eq_class
class BIOMD0000000486(KnownEquation):
    _eq_name = 'odebase_vars2_prog15'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Cao2013 - Application of ABSIS method in the reversible isomerization model"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.12*x[0] + 1.0*x[1]', '0.12*x[0] - 1.0*x[1]']

    def np_eq(self, t, x):
        return np.array([-0.12 * x[0] + 1.0 * x[1],
                         0.12 * x[0] - 1.0 * x[1]])


@register_eq_class
class BIOMD0000000785(KnownEquation):
    _eq_name = 'odebase_vars2_prog16'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Sotolongo-Costa2003 - Behavior of tumors under nonstationary therapy"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-1.0*x[0]*x[1] + 2.0*x[0]', '1.0*x[0]*x[1] - 0.2*x[0] - 0.5*x[1] + 0.25']

    def np_eq(self, t, x):
        return np.array([-1.0 * x[0] * x[1] + 2.0 * x[0],
                         1.0 * x[0] * x[1] - 0.2 * x[0] - 0.5 * x[1] + 0.25])


@register_eq_class
class BIOMD0000000553(KnownEquation):
    _eq_name = 'odebase_vars2_prog17'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Ehrenstein1997 - The choline-leakage hypothesis in Alzheimer's disease"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.007*x[0]*x[1]', '-0.004*x[0] - 0.01*x[1] + 0.33']

    def np_eq(self, t, x):
        return np.array([-0.007 * x[0] * x[1],
                         -0.004 * x[0] - 0.01 * x[1] + 0.33])


@register_eq_class
class BIOMD0000000484(KnownEquation):
    _eq_name = 'odebase_vars2_prog18'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Cao2013 - Application of ABSIS method in birth-death process"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['1.0 - 0.025*x[0]', '0.025*x[0] - 1.0']

    def np_eq(self, t, x):
        return np.array([1.0 - 0.025 * x[0],
                         0.025 * x[0] - 1.0])


@register_eq_class
class BIOMD0000000573(KnownEquation):
    _eq_name = 'odebase_vars2_prog19'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Aguilera 2014 - HIV latency. Interaction between HIV proteins and immune response"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.029*x[0]*x[1] + 0.134*x[0]/(x[0] + 380.0) + 0.001', '-0.927*x[0]*x[1] + 0.07']

    def np_eq(self, t, x):
        return np.array([-0.029 * x[0] * x[1] + 0.134 * x[0] / (x[0] + 380.0) + 0.001,
                         -0.927 * x[0] * x[1] + 0.07])


@register_eq_class
class BIOMD0000000795(KnownEquation):
    _eq_name = 'odebase_vars2_prog20'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Chen2011/2 - bone marrow invasion relative model"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.8*x[0]**2 - 0.9*x[0]*x[1] + 0.7*x[0]', '-0.1*x[0]*x[1] - 0.2*x[1]**2 + 0.1*x[1]']

    def np_eq(self, t, x):
        return np.array([-0.8 * x[0] ** 2 - 0.9 * x[0] * x[1] + 0.7 * x[0],
                         -0.1 * x[0] * x[1] - 0.2 * x[1] ** 2 + 0.1 * x[1]])


@register_eq_class
class BIOMD0000000836(KnownEquation):
    _eq_name = 'odebase_vars2_prog21'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Radosavljevic2009-BioterroristAttack-PanicProtection-1"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.6*x[0]**2 - 2.8*x[0]*x[1] + 6.0*x[0]', '1.0*x[0]*x[1]']

    def np_eq(self, t, x):
        return np.array([-0.6 * x[0] ** 2 - 2.8 * x[0] * x[1] + 6.0 * x[0],
                         1.0 * x[0] * x[1]])


@register_eq_class
class BIOMD0000000758(KnownEquation):
    _eq_name = 'odebase_vars2_prog22'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Babbs2012 - immunotherapy"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0.004*x[0] - 4.0*x[1]', '0.09*x[0]*x[1] - 0.1*x[1]']

    def np_eq(self, t, x):
        return np.array([0.004 * x[0] - 4.0 * x[1],
                         0.09 * x[0] * x[1] - 0.1 * x[1]])


@register_eq_class
class BIOMD0000000742(KnownEquation):
    _eq_name = 'odebase_vars2_prog23'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Garcia2018basic - cancer and immune cell count basic model"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0.514*x[0]', '10.0 - 0.02*x[1]']

    def np_eq(self, t, x):
        return np.array([0.514 * x[0],
                         10.0 - 0.02 * x[1]])


@register_eq_class
class BIOMD0000000753(KnownEquation):
    _eq_name = 'odebase_vars2_prog24'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Figueredo2013/1 - immunointeraction base model"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=2, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.006544*x[0]**2 - 1.0*x[0]*x[1] + 1.636*x[0]',
                         '-0.003*x[0]*x[1] + 1.131*x[0]*x[1]/(x[0] + 20.19) - 2.0*x[1] + 0.318']

    def np_eq(self, t, x):
        return np.array([-0.006544 * x[0] ** 2 - 1.0 * x[0] * x[1] + 1.636 * x[0],
                         -0.003 * x[0] * x[1] + 1.131 * x[0] * x[1] / (x[0] + 20.19) - 2.0 * x[1] + 0.318])


@register_eq_class
class BIOMD0000000922(KnownEquation):
    _eq_name = 'odebase_vars3_prog1'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Turner2015-Human/Mosquito ELP Model"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['600.0 - 0.411*x[0]', '0.361*x[0] - 0.184*x[1]', '0.134*x[1] - 0.345*x[2]']

    def np_eq(self, t, x):
        return np.array([600.0 - 0.411 * x[0],
                         0.361 * x[0] - 0.184 * x[1],
                         0.134 * x[1] - 0.345 * x[2]])


@register_eq_class
class BIOMD0000001031(KnownEquation):
    _eq_name = 'odebase_vars3_prog2'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Al-Tuwairqi2020 - Dynamics of cancer virotherapy - Phase I treatment"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-1.0*x[0]*x[2]', '1.0*x[0]*x[2] - 1.0*x[1]', '-0.02*x[0]*x[2] + 1.0*x[1] - 0.15*x[2]']

    def np_eq(self, t, x):
        return np.array([-1.0 * x[0] * x[2],
                         1.0 * x[0] * x[2] - 1.0 * x[1],
                         -0.02 * x[0] * x[2] + 1.0 * x[1] - 0.15 * x[2]])


@register_eq_class
class BIOMD0000000807(KnownEquation):
    _eq_name = 'odebase_vars3_prog3'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Fassoni2019 - Oncogenesis encompassing mutations and genetic instability"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0.01 - 0.01*x[0]', '0.03*x[1]', '-0.5*x[2]**2 + 0.034*x[2]']

    def np_eq(self, t, x):
        return np.array([0.01 - 0.01 * x[0],
                         0.03 * x[1],
                         -0.5 * x[2] ** 2 + 0.034 * x[2]])


@register_eq_class
class BIOMD0000000156(KnownEquation):
    _eq_name = 'odebase_vars3_prog4'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Zatorsky2006-p53-Model5"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-3.7*x[0]*x[1] + 2.0*x[0]', '-0.9*x[1] + 1.1*x[2]', '1.5*x[0] - 1.1*x[2]']

    def np_eq(self, t, x):
        return np.array([-3.7 * x[0] * x[1] + 2.0 * x[0],
                         -0.9 * x[1] + 1.1 * x[2],
                         1.5 * x[0] - 1.1 * x[2]])


@register_eq_class
class BIOMD0000000878(KnownEquation):
    _eq_name = 'odebase_vars3_prog5'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Lenbury2001-InsulinKineticsModel-A"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.1*x[0]*x[2] + 0.2*x[1]*x[2] + 0.1*x[2]', '-0.01*x[0] + 0.01 + 0.01/x[2]',
                         '-0.1*x[1]*x[2] + 0.257*x[1] - 0.1*x[2]**2 + 0.331*x[2] - 0.3187']

    def np_eq(self, t, x):
        return np.array([-0.1 * x[0] * x[2] + 0.2 * x[1] * x[2] + 0.1 * x[2],
                         -0.01 * x[0] + 0.01 + 0.01 / x[2],
                         -0.1 * x[1] * x[2] + 0.257 * x[1] - 0.1 * x[2] ** 2 + 0.331 * x[2] - 0.3187])


@register_eq_class
class BIOMD0000000159(KnownEquation):
    _eq_name = 'odebase_vars3_prog6'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Zatorsky2006-p53-Model1"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-3.2*x[0]*x[1] + 0.3', '-0.1*x[1] + 0.1*x[2]', '0.4*x[0] - 0.1*x[2]']

    def np_eq(self, t, x):
        return np.array([-3.2 * x[0] * x[1] + 0.3,
                         -0.1 * x[1] + 0.1 * x[2],
                         0.4 * x[0] - 0.1 * x[2]])


@register_eq_class
class BIOMD0000000519(KnownEquation):
    _eq_name = 'odebase_vars3_prog7'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Smallbone2013 - Colon Crypt cycle - Version 1"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.002207*x[0]**2 - 0.002207*x[0]*x[1] - 0.002207*x[0]*x[2] + 0.1648*x[0]',
                         '-0.01312*x[0]**2 - 0.0216*x[0]*x[1] - 0.01312*x[0]*x[2] + 1.574*x[0] - 0.008477*x[1]**2 - 0.008477*x[1]*x[2] + 0.5972*x[1]',
                         '-0.04052*x[0]*x[1] - 0.04052*x[1]**2 - 0.04052*x[1]*x[2] + 4.863*x[1] - 1.101*x[2]']

    def np_eq(self, t, x):
        return np.array([-0.002207 * x[0] ** 2 - 0.002207 * x[0] * x[1] - 0.002207 * x[0] * x[2] + 0.1648 * x[0],
                         -0.01312 * x[0] ** 2 - 0.0216 * x[0] * x[1] - 0.01312 * x[0] * x[2] + 1.574 * x[0] - 0.008477 *
                         x[1] ** 2 - 0.008477 * x[1] * x[2] + 0.5972 * x[1],
                         -0.04052 * x[0] * x[1] - 0.04052 * x[1] ** 2 - 0.04052 * x[1] * x[2] + 4.863 * x[1] - 1.101 *
                         x[2]])


@register_eq_class
class BIOMD0000000884(KnownEquation):
    _eq_name = 'odebase_vars3_prog8'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Cortes2019 - Optimality of the spontaneous prophage induction rate."

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.99*x[0]**2/(x[0] + x[1]) - 1.0*x[0]*x[1]/(x[0] + x[1]) + 0.99*x[0]',
                         '-0.99*x[0]*x[1]/(x[0] + x[1]) - 1.0*x[1]**2/(x[0] + x[1]) + 1.0*x[1]', '-0.001*x[2]']

    def np_eq(self, t, x):
        return np.array([-0.99 * x[0] ** 2 / (x[0] + x[1]) - 1.0 * x[0] * x[1] / (x[0] + x[1]) + 0.99 * x[0],
                         -0.99 * x[0] * x[1] / (x[0] + x[1]) - 1.0 * x[1] ** 2 / (x[0] + x[1]) + 1.0 * x[1],
                         -0.001 * x[2]])


@register_eq_class
class BIOMD0000000754(KnownEquation):
    _eq_name = 'odebase_vars3_prog9'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Figueredo2013/2 - immunointeraction model with IL2"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-1.0*x[0]*x[1]/(x[0] + 1.0) + 0.18*x[0]',
                         '0.05*x[0] + 0.124*x[1]*x[2]/(x[2] + 20.0) - 0.03*x[1]',
                         '5.0*x[0]*x[1]/(x[0] + 10.0) - 10.0*x[2]']

    def np_eq(self, t, x):
        return np.array([-1.0 * x[0] * x[1] / (x[0] + 1.0) + 0.18 * x[0],
                         0.05 * x[0] + 0.124 * x[1] * x[2] / (x[2] + 20.0) - 0.03 * x[1],
                         5.0 * x[0] * x[1] / (x[0] + 10.0) - 10.0 * x[2]])


@register_eq_class
class BIOMD0000000763(KnownEquation):
    _eq_name = 'odebase_vars3_prog10'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Dritschel2018 - A mathematical model of cytotoxic and helper T cell interactions in a tumour microenvironment"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-10.0*x[0]**2 - 2.075*x[0]*x[2] + 10.0*x[0]',
                         '0.19*x[0]*x[1]/(x[0]**2 + 0.0016) - 1.0*x[1] + 0.5',
                         '-2.075*x[0]*x[2] + 1.0*x[1]*x[2] - 1.0*x[2] + 2.0']

    def np_eq(self, t, x):
        return np.array([-10.0 * x[0] ** 2 - 2.075 * x[0] * x[2] + 10.0 * x[0],
                         0.19 * x[0] * x[1] / (x[0] ** 2 + 0.0016) - 1.0 * x[1] + 0.5,
                         -2.075 * x[0] * x[2] + 1.0 * x[1] * x[2] - 1.0 * x[2] + 2.0])


@register_eq_class
class BIOMD0000000882(KnownEquation):
    _eq_name = 'odebase_vars3_prog11'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Munz2009 - Zombie SIZRC"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.009*x[0]*x[1] + 0.05', '0.004*x[0]*x[1]', '0.005*x[0]*x[1]']

    def np_eq(self, t, x):
        return np.array([-0.009 * x[0] * x[1] + 0.05,
                         0.004 * x[0] * x[1],
                         0.005 * x[0] * x[1]])


@register_eq_class
class BIOMD0000000893(KnownEquation):
    _eq_name = 'odebase_vars3_prog12'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "GonzalezMiranda2013 - The effect of circadian oscillations on biochemical cell signaling by NF-κB"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-954.5*x[0]*x[2]/(x[0] + 0.029) - 0.007*x[0]/x[2] + 0.007/x[2]', '1.0*x[0]**2 - 1.0*x[1]',
                         '0.035*x[0] + 1.0*x[1] - 0.035']

    def np_eq(self, t, x):
        return np.array([-954.5 * x[0] * x[2] / (x[0] + 0.029) - 0.007 * x[0] / x[2] + 0.007 / x[2],
                         1.0 * x[0] ** 2 - 1.0 * x[1],
                         0.035 * x[0] + 1.0 * x[1] - 0.035])


@register_eq_class
class BIOMD0000000891(KnownEquation):
    _eq_name = 'odebase_vars3_prog13'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Khajanchi2019 - Stability Analysis of a Mathematical Model forGlioma-Immune Interaction under OptimalTherapy"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.482*x[0]**2 - 0.07*x[0]*x[1]/(x[0] + 0.903) - 2.745*x[0]*x[2]/(x[0] + 0.903) + 0.482*x[0]',
                         '-0.019*x[0]*x[1]/(x[0] + 0.031) - 0.331*x[1]**2 + 0.331*x[1]',
                         '0.124*x[0]*x[2]/(x[0] + 2.874) - 0.017*x[0]*x[2]/(x[0] + 0.379) - 0.007*x[2]']

    def np_eq(self, t, x):
        return np.array([-0.482 * x[0] ** 2 - 0.07 * x[0] * x[1] / (x[0] + 0.903) - 2.745 * x[0] * x[2] / (
                    x[0] + 0.903) + 0.482 * x[0],
                         -0.019 * x[0] * x[1] / (x[0] + 0.031) - 0.331 * x[1] ** 2 + 0.331 * x[1],
                         0.124 * x[0] * x[2] / (x[0] + 2.874) - 0.017 * x[0] * x[2] / (x[0] + 0.379) - 0.007 * x[2]])


@register_eq_class
class BIOMD0000000713(KnownEquation):
    _eq_name = 'odebase_vars3_prog14'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Aston2018 - Dynamics of Hepatitis C Infection"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.002*x[0] + 1.065e+4*x[0]/(x[0] + x[1]) + 0.118*x[1]',
                         '-0.118*x[1] + 342.5*x[1]/(x[0] + x[1])', '204.0*x[1] - 17.91*x[2]']

    def np_eq(self, t, x):
        return np.array([-0.002 * x[0] + 1.065e+4 * x[0] / (x[0] + x[1]) + 0.118 * x[1],
                         -0.118 * x[1] + 342.5 * x[1] / (x[0] + x[1]),
                         204.0 * x[1] - 17.91 * x[2]])


@register_eq_class
class BIOMD0000001023(KnownEquation):
    _eq_name = 'odebase_vars3_prog15'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Alharbi2020 - An ODE-based model of the dynamics of tumor cell progression and its effects on normal cell growth and immune system functionality"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.931*x[0]*x[1] - 0.138*x[0]*x[2] + 0.431*x[0]',
                         '1.189*x[0]*x[1] - 0.1772*x[1]**2 - 0.147*x[1]*x[2] + 0.443*x[1]',
                         '-0.813*x[0]*x[2] + 0.271*x[0]*x[2]/(x[0] + 0.813) - 0.363*x[1]*x[2] + 0.783*x[1]*x[2]/(x[1] + 0.862) - 0.57*x[2] + 0.7']

    def np_eq(self, t, x):
        return np.array([-0.931 * x[0] * x[1] - 0.138 * x[0] * x[2] + 0.431 * x[0],
                         1.189 * x[0] * x[1] - 0.1772 * x[1] ** 2 - 0.147 * x[1] * x[2] + 0.443 * x[1],
                         -0.813 * x[0] * x[2] + 0.271 * x[0] * x[2] / (x[0] + 0.813) - 0.363 * x[1] * x[2] + 0.783 * x[
                             1] * x[2] / (x[1] + 0.862) - 0.57 * x[2] + 0.7])


@register_eq_class
class BIOMD0000000321(KnownEquation):
    _eq_name = 'odebase_vars3_prog16'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Grange2001 - L Dopa PK model"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-2.11*x[0]', '0.889*x[0] - 1.659*x[1]', '0.4199*x[1] - 0.06122*x[2]']

    def np_eq(self, t, x):
        return np.array([-2.11 * x[0],
                         0.889 * x[0] - 1.659 * x[1],
                         0.4199 * x[1] - 0.06122 * x[2]])


@register_eq_class
class BIOMD0000000157(KnownEquation):
    _eq_name = 'odebase_vars3_prog17'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Zatorsky2006-p53-Model4"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0.9 - 1.7*x[1]', '-0.8*x[1] + 0.8*x[2]', '1.1*x[0] - 0.8*x[2]']

    def np_eq(self, t, x):
        return np.array([0.9 - 1.7 * x[1],
                         -0.8 * x[1] + 0.8 * x[2],
                         1.1 * x[0] - 0.8 * x[2]])


@register_eq_class
class BIOMD0000000911(KnownEquation):
    _eq_name = 'odebase_vars3_prog18'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Merola2008 - An insight into tumor dormancy equilibrium via the analysis of its domain of attraction"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-1.125*x[0]**2 - 0.3*x[0]*x[1] + 0.9*x[0] + 10.0', '0.1*x[1]*x[2] - 0.02*x[1]',
                         '-0.1*x[1]*x[2] - 1.143*x[2]**2 + 0.77*x[2]']

    def np_eq(self, t, x):
        return np.array([-1.125 * x[0] ** 2 - 0.3 * x[0] * x[1] + 0.9 * x[0] + 10.0,
                         0.1 * x[1] * x[2] - 0.02 * x[1],
                         -0.1 * x[1] * x[2] - 1.143 * x[2] ** 2 + 0.77 * x[2]])


@register_eq_class
class BIOMD0000000894(KnownEquation):
    _eq_name = 'odebase_vars3_prog19'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Bose2011 - Noise-assisted interactions of tumor and immune cells"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-1.0*x[0]**2 - 1.0*x[0]*x[1] + 1.748*x[0] + 2.73*x[2]', '1.0*x[1]*x[2] - 0.05*x[1]',
                         '1.126*x[0] - 15.89*x[2]']

    def np_eq(self, t, x):
        return np.array([-1.0 * x[0] ** 2 - 1.0 * x[0] * x[1] + 1.748 * x[0] + 2.73 * x[2],
                         1.0 * x[1] * x[2] - 0.05 * x[1],
                         1.126 * x[0] - 15.89 * x[2]])


@register_eq_class
class BIOMD0000000933(KnownEquation):
    _eq_name = 'odebase_vars3_prog20'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Kosiuk2015-Geometric analysis of the Goldbeter minimal model for the embryonic cell cycle"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.25*x[0] - 0.25*x[2] + 0.25',
                         '-6.0*x[0]*x[1]/(-2.0*x[0]*x[1] + 2.002*x[0] - 1.0*x[1] + 1.001) + 6.0*x[0]/(-2.0*x[0]*x[1] + 2.002*x[0] - 1.0*x[1] + 1.001) - 1.5*x[1]/(x[1] + 0.001)',
                         '-1.0*x[1]*x[2]/(1.001 - x[2]) + 1.0*x[1]/(1.001 - x[2]) - 0.7*x[2]/(x[2] + 0.001)']

    def np_eq(self, t, x):
        return np.array([-0.25 * x[0] - 0.25 * x[2] + 0.25,
                         -6.0 * x[0] * x[1] / (-2.0 * x[0] * x[1] + 2.002 * x[0] - 1.0 * x[1] + 1.001) + 6.0 * x[0] / (
                                     -2.0 * x[0] * x[1] + 2.002 * x[0] - 1.0 * x[1] + 1.001) - 1.5 * x[1] / (
                                     x[1] + 0.001),
                         -1.0 * x[1] * x[2] / (1.001 - x[2]) + 1.0 * x[1] / (1.001 - x[2]) - 0.7 * x[2] / (
                                     x[2] + 0.001)])


@register_eq_class
class BIOMD0000000783(KnownEquation):
    _eq_name = 'odebase_vars3_prog21'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Dong2014 - Mathematical modeling on helper t cells in a tumor immune system"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.003272*x[0]**2 - 1.0*x[0]*x[1] + 1.636*x[0]',
                         '0.04*x[0]*x[1] + 0.01*x[1]*x[2] - 0.374*x[1]', '0.002*x[0]*x[2] - 0.055*x[2] + 0.38']

    def np_eq(self, t, x):
        return np.array([-0.003272 * x[0] ** 2 - 1.0 * x[0] * x[1] + 1.636 * x[0],
                         0.04 * x[0] * x[1] + 0.01 * x[1] * x[2] - 0.374 * x[1],
                         0.002 * x[0] * x[2] - 0.055 * x[2] + 0.38])


@register_eq_class
class BIOMD0000000890(KnownEquation):
    _eq_name = 'odebase_vars3_prog22'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Bhattacharya2014 - A mathematical model of the sterol regulatory element binding protein 2 cholesterol biosynthesis pathway"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.001*x[0]', '1.0*x[0] - 0.002*x[1]', '0.462*x[1] - 0.004*x[2]']

    def np_eq(self, t, x):
        return np.array([-0.001 * x[0],
                         1.0 * x[0] - 0.002 * x[1],
                         0.462 * x[1] - 0.004 * x[2]])


@register_eq_class
class BIOMD0000000663(KnownEquation):
    _eq_name = 'odebase_vars3_prog23'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Wodarz2007 - HIV/CD4 T-cell interaction"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.1*x[0]**2*x[2] - 0.1*x[0]*x[1]*x[2] + 0.8*x[0]*x[2] - 0.1*x[0]',
                         '-0.1*x[0]*x[1]*x[2] + 0.2*x[0]*x[2] - 0.1*x[1]**2*x[2] + 1.0*x[1]*x[2] - 0.2*x[1]',
                         '1.0*x[1] - 0.5*x[2]']

    def np_eq(self, t, x):
        return np.array([-0.1 * x[0] ** 2 * x[2] - 0.1 * x[0] * x[1] * x[2] + 0.8 * x[0] * x[2] - 0.1 * x[0],
                         -0.1 * x[0] * x[1] * x[2] + 0.2 * x[0] * x[2] - 0.1 * x[1] ** 2 * x[2] + 1.0 * x[1] * x[
                             2] - 0.2 * x[1],
                         1.0 * x[1] - 0.5 * x[2]])


@register_eq_class
class BIOMD0000000944(KnownEquation):
    _eq_name = 'odebase_vars3_prog24'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Goldbeter2013-Oscillatory activity of cyclin-dependent kinases in the cell cycle"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.25*x[0]*x[2]/(x[0] + 0.001) - 0.046*x[0] + 0.06',
                         '-4.0*x[0]*x[1]/(-x[0]*x[1] + 1.002*x[0] - 0.5*x[1] + 0.501) + 4.0*x[0]/(-x[0]*x[1] + 1.002*x[0] - 0.5*x[1] + 0.501) - 2.0*x[1]/(x[1] + 0.002)',
                         '-1.0*x[1]*x[2]/(1.01 - x[2]) + 1.0*x[1]/(1.01 - x[2]) - 0.7*x[2]/(x[2] + 0.01)']

    def np_eq(self, t, x):
        return np.array([-0.25 * x[0] * x[2] / (x[0] + 0.001) - 0.046 * x[0] + 0.06,
                         -4.0 * x[0] * x[1] / (-x[0] * x[1] + 1.002 * x[0] - 0.5 * x[1] + 0.501) + 4.0 * x[0] / (
                                     -x[0] * x[1] + 1.002 * x[0] - 0.5 * x[1] + 0.501) - 2.0 * x[1] / (x[1] + 0.002),
                         -1.0 * x[1] * x[2] / (1.01 - x[2]) + 1.0 * x[1] / (1.01 - x[2]) - 0.7 * x[2] / (x[2] + 0.01)])


@register_eq_class
class BIOMD0000001038(KnownEquation):
    _eq_name = 'odebase_vars3_prog25'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Alharbi2019 - Tumor-normal-vitamins model (TNVM) of the effects of vitamins on delaying the growth of tumor cells"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.982*x[0]*x[1] + 0.222*x[0]*x[2] + 0.431*x[0]',
                         '0.229*x[0]*x[1] - 0.1772*x[1]**2 - 0.497*x[1]*x[2] + 0.443*x[1]', '0.898 - 0.961*x[2]']

    def np_eq(self, t, x):
        return np.array([-0.982 * x[0] * x[1] + 0.222 * x[0] * x[2] + 0.431 * x[0],
                         0.229 * x[0] * x[1] - 0.1772 * x[1] ** 2 - 0.497 * x[1] * x[2] + 0.443 * x[1],
                         0.898 - 0.961 * x[2]])


@register_eq_class
class BIOMD0000000520(KnownEquation):
    _eq_name = 'odebase_vars3_prog26'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Smallbone2013 - Colon Crypt cycle - Version 0"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0', '1.0*x[0]**2/(x[0] + 2.924) + 0.218*x[0] - 0.024*x[1]',
                         '1.0*x[1]**2/(x[1] + 29.24) + 0.547*x[1] - 1.83*x[2]']

    def np_eq(self, t, x):
        return np.array([0,
                         1.0 * x[0] ** 2 / (x[0] + 2.924) + 0.218 * x[0] - 0.024 * x[1],
                         1.0 * x[1] ** 2 / (x[1] + 29.24) + 0.547 * x[1] - 1.83 * x[2]])


@register_eq_class
class BIOMD0000000299(KnownEquation):
    _eq_name = 'odebase_vars3_prog27'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Leloup1999-CircadianRhythms-Neurospora"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.505*x[0]/(x[0] + 0.5) + 1.6/(x[2]**4.0 + 1.0)',
                         '0.5*x[0] - 0.5*x[1] - 1.4*x[1]/(x[1] + 0.13) + 0.6*x[2]', '0.5*x[1] - 0.6*x[2]']

    def np_eq(self, t, x):
        return np.array([-0.505 * x[0] / (x[0] + 0.5) + 1.6 / (x[2] ** 4.0 + 1.0),
                         0.5 * x[0] - 0.5 * x[1] - 1.4 * x[1] / (x[1] + 0.13) + 0.6 * x[2],
                         0.5 * x[1] - 0.6 * x[2]])


@register_eq_class
class BIOMD0000000906(KnownEquation):
    _eq_name = 'odebase_vars3_prog28'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Dubey2007 - A mathematical model for the effect of toxicant on the immune system (without toxicant effect) Model1"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.2*x[0]**2 - 0.05*x[0]*x[1] + 0.9*x[0]', '0.295*x[0]*x[1] - 0.8*x[1] + 0.04',
                         '2.4*x[0] - 0.1*x[2]']

    def np_eq(self, t, x):
        return np.array([-0.2 * x[0] ** 2 - 0.05 * x[0] * x[1] + 0.9 * x[0],
                         0.295 * x[0] * x[1] - 0.8 * x[1] + 0.04,
                         2.4 * x[0] - 0.1 * x[2]])


@register_eq_class
class BIOMD0000000813(KnownEquation):
    _eq_name = 'odebase_vars3_prog29'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Anderson2015 - Qualitative behavior of systems of tumor-CD4+-cytokine interactions with treatments"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-3.0e-5*x[0]**2 - 0.1*x[0]*x[2]/(x[0] + 1.0) + 0.03*x[0]',
                         '0.02*x[0]*x[1]/(x[0] + 10.0) - 0.02*x[1] + 10.0', '0.1*x[0]*x[1]/(x[0] + 0.1) - 47.0*x[2]']

    def np_eq(self, t, x):
        return np.array([-3.0e-5 * x[0] ** 2 - 0.1 * x[0] * x[2] / (x[0] + 1.0) + 0.03 * x[0],
                         0.02 * x[0] * x[1] / (x[0] + 10.0) - 0.02 * x[1] + 10.0,
                         0.1 * x[0] * x[1] / (x[0] + 0.1) - 47.0 * x[2]])


@register_eq_class
class BIOMD0000000548(KnownEquation):
    _eq_name = 'odebase_vars3_prog30'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Sneppen2009 - Modeling proteasome dynamics in Parkinson's disease"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-1.0*x[0]*x[1] + 25.0/(x[1] + 1.0)', '-1.0*x[0]*x[1] - x[1] + 1.0*x[2] + 1.0',
                         '1.0*x[0]*x[1] - 1.0*x[2]']

    def np_eq(self, t, x):
        return np.array([-1.0 * x[0] * x[1] + 25.0 / (x[1] + 1.0),
                         -1.0 * x[0] * x[1] - x[1] + 1.0 * x[2] + 1.0,
                         1.0 * x[0] * x[1] - 1.0 * x[2]])


@register_eq_class
class BIOMD0000000079(KnownEquation):
    _eq_name = 'odebase_vars3_prog31'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Goldbeter2006-weightCycling"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.1*x[0]/(x[0] + 0.2) + 0.1*x[1]',
                         '-1.5*x[1]*x[2]/(x[1] + 0.01) - 1.0*x[1]/(1.01 - x[1]) + 1.0/(1.01 - x[1])',
                         '-6.0*x[0]*x[2]/(1.01 - x[2]) + 6.0*x[0]/(1.01 - x[2]) - 2.5*x[2]/(x[2] + 0.01)']

    def np_eq(self, t, x):
        return np.array([-0.1 * x[0] / (x[0] + 0.2) + 0.1 * x[1],
                         -1.5 * x[1] * x[2] / (x[1] + 0.01) - 1.0 * x[1] / (1.01 - x[1]) + 1.0 / (1.01 - x[1]),
                         -6.0 * x[0] * x[2] / (1.01 - x[2]) + 6.0 * x[0] / (1.01 - x[2]) - 2.5 * x[2] / (x[2] + 0.01)])


@register_eq_class
class BIOMD0000000773(KnownEquation):
    _eq_name = 'odebase_vars3_prog32'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Wodarz2018/2 - model with transit amplifying cells"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0.004*x[0] + 0.0096*x[1]/(0.01*x[0]**1.0 + 1.0)', '0.006*x[0] - 0.004*x[1]',
                         '0.024*x[1] - 0.0096*x[1]/(0.01*x[0]**1.0 + 1.0) - 0.003*x[2]']

    def np_eq(self, t, x):
        return np.array([0.004 * x[0] + 0.0096 * x[1] / (0.01 * x[0] ** 1.0 + 1.0),
                         0.006 * x[0] - 0.004 * x[1],
                         0.024 * x[1] - 0.0096 * x[1] / (0.01 * x[0] ** 1.0 + 1.0) - 0.003 * x[2]])


@register_eq_class
class BIOMD0000001036(KnownEquation):
    _eq_name = 'odebase_vars3_prog33'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Cappuccio2007 - Tumor-immune system interactions and determination of the optimal therapeutic protocol in immunotherapy"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0.044*x[0]*x[2]/(x[2] + 0.02) - 0.038*x[0] + 1.009*x[1]',
                         '-0.018*x[0] - 0.123*x[1]**2 + 0.123*x[1]', '0.9*x[0] - 1.8*x[2]']

    def np_eq(self, t, x):
        return np.array([0.044 * x[0] * x[2] / (x[2] + 0.02) - 0.038 * x[0] + 1.009 * x[1],
                         -0.018 * x[0] - 0.123 * x[1] ** 2 + 0.123 * x[1],
                         0.9 * x[0] - 1.8 * x[2]])


@register_eq_class
class BIOMD0000000670(KnownEquation):
    _eq_name = 'odebase_vars3_prog34'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Owen1998 - tumour growth model"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = [
            '-17.86*x[0]*x[2]**2 + 0.05*x[0]*x[2]/(x[0] + x[1] + x[2] + 1.0) - 0.1*x[0] + 0.625*x[2] + 0.01',
            '-x[1] + 2.0*x[1]/(x[0] + x[1] + x[2] + 1.0)',
            '-25.0*x[0]*x[2]**2 - x[2] + 4.0*x[2]/(x[0] + x[1] + x[2] + 1.0)']

    def np_eq(self, t, x):
        return np.array([-17.86 * x[0] * x[2] ** 2 + 0.05 * x[0] * x[2] / (x[0] + x[1] + x[2] + 1.0) - 0.1 * x[
            0] + 0.625 * x[2] + 0.01,
                         -x[1] + 2.0 * x[1] / (x[0] + x[1] + x[2] + 1.0),
                         -25.0 * x[0] * x[2] ** 2 - x[2] + 4.0 * x[2] / (x[0] + x[1] + x[2] + 1.0)])


@register_eq_class
class BIOMD0000000781(KnownEquation):
    _eq_name = 'odebase_vars3_prog35'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Wang2016/2 - oncolytic efficacy of M1 virus-SNT model"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.2*x[0]*x[1] - 0.5*x[0]*x[2] - 0.02*x[0] + 0.02', '0.16*x[0]*x[1] - 0.03*x[1]',
                         '0.4*x[0]*x[2] - 0.028*x[2]']

    def np_eq(self, t, x):
        return np.array([-0.2 * x[0] * x[1] - 0.5 * x[0] * x[2] - 0.02 * x[0] + 0.02,
                         0.16 * x[0] * x[1] - 0.03 * x[1],
                         0.4 * x[0] * x[2] - 0.028 * x[2]])


@register_eq_class
class BIOMD0000001011(KnownEquation):
    _eq_name = 'odebase_vars3_prog36'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Leon-Triana2020 - CAR T-cell therapy in B-cell acute lymphoblastic leukaemia"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=3, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.07143*x[0]', '0.033*x[1]', '-0.01667*x[2]']

    def np_eq(self, t, x):
        return np.array([-0.07143 * x[0],
                         0.033 * x[1],
                         -0.01667 * x[2]])


@register_eq_class
class BIOMD0000000932(KnownEquation):
    _eq_name = 'odebase_vars4_prog1'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Garde2020-Minimal model describing metabolic oscillations in Bacillus subtilis biofilms"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-5.3*x[0]*x[2] + 8.29*x[0]', '2.0*x[0] - 2.3*x[1]', '2.3*x[1] - 4.0*x[2]',
                         '0.1*x[0]*x[2]*x[3]']

    def np_eq(self, t, x):
        return np.array([-5.3 * x[0] * x[2] + 8.29 * x[0],
                         2.0 * x[0] - 2.3 * x[1],
                         2.3 * x[1] - 4.0 * x[2],
                         0.1 * x[0] * x[2] * x[3]])


@register_eq_class
class BIOMD0000000881(KnownEquation):
    _eq_name = 'odebase_vars4_prog2'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Kogan2013 - A mathematical model for the immunotherapeutic control of the TH1 TH2 imbalance in melanoma"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.001*x[0] + 350.0/(x[3] + 0.35)', '-0.001*x[1] + 180.0/(x[2] + 0.18)', '0.016 - 0.6*x[2]',
                         '-0.36*x[3] + 0.06 + 0.011/(x[2] + 0.025)']

    def np_eq(self, t, x):
        return np.array([-0.001 * x[0] + 350.0 / (x[3] + 0.35),
                         -0.001 * x[1] + 180.0 / (x[2] + 0.18),
                         0.016 - 0.6 * x[2],
                         -0.36 * x[3] + 0.06 + 0.011 / (x[2] + 0.025)])


@register_eq_class
class BIOMD0000000521(KnownEquation):
    _eq_name = 'odebase_vars4_prog3'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Ribba2012 - Low-grade gliomas tumour growth inhibition model"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.24*x[0]',
                         '-0.175*x[0]*x[1] - 0.00121*x[1]**2 - 0.00121*x[1]*x[2] - 0.00121*x[1]*x[3] + 0.118*x[1] + 0.003*x[3]',
                         '-0.175*x[0]*x[2] + 0.003', '0.175*x[0]*x[2] - 0.012*x[3]']

    def np_eq(self, t, x):
        return np.array([-0.24 * x[0],
                         -0.175 * x[0] * x[1] - 0.00121 * x[1] ** 2 - 0.00121 * x[1] * x[2] - 0.00121 * x[1] * x[
                             3] + 0.118 * x[1] + 0.003 * x[3],
                         -0.175 * x[0] * x[2] + 0.003,
                         0.175 * x[0] * x[2] - 0.012 * x[3]])


@register_eq_class
class BIOMD0000000957(KnownEquation):
    _eq_name = 'odebase_vars4_prog4'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Roda2020 - SIR model of COVID-19 spread in Wuhan"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0', '-1.009*x[1]', '0.1*x[1]', '0.909*x[1]']

    def np_eq(self, t, x):
        return np.array([0,
                         -1.009 * x[1],
                         0.1 * x[1],
                         0.909 * x[1]])


@register_eq_class
class BIOMD0000000267(KnownEquation):
    _eq_name = 'odebase_vars4_prog5'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Lebeda2008 - BoNT paralysis (3 step model)"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.058*x[0]', '0.058*x[0] - 0.141*x[1]', '0.141*x[1] - 0.013*x[2]', '0.013*x[2]']

    def np_eq(self, t, x):
        return np.array([-0.058 * x[0],
                         0.058 * x[0] - 0.141 * x[1],
                         0.141 * x[1] - 0.013 * x[2],
                         0.013 * x[2]])


@register_eq_class
class BIOMD0000000254(KnownEquation):
    _eq_name = 'odebase_vars4_prog6'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Bier2000-GlycolyticOscillation"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.02*x[0]*x[1] + 0.36', '0.04*x[0]*x[1] - 0.01*x[1] - 6.0*x[1]/(x[1] + 13.0) + 0.01*x[3]',
                         '-0.02*x[2]*x[3] + 0.36', '0.01*x[1] + 0.04*x[2]*x[3] - 0.01*x[3] - 6.0*x[3]/(x[3] + 13.0)']

    def np_eq(self, t, x):
        return np.array([-0.02 * x[0] * x[1] + 0.36,
                         0.04 * x[0] * x[1] - 0.01 * x[1] - 6.0 * x[1] / (x[1] + 13.0) + 0.01 * x[3],
                         -0.02 * x[2] * x[3] + 0.36,
                         0.01 * x[1] + 0.04 * x[2] * x[3] - 0.01 * x[3] - 6.0 * x[3] / (x[3] + 13.0)])


@register_eq_class
class BIOMD0000000765(KnownEquation):
    _eq_name = 'odebase_vars4_prog7'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Mager2005 - Quasi-equilibrium pharmacokinetic model for drugs exhibiting target-mediated drug disposition"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.1*x[0]*x[2] - 1.0*x[0] + 0.1*x[3]', '0', '-0.1*x[0]*x[2] - 0.566*x[2] + 0.1*x[3]',
                         '0.1*x[0]*x[2] - 0.1*x[3]']

    def np_eq(self, t, x):
        return np.array([-0.1 * x[0] * x[2] - 1.0 * x[0] + 0.1 * x[3],
                         0,
                         -0.1 * x[0] * x[2] - 0.566 * x[2] + 0.1 * x[3],
                         0.1 * x[0] * x[2] - 0.1 * x[3]])


@register_eq_class
class BIOMD0000000888(KnownEquation):
    _eq_name = 'odebase_vars4_prog8'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Unni2019 - Mathematical Modeling Analysis and Simulation of Tumor Dynamics with Drug Interventions"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0.431*x[0]', '1.3e+4 - 0.041*x[1]', '0.024*x[2] + 480.0', '0.01*x[0]*x[2] - 0.02*x[3]']

    def np_eq(self, t, x):
        return np.array([0.431 * x[0],
                         1.3e+4 - 0.041 * x[1],
                         0.024 * x[2] + 480.0,
                         0.01 * x[0] * x[2] - 0.02 * x[3]])


@register_eq_class
class BIOMD0000000460(KnownEquation):
    _eq_name = 'odebase_vars4_prog9'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Liebal2012 - B.subtilis sigB proteolysis model"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0', '0.052*x[2] + 1.0e+4', '-0.052*x[2]', '0']

    def np_eq(self, t, x):
        return np.array([0,
                         0.052 * x[2] + 1.0e+4,
                         -0.052 * x[2],
                         0])


@register_eq_class
class BIOMD0000000880(KnownEquation):
    _eq_name = 'odebase_vars4_prog10'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Trisilowati2018 - Optimal control of tumor-immune system interaction with treatment"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0.431*x[0]', '0', '0.234*x[2]', '-1.7e-5*x[3]**2 + 0.017*x[3]']

    def np_eq(self, t, x):
        return np.array([0.431 * x[0],
                         0,
                         0.234 * x[2],
                         -1.7e-5 * x[3] ** 2 + 0.017 * x[3]])


@register_eq_class
class BIOMD0000000741(KnownEquation):
    _eq_name = 'odebase_vars4_prog11'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Eftimie2018 - Cancer and Immune biomarkers"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0.006*x[0]', '-2.079e-9*x[0]*x[1] + 2.079*x[0] - 0.4*x[1]', '4560.0 - 0.11*x[2]',
                         '1.955e+4 - 2.14*x[3]']

    def np_eq(self, t, x):
        return np.array([0.006 * x[0],
                         -2.079e-9 * x[0] * x[1] + 2.079 * x[0] - 0.4 * x[1],
                         4560.0 - 0.11 * x[2],
                         1.955e+4 - 2.14 * x[3]])


@register_eq_class
class BIOMD0000000780(KnownEquation):
    _eq_name = 'odebase_vars4_prog12'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Wang2016/1 - oncolytic efficacy of M1 virus-SNTM model"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.2*x[0]*x[1] - 0.4*x[0]*x[2] - 0.02*x[0] + 0.02', '0.16*x[0]*x[1] - 0.03*x[1]',
                         '0.32*x[0]*x[2] - 0.1*x[2]*x[3] - 0.06*x[2]', '0.05*x[2]*x[3] - 0.03*x[3] + 0.001']

    def np_eq(self, t, x):
        return np.array([-0.2 * x[0] * x[1] - 0.4 * x[0] * x[2] - 0.02 * x[0] + 0.02,
                         0.16 * x[0] * x[1] - 0.03 * x[1],
                         0.32 * x[0] * x[2] - 0.1 * x[2] * x[3] - 0.06 * x[2],
                         0.05 * x[2] * x[3] - 0.03 * x[3] + 0.001])


@register_eq_class
class BIOMD0000000748(KnownEquation):
    _eq_name = 'odebase_vars4_prog13'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Phan2017 - innate immune in oncolytic virotherapy"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.36*x[0]**2 - 0.36*x[0]*x[1] - 0.11*x[0]*x[2] + 0.36*x[0]',
                         '0.11*x[0]*x[2] - 0.48*x[1]*x[3] - 1.0*x[1]',
                         '-0.11*x[0]*x[2] + 9.0*x[1] - 0.16*x[2]*x[3] - 0.2*x[2]', '0.6*x[1]*x[3] - 0.036*x[3]']

    def np_eq(self, t, x):
        return np.array([-0.36 * x[0] ** 2 - 0.36 * x[0] * x[1] - 0.11 * x[0] * x[2] + 0.36 * x[0],
                         0.11 * x[0] * x[2] - 0.48 * x[1] * x[3] - 1.0 * x[1],
                         -0.11 * x[0] * x[2] + 9.0 * x[1] - 0.16 * x[2] * x[3] - 0.2 * x[2],
                         0.6 * x[1] * x[3] - 0.036 * x[3]])


@register_eq_class
class BIOMD0000000904(KnownEquation):
    _eq_name = 'odebase_vars4_prog14'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Admon2017 - Modelling tumor growth with immune response and drug using ordinary differential equations"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.9*x[0]*x[2] - 1.11*x[0] + 1.6*x[1]', '1.0*x[0] - 0.9*x[1]*x[2] - 1.2*x[1]',
                         '-0.085*x[0]*x[2] - 0.085*x[1]*x[2] + 0.1*x[2]*(x[0] + x[1])**3.0/((x[0] + x[1])**3.0 + 0.2) - 0.29*x[2] + 0.029',
                         '0']

    def np_eq(self, t, x):
        return np.array([-0.9 * x[0] * x[2] - 1.11 * x[0] + 1.6 * x[1],
                         1.0 * x[0] - 0.9 * x[1] * x[2] - 1.2 * x[1],
                         -0.085 * x[0] * x[2] - 0.085 * x[1] * x[2] + 0.1 * x[2] * (x[0] + x[1]) ** 3.0 / (
                                     (x[0] + x[1]) ** 3.0 + 0.2) - 0.29 * x[2] + 0.029,
                         0])


@register_eq_class
class BIOMD0000000518(KnownEquation):
    _eq_name = 'odebase_vars4_prog15'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Smallbone2013 - Colon Crypt cycle - Version 2"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = [
            '-0.003065*x[0]**2 + 0.00246*x[0]**2/(x[3] + 1.571) - 0.003065*x[0]*x[1] + 0.00246*x[0]*x[1]/(x[3] + 1.571) - 0.003065*x[0]*x[2] + 0.00246*x[0]*x[2]/(x[3] + 1.571) - 0.003065*x[0]*x[3] + 0.00246*x[0]*x[3]/(x[3] + 1.571) + 0.3678*x[0] - 0.6094*x[0]/(x[3] + 1.571)',
            '-0.01359*x[0]**2 - 0.02238*x[0]*x[1] - 0.01359*x[0]*x[2] - 0.01359*x[0]*x[3] + 1.631*x[0] - 0.008783*x[1]**2 - 0.008783*x[1]*x[2] - 0.008783*x[1]*x[3] + 1.054*x[1] - 1.321*x[1]/(x[3] + 1.571)',
            '-0.04198*x[0]*x[1] - 0.04198*x[1]**2 - 0.04198*x[1]*x[2] - 0.04198*x[1]*x[3] + 5.038*x[1] - 3.461*x[2]/(x[3] + 1.571)',
            '-0.00246*x[0]**2/(x[3] + 1.571) - 0.00246*x[0]*x[1]/(x[3] + 1.571) - 0.00246*x[0]*x[2]/(x[3] + 1.571) - 0.00246*x[0]*x[3]/(x[3] + 1.571) + 0.2952*x[0]/(x[3] + 1.571) - 0.038*x[3]']

    def np_eq(self, t, x):
        return np.array([-0.003065 * x[0] ** 2 + 0.00246 * x[0] ** 2 / (x[3] + 1.571) - 0.003065 * x[0] * x[
            1] + 0.00246 * x[0] * x[1] / (x[3] + 1.571) - 0.003065 * x[0] * x[2] + 0.00246 * x[0] * x[2] / (
                                     x[3] + 1.571) - 0.003065 * x[0] * x[3] + 0.00246 * x[0] * x[3] / (
                                     x[3] + 1.571) + 0.3678 * x[0] - 0.6094 * x[0] / (x[3] + 1.571),
                         -0.01359 * x[0] ** 2 - 0.02238 * x[0] * x[1] - 0.01359 * x[0] * x[2] - 0.01359 * x[0] * x[
                             3] + 1.631 * x[0] - 0.008783 * x[1] ** 2 - 0.008783 * x[1] * x[2] - 0.008783 * x[1] * x[
                             3] + 1.054 * x[1] - 1.321 * x[1] / (x[3] + 1.571),
                         -0.04198 * x[0] * x[1] - 0.04198 * x[1] ** 2 - 0.04198 * x[1] * x[2] - 0.04198 * x[1] * x[
                             3] + 5.038 * x[1] - 3.461 * x[2] / (x[3] + 1.571),
                         -0.00246 * x[0] ** 2 / (x[3] + 1.571) - 0.00246 * x[0] * x[1] / (x[3] + 1.571) - 0.00246 * x[
                             0] * x[2] / (x[3] + 1.571) - 0.00246 * x[0] * x[3] / (x[3] + 1.571) + 0.2952 * x[0] / (
                                     x[3] + 1.571) - 0.038 * x[3]])


@register_eq_class
class BIOMD0000000909(KnownEquation):
    _eq_name = 'odebase_vars4_prog16'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'exp', 'pow']
    _description = "dePillis2003 - The dynamics of an optimally controlled tumor model: A case study"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-1.0*x[0]**2 - 1.0*x[0]*x[1] + 0.9*x[0] + 0.1*x[0]*np.exp(-x[3])',
                         '-1.0*x[0]*x[1] - 1.5*x[1]**2 - 0.5*x[1]*x[2] + 1.2*x[1] + 0.3*x[1]*np.exp(-x[3])',
                         '-1.0*x[1]*x[2] + 0.01*x[1]*x[2]/(x[1] + 0.3) - 0.4*x[2] + 0.2*x[2]*np.exp(-x[3]) + 0.33',
                         '-1.0*x[3]']

    def np_eq(self, t, x):
        return np.array([-1.0 * x[0] ** 2 - 1.0 * x[0] * x[1] + 0.9 * x[0] + 0.1 * x[0] * np.exp(-x[3]),
                         -1.0 * x[0] * x[1] - 1.5 * x[1] ** 2 - 0.5 * x[1] * x[2] + 1.2 * x[1] + 0.3 * x[1] * np.exp(
                             -x[3]),
                         -1.0 * x[1] * x[2] + 0.01 * x[1] * x[2] / (x[1] + 0.3) - 0.4 * x[2] + 0.2 * x[2] * np.exp(
                             -x[3]) + 0.33,
                         -1.0 * x[3]])


@register_eq_class
class BIOMD0000000866(KnownEquation):
    _eq_name = 'odebase_vars4_prog17'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Simon2019 - NIK-dependent p100 processing into p52 Michaelis-Menten SBML 2v4"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0', '-0.05*x[1]*x[3]/(x[1] + 10.0) + 0.5', '0.05*x[1]*x[3]/(x[1] + 10.0)', '0']

    def np_eq(self, t, x):
        return np.array([0,
                         -0.05 * x[1] * x[3] / (x[1] + 10.0) + 0.5,
                         0.05 * x[1] * x[3] / (x[1] + 10.0),
                         0])


@register_eq_class
class BIOMD0000000887(KnownEquation):
    _eq_name = 'odebase_vars4_prog18'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Lim2014 - HTLV-I infection A dynamic struggle between viral persistence and host immunity"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.001*x[0]*x[2] - 0.012*x[0] + 10.0', '0.001*x[0]*x[2] - 0.033*x[1] + 0.011*x[2]',
                         '0.003*x[1] - 0.029*x[2]*x[3] - 0.03*x[2]', '0.036*x[2] - 0.03*x[3]']

    def np_eq(self, t, x):
        return np.array([-0.001 * x[0] * x[2] - 0.012 * x[0] + 10.0,
                         0.001 * x[0] * x[2] - 0.033 * x[1] + 0.011 * x[2],
                         0.003 * x[1] - 0.029 * x[2] * x[3] - 0.03 * x[2],
                         0.036 * x[2] - 0.03 * x[3]])


@register_eq_class
class BIOMD0000000233(KnownEquation):
    _eq_name = 'odebase_vars4_prog19'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Wilhelm2009-BistableReaction"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0', '0', '-1.0*x[2]**2 - 1.0*x[2]*x[3] - 1.5*x[2] + 16.0*x[3]', '1.0*x[2]**2 - 8.0*x[3]']

    def np_eq(self, t, x):
        return np.array([0,
                         0,
                         -1.0 * x[2] ** 2 - 1.0 * x[2] * x[3] - 1.5 * x[2] + 16.0 * x[3],
                         1.0 * x[2] ** 2 - 8.0 * x[3]])


@register_eq_class
class BIOMD0000000642(KnownEquation):
    _eq_name = 'odebase_vars4_prog20'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Mufudza2012 - Estrogen effect on the dynamics of breast cancer"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.3*x[0]**2 - 1.0*x[0]*x[1] + 0.1*x[0]',
                         '0.47*x[0] - 0.4*x[1]**2 - 0.9*x[1]*x[2] + 1.0*x[1]',
                         '-0.085*x[1]*x[2] + 0.2*x[1]*x[2]/(x[1] + 0.3) - 0.4567*x[2] + 0.4', '0']

    def np_eq(self, t, x):
        return np.array([-0.3 * x[0] ** 2 - 1.0 * x[0] * x[1] + 0.1 * x[0],
                         0.47 * x[0] - 0.4 * x[1] ** 2 - 0.9 * x[1] * x[2] + 1.0 * x[1],
                         -0.085 * x[1] * x[2] + 0.2 * x[1] * x[2] / (x[1] + 0.3) - 0.4567 * x[2] + 0.4,
                         0])


@register_eq_class
class BIOMD0000001034(KnownEquation):
    _eq_name = 'odebase_vars4_prog21'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Bunimovich-Mendrazitsky2007 - Mathematical model of BCG immunotherapy"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-1.25*x[0]*x[1] - 0.285*x[0]*x[3] - 1.0*x[0] + 1.9',
                         '0.085*x[0]*x[1] - 0.003*x[1]*x[2] - 0.41*x[1] + 0.52*x[2]', '0.285*x[0]*x[3] - 1.1*x[1]*x[2]',
                         '-0.285*x[0]*x[3] - 0.0018*x[3]**2 + 0.12*x[3]']

    def np_eq(self, t, x):
        return np.array([-1.25 * x[0] * x[1] - 0.285 * x[0] * x[3] - 1.0 * x[0] + 1.9,
                         0.085 * x[0] * x[1] - 0.003 * x[1] * x[2] - 0.41 * x[1] + 0.52 * x[2],
                         0.285 * x[0] * x[3] - 1.1 * x[1] * x[2],
                         -0.285 * x[0] * x[3] - 0.0018 * x[3] ** 2 + 0.12 * x[3]])


@register_eq_class
class BIOMD0000000275(KnownEquation):
    _eq_name = 'odebase_vars4_prog22'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Goldbeter2007-Somitogenesis-Switch"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-1.0*x[0]*x[2] + 4.97', '-1.0*x[1] + 7.1*x[3]**2.0/(x[3]**2.0 + 0.04) + 0.365',
                         '1.0*x[1] - 0.28*x[2]', '-1.0*x[3] + 0.04/(x[0]**2.0 + 0.04)']

    def np_eq(self, t, x):
        return np.array([-1.0 * x[0] * x[2] + 4.97,
                         -1.0 * x[1] + 7.1 * x[3] ** 2.0 / (x[3] ** 2.0 + 0.04) + 0.365,
                         1.0 * x[1] - 0.28 * x[2],
                         -1.0 * x[3] + 0.04 / (x[0] ** 2.0 + 0.04)])


@register_eq_class
class BIOMD0000000876(KnownEquation):
    _eq_name = 'odebase_vars4_prog23'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Aavani2019 - The role of CD4 T cells in immune system activation and viral reproduction in a simple model for HIV infection"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['10.0 - 0.01*x[0]', '-1.0*x[1]*x[2] - 1.0*x[1]',
                         '0.001*x[0]*x[2]*x[3]/(x[2] + 1000.0) - 0.1*x[2]', '2000.0*x[1] - 23.0*x[3]']

    def np_eq(self, t, x):
        return np.array([10.0 - 0.01 * x[0],
                         -1.0 * x[1] * x[2] - 1.0 * x[1],
                         0.001 * x[0] * x[2] * x[3] / (x[2] + 1000.0) - 0.1 * x[2],
                         2000.0 * x[1] - 23.0 * x[3]])


@register_eq_class
class BIOMD0000000875(KnownEquation):
    _eq_name = 'odebase_vars4_prog24'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Nelson2000- HIV-1 general model 1"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['10.0 - 0.03*x[0]', '-0.5*x[1]', '120.0*x[1] - 3.0*x[2]', '120.0*x[1] - 3.0*x[3]']

    def np_eq(self, t, x):
        return np.array([10.0 - 0.03 * x[0],
                         -0.5 * x[1],
                         120.0 * x[1] - 3.0 * x[2],
                         120.0 * x[1] - 3.0 * x[3]])


@register_eq_class
class BIOMD0000000283(KnownEquation):
    _eq_name = 'odebase_vars4_prog25'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Chance1943-Peroxidase-ES-Kinetics"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-1.0*x[0]*x[1]', '-1.0*x[0]*x[1] + 0.5*x[2]', '1.0*x[0]*x[1] - 0.5*x[2]', '0.5*x[2]']

    def np_eq(self, t, x):
        return np.array([-1.0 * x[0] * x[1],
                         -1.0 * x[0] * x[1] + 0.5 * x[2],
                         1.0 * x[0] * x[1] - 0.5 * x[2],
                         0.5 * x[2]])


@register_eq_class
class BIOMD0000000854(KnownEquation):
    _eq_name = 'odebase_vars4_prog26'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Gray2016 - The Akt switch model"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.0077*x[0] + 0.35*x[1] + 0.55*x[2]', '-0.3577*x[1] + 0.55*x[3]',
                         '0.0077*x[0] - 1.32*x[2] + 0.35*x[3]', '0.0077*x[1] + 0.77*x[2] - 0.9*x[3]']

    def np_eq(self, t, x):
        return np.array([-0.0077 * x[0] + 0.35 * x[1] + 0.55 * x[2],
                         -0.3577 * x[1] + 0.55 * x[3],
                         0.0077 * x[0] - 1.32 * x[2] + 0.35 * x[3],
                         0.0077 * x[1] + 0.77 * x[2] - 0.9 * x[3]])


@register_eq_class
class BIOMD0000000363(KnownEquation):
    _eq_name = 'odebase_vars4_prog27'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Lee2010-ThrombinActivation-OneForm-minimal"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.005*x[0]', '0.005*x[0] - 0.01*x[1]', '0.01*x[1]', '0']

    def np_eq(self, t, x):
        return np.array([-0.005 * x[0],
                         0.005 * x[0] - 0.01 * x[1],
                         0.01 * x[1],
                         0])


@register_eq_class
class BIOMD0000001035(KnownEquation):
    _eq_name = 'odebase_vars4_prog28'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Al-Tuwairqi2020 - Dynamics of cancer virotherapy with immune response"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=4, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.36*x[0]**2 - 0.36*x[0]*x[1] - 0.5*x[0]*x[2] - 0.36*x[0]*x[3] + 0.232*x[0]',
                         '0.5*x[0]*x[2] - 0.48*x[1]*x[3] - 1.0*x[1]',
                         '-0.5*x[0]*x[2] + 2.0*x[1] - 0.16*x[2]*x[3] - 0.2*x[2]',
                         '0.29*x[0]*x[3] + 0.6*x[1]*x[3] - 0.16*x[3]']

    def np_eq(self, t, x):
        return np.array([-0.36 * x[0] ** 2 - 0.36 * x[0] * x[1] - 0.5 * x[0] * x[2] - 0.36 * x[0] * x[3] + 0.232 * x[0],
                         0.5 * x[0] * x[2] - 0.48 * x[1] * x[3] - 1.0 * x[1],
                         -0.5 * x[0] * x[2] + 2.0 * x[1] - 0.16 * x[2] * x[3] - 0.2 * x[2],
                         0.29 * x[0] * x[3] + 0.6 * x[1] * x[3] - 0.16 * x[3]])


@register_eq_class
class BIOMD0000000289(KnownEquation):
    _eq_name = 'odebase_vars5_prog1'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Alexander2010-Tcell-Regulation-Sys1"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.5*x[0]', '0.016*x[0]*x[2] + 200.0*x[0] - 0.25*x[1]', '1000.0*x[0] - 0.25*x[2]',
                         '2000.0*x[2] - 5.003*x[3]', '0']

    def np_eq(self, t, x):
        return np.array([-0.5 * x[0],
                         0.016 * x[0] * x[2] + 200.0 * x[0] - 0.25 * x[1],
                         1000.0 * x[0] - 0.25 * x[2],
                         2000.0 * x[2] - 5.003 * x[3],
                         0])


@register_eq_class
class BIOMD0000000980(KnownEquation):
    _eq_name = 'odebase_vars5_prog2'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Malkov2020 - SEIRS model of COVID-19 transmission with time-varying R values and reinfection"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.168*x[0]*x[2]/x[4] + 0.017*x[3]', '0.168*x[0]*x[2]/x[4] - 0.192*x[1]',
                         '0.192*x[1] - 0.056*x[2]', '0.056*x[2] - 0.017*x[3]', '0']

    def np_eq(self, t, x):
        return np.array([-0.168 * x[0] * x[2] / x[4] + 0.017 * x[3],
                         0.168 * x[0] * x[2] / x[4] - 0.192 * x[1],
                         0.192 * x[1] - 0.056 * x[2],
                         0.056 * x[2] - 0.017 * x[3],
                         0])


@register_eq_class
class BIOMD0000000869(KnownEquation):
    _eq_name = 'odebase_vars5_prog3'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Simon2019 - NIK-dependent p100 processing into p52 and IkBd degradation Michaelis-Menten SBML 2v4"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0', '-0.05*x[1]*x[3]/(x[1] + 10.0) + 0.5', '0.05*x[1]*x[3]/(x[1] + 10.0)', '0',
                         '-0.05*x[3]*x[4]/(x[4] + 10.0)']

    def np_eq(self, t, x):
        return np.array([0,
                         -0.05 * x[1] * x[3] / (x[1] + 10.0) + 0.5,
                         0.05 * x[1] * x[3] / (x[1] + 10.0),
                         0,
                         -0.05 * x[3] * x[4] / (x[4] + 10.0)])


@register_eq_class
class BIOMD0000000868(KnownEquation):
    _eq_name = 'odebase_vars5_prog4'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Simon2019 - NIK-dependent p100 processing into p52 Mass Action SBML 2v4"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['0', '-0.005*x[1]*x[3] + 0.5', '0.05*x[4]', '-0.005*x[1]*x[3] + 0.05*x[4]',
                         '0.005*x[1]*x[3] - 0.05*x[4]']

    def np_eq(self, t, x):
        return np.array([0,
                         -0.005 * x[1] * x[3] + 0.5,
                         0.05 * x[4],
                         -0.005 * x[1] * x[3] + 0.05 * x[4],
                         0.005 * x[1] * x[3] - 0.05 * x[4]])


@register_eq_class
class BIOMD0000000851(KnownEquation):
    _eq_name = 'odebase_vars5_prog5'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Ho2019 - Mathematical models of transmission dynamics and vaccine strategies in Hong Kong during the 2017-2018 winter influenza season (Simple)"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-2.752*x[0]*x[3] + 0.1293*x[2] - 0.015', '-1.514*x[1]*x[3] - 0.1293*x[2] + 0.015',
                         '0.015 - 0.1293*x[2]', '2.752*x[0]*x[3] + 1.514*x[1]*x[3] - 2.127*x[3]', '2.127*x[3]']

    def np_eq(self, t, x):
        return np.array([-2.752 * x[0] * x[3] + 0.1293 * x[2] - 0.015,
                         -1.514 * x[1] * x[3] - 0.1293 * x[2] + 0.015,
                         0.015 - 0.1293 * x[2],
                         2.752 * x[0] * x[3] + 1.514 * x[1] * x[3] - 2.127 * x[3],
                         2.127 * x[3]])


@register_eq_class
class BIOMD0000000796(KnownEquation):
    _eq_name = 'odebase_vars5_prog6'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Yang2012 - cancer growth with angiogenesis"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.01*x[0]**2 - 0.01*x[0]*x[2] + 0.09*x[0]', '-0.005*x[1]**2 - 0.01*x[1]*x[2] + 0.05*x[1]',
                         '-0.01*x[0]*x[2] - 0.04*x[2]**2*x[4] + 0.2*x[2]*x[4] - 0.05*x[2]',
                         '0.01*x[1]*x[2] - 0.11*x[3]', '-0.01*x[2]*x[4]**2 + 0.01*x[2]*x[4] + 0.1*x[3] - 0.01*x[4]']

    def np_eq(self, t, x):
        return np.array([-0.01 * x[0] ** 2 - 0.01 * x[0] * x[2] + 0.09 * x[0],
                         -0.005 * x[1] ** 2 - 0.01 * x[1] * x[2] + 0.05 * x[1],
                         -0.01 * x[0] * x[2] - 0.04 * x[2] ** 2 * x[4] + 0.2 * x[2] * x[4] - 0.05 * x[2],
                         0.01 * x[1] * x[2] - 0.11 * x[3],
                         -0.01 * x[2] * x[4] ** 2 + 0.01 * x[2] * x[4] + 0.1 * x[3] - 0.01 * x[4]])


@register_eq_class
class BIOMD0000000629(KnownEquation):
    _eq_name = 'odebase_vars5_prog7'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Haffez2017 - RAR interaction with synthetic analogues"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.6*x[0]*x[2] + 0.1*x[1]', '0.6*x[0]*x[2] - 0.014*x[1]*x[3] - 0.1*x[1] + 0.2*x[4]',
                         '-0.6*x[0]*x[2] + 0.1*x[1]', '-0.014*x[1]*x[3] + 0.2*x[4]', '0.014*x[1]*x[3] - 0.2*x[4]']

    def np_eq(self, t, x):
        return np.array([-0.6 * x[0] * x[2] + 0.1 * x[1],
                         0.6 * x[0] * x[2] - 0.014 * x[1] * x[3] - 0.1 * x[1] + 0.2 * x[4],
                         -0.6 * x[0] * x[2] + 0.1 * x[1],
                         -0.014 * x[1] * x[3] + 0.2 * x[4],
                         0.014 * x[1] * x[3] - 0.2 * x[4]])


@register_eq_class
class BIOMD0000000413(KnownEquation):
    _eq_name = 'odebase_vars5_prog8'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Band2012-DII-Venus-FullModel"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.001*x[0]*x[1] - 0.79*x[0] + 0.334*x[2] + 30.5', '-0.001*x[0]*x[1] + 0.334*x[2]',
                         '0.001*x[0]*x[1] - 1.15*x[2]*x[4] - 0.334*x[2] + 4.665*x[3]', '1.15*x[2]*x[4] - 4.665*x[3]',
                         '-1.15*x[2]*x[4] + 4.49*x[3] - 0.003*x[4] + 0.486']

    def np_eq(self, t, x):
        return np.array([-0.001 * x[0] * x[1] - 0.79 * x[0] + 0.334 * x[2] + 30.5,
                         -0.001 * x[0] * x[1] + 0.334 * x[2],
                         0.001 * x[0] * x[1] - 1.15 * x[2] * x[4] - 0.334 * x[2] + 4.665 * x[3],
                         1.15 * x[2] * x[4] - 4.665 * x[3],
                         -1.15 * x[2] * x[4] + 4.49 * x[3] - 0.003 * x[4] + 0.486])


@register_eq_class
class BIOMD0000000745(KnownEquation):
    _eq_name = 'odebase_vars5_prog9'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Jarrett2018 - trastuzumab-induced immune response in murine HER2+ breast cancer model"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.187*x[0]*x[1] + 0.06701*x[0]*x[4] + 0.044*x[0]',
                         '-0.722*x[0]*x[1] - 0.199*x[1]*x[2] - 0.2*x[1]*x[3] + 0.199*x[2] + 0.2*x[3]',
                         '-1.824*x[0]*x[2] + 0.101*x[0] - 0.045*x[1]*x[2] + 0.045*x[1]',
                         '-0.911*x[1]*x[3] + 0.027*x[2]*x[3] - 0.027*x[2] - 0.027*x[3] + 0.027',
                         '0.743*x[2]*x[4]**2 - 0.743*x[2]*x[4] - 0.211*x[4]**2 + 0.211*x[4]']

    def np_eq(self, t, x):
        return np.array([-0.187 * x[0] * x[1] + 0.06701 * x[0] * x[4] + 0.044 * x[0],
                         -0.722 * x[0] * x[1] - 0.199 * x[1] * x[2] - 0.2 * x[1] * x[3] + 0.199 * x[2] + 0.2 * x[3],
                         -1.824 * x[0] * x[2] + 0.101 * x[0] - 0.045 * x[1] * x[2] + 0.045 * x[1],
                         -0.911 * x[1] * x[3] + 0.027 * x[2] * x[3] - 0.027 * x[2] - 0.027 * x[3] + 0.027,
                         0.743 * x[2] * x[4] ** 2 - 0.743 * x[2] * x[4] - 0.211 * x[4] ** 2 + 0.211 * x[4]])


@register_eq_class
class BIOMD0000000979(KnownEquation):
    _eq_name = 'odebase_vars5_prog10'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Malkov2020 - SEIRS model of COVID-19 transmission with reinfection"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.168*x[0]*x[2]/x[4] + 0.017*x[3]', '0.168*x[0]*x[2]/x[4] - 0.192*x[1]',
                         '0.192*x[1] - 0.056*x[2]', '0.056*x[2] - 0.017*x[3]', '0']

    def np_eq(self, t, x):
        return np.array([-0.168 * x[0] * x[2] / x[4] + 0.017 * x[3],
                         0.168 * x[0] * x[2] / x[4] - 0.192 * x[1],
                         0.192 * x[1] - 0.056 * x[2],
                         0.056 * x[2] - 0.017 * x[3],
                         0])


@register_eq_class
class BIOMD0000000905(KnownEquation):
    _eq_name = 'odebase_vars5_prog11'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Dubey2007 - A mathematical model for the effect of toxicant on the immune system (with toxicant effect) Model2"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.2*x[0]**2 - 0.05*x[0]*x[1] + 0.5*x[0]',
                         '0.295*x[0]*x[1] - 0.3*x[1]*x[4] - 0.8*x[1] + 0.04', '2.4*x[0] - 0.1*x[2]', '5.0 - 0.4*x[3]',
                         '-0.6*x[1]*x[4] + 1.2*x[3] - 0.02*x[4]']

    def np_eq(self, t, x):
        return np.array([-0.2 * x[0] ** 2 - 0.05 * x[0] * x[1] + 0.5 * x[0],
                         0.295 * x[0] * x[1] - 0.3 * x[1] * x[4] - 0.8 * x[1] + 0.04,
                         2.4 * x[0] - 0.1 * x[2],
                         5.0 - 0.4 * x[3],
                         -0.6 * x[1] * x[4] + 1.2 * x[3] - 0.02 * x[4]])


@register_eq_class
class BIOMD0000000916(KnownEquation):
    _eq_name = 'odebase_vars5_prog12'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Kraan199-Kinetics of Cortisol Metabolism and Excretion."

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-26.6*x[0]', '26.6*x[0] - 4.8*x[1] + 1.2*x[3]', '1.2*x[3]', '1.2*x[1] - 2.4*x[3]', '3.6*x[1]']

    def np_eq(self, t, x):
        return np.array([-26.6 * x[0],
                         26.6 * x[0] - 4.8 * x[1] + 1.2 * x[3],
                         1.2 * x[3],
                         1.2 * x[1] - 2.4 * x[3],
                         3.6 * x[1]])


@register_eq_class
class BIOMD0000000886(KnownEquation):
    _eq_name = 'odebase_vars5_prog13'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Dubey2008 - Modeling the interaction between avascular cancerous cells and acquired immune response"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-4.6*x[0]**2 - 0.101*x[0]*x[2] - 0.008*x[0]*x[4] + 0.18*x[0]',
                         '0.3*x[0]*x[1] + 1.5*x[0] - 0.2*x[1]',
                         '0.3*x[0]*x[2] + 1.4*x[0] + 0.05*x[1]*x[2] - 0.041*x[2]',
                         '0.4*x[0]*x[3] + 0.45*x[0] + 0.3*x[1]*x[3] - 0.03*x[3]',
                         '-0.5*x[0]*x[4] + 0.35*x[3] - 0.3*x[4]']

    def np_eq(self, t, x):
        return np.array([-4.6 * x[0] ** 2 - 0.101 * x[0] * x[2] - 0.008 * x[0] * x[4] + 0.18 * x[0],
                         0.3 * x[0] * x[1] + 1.5 * x[0] - 0.2 * x[1],
                         0.3 * x[0] * x[2] + 1.4 * x[0] + 0.05 * x[1] * x[2] - 0.041 * x[2],
                         0.4 * x[0] * x[3] + 0.45 * x[0] + 0.3 * x[1] * x[3] - 0.03 * x[3],
                         -0.5 * x[0] * x[4] + 0.35 * x[3] - 0.3 * x[4]])


@register_eq_class
class BIOMD0000000707(KnownEquation):
    _eq_name = 'odebase_vars5_prog14'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Revilla2003 - Controlling HIV infection using recombinant viruses"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.004*x[0]*x[1] - 0.01*x[0] + 2.0', '-2.0*x[1] + 50.0*x[2]',
                         '0.004*x[0]*x[1] - 0.004*x[2]*x[3] - 0.33*x[2]', '-2.0*x[3] + 2000.0*x[4]',
                         '0.004*x[2]*x[3] - 2.0*x[4]']

    def np_eq(self, t, x):
        return np.array([-0.004 * x[0] * x[1] - 0.01 * x[0] + 2.0,
                         -2.0 * x[1] + 50.0 * x[2],
                         0.004 * x[0] * x[1] - 0.004 * x[2] * x[3] - 0.33 * x[2],
                         -2.0 * x[3] + 2000.0 * x[4],
                         0.004 * x[2] * x[3] - 2.0 * x[4]])


@register_eq_class
class BIOMD0000000798(KnownEquation):
    _eq_name = 'odebase_vars5_prog15'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Sharp2019 - AML"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.5*x[0]**2 + 0.36*x[0]', '0.14*x[0] - 0.43*x[1]**2 - 0.43*x[1]*x[3] - 0.009998*x[1]',
                         '0.44*x[1] - 0.275*x[2]',
                         '-0.27*x[1]*x[3] - 0.27*x[3]**2 + 0.22*x[3] - 0.015*x[3]/(x[3] + 0.01)',
                         '0.05*x[3] - 0.3*x[4]']

    def np_eq(self, t, x):
        return np.array([-0.5 * x[0] ** 2 + 0.36 * x[0],
                         0.14 * x[0] - 0.43 * x[1] ** 2 - 0.43 * x[1] * x[3] - 0.009998 * x[1],
                         0.44 * x[1] - 0.275 * x[2],
                         -0.27 * x[1] * x[3] - 0.27 * x[3] ** 2 + 0.22 * x[3] - 0.015 * x[3] / (x[3] + 0.01),
                         0.05 * x[3] - 0.3 * x[4]])


@register_eq_class
class BIOMD0000000945(KnownEquation):
    _eq_name = 'odebase_vars5_prog16'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Evans2004 - Cell based mathematical model of topotecan"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.029*x[0] + 6.116*x[2]', '0.029*x[0]',
                         '0.001*x[2]*x[4] - 1.07*x[2] + 0.186*x[3] + 1.75*x[4]', '0.027*x[2] - 0.186*x[3]',
                         '-0.0003932*x[2]*x[4] + 0.01136*x[2] - 4.449*x[4]']

    def np_eq(self, t, x):
        return np.array([-0.029 * x[0] + 6.116 * x[2],
                         0.029 * x[0],
                         0.001 * x[2] * x[4] - 1.07 * x[2] + 0.186 * x[3] + 1.75 * x[4],
                         0.027 * x[2] - 0.186 * x[3],
                         -0.0003932 * x[2] * x[4] + 0.01136 * x[2] - 4.449 * x[4]])


@register_eq_class
class BIOMD0000000984(KnownEquation):
    _eq_name = 'odebase_vars5_prog17'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const']
    _description = "Fang2020 - SEIR model of COVID-19 transmission considering government interventions in Wuhan"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-1.0*x[0]*x[2]/x[4]', '1.0*x[0]*x[2]/x[4] - 0.143*x[1]', '0.143*x[1] - 0.098*x[2]',
                         '0.098*x[2]', '0']

    def np_eq(self, t, x):
        return np.array([-1.0 * x[0] * x[2] / x[4],
                         1.0 * x[0] * x[2] / x[4] - 0.143 * x[1],
                         0.143 * x[1] - 0.098 * x[2],
                         0.098 * x[2],
                         0])


@register_eq_class
class BIOMD0000000040(KnownEquation):
    _eq_name = 'odebase_vars5_prog18'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Field1974-Oregonator"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-1.6e+9*x[0]*x[3] - 0.0804*x[0] + 1.0*x[2]', '0', '-1.0*x[2] + 480.0*x[3]',
                         '-1.6e+9*x[0]*x[3] + 0.0804*x[0] - 8.0e+7*x[3]**2 + 480.0*x[3]', '0']

    def np_eq(self, t, x):
        return np.array([-1.6e+9 * x[0] * x[3] - 0.0804 * x[0] + 1.0 * x[2],
                         0,
                         -1.0 * x[2] + 480.0 * x[3],
                         -1.6e+9 * x[0] * x[3] + 0.0804 * x[0] - 8.0e+7 * x[3] ** 2 + 480.0 * x[3],
                         0])


@register_eq_class
class BIOMD0000000914(KnownEquation):
    _eq_name = 'odebase_vars5_prog19'
    _operator_set = ['add', 'sub', 'mul', 'div', 'const', 'pow']
    _description = "Parra-Guillen2013 - Mathematical model approach to describe tumour response in mice after vaccine administration-model1"

    def __init__(self):
        self.vars_range_and_types = [LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True),
                                     LogUniformSampling((1e-2, 10.0), only_positive=True)]
        super().__init__(num_vars=5, vars_range_and_types=self.vars_range_and_types)
        x = self.x
        self.sympy_eq = ['-0.091*x[0]', '0.091*x[0] - 0.091*x[1]', '0.091*x[1] - 0.091*x[2]',
                         '-463.6*x[2]*x[3]/(x[4]**5.24 + 429.3) + 5.24', '0.039*x[3] - 0.039*x[4]']

    def np_eq(self, t, x):
        return np.array([-0.091 * x[0],
                         0.091 * x[0] - 0.091 * x[1],
                         0.091 * x[1] - 0.091 * x[2],
                         -463.6 * x[2] * x[3] / (x[4] ** 5.24 + 429.3) + 5.24,
                         0.039 * x[3] - 0.039 * x[4]])
