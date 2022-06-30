###what next: change config_file to the basic one and test by replacing inference_cfg 
##
from random import shuffle
import deeplabcut 
config_path= path_config_file = '/home/ulaval.ca/amngb2/projects/ul-val-prj-def-erpaq33/sophie/cdpq/deeplabcut/CDPQ_test-CDPQ_experiment-2022-02-22/config_center_tail.yaml'

#deeplabcut.check_labels(path_config_file)
#test_graph = [[0,1],[0,2],[1,3],[2,3],[3,4]]  # These are indices in the list of multianimalbodyparts
#!!!!make sure in  dlc-model/train/inference_cfg.yaml you put minimalnumberofconnections: 0 ###-- ca ne marche pas en tt cas pas dans le create_training 
#deeplabcut.create_multianimaltraining_dataset(path_config_file, paf_graph=my_better_graph)
deeplabcut.dropannotationfileentriesduetodeletedimages(config_path) #nettoyer les parties non labélisées correctement dans le H5
deeplabcut.create_multianimaltraining_dataset(
    path_config_file,
    Shuffles=[4],
    net_type="dlcrnet_ms5",
   # paf_graph=test_graph, # , paf_graph='config' 
   )

 
deeplabcut.train_network(
    config_path,
     shuffle=4,
    saveiters=3,
    maxiters=5,
    allow_growth=False,
)

scorername= deeplabcut.analyze_videos(config_path,['/home/ulaval.ca/amngb2/projects/ul-val-prj-def-erpaq33/sophie/cdpq/deeplabcut/CDPQ_test-CDPQ_experiment-2022-02-22/videos/center_tail/GR77_20200512_111314C.mp4'], videotype='.mp4', identity_only=True,save_as_csv=True,auto_track=True,shuffle=4)#,auto_track=True, identity_only=True)#auto_track=True
"""deeplabcut.convert_detections2tracklets(config_path,['/home/ulaval.ca/amngb2/projects/ul-val-prj-def-erpaq33/sophie/cdpq/deeplabcut/CDPQ_test-CDPQ_experiment-2022-02-22/videos/center_tail/GR77_20200512_111314C.mp4'], videotype='.mp4', overwrite=True, ignore_bodyparts=["head","lear","rear"],track_method="ellipse")
#deeplabcut.stitch_tracklets(config_path,['/home/ulaval.ca/amngb2/projects/ul-val-prj-def-erpaq33/sophie/cdpq/deeplabcut/CDPQ_test-CDPQ_experiment-2022-02-22/videos/center_tail_stitch_tracklet/GR77_20200512_111314C.mp4'], videotype='.mp4', overwrite=True, ignore_bodyparts=["head","lear","rear"],track_method="ellipse",overwrite=True)

#deeplabcut.create_video_with_all_detections(config_path, ['/home/ulaval.ca/amngb2/projects/ul-val-prj-def-erpaq33/sophie/cdpq/deeplabcut/CDPQ_test-CDPQ_experiment-2022-02-22/videos/center_tail/GR77_20200512_111314C.mp4'], videotype='.mp4')
deeplabcut.create_labeled_video(config_path, ['/home/ulaval.ca/amngb2/projects/ul-val-prj-def-erpaq33/sophie/cdpq/deeplabcut/CDPQ_test-CDPQ_experiment-2022-02-22/videos/center_tail/GR77_20200512_111314C.mp4'], videotype='.mp4', draw_skeleton=True,track_method="ellipse",color_by="individual",displayedindividuals="all",displayedbodypats=["center","tail"])

"""