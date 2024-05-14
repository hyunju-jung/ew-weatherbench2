#!/bin/bash -l
module purge
module load devel/miniconda
source activate env-weatherbench

python realtime_waves_v1.py --wave Kelvin --dir era5
python realtime_waves_v1.py --wave Kelvin --dir fuxi
python realtime_waves_v1.py --wave Kelvin --dir graphcast
python realtime_waves_v1.py --wave Kelvin --dir hres
python realtime_waves_v1.py --wave Kelvin --dir keisler
python realtime_waves_v1.py --wave Kelvin --dir neuralgcm_deterministic
python realtime_waves_v1.py --wave Kelvin --dir pangu
python realtime_waves_v1.py --wave Kelvin --dir sphericalcnn