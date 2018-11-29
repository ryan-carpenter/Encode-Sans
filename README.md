Encode Sans Fonts
=================

The Encode Sans family is a versatile workhorse. Featuring a huge range of weights and widths, it's ready for all kind of typographic challenges. It also includes Tabular and Old Style figres, as well as full set of Small Caps and other Open Type features.

Designed by Pablo Impallari and Andres Torresi.

Released under the SIL Open Font License.

#### Encode Sans covers all 104 Latin Languages:

Afar, Afrikaans, Albanian, Azerbaijani, Basque, Belarusian, Bislama, Bosnian, Breton, Catalan, Chamorro, Chichewa, Comorian, Croatian, Czech, Danish, Dutch, English, Esperanto, Estonian, Faroese, Fijian, Filipino/Tagalog, Finnish, Flemish, French, Gaelic (Irish / Manx / Scottish), Gagauz, German, Gikuyu, Gilbertese/Kiribati, Greenlandic, Guarani, Haitian_Creole, Hawaiian, Hungarian, Icelandic, Igo/Igbo, Indonesian, Irish, Italian, Javanese, Kashubian, Kinyarwanda, Kirundi, Latin, Latvian, Lithuanian, Luba/Ciluba/Kasai, Luxembourgish, Malagasy, Malay, Maltese, Maori, Marquesan, Marshallese, Moldovan/Moldovian/Romanian, Montenegrin, Nauruan, Ndebele, Norwegian, Oromo, Palauan/Belauan, Polish, Portuguese, Quechua, Romanian, Romansh, Sami, Samoan, Sango, Serbian, Sesotho, Setswana/Sitswana/Tswana, Seychellois_Creole, SiSwati/Swati/Swazi, Silesian, Slovak, Slovenian, Somali, Sorbian, Sotho, Spanish, Swahili, Swedish, Tahitian, Tetum, Tok_Pisin, Tongan, Tsonga, Tswana, Tuareg/Berber, Turkish, Turkmen, Tuvaluan, Uzbek/Usbek, Wallisian, Walloon, Welsh, Xhosa, Yoruba, Zulu.

TTF Files hinted using TTF Autohint v1.1


# Build Process

To operate the scripts within this repo, install requirements with:

```
pip install -r requirements.txt
```

You can then build sources by running shell scripts in `scripts/`

```
scripts/build.sh [OPTIONS]
```

Add one of the are the following flags to build the fonts:


`--statics` or `-s` to build the static TTF instances (there are 45, so it takes awhile)

`--linked` or `-l` to build the split variable fonts (split into 5 width families, each with a variable weight axis)

`--full` or `-f` to build the one full variable font, with weight & width axes

`--all` or `-a` to build all of the fonts and take a coffee break.

The first time you run them, you will need to give run permissions to the build scripts. 

On the command line, navigate to the project folder (`cd Encode-Sans`), and then give permissions to the shell scripts with:

```
chmod -R +x scripts
```

The `-R` applies your permission to each of the shell scripts in the directory, and the `+x` adds execute permissions. Before you do this for shell scripts, you should probably take a look through their contents, to be sure they aren't doing anything bad. The ones in this repo simply build from the Encode Sans GlyphsApp sources.