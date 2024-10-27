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

    private void ExecutePythonScript()
    {
        // Path to the Python interpreter (modify if necessary)
        string pythonPath = "python"; // or specify full path, e.g., "C:/Python39/python.exe"
        // Path to the Python script
        string scriptPath = Application.dataPath + "/Scripts/test1.py";

        // Set up the process start information
        ProcessStartInfo startInfo = new ProcessStartInfo
        {
            FileName = pythonPath,
            Arguments = $"\"{scriptPath}\"", // Quotes around path in case it has spaces
            UseShellExecute = false,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            CreateNoWindow = true
        };

        try
        {
            // Start the process
            using (Process process = Process.Start(startInfo))
            {
                // Capture output for debugging
                string output = process.StandardOutput.ReadToEnd();
                string error = process.StandardError.ReadToEnd();

                process.WaitForExit();

                // Log the output and errors
                UnityEngine.Debug.Log("Python output: " + output);
                if (!string.IsNullOrEmpty(error))
                {
                    UnityEngine.Debug.LogError("Python error: " + error);
                }
            }
        }
        catch (Exception e)
        {
            UnityEngine.Debug.LogError("Failed to execute Python script: " + e.Message);
        }
    }

}
