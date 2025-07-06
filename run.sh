#! /bin/bash

# # conda activate street-gaussian

# time python train.py --config configs/example/waymo_train_002.yaml

# # time  python make_ply.py --config configs/example/waymo_train_002.yaml viewer.frame_id 10 mode evaluate
# # time python render.py --config configs/example/waymo_train_002.yaml mode evaluate
# time python render.py --config configs/example/waymo_train_002.yaml mode trajectory

# # time python -m ptvsd --host 0.0.0.0 --port 5678 render.py --config configs/example/waymo_train_002.yaml mode trajectory


#! /bin/bash

# conda activate street-gaussian

# time python train.py --config configs/example/waymo_train_031.yaml

# time  python make_ply.py --config configs/example/waymo_train_002.yaml viewer.frame_id 10 mode evaluate
# time python render.py --config configs/example/waymo_train_002.yaml mode evaluate
# time python -m ptvsd --host 0.0.0.0 --port 5678 render.py --config configs/example/waymo_train_031.yaml mode trajectory
time python render.py --config configs/example/waymo_train_031.yaml mode trajectory

# time python -m ptvsd --host 0.0.0.0 --port 5678 render.py --config configs/example/waymo_train_002.yaml mode trajectory