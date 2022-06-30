###what next: change config_file to the basic one and test by replacing inference_cfg 
##
import deeplabcut 
config_path= path_config_file = '/home/ulaval.ca/amngb2/projects/ul-val-prj-def-erpaq33/sophie/cdpq/deeplabcut/CDPQ_test-CDPQ_experiment-2022-02-22/config_center_tail.yaml'

deeplabcut.train_network(
    config_path,
     shuffle=2,
    saveiters=30000,
    maxiters=50000,
    allow_growth=False,
    iteration=1
    #gputouse=1,
)


