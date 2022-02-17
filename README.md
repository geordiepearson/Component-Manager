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
pip install digikey-api
pip install direnv
pip install pickel
```
Create the virtual environment.
```
python -m venv venv
source ./venv/bin/activate
pip install -e .
direnv allow .
```
Set the enviromental variables to use the Digikey API.
```
export DIGIKEY_CLIENT_ID=SoiqBpAtiBehMalnYBPvpspK4YIF80nJ
export DIGIKEY_CLIENT_SECRET=wgraTG5KhDzSDDyi
export DIGIKEY_STORAGE_PATH=/mnt/c/Users/Geord/Desktop/Projects/component_manager/cache
```
# File Structure

# Example Uses
