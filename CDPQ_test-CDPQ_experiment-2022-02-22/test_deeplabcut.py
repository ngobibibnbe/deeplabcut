import deeplabcut 
config_path= path_config_file = '/home/ulaval.ca/amngb2/projects/ul-val-prj-def-erpaq33/sophie/cdpq/deeplabcut/CDPQ_test-CDPQ_experiment-2022-02-22/config.yaml'

#deeplabcut.check_labels(path_config_file)
deeplabcut.create_multianimaltraining_dataset(
    path_config_file,
    num_shuffles=1,
    net_type="dlcrnet_ms5",
)
#deeplabcut.train_network(path_config_file, shuffle=1, max_snapshots_to_keep=5, displayiters=100, saveiters=200, maxiters=500)
deeplabcut.train_network(
    config_path,
    saveiters=300000,
    maxiters=500000,
    allow_growth=True,
)

deeplabcut.evaluate_network(
    config_path,
    plotting=True,
)
videos=["/home/ulaval.ca/amngb2/projects/ul-val-prj-def-erpaq33/sophie/cdpq/deeplabcut/CDPQ_test-CDPQ_experiment-2022-02-22/videos/GR77_20200512_111314.mp4"]
deeplabcut.analyze_videos(
    config_path,
    videos,
    auto_track=True
)
deeplabcut.stitch_tracklets(
    config_path,
    videos,
    track_method="ellipse",
    min_length=5,
)

#Filter the predictions to remove small jitter, if desired:
deeplabcut.filterpredictions(config_path, 
                                 videos, 
                                 shuffle=1,
                                 videotype='mp4', 
                                 track_method = "ellipse")

deeplabcut.create_labeled_video(
    config_path,
    videos,
    videotype='mp4',
    shuffle=1,
    color_by="individual",
    keypoints_only=False,
    draw_skeleton=True,
    track_method="ellipse")

deeplabcut.plot_trajectories(config_path, [videos], shuffle=1,videotype='mp4', track_method="ellipse")