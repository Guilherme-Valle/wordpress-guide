# wordpress-guide
Wordpress user guides 4.1~5.1, created using GuideAutomator tool (https://github.com/aside-ufba/guide-automator-python) and Docker.

# Modus Operandi
On my scientific research project, i had to make automatic user guides of some versions of Wordpress. To manage that versions, i used Docker and Docker-Compose to get up those versions, runned the GuideAutomator inside the version and do the adjustments on the guide. I run that process with a sh script.

# Configuration
To run the process, has some requirements:
1. Install Docker and Docker-Compose
2. Install Python3
3. Install Jupyter-Lab or Jupyter Notebook
4. Use the environment variable PYTHONPATH to configure the imports of the guide files (PYTHONPATH is used by the python interpreter to determine which modules to load), running `export PYTHONPATH=../../guide-automator-python:$PYTHONPATH`


# Process
1. Setup the docker-compose.yml file, setting the settings like version of Wordpress.
2. Run the file run_guide.sh. 
3. The script setup the container of docker, run the guide-automator, and generate the outputs with Jupyter-lab. 
4. If had some error on running the guide, i fix the document and run again.

