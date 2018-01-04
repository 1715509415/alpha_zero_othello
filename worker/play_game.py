from alpha_zero_othello.config import EvaluateConfig
from alpha_zero_othello.lib import tf_util
from alpha_zero_othello.player.player import HumanPlayer, RandomPlayer
from alpha_zero_othello.player.aiplayer import AIPlayer
from alpha_zero_othello.othello import Othello
from random import random
from time import time
import glob

def start():
    config = EvaluateConfig()
    tf_util.update_memory(config.gpu_mem_fraction)
    AIPlayer.create_if_nonexistant(config)
    run_games(config)
             
    
def run_games(config):
    game = Othello()
    i = random() > 0.5
    
    p1 = create_player(config.model_1, config)
    print("You are playing against", config.model_1)
    print("Playing games with %d simulations per move" % config.game.simulation_num_per_move)
    p2 = HumanPlayer()
    side = -1
    while not game.game_over():
        game.print_board()
        if i:
            if side == -1:
                t = p1.pick_move(game, side)
            else:
                t = p2.pick_move(game, side)
        else:
            if side == 1:
                t = p1.pick_move(game, side)
            else:
                t = p2.pick_move(game, side)
        game.play_move(t[0], t[1], side)
        side *= -1
    print("\n\nFinal Board:")
    game.print_board()
    if (i and -1 == game.get_winner()) or (not i and 1 == game.get_winner()):
        print("You lose!")
    elif game.get_winner() == 0:
        print("Its a draw!")
    else:
        print("You win!")

def create_player(player_name, config):
    if player_name == "random":
        model = "random"
        player = RandomPlayer()
    elif player_name == "newest":
        model = sorted(glob.glob(config.data.model_location+"*.h5"))[-1]
        print("Loading model: %s" % model)
        player = AIPlayer(0, config.game.simulation_num_per_move, train=False, model=model, tau=config.game.tau_1)
    else:
        model = config.data.model_location+player_name
        player = AIPlayer(0, config.game.simulation_num_per_move, train=False, model=model, tau=config.game.tau_1)
    return player