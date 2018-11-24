# Generating static instances

I'm working to generate static instances through FontMake (so I can ultimately share the same build flow).


On my first try with the following command:

```
fontmake -m master_ufo/EncodeSans.designspace --output ttf --interpolate "Encode Sans Condensed ExtraLight" --autohint
```

...I got this message:

```
FileNotFoundError: [Errno 2] No such file or directory: 'ttfautohint': 'ttfautohint'
```

I followed the "git clone approach" instructions at https://github.com/source-foundry/ttfautohint-build, but I got the message again.

Then, I had to add:

```
export PATH="$HOME/ttfautohint-build/local/bin/:$PATH"
```

...to my `.bash_profile`, and it started working!

## Should I add to my usual `build.sh` script, or start a new, static-specific script?

For now, I'm just putting a `buildStaticInstances` true/false `if` statement into my `build.sh` script. If this gets too big or unwieldy, I'll move it to its own script.

## How should I handle the lack of a `dsig` table in a bunch of individual instances?

```
for filename in *; do echo "put ${filename}"; done
```

https://stackoverflow.com/questions/8512462/shellscript-looping-through-all-files-in-a-folder

## Do OTFs get autohinted?

When I run:

```
fontmake -m master_ufo/EncodeSans.designspace --output otf --interpolate "Encode Sans Condensed Bold" --autohint
```

...the OTF output goes into `instance_otf`, rather than the `autohinted/` folder that the TTF output went into. Does this mean it wasn't autohinted? 

I know that the AFDKO autohints CFF/OTF files, so I know that OTFs *can be* autohinted. But, maybe I need to use the  AFDKO to compile these instances?

- [ ] ask Micah about this
