using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public static class StaticVariables
{
    private static bool hasSubmitted = false;
    public static bool getHasSubmitted() {  return hasSubmitted; }
    public static void setHasSubmitted(bool hasSubmitted){ StaticVariables.hasSubmitted = hasSubmitted; }
    private static string name = "";
    public static string getName() {  return name; }
    public static void setName(string name) {  StaticVariables.name = name; }
}
