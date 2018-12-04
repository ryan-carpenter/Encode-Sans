import re

__doc__="""
    Assumes first line has 'nameID="###"' in it.
    
    To use:
    1. Paste in your namerecord block. 
    2. Make the first nameID correct, and the rest will count up properly.
"""

XMLpropToIterate="AxisValue index"

countFrom=0

xmlString="""  
  <!-- ===== WEIGHT ===== -->
        <AxisValue index="5" Format="1">
            <AxisIndex value="0"/>
            <Flags value="0"/>
            <!-- Thin -->
            <ValueNameID value="276"/>
            <Value value="250.0"/>
        </AxisValue>
        <AxisValue index="6" Format="1">
            <AxisIndex value="0"/>
            <Flags value="0"/>
            <!-- ExtraLight -->
            <ValueNameID value="277"/>
            <Value value="275.0"/>
        </AxisValue>
        <AxisValue index="7" Format="1">
            <AxisIndex value="0"/>
            <Flags value="0"/>
            <!-- Light -->
            <ValueNameID value="278"/>
            <Value value="300.0"/>
        </AxisValue>
        <AxisValue index="8" Format="8">
            <AxisIndex value="0"/>
            <!-- ElidedFallbackNameID value (Regular) -->
            <Flags value="2"/>
            <!-- Regular -->
            <ValueNameID value="279"/>
            <Value value="400.0"/>
        </AxisValue>
        <AxisValue index="9" Format="1">
            <AxisIndex value="0"/>
            <Flags value="0"/>
            <!-- Medium -->
            <ValueNameID value="280"/>
            <Value value="500.0"/>
        </AxisValue>
        <AxisValue index="10" Format="1">
            <AxisIndex value="0"/>
            <Flags value="0"/>
            <!-- SemiBold -->
            <ValueNameID value="281"/>
            <Value value="600.0"/>
        </AxisValue>
        <AxisValue index="11" Format="1">
            <AxisIndex value="0"/>
            <Flags value="0"/>
            <!-- Bold -->
            <ValueNameID value="282"/>
            <Value value="700.0"/>
        </AxisValue>
        <AxisValue index="12" Format="1">
            <AxisIndex value="0"/>
            <Flags value="0"/>
            <!-- ExtraBold -->
            <ValueNameID value="283"/>
            <Value value="800.0"/>
        </AxisValue>
        <AxisValue index="13" Format="1">
            <AxisIndex value="0"/>
            <Flags value="0"/>
            <!-- Black -->
            <ValueNameID value="284"/>
            <Value value="900.0"/>
        </AxisValue>
        
        <!-- ===== WIDTH ===== -->
        <AxisValue index="0" Format="1">
            <AxisIndex value="1"/>
            <Flags value="0"/>
            <!-- Condensed -->
            <ValueNameID value="303"/>
            <Value value="70.0"/>
        </AxisValue>
        <AxisValue index="1" Format="1">
            <AxisIndex value="1"/>
            <Flags value="0"/>
            <!-- SemiCondensed -->
            <ValueNameID value="304"/>
            <Value value="85.0"/>
        </AxisValue>
        <AxisValue index="2" Format="1">
            <AxisIndex value="1"/>
            <!-- ElidedFallbackNameID value (Regular) -->
            <Flags value="2"/>
            <!-- Normal -->
            <ValueNameID value="305"/>
            <Value value="100.0"/>
        </AxisValue>
        <AxisValue index="3" Format="1">
            <AxisIndex value="1"/>
            <Flags value="0"/>
            <!-- SemiExpanded -->
            <ValueNameID value="306"/>
            <Value value="115.0"/>
        </AxisValue>
        <AxisValue index="4" Format="1">
            <AxisIndex value="1"/>
            <Flags value="0"/>
            <!-- Expanded -->
            <ValueNameID value="307"/>
            <Value value="130.0"/>
        </AxisValue>
"""
   
def editLines(inputString, xmlProp, countFrom): 
    newString=""
    for i, line in enumerate(inputString.splitlines()):

        if f'{xmlProp}=' in line:
            # print(line)
        
            pattern = re.compile(f'{xmlProp}="(\d+)"')
            propValueNum = pattern.search(line).group(1)
        
            # print(propValueNum)
        
            line = line.replace(propValueNum, str(countFrom))
        
            # print(line +"\n\n ===== \n")
            
            countFrom += 1
            
        newString += line + "\n"
    return(newString)
        

print(editLines(xmlString,XMLpropToIterate, countFrom))  
        
        