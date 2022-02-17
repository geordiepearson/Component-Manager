# Python Interface and Application for Digikey API
The Component Manager is a tool that automates various tasks for embedded system designers through the use of the digikey api. BoMs can be provided to the application using a specificed CSV file format and data manipluation can be done using a command line interface. Note that this tool is intended to be used in a linux based environment but can be adapted to other operating systems.

# Functionality
The functionality of the component manager applications include:
  - Estimating BoM costs
  - Acquring component lead times
  - Verifying provided alternative parts satisfy original functionality

# Quickstart
## Install
This application requires the use of python3 and the pip module. 
```
sudo apt-get install python3-venv
```
Create the virtual environment.
```
python3 -m venv Component-Manager
source ./Component-Manager/bin/activate
cd Component-Manager
pip install -e .
```
Set the enviromental variables to use the Digikey API in the .envrc file.
```
echo "export DIGIKEY_CLIENT_ID=Client ID" >> .envrc
echo "export DIGIKEY_CLIENT_SECRET="Digikey Client Secret" > .envrc
echo "export DIGIKEY_STORAGE_PATH="Digikey Storage Path" > .envrc
```
Install all needed packages.
```
pip install digikey-api
pip install direnv
pip install pickel
```
# File Structure

# Example Uses
