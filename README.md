We learn how to run WeatherBench using Jupyter Notebook on a cluster.

module load devel/miniconda/4.9.2

Set up a kernel for jupyternotebook

    conda create -n env-weatherbench ipykernel python=3.9.1
    source activate env-weatherbench
    python -m ipykernel install --user --name weatherbench-kernel --display-name="WeatherBench"

Install WeatherBench 2

    pip install git+https://github.com/google-research/weatherbench2.git
    pip install gcsfs