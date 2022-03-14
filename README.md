# Setup Environment

We provide the `environment.yml` file in the main folder to recreate the exact Conda environment with the same pip and Conda packages.
(Download Conda for your system [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html))
Run the following command:
```bash
conda env create -f environment.yml
```
Then activate the environment with:
```bash
conda activate MorphQ
```

# Prepare the Data Folder
Before starting the test, decide where to store the data.
Typically, we recommend to create a new folder in the `data` folder, following the name convention: `qmt_vXX` where XX is the version of your run or specific configuration settings.
Note that this step is required to be sure that the folder is available since the beginning, so that we can also store the log of our runs.

# Metamorphic Testing Settings
Before starting your test run, you need to prepare some configuration files in the data [`config`](config) folder.

1. create a `qmt_vXX.yaml` file in the `config` folder. On this file you can set almost all the parameters of the test. Including the metamorphic relationships to use (via the `metamorphic_strategies` field) and the program generation mechanism (via the `generation_strategy` field).

**IMPORTANT**: Remember to update the two field: `experiment_folder` to point to the data folder (e.g., `data/qmt_vXX/`) and `coverage_settings_filepath` to point to the file containing the coverage settings (e.g., `config/qmt_vXX.cover`).

2. create a `qmt_vXX.cover` file in the `config` folder. On this file you can set the coverage settings.

**IMPORTANT**: update the `data_file` field to specify the final name of the coverage database in the correct data folder (e.g., `data/qmt_vXX/.coverage`).

3. (optional) to avoid that the generated programs are processed by the git installation add the data folder to your `.gitignore` file.
```
data/qmt_vXX/*
```

# Our Hardware Setup
We tested MorphQ with the following setup:

- Operating System: Ubuntu 18.04.6 LTS
- Linux version 4.15.0-167-generic
- Architecture: x86-64
- CPU: Intel(R) Xeon(R) Silver 4214 CPU @ 2.20GHz
- conda 4.11.0
- RAM: 252 GB

# Metamorphic on Qiskit
To run `MorphQ` use the following command:
```bash
screen -L -Logfile data/qmt_vXX/log_run.txt -S qmt_vXX python3 -m lib.qmt config/qmt_vXX.yaml
```

# Inspect Warnings

## Warnings [your run]
The relevant warnings of your run will be stored in a the `qfl.db` sqlite database in the `data/qmt_vXX/` folder.
To inspect them use the notebook [`notebooks/42_Demo_Warnings_Inspection.ipynb`](notebooks/42_Demo_Warnings_Inspection.ipynb).


## Warnings [our Empirical Evaluation]
To see the warnings described in our empirical evaluation of the paper refer to the [`warnings/program_pairs`](warnings/program_pairs) folder.
There you will find a subfolder for each program pairs which contains:
- the source quantum program: `source.py`
- the follow-up quantum program generated via metamorphic transformations: `follow-up.py`
- the metadata of the generation of the program pair: `metadata.json`
- the metadata of the execution of the program pair: `metadata_exec.json`


# Troubleshooting
1. Did you install and activate the conda environment? via `conda activate ML4Quantum`