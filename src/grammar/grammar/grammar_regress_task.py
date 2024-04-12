import numpy as np


class RegressTask(object):
    """
    used to handle the initial condition and the time span of the ODE for querying the data oracle.
    """

    def __init__(self, batch_size, n_vars, dataX, data_query_oracle,
                 time_span=(0, 10), t_evals=np.linspace(0,10,50)):
        """
            n_vars: number of variables
            dataX: draw the initial conditions
            data_query_oracle: generate the time trajectory sequence
        """
        self.batch_size = batch_size
        self.time_span = time_span
        self.t_evals = t_evals
        self.dataX = dataX
        self.data_query_oracle = data_query_oracle
        #
        self.n_vars = n_vars

    def rand_draw_init_cond(self):
        self.init_cond = self.dataX.randn(sample_size=self.batch_size).T

    def evaluate(self):
        return self.data_query_oracle.evaluate(self.init_cond, self.time_span, self.t_evals)

    def reward_function(self, pred_trajectories):
        return self.data_query_oracle._evaluate_loss(self.init_cond, self.time_span, self.t_evals, pred_trajectories)

    def evaluate_all_losses(self, pred_trajectories):
        return self.data_query_oracle._evaluate_all_loss(self.init_cond,self.time_span, self.t_evals, pred_trajectories)