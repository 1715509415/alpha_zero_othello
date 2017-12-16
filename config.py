import os

def project_dir():
    return os.path.dirname(os.path.abspath(__file__))

def data_dir():
    return os.path.join(project_dir(), "data")

class DataConfig:
    game_location = data_dir()+'\\'+"games"+"\\"
    model_location = data_dir()+'\\'+"models"+"\\"
    history_location = data_dir()+'\\'+"history"+"\\"

class SelfPlayConfig:
    simulation_num_per_move = 50
    nb_game_in_file = 10
    buffer_size = 64 * nb_game_in_file
    max_file_num = 2000  # 50000
    iterations = -1 #-1 for infinite
    gpu_mem_fraction = 0.1
    data = DataConfig()


class OptimizerConfig:
    batch_size = 64
    buffer_size = 1000000
    epochs_per_cycle = 50
    save_model_cycles = 1
    min_game_files = 100
    min_new_game_files = 20
    iterations = -1 #-1 for infinite
    gpu_mem_fraction = 0.6
    verbose = 0 #0,1,2 like keras model.fit
    data = DataConfig()

class EvaluateConfig:
    game_num = 100
    repeat_with_new_model = True
    simulation_num_per_move = 25
    gpu_mem_fraction = 0.1
    model_1 = "newest" # options: "newest", "random" or file name in model location
    model_2 = "1513442569.5649455.h5" # options: "newest", "random" or file name in model location
    data = DataConfig()