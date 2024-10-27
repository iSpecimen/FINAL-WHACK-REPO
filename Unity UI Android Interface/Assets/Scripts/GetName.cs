using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.UI;

public class GetName : MonoBehaviour
{

    public TMP_InputField nameText;
    string prevName;

    // Start is called before the first frame update
    void Start()
    {
        nameText = nameText.GetComponent<TMP_InputField>();
        prevName = nameText.name;
    }

    // Update is called once per frame
    void Update()
    {
        if (!StaticVariables.getHasSubmitted())
        {
            string name = nameText.text;
            if (name != prevName)
            {
                StaticVariables.setName(name);
            }
            else
            {
                prevName = name;
            }
        }
    }

    
}
