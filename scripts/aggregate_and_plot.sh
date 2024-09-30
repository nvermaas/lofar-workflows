#!/usr/bin/sh

ls > test.txt

if [ -d "toil_venv" ]; then
    echo "Activating existing virtual environment."
    source toil_venv/bin/activate
else
    echo "Creating new virtual environment for using toil"
    python3.11 -m venv toil_venv
    source toil_venv/bin/activate
    pip install --upgrade pip setuptools wheel
    pip install toil[cwl] singularity
fi
export SINGULARITY_BIND="$PWD:/mnt/workdir,/project:/project"
toil-cwl-runner --singularity imaging_compress_pipeline.git/aggregate_and_plot.cwl