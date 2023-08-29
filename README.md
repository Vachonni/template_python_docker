# TEMPLATE for Python development in Docker container using VSCode

## How to use

1. git clone this template
2. Change all \_\_XXXXX\_\_ values with the name of your project
3. **Uncomment #\*devcontainer.env\* in .gitignore file** to keep your secrets local
3. Change folder name to \<new folder name\>
4. Create repo \<new folder name\> on Git Hub 
5. git push --set-upstream origin \<new folder name\>



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



