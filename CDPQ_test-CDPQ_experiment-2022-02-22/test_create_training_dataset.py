###what next: change config_file to the basic one and test by replacing inference_cfg 
##
import deeplabcut 
config_path= path_config_file = '/home/ulaval.ca/amngb2/projects/ul-val-prj-def-erpaq33/sophie/cdpq/deeplabcut/CDPQ_test-CDPQ_experiment-2022-02-22/config_full.yaml'

#deeplabcut.check_labels(path_config_file)
#test_graph = [[0,1],[0,2],[1,3],[2,3],[3,4]]  # These are indices in the list of multianimalbodyparts
#!!!!make sure in  dlc-model/train/inference_cfg.yaml you put minimalnumberofconnections: 0 ###-- ca ne marche pas en tt cas pas dans le create_training 
#deeplabcut.create_multianimaltraining_dataset(path_config_file, paf_graph=my_better_graph)
deeplabcut.dropannotationfileentriesduetodeletedimages(config_path) #nettoyer les parties non labélisées correctement dans le H5
deeplabcut.create_multianimaltraining_dataset(
    path_config_file,
    Shuffles=[1,2,3],
    net_type="dlcrnet_ms5",
    crop_size=(1280,720)
   # paf_graph=test_graph, # , paf_graph='config' 
   
   )