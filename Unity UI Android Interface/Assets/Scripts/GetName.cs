using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.UI;

public class GetName : MonoBehaviour
{
    private Encrypter encrypt;
    public TMP_InputField nameText;
    string prevName;

    // Start is called before the first frame update
    void Start()
    {
        nameText = nameText.GetComponent<TMP_InputField>();
        prevName = nameText.name;
        encrypt = new Encrypter();
    }

    // Update is called once per frame
    void Update()
    {
        if (!StaticVariables.getHasSubmitted())
        {
            string name = nameText.text;
            if (name != prevName)
            {
                name = encrypt.EncryptString(name, "qword321");
                StaticVariables.setName(name);
            }
            else
            {
                prevName = name;
            }
        }
    }

    
}
