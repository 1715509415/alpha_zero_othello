import argparse

def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", help="which mode to run in: \"opt\" to train the network," + 
                        " \"self\" to generate selfplay games," + 
                        " \"play\" to play the best network yourself," + 
                        "or \"eval\" to evaluate the network against random or a different version.",
                        choices = ["opt", "self", "play", "eval"])
    
    args = parser.parse_args()
    
    if args.mode == "opt":
        from .worker import optimizer
        optimizer.start()
    elif args.mode == "self":
        from .worker import self_play
        self_play.start()
    elif args.mode == "play":
        from .worker import play_game
        play_game.start()
    elif args.mode == "eval":
        from .worker import evaluate
        evaluate.start()