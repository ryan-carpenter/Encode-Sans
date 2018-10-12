import re

__doc__="""
    Assumes first line has 'nameID="###"' in it.
    
    To use:
    1. Paste in your namerecord block. 
    2. Make the first nameID correct, and the rest will count up properly.
"""

XMLpropToIterate="ValueNameID value"

countFrom=256

xmlString="""  
  <AxisValueArray>
        <AxisValue index="0" Format="1">
            <AxisIndex value="0"/>
            <Flags value="0"/>
            <ValueNameID value="498"/>
            <!-- Thin -->
            <Value value="250.0"/>
        </AxisValue>
        <AxisValue index="0" Format="1">
            <AxisIndex value="0"/>
            <Flags value="0"/>
            <ValueNameID value="259"/>
            <!-- ExtraLight -->
            <Value value="275.0"/>
        </AxisValue>
        <AxisValue index="0" Format="1">
            <AxisIndex value="0"/>
            <Flags value="0"/>
            <ValueNameID value="260"/>
            <!-- Light -->
            <Value value="300.0"/>
        </AxisValue>
        <AxisValue index="1" Format="1">
            <AxisIndex value="0"/>
            <Flags value="0"/>
            <ValueNameID value="261"/>
            <!-- Regular -->
            <Value value="400.0"/>
        </AxisValue>
        <AxisValue index="2" Format="1">
            <AxisIndex value="0"/>
            <Flags value="0"/>
            <ValueNameID value="262"/>
            <!-- Medium -->
            <Value value="500.0"/>
        </AxisValue>
        <AxisValue index="3" Format="1">
            <AxisIndex value="0"/>
            <Flags value="0"/>
            <ValueNameID value="263"/>
            <!-- SemiBold -->
            <Value value="600.0"/>
        </AxisValue>
        <AxisValue index="3" Format="1">
            <AxisIndex value="0"/>
            <Flags value="0"/>
            <ValueNameID value="264"/>
            <!-- Bold -->
            <Value value="700.0"/>
        </AxisValue>
        <AxisValue index="3" Format="1">
            <AxisIndex value="0"/>
            <Flags value="0"/>
            <ValueNameID value="265"/>
            <!-- ExtraBold -->
            <Value value="800.0"/>
        </AxisValue>
        <AxisValue index="4" Format="1">
            <AxisIndex value="0"/>
            <Flags value="0"/>
            <ValueNameID value="266"/>
            <!-- Black -->
            <Value value="900.0"/>
        </AxisValue>

        <AxisValue index="5" Format="1">
            <AxisIndex value="1"/>
            <Flags value="0"/>
            <ValueNameID value="267"/>
            <!-- Condensed -->
            <Value value="70.0"/>
        </AxisValue>
        <AxisValue index="6" Format="1">
            <AxisIndex value="1"/>
            <Flags value="0"/>
            <ValueNameID value="268"/>
            <!-- SemiCondensed -->
            <Value value="85.0"/>
        </AxisValue>
        <AxisValue index="7" Format="1">
            <AxisIndex value="1"/>
            <Flags value="2"/>
            <ValueNameID value="269"/>
            <!-- Normal -->
            <Value value="100.0"/>
        </AxisValue>
        <AxisValue index="8" Format="1">
            <AxisIndex value="1"/>
            <Flags value="0"/>
            <ValueNameID value="270"/>
            <!-- SemiExpanded -->
            <Value value="115.0"/>
        </AxisValue>
        <AxisValue index="8" Format="1">
            <AxisIndex value="1"/>
            <Flags value="0"/>
            <ValueNameID value="271"/>
            <!-- Expanded -->
            <Value value="130.0"/>
        </AxisValue>
    </AxisValueArray>
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
        
        