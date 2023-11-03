## Data Availability 
All data used in this study is available in the data folder on this repository. The file named **240_B.txt** is used for the major analysis of this study while the **journal_data.csv** file is used for creating a supplementary table. 
## Code Availability 
All code used to generate the figures in this study and all relevant statistics are available in the notebooks folder in the **Figure.ipynb** notebook file. 


## Running Notebook
### Conda 
In order to run the notebook, we reccomend first either creating a conda environment using the **environment.yml** file we provide in our dependencies folder. You can create the environment by running the following commands: 
`conda env create -f environment.yml`
Once created, then just use the following command to activate your environement. 
`conda activate code_availability_env`
If you are running the notebook in VSCode, then use the change kernel button to select the code_availability_env as the environment to run the notebook in. 
If you are running the notebook in Jupyter Notebook, then just make sure the environment is activated before running calling jupyter notebook to run the notebook. 

### Pip 
If you do not want to use conda and have some other preference for environments or rather just don't use environments, you can use the requirements.txt file which will allow you to install all of the dependencies as well via pip:
`pip install -r requirements.txt`
Once this is done running, the notebook should run

### Google Collab
We will be adding a google collab notebook that everyone can use to rerun the code to generate the figures as well in the near future. 
