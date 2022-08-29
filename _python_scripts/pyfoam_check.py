from PyFoam.RunDictionary.ParsedParameterFile import ParsedParameterFile
 
f=ParsedParameterFile("pitzDaily/0/U")
 
for b in f["boundaryField"]:
    if "Wall" in b:
        f["boundaryField"][b]["value"]="uniform (10 0 0)"
        f["boundaryField"][b]["type"]="fixedValue"
 
f.writeFile()