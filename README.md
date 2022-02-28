# Python Interface and Application for Digikey API
The Component Manager is a tool that automates various tasks for embedded system designers through the use of the digikey api. BoMs can be provided to the application using a specificed CSV file format and data manipluation can be done using a command line interface. Note that this tool is intended to be used in a linux based environment but can be adapted to other operating systems.

# Functionality
The functionality of the component manager applications include:
  - Estimating BoM costs
  - Acquring component lead times
  - Verifying provided alternative parts satisfy original functionality

# Quickstart
## Install
This application requires the use of python3 and the pip module. Initially configure the virtual environment using direnv.
```
pip3 install direnv
cd Component-Manager
```
After this is done, direnv must be hooked into the shell. In bash, this can be done by appending ```eval "$(direnv hook bash)"```to your ```~/.bashrc``` file. Restart the shell and create a new .envrc file in the Component-Manager directroy and export the Digikey API environment variables.
```
echo "export DIGIKEY_CLIENT_ID=Client ID" > .envrc
echo "export DIGIKEY_CLIENT_SECRET=Digikey Client Secret" >> .envrc
echo "export DIGIKEY_STORAGE_PATH=Digikey Storage Path" >> .envrc
mkdir "Digikey Storage Path"
export PYTHONPATH="{PYTHONPATH}:"
```
With the virtual environment created, all needed packages can be installed.
```
pip3 install digikey-api
pip3 install pickle-mixin
pip3 install .
```
The tool is now ready to be used.
# Example Uses
Conducts an alternative parts check on the given csv file.
```
python3 component_manager/src/component_app.py components.csv -a
```
Checks the lead time and price of the components in the give file.
```
python3 component_manager/src/component_app.py components -p -l
```
Runs all tests for the application
```
python3 -m unittest discover component_manager/test/
```
# File Structure

