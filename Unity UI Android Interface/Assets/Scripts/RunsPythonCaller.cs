using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using System.Diagnostics; // For running external processes

public class RunsPythonCaller : MonoBehaviour
{
    private double acceleration;

    public void RunPythonScript(string acc)
    {
        // Convert the acceleration value
        acceleration = double.TryParse(acc, out double parsedAcc) ? parsedAcc : 0.0;

        // Prepare data to be written to a text file
        string name = "Jenny Fier";
        string location = "rats. slower. unwanted";
        string fileData = $"Name: {name}\nLocation: {location}\nAcc: {acceleration}";

        // Write data to a file
        string filePath = Application.dataPath + "/in_case_of_crash_deets.txt";
        File.WriteAllText(filePath, fileData);

        // Run the Python script at runtime
        ExecutePythonScript();
    }

}
