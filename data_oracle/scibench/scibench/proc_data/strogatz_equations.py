
"""
A selection of ordinary differential equations primarily from Steven Strogatz's book "Nonlinear Dynamics and Chaos" with manually chosen parameter values and initial conditions.
Some other famous known systems have been selected from other sources, which are included in the dictionary entries as well.
We selected ODEs primarily based on whether they have actually been suggested as models for real-world phenomena as well as on whether they are 'iconic' ODEs in the sense that they are often used as examples in textbooks and/or have recognizable names.
Whenever there were 'realistic' parameter values suggested, we chose those.
In this benchmark, we typically include only one set of parameter values per equation.
Many of the ODEs in Strogatz' book are analyzed in terms of the different limiting behavior for different parameter settings.
For some systems that exhibit wildely different behavior for different parameter settings, we include multiple sets of parameter values as separate equations (e.g., Lorenz system in chaotic and non-chaotic regime).
For each equation, we include two sets of manually chosen initial conditions.
There are 23 equations with dimension 1, 28 equations with dimension 2, 10 equation with dimension 3, and 2 equations with dimension 4.
This results in a total of 63 equations, 4 of which display chaotic behavior.
"""


equations = [
{
    'id': 1,
    'eq': '(c_0 - x_0 / c_1) / c_2',
    'dim': 1,
    'consts': [[0.7, 1.2, 2.31]],
    'init': [[10.], [3.54]],
    'init_constraints': 'x_0 > 0',
    'const_constraints': 'c_1 > 0, c_2 > 0',
    'eq_description': 'RC-circuit (charging capacitor)',
    'const_description': 'c_0: fixed voltage source, c_1: capacitance, c_2: resistance',
    'var_description': 'x_0: charge',
    'source': 'strogatz p.20'
},
{
    'id': 2,
    'eq': 'c_0 * x_0',
    'dim': 1,
    'consts': [[0.23]],
    'init': [[4.78], [0.87]],
    'init_constraints': 'x_0 > 0',
    'const_constraints': '',
    'eq_description': 'Population growth (naive)',
    'const_description': 'c_0: growth rate',
    'var_description': 'x_0: population',
    'source': 'strogatz p.22'
},
{
    'id': 3,
    'eq': 'c_0 * x_0 * (1 - x_0 / c_1)',
    'dim': 1,
    'consts': [[0.79, 74.3]],
    'init': [[7.3], [21.]],
    'init_constraints': 'x_0 > 0',
    'const_constraints': 'c_1 > 0',
    'eq_description': 'Population growth with carrying capacity',
    'const_description': 'c_0: growth rate, c_1: carrying capacity',
    'var_description': 'x_0: population',
    'source': 'strogatz p.22'
},
{
    'id': 4,
    'eq': '1 / (1 + exp(c_0 - x_0 / c_1)) - 0.5',
    'dim': 1,
    'consts': [[0.5, 0.96]],
    'init': [[0.8], [0.02]],
    'init_constraints': 'x_0 > 0',
    'const_constraints': 'c_1 > 0',
    'eq_description': 'RC-circuit with non-linear resistor (charging capacitor)',
    'const_description': 'c_0: fixed voltage source, c_1: capacitance',
    'var_description': 'x_0: charge',
    'source': 'strogatz p.38'
},
{
    'id': 5,
    'eq': 'c_0 - c_1 * x_0^2',
    'dim': 1,
    'consts': [[9.81, 0.0021175]],
    'init': [[0.5], [73.]],
    'init_constraints': '',
    'const_constraints': 'c_0 > 0, c_1 > 0',
    'eq_description': 'Velocity of a falling object with air resistance',
    'const_description': 'c_0: gravitational acceleration, c_1: overall drag for human: 0.5 * C * rho * A / m, with drag coeff C=0.7, air density rho=1.21, cross-sectional area A=0.25, mass m=50',
    'var_description': 'x_0: velocity',
    'source': 'strogatz p.38'
},
{
    'id': 6,
    'eq': 'c_0 * x_0 - c_1 * x_0^2',
    'dim': 1,
    'consts': [[2.1, 0.5]],
    'init': [[0.13], [2.24]],
    'init_constraints': 'x_0 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0',
    'eq_description': 'Autocatalysis with one fixed abundant chemical',
    'const_description': 'c_0: concentration of abundant chemical A times the rate constant of A + X -> 2 X, c_1: rate constant of A + X -> 2X',
    'var_description': 'x_0: concentration of chemical X',
    'source': 'strogatz p.39'
},
{
    'id': 7,
    'eq': 'c_0 * x_0 * log(c_1 * x_0)',
    'dim': 1,
    'consts': [[0.032, 2.29]],
    'init': [[1.73], [9.5]],
    'init_constraints': 'x_0 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0',
    'eq_description': 'Gompertz law for tumor growth',
    'const_description': 'c_0: growth rate, c_1: tumor carrying capacity',
    'var_description': 'x_0: proportional to number of cells (tumor size)',
    'source': 'strogatz p.39'
},
{
    'id': 8,
    'eq': 'c_0 * x_0 * (1 - x_0 / c_1) * (x_0 / c_2 - 1)',
    'dim': 1,
    'consts': [[0.14, 130., 4.4]],
    'init': [[6.123], [2.1]],
    'init_constraints': 'x_0 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0, c_2 > 0',
    'eq_description': 'Logistic equation with Allee effect',
    'const_description': 'c_0: growth rate, c_1: carrying capacity, c_2: Allee effect parameter',
    'var_description': 'x_0: population',
    'source': 'strogatz p.39'
},
{
    'id': 9,
    'eq': '(1 - x_0) * c_0 - x_0 * c_1',
    'dim': 1,
    'consts': [[0.32, 0.28]],
    'init': [[0.14], [0.55]],
    'init_constraints': '0 < x_0 < 1',
    'const_constraints': 'c_0 >= 0, c_1 >= 0',
    'eq_description': 'Language death model for two languages',
    'const_description': 'c_0: rate of language 1 speakers switching to language 2, c_1: rate of language 2 speakers switching to language 1',
    'var_description': 'x_0: proportion of population speaking language 1',
    'source': 'strogatz p.40'
},
{
    'id': 10,
    'eq': '(1 - x_0) * c_0 * x_0^c_1 - x_0 * (1 - c_0) * (1 - x_0)^c_1',
    'dim': 1,
    'consts': [[0.2, 1.2]],
    'init': [[0.83], [0.34]],
    'init_constraints': '0 < x_0 < 1',
    'const_constraints': '0 <= c_0 <= 1, c_1 > 1',
    'eq_description': 'Refined language death model for two languages',
    'const_description': 'c_0: perceived status of language 1, c_1: adjustable exponent',
    'var_description': 'x_0: proportion of population speaking language 1',
    'source': 'strogatz p.40'
},
{
    'id': 11,
    'eq': '- x_0^3',
    'dim': 1,
    'consts': [[]],
    'init': [[3.4], [1.6]],
    'init_constraints': '',
    'const_constraints': '',
    'eq_description': 'Naive critical slowing down (statistical mechanics)',
    'const_description': '',
    'var_description': 'x_0: order parameter',
    'source': 'strogatz p.41'
},
{
    'id': 12,
    'eq': 'c_0 * x_0 - c_1 * x_0^2',
    'dim': 1,
    'consts': [[1.8, 0.1107]],
    'init': [[11.], [1.3]],
    'init_constraints': 'x_0 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0',
    'eq_description': 'Photons in a laser (simple)',
    'const_description': 'c_0: G * N0 - k, for G: gain coefficient, N0: initial excited atoms, k: loss rate, c_1: alpha * G, for G: gain coefficient, alpha: rate of atoms dropping back to ground state',
    'var_description': 'x_0: number of photons',
    'source': 'strogatz p.55'
},
{
    'id': 13,
    'eq': 'c_0 * sin(x_0) * (c_1 * cos(x_0) - 1)',
    'dim': 1,
    'consts': [[0.0981, 9.7]],
    'init': [[3.1], [2.4]],
    'init_constraints': '',
    'const_constraints': 'c_0 > 0, c_1 > 0',
    'eq_description': 'Overdamped bead on a rotating hoop',
    'const_description': 'c_0: m * g, for m: mass, g: gravitational acceleration, c_1: r * omega^2 / g, for r: radius, omega: angular velocity',
    'var_description': 'x_0: angle',
    'source': 'strogatz p.63'
},
{
    'id': 14,
    'eq': 'c_0 * x_0 * (1 - x_0 / c_1) - c_3 * x_0^2 / (c_2^2 + x_0^2)',
    'dim': 1,
    'consts': [[0.78, 81., 21.2, 0.9]],
    'init': [[2.76], [23.3]],
    'init_constraints': 'x_0 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0, c_2 > 0, c_3 > 0',
    'eq_description': 'Budworm outbreak model with predation',
    'const_description': 'c_0: growth rate, c_1: carrying capacity, c_2: predation onset, c_3: predation limit',
    'var_description': 'x_0: population',
    'source': 'strogatz p.75'
},
{
    'id': 15,
    'eq': 'c_0 * x_0 * (1 - x_0 / c_1) - x_0^2 / (1 + x_0^2)',
    'dim': 1,
    'consts': [[0.4, 95.]],
    'init': [[44.3], [4.5]],
    'init_constraints': 'x_0 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0',
    'eq_description': 'Budworm outbreak with predation (dimensionless)',
    'const_description': 'c_0: growth rate (<0.5 for young forest, 1 for mature), c_1: carrying capacity (~300 for young forest)',
    'var_description': 'x_0: population',
    'source': 'strogatz p.76'
},
{
    'id': 16,
    'eq': 'c_0 * x_0 - c_1 * x_0^3 - c_2 * x_0^5',
    'dim': 1,
    'consts': [[0.1, -0.04, 0.001]],
    'init': [[0.94], [1.65]],
    'init_constraints': '',
    'const_constraints': 'c_0 > 0',
    'eq_description': 'Landau equation (typical time scale tau = 1)',
    'const_description': 'c_0: small dimensionless parameter, c_1: constant, c_2: constant; c_1 > 0 for supercritical bifurcation; c_1 < 0 and c_2 > 0 for subcritical bifurcation',
    'var_description': 'x_0: order parameter',
    'source': 'strogatz p.87'
},
{
    'id': 17,
    'eq': 'c_0 * x_0 * (1 - x_0 / c_1) - c_2',
    'dim': 1,
    'consts': [[0.4, 100., 0.3]],
    'init': [[14.3], [34.2]],
    'init_constraints': 'x_0 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0, c_2 >= 0',
    'eq_description': 'Logistic equation with harvesting/fishing',
    'const_description': 'c_0: growth rate, c_1: carrying capacity, c_2: harvesting rate',
    'var_description': 'x_0: population',
    'source': 'strogatz p.89'
},
{
    'id': 18,
    'eq': 'c_0 * x_0 * (1 - x_0 / c_1) - c_2 * x_0 / (c_3 + x_0)',
    'dim': 1,
    'consts': [[0.4, 100., 0.24, 50.]],
    'init': [[21.1], [44.1]],
    'init_constraints': 'x_0 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0, c_2 > 0, c_3 > 0',
    'eq_description': 'Improved logistic equation with harvesting/fishing',
    'const_description': 'c_0: growth rate, c_1: carrying capacity, c_2: harvesting rate, c_3: harvesting onset',
    'var_description': 'x_0: population',
    'source': 'strogatz p.90'
},
{
    'id': 19,
    'eq': 'x_0 * (1 - x_0) - c_0 * x_0 / (c_1 + x_0)',
    'dim': 1,
    'consts': [[0.08, 0.8]],
    'init': [[0.13], [0.03]],
    'init_constraints': 'x_0 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0',
    'eq_description': 'Improved logistic equation with harvesting/fishing (dimensionless)',
    'const_description': 'c_0: harvesting rate, c_1: harvesting onset',
    'var_description': 'x_0: population',
    'source': 'strogatz p.90'
},
{
    'id': 20,
    'eq': 'c_0 - c_1 * x_0 + x_0^2 / (1 + x_0^2)',
    'dim': 1,
    'consts': [[0.1, 0.55]],
    'init': [[0.002], [0.25]],
    'init_constraints': 'x_0 > 0',
    'const_constraints': 'c_0 >= 0, c_1 > 0',
    'eq_description': 'Autocatalytic gene switching (dimensionless)',
    'const_description': 'c_0: basal production rate, c_1: degradation rate',
    'var_description': 'x_0: gene product',
    'source': 'strogatz p.91'
},
{
    'id': 21,
    'eq': 'c_0 - c_1 * x_0 - exp(-x_0)',
    'dim': 1,
    'consts': [[1.2, 0.2]],
    'init': [[0.], [0.8]],
    'init_constraints': 'x_0 >= 0',
    'const_constraints': 'c_0 >= 1, c_1 > 0',
    'eq_description': 'Dimensionally reduced SIR infection model for dead people (dimensionless)',
    'const_description': 'c_0: death rate, c_1: unknown parameter group',
    'var_description': 'x_0: dead people',
    'source': 'strogatz p.92'
},
{
    'id': 22,
    'eq': 'c_0 + c_1 * x_0^5 / (c_2 + x_0^5) - c_3 * x_0',
    'dim': 1,
    'consts': [[1.4, 0.4, 123., 0.89]],
    'init': [[3.1], [6.3]],
    'init_constraints': 'x_0 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0, c_2 > 0, c_3 > 0',
    'eq_description': 'Hysteretic activation of a protein expression (positive feedback, basal promoter expression)',
    'const_description': 'c_0: basal transcription rate, c_1: maximum transcription rate, c_2: activation coefficient, c_3: decay rate',
    'var_description': 'x_0: protein concentration',
    'source': 'strogatz p.93'
},
{
    'id': 23,
    'eq': 'c_0 - sin(x_0)',
    'dim': 1,
    'consts': [[0.21]],
    'init': [[-2.74], [1.65]],
    'init_constraints': '-pi <= x_0 <= pi',
    'const_constraints': 'c_0 > 0',
    'eq_description': 'Overdamped pendulum with constant driving torque/fireflies/Josephson junction (dimensionless)',
    'const_description': 'c_0: ratio of driving torque to maximum gravitational torque',
    'var_description': 'x_0: angle',
    'source': 'strogatz p.104'
},
{
    'id': 24,
    'eq': 'x_1 | - c_0 * x_0',
    'dim': 2,
    'consts': [[2.1]],
    'init': [[0.4, -0.03], [0.0, 0.2]],
    'init_constraints': '',
    'const_constraints': 'c_0 > 0',
    'eq_description': 'Harmonic oscillator without damping',
    'const_description': 'c_0: spring constant to mass ratio',
    'var_description': 'x_0: position, x_1: velocity',
    'source': 'strogatz p.126'
},
{
    'id': 25,
    'eq': 'x_1 | - c_0 * x_0 - c_1 * x_1',
    'dim': 2,
    'consts': [[4.5, 0.43]],
    'init': [[0.12, 0.043], [0.0, -0.3]],
    'init_constraints': '',
    'const_constraints': 'c_0 > 0, c_1 > 0',
    'eq_description': 'Harmonic oscillator with damping',
    'const_description': 'c_0: spring constant to mass ratio, c_1: damping coefficient to mass ratio',
    'var_description': 'x_0: position, x_1: velocity',
    'source': 'strogatz p.144'
},
{
    'id': 26,
    'eq': 'x_0 * (c_0 - x_0 - c_1 * x_1) | x_1 * (c_2 - x_0 - x_1)',
    'dim': 2,
    'consts': [[3., 2., 2.]],
    'init': [[5.0, 4.3], [2.3, 3.6]],
    'init_constraints': 'x_0 > 0, x_1 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0, c_2 > 0',
    'eq_description': 'Lotka-Volterra competition model (Strogatz version with sheeps and rabbits)',
    'const_description': 'c_0: growth rate of rabbits, c_1: death rate of rabbits due to sheeps, c_2: growth rate of sheeps',
    'var_description': 'x_0: rabbits, x_1: sheeps',
    'source': 'strogatz p.157'
},
{
    'id': 27,
    'eq': 'x_0 * (c_0 - c_1 * x_1) | - x_1 * (c_2 - c_3 * x_0)',
    'dim': 2,
    'consts': [[1.84, 1.45, 3.0, 1.62]],
    'init': [[8.3, 3.4], [0.4, 0.65]],
    'init_constraints': 'x_0 > 0, x_1 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0, c_2 > 0, c_3 > 0',
    'eq_description': 'Lotka-Volterra simple (as on Wikipedia)',
    'const_description': 'c_0: growth rate of prey without predators, c_1: killing rate of prey due to predators, c_2: death rate of predators without prey, c_3: growth rate of predators per prey',
    'var_description': 'x_0: prey, x_1: predators',
    'source': 'Lotka-Volterra'
},
{
    'id': 28,
    'eq': 'x_1 | - c_0 * sin(x_0)',
    'dim': 2,
    'consts': [[0.9]],
    'init': [[-1.9, 0.], [0.3, 0.8]],
    'init_constraints': '-pi <= x_0 <= pi',
    'const_constraints': 'c_0 > 0',
    'eq_description': 'Pendulum without friction',
    'const_description': 'c_0: gravitational acceleration to length ratio',
    'var_description': 'x_0: angle, x_1: angular velocity',
    'source': 'strogatz p.169'
},
{
    'id': 29,
    'eq': 'c_0 * x_0 * x_1 | x_1^2 - x_0^2',
    'dim': 2,
    'consts': [[0.65]],
    'init': [[3.2, 1.4], [1.3, 0.2]],
    'init_constraints': '',
    'const_constraints': 'c_0 > 0',
    'eq_description': 'Dipole fixed point',
    'const_description': 'c_0: constant',
    'var_description': 'x_0: x, x_1: y',
    'source': 'strogatz p.181'
},
{
    'id': 30,
    'eq': 'x_0 * (x_1 - c_0 * x_0 * x_1) | x_1 * (x_0 - c_0 * x_0 * x_1)',
    'dim': 2,
    'consts': [[1.61]],
    'init': [[0.3, 0.04], [0.1, 0.21]],
    'init_constraints': 'x_0 > 0, x_1 > 0',
    'const_constraints': 'c_0 > 0',
    'eq_description': 'RNA molecules catalyzing each others replication',
    'const_description': 'c_0: catalytic rate',
    'var_description': 'x_0: concentration of molecule 1, x_1: concentration of molecule 2',
    'source': 'strogatz p.187'
},
{
    'id': 31,
    'eq': '- c_0 * x_0 * x_1 | c_0 * x_0 * x_1 - c_1 * x_1',
    'dim': 2,
    'consts': [[0.4, 0.314]],
    'init': [[7.2, 0.98], [20., 12.4]],
    'init_constraints': 'x_0 > 0, x_1 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0',
    'eq_description': 'SIR infection model only for healthy and sick',
    'const_description': 'c_0: recovery rate, c_1: infection rate',
    'var_description': 'x_0: healthy, x_1: sick',
    'source': 'strogatz p.188'
},
{
    'id': 32,
    'eq': 'x_1 | - c_0 * x_1 + x_0 - x_0^3',
    'dim': 2,
    'consts': [[0.18]],
    'init': [[-1.8, -1.8], [5.8, 0.]],
    'init_constraints': '',
    'const_constraints': 'c_0 > 0',
    'eq_description': 'Damped double well oscillator',
    'const_description': 'c_0: damping coefficient',
    'var_description': 'x_0: position, x_1: velocity',
    'source': 'strogatz p.190'
},
{
    'id': 33,
    'eq': '- sin(x_1) - c_0 * x_0^2 | x_0 - cos(x_1) / x_0',
    'dim': 2,
    'consts': [[0.08]],
    'init': [[5.0, 0.7], [9.81, -0.8]],
    'init_constraints': 'x_0 > 0',
    'const_constraints': 'c_0 > 0',
    'eq_description': 'Glider (dimensionless)',
    'const_description': 'c_0: drag coefficient',
    'var_description': 'x_0: speed, x_1: angle to horizontal',
    'source': 'strogatz p.190'
},
{
    'id': 34,
    'eq': 'x_1 | sin(x_0) * (cos(x_0) - c_0)',
    'dim': 2,
    'consts': [[0.93]],
    'init': [[2.1, 0.], [-1.2, -0.2]],
    'init_constraints': '',
    'const_constraints': 'c_0 > 0',
    'eq_description': 'Frictionless bead on a rotating hoop (dimensionless)',
    'const_description': 'c_0: gravitational acceleration over radius times omega^2',
    'var_description': 'x_0: angle, x_1: angular velocity',
    'source': 'strogatz p.191'
},
{
    'id': 35,
    'eq': 'cot(x_1) * cos(x_0) | sin(x_0) * (cos(x_1)^2 + c_0 * sin(x_1)^2)',
    'dim': 2,
    'consts': [[4.2]],
    'init': [[1.13, -0.3], [2.4, 1.7]],
    'init_constraints': '-pi < x_0 <= pi, -pi / 2 <= x_1 <= pi / 2',
    'const_constraints': 'c_0 > 0',
    'eq_description': 'Rotational dynamics of an object in a shear flow',
    'const_description': 'c_0: shape dependent parameter',
    'var_description': 'x_0: longitude (angle around z-axis), x_1: latitue (angle from north)',
    'source': 'strogatz p.194'
},
{
    'id': 36,
    'eq': 'x_1 | - sin(x_0) - x_1 - c_0 * cos(x_0) * x_1',
    'dim': 2,
    'consts': [[0.07]],
    'init': [[0.45, 0.9], [1.34, -0.8]],
    'init_constraints': '-pi < x_o < pi',
    'const_constraints': 'c_0 > 0',
    'eq_description': 'Pendulum with non-linear damping, no driving (dimensionless)',
    'const_description': 'c_0: Damping coefficient',
    'var_description': 'x_0: angle, x_1: angular velocity',
    'source': 'strogatz p.195'
},
{
    'id': 37,
    'eq': 'x_1 | - x_0 - c_0 * (x_0^2 - 1) * x_1',
    'dim': 2,
    'consts': [[0.43]],
    'init': [[2.2, 0.], [0.1, 3.2]],
    'init_constraints': '',
    'const_constraints': 'c_0 > 0',
    'eq_description': 'Van der Pol oscillator (standard form)',
    'const_description': 'c_0: damping parameter for nonlinear damping term',
    'var_description': 'x_0: position, x_1: velocity',
    'source': 'strogatz p.200'
},
{
    'id': 38,
    'eq': 'c_0 * (x_1 - x_0^3 / 3 + x_0) | - x_0 / c_0',
    'dim': 2,
    'consts': [[3.37]],
    'init': [[0.7, 0.], [-1.1, -0.7]],
    'init_constraints': '',
    'const_constraints': 'c_0 > 0',
    'eq_description': 'Van der Pol oscillator (simplified form from Strogatz)',
    'const_description': 'c_0: damping parameter for nonlinear damping term',
    'var_description': 'x_0: position, x_1: velocity',
    'source': 'strogatz p.214'
},
{
    'id': 39,
    'eq': '- x_0 + c_0 * x_1 + x_0^2 * x_1 | c_1 - c_0 * x_0 - x_0^2 * x_1',
    'dim': 2,
    'consts': [[2.4, 0.07]],
    'init': [[0.4, 0.31], [0.2, -0.7]],
    'init_constraints': 'x_0 > 0, x_1 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0',
    'eq_description': 'Glycolytic oscillator, e.g., ADP and F6P in yeast (dimensionless)',
    'const_description': 'c_0: kinetic parameter, c_1: kinetic parameter',
    'var_description': 'x_0: concentration of ADP, x_1: concentration of F6P',
    'source': 'strogatz p.207'
},
{
    'id': 40,
    'eq': 'x_1 | - x_0 + c_0 * x_1 * (1 - x_0^2)',
    'dim': 2,
    'consts': [[0.886]],
    'init': [[0.63, -0.03], [0.2, 0.2]],
    'init_constraints': '',
    'const_constraints': 'c_0 > 0',
    'eq_description': 'Duffing equation (weakly non-linear oscillation)',
    'const_description': 'c_0: parameter for cubic nonlinearity',
    'var_description': 'x_0: position, x_1: velocity',
    'source': 'strogatz p.217'
},
{
    'id': 41,
    'eq': 'c_0 * (x_1 - x_0) * (c_1 + x_0^2) - x_0 | c_2 - x_0',
    'dim': 2,
    'consts': [[15.3, 0.001, 0.3]],
    'init': [[0.8, 0.3], [0.02, 1.2]],
    'init_constraints': 'x_0 > 0, x_1 > 0',
    'const_constraints': 'c_0 > 1, 0 < c_1 < 1, c_2 > 0, 8 * c_0 * c_1 < 1',
    'eq_description': 'Cell cycle model by Tyson for interaction between protein cdc2 and cyclin (dimensionless)',
    'const_description': 'c_0: parameter >> 1, c_1: parameter << 1, c_2: adjustable parameter',
    'var_description': 'x_0: concentration of cdc2, x_1: concentration of cyclin',
    'source': 'strogatz p.238'
},
{
    'id': 42,
    'eq': 'c_0 - x_0 - c_1 * x_0 * x_1 / (1 + x_0^2) | c_2 * x_0 * (1 - x_1 / (1 + x_0^2))',
    'dim': 2,
    'consts': [[8.9, 4.0, 1.4]],
    'init': [[0.2, 0.35], [3.0, 7.8]],
    'init_constraints': 'x_0 > 0, x_1 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0, c_2 > 0',
    'eq_description': 'Reduced model for chlorine dioxide-iodine-malonic acid rection (dimensionless)',
    'const_description': 'c_0: empirical rate parameter, c_1: fixed to 4 by strogatz, c_2: empirical rate parameter',
    'var_description': 'x_0: dimensionless I- concentration, x_1: dimensionless ClO2 concentration',
    'source': 'strogatz p.260'
},
{
    'id': 43,
    'eq': 'x_1 | c_0 - sin(x_0) - c_1 * x_1',
    'dim': 2,
    'consts': [[1.67, 0.64]],
    'init': [[1.47, -0.2], [-1.9, 0.03]],
    'init_constraints': '',
    'const_constraints': 'c_0 > 0, c_1 > 0',
    'eq_description': 'Driven pendulum with linear damping / Josephson junction (dimensionless)',
    'const_description': 'c_0: driving force/current, c_1: damping parameter',
    'var_description': 'x_0: angle, x_1: angular velocity',
    'source': 'strogatz p.269'
},
{
    'id': 44,
    'eq': 'x_1 | c_0 - sin(x_0) - c_1 * x_1 * abs(x_1)',
    'dim': 2,
    'consts': [[1.67, 0.64]],
    'init': [[1.47, -0.2], [-1.9, 0.03]],
    'init_constraints': '',
    'const_constraints': 'c_0 > 0, c_1 > 0',
    'eq_description': 'Driven pendulum with quadratic damping (dimensionless)',
    'const_description': 'c_0: driving torque, c_1: damping parameter',
    'var_description': 'x_0: angle, x_1: angular velocity',
    'source': 'strogatz p.300'
},
{
    'id': 45,
    'eq': 'c_0 * (1 - x_0) - x_0 * x_1^2 | x_0 * x_1^2 - c_1 * x_1',
    'dim': 2,
    'consts': [[0.5, 0.02]],
    'init': [[1.4, 0.2], [0.32, 0.64]],
    'init_constraints': 'x_0 > 0, x_1 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0',
    'eq_description': 'Isothermal autocatalytic reaction model by Gray and Scott 1985 (dimensionless)',
    'const_description': 'c_0: rate constant, c_1: rate constant',
    'var_description': 'x_0: concentration 1, x_1: concentration 2',
    'source': 'strogatz p.288'
},
{
    'id': 46,
    'eq': 'c_0 * sin(x_0 - x_1) - sin(x_0) | c_0 * sin(x_1 - x_0) - sin(x_1)',
    'dim': 2,
    'consts': [[0.33]],
    'init': [[0.54, -0.1], [0.43, 1.21]],
    'init_constraints': '',
    'const_constraints': 'c_0 > 0',
    'eq_description': 'Interacting bar magnets',
    'const_description': 'c_0: coupling constant',
    'var_description': 'x_0: angle of magnet 1, x_1: angle of magnet 2',
    'source': 'strogatz p.289'
},
{
    'id': 47,
    'eq': '- x_0 + 1 / (1 + exp(c_0 * x_1 - c_1)) | - x_1 + 1 / (1 + exp(c_0 * x_0 - c_1))',
    'dim': 2,
    'consts': [[4.89, 1.4]],
    'init': [[0.65, 0.59], [3.2, 10.3]],
    'init_constraints': 'x_0 > 0, x_1 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0',
    'eq_description': 'Binocular rivalry model (no oscillations)',
    'const_description': 'c_0: strength of mutual antagonism, c_1: strength of input stimulus',
    'var_description': 'x_0: perception of left eye stimulus, x_1: perception of right eye stimulus',
    'source': 'strogatz p.290'
},
{
    'id': 48,
    'eq': 'c_0 - x_0 - x_0 * x_1 / (1 + c_1 * x_0^2) | c_2 - x_0 * x_1 / (1 + c_1 * x_0^2)',
    'dim': 2,
    'consts': [[18.3, 0.48, 11.23]],
    'init': [[0.1, 30.4], [13.2, 5.21]],
    'init_constraints': 'x_0 > 0, x_1 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0, c_2 > 0',
    'eq_description': 'Bacterial respiration model for nutrients and oxygen levels',
    'const_description': 'c_0: parameter, c_1: parameter, c_2: parameter',
    'var_description': 'x_0: concentration of nutrients, x_1: concentration of oxygen',
    'source': 'strogatz p.293'
},
{
    'id': 49,
    'eq': '1 - (c_0 + 1) * x_0 + c_1 * x_0^2 * x_1 | c_0 * x_0 - c_1 * x_0^2 * x_1',
    'dim': 2,
    'consts': [[3.03, 3.1]],
    'init': [[0.7, -1.4], [2.1, 1.3]],
    'init_constraints': 'x_0 > 0, x_1 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0',
    'eq_description': 'Brusselator: hypothetical chemical oscillation model (dimensionless)',
    'const_description': 'c_0: parameter, c_1: parameter',
    'var_description': 'x_0: concentration of X, x_1: concentration of Y',
    'source': 'strogatz p.296'
},
{
    'id': 50,
    'eq': 'c_0 - x_0 + x_0^2 * x_1 | c_1 - x_0^2 * x_1',
    'dim': 2,
    'consts': [[0.24, 1.43]],
    'init': [[0.14, 0.6], [1.5, 0.9]],
    'init_constraints': 'x_0 > 0, x_1 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0',
    'eq_description': 'Chemical oscillator model by Schnackenberg 1979 (dimensionless)',
    'const_description': 'c_0: parameter, c_1: parameter',
    'var_description': 'x_0: concentration of X, x_1: concentration of Y',
    'source': 'strogatz p.296'
},
{
    'id': 51,
    'eq': 'c_0 + sin(x_1) * cos(x_0) | c_1 + sin(x_1) * cos(x_0)',
    'dim': 2,
    'consts': [[1.432, 0.972]],
    'init': [[2.2, 0.67], [0.03, -0.12]],
    'init_constraints': '-pi < x_0 < pi, -pi < x_1 < pi',
    'const_constraints': 'c_0 > 0, c_1 > 0',
    'eq_description': 'Oscillator death model by Ermentrout and Kopell 1990',
    'const_description': 'c_0: driving torque 1, c_1: driving torque 2',
    'var_description': 'x_0: angle 1, x_1: angle 2',
    'source': 'strogatz p.301'
},
{
    'id': 52,
    'eq': 'c_0 * (x_1 - x_0) | c_1 * (x_0 * x_2 - x_1) | c_2 * (c_3 + 1 - x_2 - c_3 * x_0 * x_1)',
    'dim': 3,
    'consts': [[0.1, 0.21, 0.34, 3.1]],
    'init': [[1.3, 1.1, 0.89], [0.89, 1.3, 1.1]],
    'init_constraints': 'x_0 > 0, x_1 > 0, x_2 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0, c_2 > 0, c_3 > 0',
    'eq_description': 'Maxwell-Bloch equations (laser dynamics)',
    'const_description': 'c_0: decay rate in cavity, c_1: decay rate atomic polarization, c_2: decay rate population inversion, c_3: pumping energy parameter',
    'var_description': 'x_0: E, x_1: P, x_2: D',
    'source': 'strogatz p.82'
},
{
    'id': 53,
    'eq': 'c_0 - c_5 * x_1 * x_0 / (c_9 + x_0) - c_4 * x_0 | c_1 * x_2 * (c_8 + x_1) - c_2 * x_1 / (c_6 + x_1) - c_3 * x_0 * x_1 / (c_7 + x_1) | - c_1 * x_2 * (c_8 + x_1) + c_2 * x_1 / (c_6 + x_1) + c_3 * x_0 * x_1 / (c_7 + x_1)',
    'dim': 3,
    'consts': [[0.1, 0.6, 0.2, 7.95, 0.05, 0.4, 0.1, 2.0, 0.1, 0.1]],
    'init': [[0.005, 0.26, 2.15], [0.248, 0.0973, 0.0027]],
    'init_constraints': 'x_0 > 0, x_1 > 0, x_2 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0, c_2 > 0, c_3 > 0, c_4 > 0, c_5 > 0, c_6 > 0, c_7 > 0, c_8 > 0, c_9 > 0',
    'eq_description': 'Model for apoptosis (cell death)',
    'const_description': 'c_0: parameter, c_1: parameter, c_2: parameter, c_3: parameter, c_4: parameter, c_5: parameter, c_6: parameter, c_7: parameter, c_8: parameter, c_9: parameter',
    'var_description': 'x_0: x, x_1: y, x_2: z',
    'source': 'Model for apoptosis',
},
{
    'id': 54,
    'eq': 'c_0 * (x_1 - x_0) | c_1 * x_0 - x_1 - x_0 * x_2 | x_0 * x_1 - c_2 * x_2',
    'dim': 3,
    'consts': [[5.1, 12., 1.67]],
    'init': [[2.3, 8.1, 12.4], [10., 20., 30.]],
    'init_constraints': 'x_0 > 0, x_1 > 0, x_2 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0, c_2 > 0',
    'eq_description': 'Lorenz equations in well-behaved periodic regime',
    'const_description': 'c_0: Prandtl number (sigma), c_1: Rayleigh number (r), c_2: unnamed parameter (b)',
    'var_description': 'x_0: x, x_1: y, x_2: z',
    'source': 'strogatz p.319'
},
{
    'id': 55,
    'eq': 'c_0 * (x_1 - x_0) | c_1 * x_0 - x_1 - x_0 * x_2 | x_0 * x_1 - c_2 * x_2',
    'dim': 3,
    'consts': [[10., 99.96, 8. / 3.]],
    'init': [[2.3, 8.1, 12.4], [10., 20., 30.]],
    'init_constraints': 'x_0 > 0, x_1 > 0, x_2 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0, c_2 > 0',
    'eq_description': 'Lorenz equations in complex periodic regime',
    'const_description': 'c_0: Prandtl number (sigma), c_1: Rayleigh number (r), c_2: unnamed parameter (b)',
    'var_description': 'x_0: x, x_1: y, x_2: z',
    'source': 'strogatz p.319'
},
{
    'id': 56,
    'eq': 'c_0 * (x_1 - x_0) | c_1 * x_0 - x_1 - x_0 * x_2 | x_0 * x_1 - c_2 * x_2',
    'dim': 3,
    'consts': [[10., 28., 8. / 3.]],
    'init': [[2.3, 8.1, 12.4], [10., 20., 30.]],
    'init_constraints': 'x_0 > 0, x_1 > 0, x_2 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0, c_2 > 0',
    'eq_description': 'Lorenz equations standard parameters (chaotic)',
    'const_description': 'c_0: Prandtl number (sigma), c_1: Rayleigh number (r), c_2: unnamed parameter (b)',
    'var_description': 'x_0: x, x_1: y, x_2: z',
    'source': 'strogatz p.319'
},
{
    'id': 57,
    'eq': 'c_3 * (- x_1 - x_2) | c_3 * (x_0  + c_0 * x_1) | c_3 * (c_1 + x_2 * (x_0 - c_2))',
    'dim': 3,
    'consts': [[-0.2, 0.2, 5.7, 5.]],
    'init': [[2.3, 1.1, 0.8], [-0.1, 4.1, -2.1]],
    'init_constraints': '',
    'const_constraints': 'c_1 > 0, c_2 > 0',
    'eq_description': 'Rössler attractor (stable fixed point)',
    'const_description': 'c_0: parameter, c_1: parameter, c_2: parameter, c_3: just for time scaling',
    'var_description': 'x_0: x, x_1: y, x_2: z',
    'source': 'Rossler_attractor',
},
{
    'id': 58,
    'eq': 'c_3 * (- x_1 - x_2) | c_3 * (x_0  + c_0 * x_1) | c_3 * (c_1 + x_2 * (x_0 - c_2))',
    'dim': 3,
    'consts': [[0.1, 0.2, 5.7, 5.]],
    'init': [[2.3, 1.1, 0.8], [-0.1, 4.1, -2.1]],
    'init_constraints': '',
    'const_constraints': 'c_1 > 0, c_2 > 0',
    'eq_description': 'Rössler attractor (periodic)',
    'const_description': 'c_0: parameter, c_1: parameter, c_2: parameter, c_3: just for time scaling',
    'var_description': 'x_0: x, x_1: y, x_2: z',
    'source': 'Rossler_attractor_periodic',
},
{
    'id': 59,
    'eq': 'c_3 * (- x_1 - x_2) | c_3 * (x_0  + c_0 * x_1) | c_3 * (c_1 + x_2 * (x_0 - c_2))',
    'dim': 3,
    'consts': [[0.2, 0.2, 5.7, 5.]],
    'init': [[2.3, 1.1, 0.8], [-0.1, 4.1, -2.1]],
    'init_constraints': '',
    'const_constraints': 'c_1 > 0, c_2 > 0',
    'eq_description': 'Rössler attractor (chaotic)',
    'const_description': 'c_0: parameter, c_1: parameter, c_2: parameter, c_3: just for time scaling',
    'var_description': 'x_0: x, x_1: y, x_2: z',
    'source': 'Rossler_attractor_chaotic',
},
{
    'id': 60,
    'eq': 'x_0 * (x_2 - c_1) - c_3 * x_1 | c_3 * x_0 + x_1 * (x_2 - c_1) | c_2 + c_0 * x_2 - x_2^3 / 3. - (x_0^2 + x_1^2) * (1 + c_4 * x_2) + c_5 * x_2 * x_0^3',
    'dim': 3,
    'consts': [[0.95, 0.7, 0.65, 3.5, 0.25, 0.1]],
    'init': [[0.1, 0.05, 0.05], [-0.3, 0.2, 0.1]],
    'init_constraints': '',
    'const_constraints': 'c_0 > 0, c_1 > 0, c_2 > 0, c_3 > 0, c_4 > 0',
    'eq_description': 'Aizawa attractor (chaotic)',
    'const_description': 'c_0: parameter, c_1: parameter, c_2: parameter, c_3: parameter, c_4: parameter',
    'var_description': 'x_0: x, x_1: y, x_2: z',
    'source': 'Aizawa attractor chaotic',
},
{
    'id': 61,
    'eq': 'c_0 * x_0 - x_1 * x_2 | c_1 * x_1 + x_0 * x_2 | c_2 * x_2 + x_0 * x_1 / c_3',
    'dim': 3,
    'consts': [[5.0, -10.0, -3.8, 3.0]],
    'init': [ [15, -15, -15], [8, 14, -10],],
    'init_constraints': '',
    'const_constraints': '',
    'eq_description': 'Chen-Lee attractor; system for gyro motion with feedback control of rigid body (chaotic)',
    'const_description': 'c_0: parameter, c_1: parameter, c_2: parameter, c_3: fixed constant; parameters relate to principal moments of inertia',
    'var_description': 'x_0: omega_x, x_1: omega_y, x_2: omega_z; variables are essentially angular velocities',
    'source': 'Chen-Lee attractor'
},
{
    'id': 62,
    'eq': '- x_0 + 1 / (1 + exp(c_0 * x_2 + c_1 * x_1 - c_2)) | c_3 * (x_0 - x_1) | - x_2 + 1 / (1 + exp(c_0 * x_0 + c_1 * x_3 - c_2)) | c_3 * (x_2 - x_3)',
    'dim': 4,
    'consts': [[0.89, 0.4, 1.4, 1.0]],
    'init': [[2.25, -0.5, -1.13, 0.4], [0.342, -0.431, -0.86, 0.041]],
    'init_constraints': 'x_0 > 0, x_1 > 0, x_2 > 0, x_3 > 0',
    'const_constraints': 'c_0 > 0, c_1 > 0, c_2 > 0, c_3 > 0',
    'eq_description': 'Binocular rivalry model with adaptation (oscillations)',
    'const_description': 'c_0: strength of mutual antagonism, c_1: influence of adaptation, c_2: strength of input stimulus, c_3: time scale of adaptation',
    'var_description': 'x_0: perception of left eye stimulus, x_1: adaptation of left eye stimulus, x_2: perception of right eye stimulus, x_3: adaptation of right eye stimulus',
    'source': 'strogatz p.295'
},
{
    'id': 63,
    'eq': '- c_1 * x_0 * x_2 | c_1 * x_0 * x_2 - c_0 * x_1 | c_0 * x_1 - c_2 * x_2 | c_2 * x_2',
    'dim': 4,
    'consts': [[0.47, 0.28, 0.3]],
    'init': [[0.6, 0.3, 0.09, 0.01], [0.4, 0.3, 0.25, 0.05]],
    'init_constraints': '0 < x_0 < 1, 0 < x_1 < 1, 0 < x_2 < 1, 0 < x_3 < 1, x_1 + x_2 + x_3 + x_4 = 1',
    'const_constraints': 'c_0 > 0, c_1 > 0, c_2 > 0',
    'eq_description': 'SEIR infection model (proportions)',
    'const_description': 'c_0: transfer rate rate, c_1: transmission rate, c_2: recovery rate',
    'var_description': 'x_0: susceptible, x_1: exposed, x_2: infected, x_3: recovered',
    'source': 'SEIR infection model proportions'
}]
