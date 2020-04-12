#!/bin/bash

###          freetype2-infinality-ultimate settings          ###
###              rev. 0.5, for freetype2 v.2.6.3             ###
###                                                          ###
###                Copyright (c) 2015 bohoomil               ###
### The MIT License (MIT) http://opensource.org/licenses/MIT ###
###      part of infinality-bundle  http://bohoomil.com      ###


### As of version 2.6.2-1, freetype2-infinality-ultimate comes with
### the "ultimate3" rendering style enabled internally by default.
### It is still possible to use the optional "infinality-settings.sh"
### script to switch between additional built-in rendering schemes and
### create custom ones if necessary. Once modified, "infinality-settings.sh"
### needs to be copied to "/etc/X11/xinit/xinitrc.d/".
###
### There are two levels of customization available to a user:
###
### 1. A set of 7 preconfigured styles selectable by name.

### Available styles:
### ultimate1 <> extra sharp
### ultimate2 <> sharper & lighter ultimate
### ultimate3 <> ultimate: well balanced (default)
### ultimate4 <> darker & smoother
### ultimate5 <> darkest & heaviest ("MacIsh")
### osx       <> Apple OS X
### windowsxp <> MS Windows XP

### If you want to use a style from the list, uncomment the variable below
### and set its name as the value.


export INFINALITY_FT="ultimate3"


### 2. If you want to create a custom style, uncomment the variables below
###    and enter the values of your choice.


#export INFINALITY_FT_FILTER_PARAMS="08 24 36 24 08"
#export INFINALITY_FT_GRAYSCALE_FILTER_STRENGTH="0"
#export INFINALITY_FT_FRINGE_FILTER_STRENGTH="25"
#export INFINALITY_FT_AUTOHINT_HORIZONTAL_STEM_DARKEN_STRENGTH="0"
#export INFINALITY_FT_AUTOHINT_VERTICAL_STEM_DARKEN_STRENGTH="25"
#export INFINALITY_FT_WINDOWS_STYLE_SHARPENING_STRENGTH="25"
#export INFINALITY_FT_CHROMEOS_STYLE_SHARPENING_STRENGTH="0"
#export INFINALITY_FT_STEM_ALIGNMENT_STRENGTH="15"
#export INFINALITY_FT_STEM_FITTING_STRENGTH="15"
#export INFINALITY_FT_STEM_DARKENING_AUTOFIT="false"
#export INFINALITY_FT_STEM_DARKENING_CFF="false"
#export INFINALITY_FT_GAMMA_CORRECTION="0 100"
#export INFINALITY_FT_BRIGHTNESS="0"
#export INFINALITY_FT_CONTRAST="0"
#export INFINALITY_FT_USE_VARIOUS_TWEAKS="true"
#export INFINALITY_FT_AUTOHINT_INCREASE_GLYPH_HEIGHTS="false"
#export INFINALITY_FT_AUTOHINT_SNAP_STEM_HEIGHT="0"
#export INFINALITY_FT_STEM_SNAPPING_SLIDING_SCALE="0"
#export INFINALITY_FT_USE_KNOWN_SETTINGS_ON_SELECTED_FONTS="false"

### Please refer to "infinality-settings-generic" file for detailed explanation
### of customization options and provided examples.

# vim:ft=sh:
