# FINAL-WHACK-REPO
Our project name: [NULL] - SafeDriving

## Project Description

We have used fetch.ai's tech stack and user agents with the unity engine and a python server to access real-time information about location and acceleration in order to detect crashes and provide information to emergency responders. Python libraries such as textttospeech, speechtotext and twilio to make phone calls to the mergency responders informing them of the accident and to interact with the user while they are driving.
Our project aimed to improve safety on the roads in several ways:
* Give advice such as instructions to the nearest safe place to pull over and take a break in high stress situations
* Suggest places for the user to take a break every 2 hours
* Inform emergency responders of a crash and vital information such as location (using what3words) and level of seriousness of the crash (calculated using the number of Gs experienced from gyroscope data)
* Warn users of potential weather conditions and subsequent dangers
* Discourage users from looking at their phone by using only voice inputs/outputs while the user is driving

Our project placed a great deal of importance on security, and as such, the user's personal information is encrypted; this includes information such as full name and any health conditions were encrypted.


## Use-Case Example

This product is intended for a driver of a car to use to monitor and provide suggestions to improve their safety on the road by having it as an app on their phone. Because sensors can be triggered for a range of movement there is potential for application among a wide range of scenarios, not only limited to car drivers. This could include users of mobility scooters, cyclists even runners to check if there were any sudden collisions.


## Challenges

Unfortunately, this project is currently incapable of running as a whole. This is because of some extensive set-up issues we have had regarding the difficulty of using python (the language of fetch.ai's libraries) to interface in any way with a mobile application; C# and Unity do not naturally interface with Python. Although most of the back end has been created successfully using Fetch AI's agents, for the complete project we required phone gyroscope, accelerometer and geolocation data, which could not be obtained until the front end technology was set up.

We have also had some issues with incorporating the UAgent software for multiple agents, due to a few things that weren't mentioned in the documentation.

We hope that you wiil still be able to appreciate and understand the ideas and potential implementation portrayed by this project.

## Extra information
The majority of important Agents are stored under "Core UAgents", the "Miscellaneous" folder includes other versions that were used at times for specific testing or other purposes, but not particularly necessary or important to the core concepts of the project.
