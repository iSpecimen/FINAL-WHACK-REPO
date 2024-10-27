# FINAL-WHACK-REPO
Our project name: [NULL] - SafeDriving

## Project Description

We have used fetch.ai's tech stack and user agents with the unity engine and a python server to access real-time information about location and acceleration in order to detect crashes and provide information to emergency responders. Python libraries such as textttospeech, speechtotext and twilio to make phone calls to the mergency responders informing them of the accident and to interact with the user while they are driving.
Our project aimed to improve safety on the roads in several ways:
* Give advice such as instructions to the nearest safe place to pull over and take a break in high stress situations
* Suggest places for the user to take a break every 2 hours
* Inform emergency responders of a crash and vital information such as location (using what3words) and level of seriousness of the crash (calculated using the number of gs experienced)
* Warn users of potential weather conditions and subsequent dangers
* Discourage users from looking at their phone by using only voice inputs/outputs while the user is driving

Our project placed a great deal of importance on security, and as such, the user's personal information is encrypted.

## Instructions to run the project

///

## Use-Case Example

This product is intended for a driver of a car to use to monitor and provide suggestions to improve their safety on the road by having it as an app on their phone.

## Special Considerations

This project is currently incapable of running as a whole. This is because of some extensive set-up issues we have had regarding the difficulty of using python (the language of fetch.ai's libraries) to interface in any way with a mobile application (required for the use case and for acccess to needed data such as from the gyroscope sensor and the geolocation data). C# and Unity do not naturally interface with Python.

We hope that you wiil still be able to appreciate and understand the ideas and potential implementation portrayed by this project.
