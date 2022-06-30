import deeplabcut 
config_path= path_config_file = '/home/ulaval.ca/amngb2/projects/ul-val-prj-def-erpaq33/sophie/cdpq/deeplabcut/CDPQ_test-CDPQ_experiment-2022-02-22/config.yaml'
#deeplabcut.check_labels(path_config_file)
my_better_graph = [[3,4]]  # These are indices in the list of multianimalbodyparts
#!!!!make sure in  dlc-model/train/inference_cfg.yaml you put minimalnumberofconnections: 0
#deeplabcut.create_multianimaltraining_dataset(path_config_file, paf_graph=my_better_graph)
deeplabcut.create_multianimaltraining_dataset(
    path_config_file,
    #num_shuffles=1,
    net_type="dlcrnet_ms5",
    #paf_graph=my_better_graph, # , paf_graph='config'
    #augmenter_type='imgaug'
)
#deeplabcut.train_network(path_config_file, shuffle=1, max_snapshots_to_keep=5, displayiters=100, saveiters=200, maxiters=500)
"""deeplabcut.train_network(
    config_path,
    saveiters=3,
    maxiters=5,
    allow_growth=True,
)"""
deeplabcut.evaluate_network(config_path, plotting=True)
deeplabcut.extract_save_all_maps(config_path, shuffle=1, Indices=[0, 1])