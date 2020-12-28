Encode Sans Fonts
=================

![](sample.png)

This project is forked from Pablo Impallari's original repo in order to upgrade the family to a variable font and make some small refinements. The description from the original is:

> The Encode Sans family is a versatile workhorse. Featuring a huge range of weights and > widths, it's ready for all kind of typographic challenges. It also includes Tabular and > Old Style figures, as well as full set of Small Caps and other OpenType features.
> 
> Designed by Pablo Impallari and Andres Torresi.
> 
> Released under the SIL Open Font License.
> 
> #### Encode Sans covers all 104 Latin Languages:
> 
> Afar, Afrikaans, Albanian, Azerbaijani, Basque, Belarusian, Bislama, Bosnian, Breton, > Catalan, Chamorro, Chichewa, Comorian, Croatian, Czech, Danish, Dutch, English, Esperanto, > Estonian, Faroese, Fijian, Filipino/Tagalog, Finnish, Flemish, French, Gaelic (Irish / > Manx / Scottish), Gagauz, German, Gikuyu, Gilbertese/Kiribati, Greenlandic, Guarani, > Haitian_Creole, Hawaiian, Hungarian, Icelandic, Igo/Igbo, Indonesian, Irish, Italian, > Javanese, Kashubian, Kinyarwanda, Kirundi, Latin, Latvian, Lithuanian, Luba/Ciluba/Kasai, > Luxembourgish, Malagasy, Malay, Maltese, Maori, Marquesan, Marshallese, > Moldovan/Moldovian/Romanian, Montenegrin, Nauruan, Ndebele, Norwegian, Oromo, > Palauan/Belauan, Polish, Portuguese, Quechua, Romanian, Romansh, Sami, Samoan, Sango, > Serbian, Sesotho, Setswana/Sitswana/Tswana, Seychellois_Creole, SiSwati/Swati/Swazi, > Silesian, Slovak, Slovenian, Somali, Sorbian, Sotho, Spanish, Swahili, Swedish, Tahitian, > Tetum, Tok_Pisin, Tongan, Tsonga, Tswana, Tuareg/Berber, Turkish, Turkmen, Tuvaluan, > Uzbek/Usbek, Wallisian, Walloon, Welsh, Xhosa, Yoruba, Zulu.
 
# Build Process

The sources can be built with FontMake, but I've put together some specific build scripts to pass the fonts through some steps that fix metadata issues.

The build process requires you to open up a terminal and navigate to this project's directory.

## Step 1: Install Requirements

I suggest using a Python virtual environment to build this project. If you've never set up a virtual environment before, [read more virtualenv in this guide](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).

First, set up a virtual environment with:

```
virtualenv -p python3 venv
```

Here, `venv` will be the name of the virtual environment and of the folder holding its dependencies. You need to activate it with:

```
source venv/bin/activate
```

To operate the scripts within this repo, install requirements with:

```
pip install --upgrade -r requirements.txt
```

If you run into issues installing some of the dependencies (such as Pillow), it may help to separately install the packages with individual commands, such as `pip install Pillow==5.4.1`.

**Installing TTFautohint (for static builds only):** Download the latest version of TTFautohint from https://sourceforge.net/projects/freetype/files/ttfautohint/, unzip the file (e.g. `ttfautohint-1.8.3-tty-osx.tar.gz`), and place the unix executable file directly into the new `venv/bin` within this project.


## Step 2: Give permissions to build scripts

The first time you run the build, you will need to give run permissions to the build scripts.

On the command line, navigate to the project folder (`cd Encode-Sans`), and then give permissions to the shell scripts with:

```
chmod -R +x sources/scripts
```

The `-R` applies your permission to each of the shell scripts in the directory, and the `+x` adds execute permissions. Before you do this for shell scripts, you should probably take a look through their contents, to be sure they aren't doing anything bad. The ones in this repo simply build from the GlyphsApp sources and apply various fixes to the results.

## Step 3: Run the build scripts!

You can then build sources by running shell scripts in `sources/scripts/`.

```
sources/scripts/build.sh <optionalflag>
```

Add one of the are the following flags to build the fonts:

`--statics` or `-s` to build the static TTF instances (there are 45, so it takes awhile)

`--variable` or `-v` to build the variable font

Without a flag, it will build both.

# Variable font upgrade project documentation

Notes were taken throughout the variable font upgrade project and added to the [docs](/docs) directory. I tend to take notes while working anyway, in order to think through problems and record solutions for later reference. In this project, I have included these in the repo so that others might find references to solve similar problems, especially because variable font-making processes are relatively new, and there is a general scarcity of online knowledge on font mastering. Because they were often made alongside work, the notes can at times be a bit disjointed. Hopefully they are still helpful to others! 

If you have any questions about the project or the notes, feel free to [file an issue](/issues) or to reach out to Stephen Nixon via Twitter ([@thundernixon](https://twitter.com/thundernixon)) or other social media (typically also @thundernixon).
