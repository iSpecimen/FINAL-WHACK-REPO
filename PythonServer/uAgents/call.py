from twilio.rest import Client
import TextToSpeech as tts
import SpeechToText as sst

def CallForHelp(): 
    #need twilio downloaded to run: max python-11 (!!!)
    #with pip type pip3 install twilio


    account_sid = 'AC078341550555939607e5bcf7267a3ac8'
    auth_token = 'a997d9b67e065cdcacc3e67324219391'
    client = Client(account_sid, auth_token)

    #read the json file
    # Opening JSON file
    f = open('in_case_of_emergency_deets.txt',"r")
    lines = f.readlines()
    data = []
    for line in lines:
        data.append(line.split(":")[1])
    # Closing file
    f.close()


    file_name = "Response.xml"
    #this passes all the correct info to the xml file <3
    #dummy info
    name = data[0]
    location = data[1]
    crashgforce = data[2]/9.81
    #initial text
    calltext = "Police, please. There has been a vehicle accident at location with what three words "+location+". The person involved is" + name + ". The crash involved " + crashgforce + "g force."
    xmlfiletemplate = "<Response>\n<Say voice=\"woman\">"+calltext+"</Say>\n</Response>"
    f = open(file_name,"w")
    f.write(xmlfiletemplate)
    f.close()



    #this does the call thingy

    call = client.calls.create(
        url="Response.xml",
        to="+447376215921",
        from_="+16122132434"
    )
    print(call.sid)

    #overwrites the xml file for privacy reasons
    f = open(file_name,"w")
    f.write("")
    f.close()

#check in - do we need to call 999???
sst.outputText("Have you been in a crash? Yes or No?")
helpNeeded = tts.recordInput()
if "yes" in helpNeeded:
    CallForHelp()
else:
    #run Gargi's stressful scenarios <3
    ue.Debug.Log("I'm going to give some passive agressive advice now :)")