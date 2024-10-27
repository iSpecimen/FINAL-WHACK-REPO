using UnityEngine;
using UnityEngine.Networking;
using System.Collections;

public class PythonCommunicator : MonoBehaviour
{
    private string serverUrl = "http://127.0.0.1:5000/data"; // Replace <your_server_ip> with the actual server IP
    private string messageRecieved;
    public string getMessage()
    {
        return messageRecieved;
    }

    void Start()
    {
        StartCoroutine(GetData());
    }

    public IEnumerator SendData(string jsonData)
    {
        UnityWebRequest request = new UnityWebRequest(serverUrl, "POST");
        byte[] bodyRaw = System.Text.Encoding.UTF8.GetBytes(jsonData);
        request.uploadHandler = new UploadHandlerRaw(bodyRaw);
        request.downloadHandler = new DownloadHandlerBuffer();
        request.SetRequestHeader("Content-Type", "application/json");

        yield return request.SendWebRequest();

        if (request.result != UnityWebRequest.Result.Success)
        {
            Debug.LogError($"Error: {request.error}");
        }
        else
        {
            Debug.Log("Data sent successfully");
            Debug.Log(request.downloadHandler.text);
        }
    }

    IEnumerator GetData()
    {
        UnityWebRequest request = UnityWebRequest.Get(serverUrl);
        yield return request.SendWebRequest();

        if (request.result != UnityWebRequest.Result.Success)
        {
            Debug.LogError($"Error: {request.error}");
        }
        else
        {
            Debug.Log("Data received successfully");

            //output
            messageRecieved = request.downloadHandler.text;
        }
    }
}
