# wordpress-guide
Wordpress user guides 4.1~5.1, created using GuideAutomator tool (https://github.com/aside-ufba/guide-automator-python) and Docker.

# Modus Operandi
On my scientific research project, i had to make automatic user guides of some versions of Wordpress. To manage that versions, i used Docker and Docker-Compose to get up those versions, runned the GuideAutomator inside the version and do the adjustments on the guide.

# Process
1. Setup the docker-compose.yml file, setting the settings like version of Wordpress.
2. Execute the command 'docker-compose up'
3. Run the GuideAutomator on 'localhost
