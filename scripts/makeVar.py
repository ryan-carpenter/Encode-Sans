import os
import shutil
import fontmake
from fontmake.font_project import FontProject
from datetime import datetime

# DS_PATH = 'recursive-mono-roman.designspace' # use for designspace
GLYPHS_PATH = 'sources/Encode-Sans.glyphs' # use for glyphs file

# make folder like SampleFont_2015-10-21-017_03

currentDatetime = datetime.now().strftime('%Y-%m-%d-%H_%M')

outputFolder = 'dist/' + GLYPHS_PATH.replace('sources/', '').replace('.glyphs', '-VF-') + currentDatetime + '/'

if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

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
        'interpolate': False,
        'use_afdko': False,
        'subroutinize': True,
        'output':['variable'],
        'instance_dir': outputFolder
    }
    return args

project = FontProject()

args = getRunArguments()

# TODO: is there a way to automatically export this to a specified folder? 
print(project.run_from_glyphs(glyphs_path=GLYPHS_PATH, **args))

# TODO: get family name from glyphs file (?)
# defaultFontPath = 'variable_ttf/' + GLYPHS_PATH.replace('sources/', '').replace('.glyphs', '-VF.ttf')
# newFontPath = outputFolder + GLYPHS_PATH.replace('sources/', '').replace('.glyphs', '-VF.ttf')
# shutil.move(defaultFontPath, newFontPath)

os.system('open %s' % fontPath)