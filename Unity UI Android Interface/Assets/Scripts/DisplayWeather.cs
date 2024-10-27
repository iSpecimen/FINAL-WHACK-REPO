using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class DisplayWeather : MonoBehaviour
{

    TMP_Text tmp;

    void Start()
    {
        tmp = GetComponent<TextMeshProUGUI>();
    }

    private void DisplayText(string str)
    {
         tmp.text = str;
    }
}
