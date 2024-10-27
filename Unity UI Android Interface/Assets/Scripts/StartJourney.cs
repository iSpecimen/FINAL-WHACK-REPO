using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class StartJourney : MonoBehaviour
{

    public Button submitButton;


    void Start()
    {
        Button btn = submitButton.GetComponent<Button>();
        btn.onClick.AddListener(TaskOnClick);
    }

    void TaskOnClick()
    {
        OnStart();
    }

    public void OnStart()
    {
        // Tells python server to run the crash has been detected script
        PythonCommunicator pyth = FindObjectOfType<PythonCommunicator>();

        if (pyth != null&&!StaticVariables.getHasSubmitted())
        {
            string jsonData = "{\"Type\": \"" + "Journey_Started" + "\"}";
            StartCoroutine(pyth.SendData(jsonData));
            StaticVariables.setHasSubmitted(true);
            
        }
        else
        {
            //error
        }
    }
}
