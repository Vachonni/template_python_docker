# TEMPLATE for Python development in Docker container using VSCode

## How to use

1. Create a new repo on GitHub using this template
2. git clone the new repo
3. Open repo in VSCode. **Do NOT open in container now**
4. Change all \_\_XXXXX\_\_ values with \<new project name\>
5. **IMPORTANT:** Uncomment #\*devcontainer.env\* in .gitignore fileto keep your secrets local
6. Reopen in container




----------------------

<br><br><br>

# __XXXXX__

*Project description*

## Connection to Azure ML

Connection information to Worspace are in devcontainer.env

## Creation of Azure Ennvironement 'RLCondaEnvFromExisting'
<i> no success with Dockerfile </i> :(

1- Start an Azure ML Computer Instance 

2- Connect to it through VSCode AzureML extension (right click)

3- Create a conda ennvironement `conda create --name RLCondaEnv python=3.10`

4- Activate it `source activate RLCondaEnv`

5- After insuring you are in the proper folder, with requirements fileInstall requirements `pip install -r requirements.txt`

6- Install local folder `pip install -e .`

7- Register it as AML Environment called "RLCondaEnvFromExisting". See script in AML_CreateENV.py

<i>NOTE: If you want to use this conda file to have the same environment from a new workspace, need to run `pip install -e .` </i>


<br><br><br>

#### Observations:

#### Next steps:



