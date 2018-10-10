import os
import shutil
import fontmake
from fontmake.font_project import FontProject
from datetime import datetime

######################################
##### DEFINE THE VARIABLE BELOW #####

# DS_PATH = 'master_ufo/EncodeSans-mathfix-normal_wdth.designspace' # use for a designspace
glyphs_path = 'sources/Encode-Sans copy-decomposed.glyphs'

##### DEFINE THE VARIABLE ABOVE #####
######################################



# define run args
def getRunArguments():
    u"""Arguments to be passed to a fontmake project run. The values below
    make Decovar build without errors. See also fontmake.__main__.py."""

    args = {
        'subset': None,
        'use_production_names': False,
        #'mark_writer_class': None,
        'reverse_direction': False,
        #'kern_writer_class': None,
        'interpolate_binary_layout': False,
        'remove_overlaps': True,
        'autohint': None,
        'conversion_error': None,
        #'no_round': False,
        'masters_as_instances': False,
        'use_afdko': False,
        'subroutinize': True,
        'output':['variable'],
    }
    return args

project = FontProject()

args = getRunArguments()

# print(project.run_from_designspace(designspace_path=DS_PATH, **args))
print(project.run_from_glyphs(glyphs_path=glyphs_path, **args))