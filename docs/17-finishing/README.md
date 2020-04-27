# Finishing & PRing to Google Fonts

It's been a long time (more than a year) since this variable font upgrade was started. In that time, Google Fonts has grown a lot in the processes around variable fonts, and the support for them on the front end of fonts.google.com. I have learned a lot myself! So, now it's time to finish this and PR it.

Goals:
- PR as a single variable font, removing the script setup to split fonts by widths in preprocessing (this can just be done with the FontTools Instancer)
- Pass as many FontBakery checks as possible
- Set `name` table as well as possible 
- Set up a proper STAT table with statmake
- Smallcaps separated into a separate family & PR
- Static fonts autohinted and put into `static` subfolder for PR