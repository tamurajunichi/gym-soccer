import logging
from gym_soccer.envs.soccer_empty_goal import SoccerEmptyGoalEnv

logger = logging.getLogger(__name__)


class SoccerMultiagentEnv(SoccerEmptyGoalEnv):

    def __init__(self):
        super(SoccerMultiagentEnv, self).__init__()

    def _configure_environment(self):
        super(SoccerMultiagentEnv, self)._start_hfo_server(defense_npcs=1,
                                                           offense_on_ball=1,
                                                           offense_agents=2)
    def _get_reward(self):
        if self.status == hfo_py.GOAL:
            return 1
        else:
            return 0

