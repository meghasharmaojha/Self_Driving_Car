#!/bin/bash

#apt-get update

VENV_VAR = 'sdc_venv'

virtualenv $VENV_VAR 
source ./$VENV_VAR/bin/activate
retinanet-train --weights resnet50_coco_best_v2.1.0.h5 \
--batch-size 7 --steps 9 --epochs 4 \
--snapshot-path snapshots --tensorboard-dir tensorboard \
csv dataset/train.csv dataset/classes.csv


#pip3 install http://download.pytorch.org/whl/cu90/torch-0.4.1-cp36-cp36m-win_amd64.whl
#pip3 install torchvision
