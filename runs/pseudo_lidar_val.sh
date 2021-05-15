#!/usr/bin/env bash

cd ..
python scripts/preprocessing/gen_mini_batches.py --dataset_dir Kitti/scratch_300_val/ --plane scratch_300_val

# train the model
#python avod/experiments/run_training.py --pipeline_config=avod/configs/pyramid_cars_with_aug_example_scratch_300_val.config --device='0' --data_split='train'

# evaluate the model
python avod/experiments/run_evaluation.py --pipeline_config=avod/configs/pyramid_cars_with_aug_example_scratch_300_val.config --device='0' --data_split='val'