import deeplabcut 
config_path= path_config_file = '/home/ulaval.ca/amngb2/projects/ul-val-prj-def-erpaq33/sophie/cdpq/deeplabcut/CDPQ_test-CDPQ_experiment-2022-02-22/config_full.yaml'

"""deeplabcut.evaluate_network(
    config_path,
    Shuffles=[2],
    gputouse=1,
    plotting="individual"
)
# put  all instead of -1  on trans... variable of the config path index to have for all snapshot
"""
#deeplabcut.extract_save_all_maps(config_path, shuffle=3)

scorername = deeplabcut.analyze_videos(config_path,['/home/ulaval.ca/amngb2/projects/ul-val-prj-def-erpaq33/sophie/cdpq/deeplabcut/CDPQ_test-CDPQ_experiment-2022-02-22/videos/center_tail/GR77_20200512_111314C.mp4'], videotype='.mp4', save_as_csv=True, n_tracks=15)#,auto_track=True, identity_only=True)#auto_track=True
print(scorername)
deeplabcut.convert_detections2tracklets(config_path,['/home/ulaval.ca/amngb2/projects/ul-val-prj-def-erpaq33/sophie/cdpq/deeplabcut/CDPQ_test-CDPQ_experiment-2022-02-22/videos/all_body_convert_to_tracklet/GR77_20200512_111314C.mp4'], videotype='.mp4', overwrite=True, ignore_bodyparts=["head"], identity_only=True,track_method="ellipse")

deeplabcut.create_video_with_all_detections(config_path, ['/home/ulaval.ca/amngb2/projects/ul-val-prj-def-erpaq33/sophie/cdpq/deeplabcut/CDPQ_test-CDPQ_experiment-2022-02-22/videos/all_body_convert_to_tracklet/GR77_20200512_111314C.mp4'], videotype='.mp4')
deeplabcut.create_labeled_video(config_path, ['/home/ulaval.ca/amngb2/projects/ul-val-prj-def-erpaq33/sophie/cdpq/deeplabcut/CDPQ_test-CDPQ_experiment-2022-02-22/videos/all_body_convert_to_tracklet/GR77_20200512_111314C.mp4'], videotype='.mp4', draw_skeleton=True,track_method="ellipse",color_by="individual",displayedindividuals="all")
# deeplabcut.transformer_reID(config_path, ['/home/ulaval.ca/amngb2/projects/ul-val-prj-def-erpaq33/sophie/cdpq/deeplabcut/CDPQ_test-CDPQ_experiment-2022-02-22/videos/all_body_convert_to_tracklet/GR77_20200512_111314C.mp4'], videotype='.mp4', n_tracks=15)
#faire le center tail mais normal le auto track doit choisir le skeleton optimal