using UnityEngine;
using System.Collections;
using System.IO;

public class GetLocationData : MonoBehaviour
{
    IEnumerator Start()
    {
        // Check if the user has location service enabled.
        if (!Input.location.isEnabledByUser)
            Debug.Log("Location not enabled on device or app does not have permission to access location");

        // Starts the location service.
        Input.location.Start();

        // Waits until the location service initializes
        int maxWait = 20;
        while (Input.location.status == LocationServiceStatus.Initializing && maxWait > 0)
        {
            yield return new WaitForSeconds(1);
            maxWait--;
        }

        // If the service didn't initialize in 20 seconds this cancels location service use.
        if (maxWait < 1)
        {
            Debug.Log("Timed out");
            yield break;
        }

        // If the connection failed this cancels location service use.
        if (Input.location.status == LocationServiceStatus.Failed)
        {
            Debug.LogError("Unable to determine device location");
            yield break;
        }
        else
        {
            // If the connection succeeded, this retrieves the device's current location and writes it to the text file
            string lat = Input.location.lastData.latitude.ToString();
            string longi = Input.location.lastData.longitude.ToString();
            string fileData = lat + "\n" + longi;

            string filePath = Application.dataPath + "location_data.txt";
            File.WriteAllText(filePath, fileData);

        }

        // Stops the location service if there is no need to query location updates continuously.
        Input.location.Stop();
    }
}
