import re

__doc__="""
    Assumes first line has 'nameID="###"' in it.
    
    To use:
    1. Paste in your namerecord block. 
    2. Make the first nameID correct, and the rest will count up properly.
"""

XMLpropToIterate="namerecord nameID"

countFrom=256

xmlString="""  
  <namerecord nameID="256" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Weight
    </namerecord>
    <namerecord nameID="257" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Width
    </namerecord>
    <namerecord nameID="258" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Thin Condensed
    </namerecord>
    <namerecord nameID="259" platformID="1" platEncID="0" langID="0x0" unicode="True">
      ExtraLight Condensed
    </namerecord>
    <namerecord nameID="260" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Light Condensed
    </namerecord>
    <namerecord nameID="261" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Regular Condensed
    </namerecord>
    <namerecord nameID="262" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Medium Condensed
    </namerecord>
    <namerecord nameID="263" platformID="1" platEncID="0" langID="0x0" unicode="True">
      SemiBold Condensed
    </namerecord>
    <namerecord nameID="264" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Bold Condensed
    </namerecord>
    <namerecord nameID="265" platformID="1" platEncID="0" langID="0x0" unicode="True">
      ExtraBold Condensed
    </namerecord>
    <namerecord nameID="266" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Black Condensed
    </namerecord>
    <namerecord nameID="267" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Thin SemiCondensed
    </namerecord>
    <namerecord nameID="268" platformID="1" platEncID="0" langID="0x0" unicode="True">
      ExtraLight SemiCondensed
    </namerecord>
    <namerecord nameID="269" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Light SemiCondensed
    </namerecord>
    <namerecord nameID="270" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Regular SemiCondensed
    </namerecord>
    <namerecord nameID="271" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Medium SemiCondensed
    </namerecord>
    <namerecord nameID="272" platformID="1" platEncID="0" langID="0x0" unicode="True">
      SemiBold SemiCondensed
    </namerecord>
    <namerecord nameID="273" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Bold SemiCondensed
    </namerecord>
    <namerecord nameID="274" platformID="1" platEncID="0" langID="0x0" unicode="True">
      ExtraBold SemiCondensed
    </namerecord>
    <namerecord nameID="275" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Black SemiCondensed
    </namerecord>
    <namerecord nameID="276" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Thin
    </namerecord>
    <namerecord nameID="277" platformID="1" platEncID="0" langID="0x0" unicode="True">
      ExtraLight
    </namerecord>
    <namerecord nameID="278" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Light
    </namerecord>
    <namerecord nameID="279" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Regular
    </namerecord>
    <namerecord nameID="280" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Medium
    </namerecord>
    <namerecord nameID="281" platformID="1" platEncID="0" langID="0x0" unicode="True">
      SemiBold
    </namerecord>
    <namerecord nameID="282" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Bold
    </namerecord>
    <namerecord nameID="283" platformID="1" platEncID="0" langID="0x0" unicode="True">
      ExtraBold
    </namerecord>
    <namerecord nameID="284" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Black
    </namerecord>
    <namerecord nameID="285" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Thin SemiExpanded
    </namerecord>
    <namerecord nameID="286" platformID="1" platEncID="0" langID="0x0" unicode="True">
      ExtraLight SemiExpanded
    </namerecord>
    <namerecord nameID="287" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Light SemiExpanded
    </namerecord>
    <namerecord nameID="288" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Regular SemiExpanded
    </namerecord>
    <namerecord nameID="289" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Medium SemiExpanded
    </namerecord>
    <namerecord nameID="290" platformID="1" platEncID="0" langID="0x0" unicode="True">
      SemiBold SemiExpanded
    </namerecord>
    <namerecord nameID="290" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Bold SemiExpanded
    </namerecord>
    <namerecord nameID="291" platformID="1" platEncID="0" langID="0x0" unicode="True">
      ExtraBold SemiExpanded
    </namerecord>
    <namerecord nameID="292" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Black SemiExpanded
    </namerecord>
    <namerecord nameID="293" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Thin Expanded
    </namerecord>
    <namerecord nameID="294" platformID="1" platEncID="0" langID="0x0" unicode="True">
      ExtraLight Expanded
    </namerecord>
    <namerecord nameID="295" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Light Expanded
    </namerecord>
    <namerecord nameID="296" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Regular Expanded
    </namerecord>
    <namerecord nameID="297" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Medium Expanded
    </namerecord>
    <namerecord nameID="298" platformID="1" platEncID="0" langID="0x0" unicode="True">
      SemiBold Expanded
    </namerecord>
    <namerecord nameID="299" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Bold Expanded
    </namerecord>
    <namerecord nameID="300" platformID="1" platEncID="0" langID="0x0" unicode="True">
      ExtraBold Expanded
    </namerecord>
    <namerecord nameID="301" platformID="1" platEncID="0" langID="0x0" unicode="True">
      Black Expanded
    </namerecord>
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
        
        