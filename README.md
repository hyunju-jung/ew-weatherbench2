We learn how to read [WeatherBench 2](https://doi.org/10.48550/arXiv.2308.15560) using Jupyter Notebook on a cluster.

First, we load a conda environment. I load `miniconda` on bwUniCluster 2.0. 

    module load devel/miniconda/4.9.2

Set up a kernel for jupyter notebook. 

    conda create -n env-weatherbench ipykernel python=3.9.1
    source activate env-weatherbench
    python -m ipykernel install --user --name weatherbench-kernel --display-name="WeatherBench"

Install WeatherBench 2.

    pip install git+https://github.com/google-research/weatherbench2.git
    pip install gcsfs basemap

