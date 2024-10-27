using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DetCrash : MonoBehaviour
{
    //anything defined as doubles is because unity got mad at me
    public float timePeriod = 0.5f;
    public double crashAcc = 4*9.81;
    private WaitForSeconds delay;
    double prevShakeSpeed;
    double newShakeSpeed;
    double acc;

    void Start()
    {
        //defined here for efficiency, thing that will wait in between taking speed measurements
        delay = new WaitForSeconds(timePeriod);
        StartCoroutine(calcAcc());
    }

    IEnumerator calcAcc()
    {
        while (true)
        {
            //this is only for the rotation in the y direction but like that shouldn't matter? I don't think?
            prevShakeSpeed = Input.gyro.rotationRateUnbiased.y;
            //waits set no of seconds
            yield return delay;
            newShakeSpeed = Input.gyro.rotationRateUnbiased.y;
            //calcs average acc using (v-u)/t = a (love you suvat)
            //fixed so its def positive and it's linear acceleration
            acc = Math.Abs((prevShakeSpeed - newShakeSpeed)/timePeriod*2*3.14159);
            //if num of gs is too high, it's a crash and we run inCaseOfCrash
            if (acc > crashAcc) {
                //run function SENDHELP
                inCaseOfCrash();
            }
        }
    }

    void inCaseOfCrash()
    {
        Debug.Log("There has been a deadly awful crash :(.");
        // Corrected line to instantiate RunsPythonCaller
        RunsPythonCaller pyth = new RunsPythonCaller();
        
        // Call the method to run the Python script
        pyth.RunPythonScript(Convert.ToString(acc));
    }
}
