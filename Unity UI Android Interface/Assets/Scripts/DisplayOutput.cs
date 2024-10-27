using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.IO;
using TMPro;

public class DisplayOutput : MonoBehaviour
{
    TMP_Text tmp;
    // Start is called before the first frame update
    void Start()
    {
        tmp = GetComponent<TextMeshProUGUI>();
    }

    // Update is called once per frame
    void Update()
    {
        string file = Application.dataPath + "/logoutput.txt";
        if (File.Exists(file))
        {
            string str = File.ReadAllText(file);
            tmp.text = str;
        }
    }
}
