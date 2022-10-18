echo [$(date)]:"START"
echo [$(date)]:"Creating Conda environment"
conda create --prefix ./env python=3.8 -y
echo [$(date)]:"Activating Conda environment"
source activate ./env 
echo [$(date)]:"Installing RequirementsDev "
pip install -r requirements_dev.txt
echo [$(date)]:"END"