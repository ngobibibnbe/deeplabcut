#!/bin/bash
#SBATCH --partition=gpu_48h
#SBATCH --cpus-per-task=24
#SBATCH --gres=gpu:1
#SBATCH --mem=24G
#SBATCH --time=2-00:0:0

source ../../our_virtual_envs/dlc/venv/bin/activate
python test_deeplabcut.py

#make sure you have done source deeplabcut/venv/bin/activate and you are in the directory of the project
# sq for consulting if the training is already done 
# check this link to know, how to cancel, and get info on the usage of the machine https://git.valeria.science/valeria/val-exemples/-/tree/main/200 