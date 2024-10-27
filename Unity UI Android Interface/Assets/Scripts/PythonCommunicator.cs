using UnityEngine;
using UnityEngine.Networking;
using System.Collections;

public class ServerCommunication : MonoBehaviour
{
    private string serverUrl = "http://<your_server_ip>:5000/data"; // Replace <your_server_ip> with the actual server IP

    void Start()
    {
        StartCoroutine(GetData());
    }

    IEnumerator SendData(string jsonData)
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
            Debug.Log(request.downloadHandler.text);
        }
    }
}
