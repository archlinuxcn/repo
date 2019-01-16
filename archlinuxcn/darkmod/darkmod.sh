#!/bin/bash

# Should return false if darkmod folder does not exist
if [ ! -d $(eval echo ~$USER)/.local/share/darkmod/fms ]; then
    mkdir -p $(eval echo ~$USER)/.local/share/darkmod/fms
fi

function link_file() {
    if [ ! -f "$(eval echo ~$USER)/.local/share/darkmod/$1" ]; then
        echo -e "Linking missing game file $1\n"
        ln -s "/opt/darkmod/$1" "$(eval echo ~$USER)/.local/share/darkmod/$1"
    fi
}

# Not only was the saintlucia mission renamed to stlucia, but these symlinks
# break saving games and prevent mission info from showing in the menu
# The replacement links later fix this

if [ -L "$(eval echo ~$USER)/.local/share/darkmod/fms/saintlucia" ]; then
    echo -e "Removing symlink to old Saint Lucia mission"
    rm "$(eval echo ~$USER)/.local/share/darkmod/fms/saintlucia"
fi

if [ -L "$(eval echo ~$USER)/.local/share/darkmod/fms/training_mission" ]; then
    echo -e "Removing symlink to old Training Mission"
    rm "$(eval echo ~$USER)/.local/share/darkmod/fms/training_mission"
fi

link_file "tdm_ai_humanoid_nobles01.pk4"
link_file "tdm_models01.pk4"
link_file "tdm_sound_vocals06.pk4"
link_file "tdm_textures_sfx01.pk4"
link_file "tdm_ai_humanoid_pagans01.pk4"
link_file "tdm_models02.pk4"
link_file "tdm_sound_vocals07.pk4"
link_file "tdm_textures_stone_brick01.pk4"
link_file "tdm_ai_humanoid_townsfolk01.pk4"
link_file "tdm_models_decls01.pk4"
link_file "tdm_sound_vocals_decls01.pk4"
link_file "tdm_textures_stone_cobblestones01.pk4"
link_file "tdm_ai_humanoid_undead01.pk4"
link_file "tdm_player01.pk4"
link_file "tdm_standalone.pk4"
link_file "tdm_textures_stone_flat01.pk4"
link_file "tdm_ai_monsters_spiders01.pk4"
link_file "tdm_prefabs01.pk4"
link_file "tdm_textures_base01.pk4"
link_file "tdm_textures_stone_natural01.pk4"
link_file "tdm_ai_steambots01.pk4"
link_file "tdm_sound_ambient01.pk4"
link_file "tdm_textures_carpet01.pk4"
link_file "tdm_textures_stone_sculpted01.pk4"
link_file "tdm_base01.pk4"
link_file "tdm_sound_ambient02.pk4"
link_file "tdm_textures_decals01.pk4"
link_file "tdm_textures_window01.pk4"

if [ ! -d "$(eval echo ~$USER)/.local/share/darkmod/fms/stlucia" ]; then
    echo -e "Linking missing game file fms/stlucia\n"
    mkdir "$(eval echo ~$USER)/.local/share/darkmod/fms/stlucia"
    ln -s "/opt/darkmod/fms/stlucia/stlucia.pk4" "$(eval echo ~$USER)/.local/share/darkmod/fms/stlucia/stlucia.pk4"
fi
if [ ! -d "$(eval echo ~$USER)/.local/share/darkmod/fms/newjob" ]; then
    echo -e "Linking missing game file fms/newjob\n"
    mkdir "$(eval echo ~$USER)/.local/share/darkmod/fms/newjob"
    ln -s "/opt/darkmod/fms/newjob/newjob.pk4" "$(eval echo ~$USER)/.local/share/darkmod/fms/newjob/newjob.pk4"
fi
if [ ! -d "$(eval echo ~$USER)/.local/share/darkmod/fms/training_mission" ]; then
    echo -e "Linking missing game file fms/training_mission\n"
    mkdir "$(eval echo ~$USER)/.local/share/darkmod/fms/training_mission"
    ln -s "/opt/darkmod/fms/training_mission/training_mission.pk4" "$(eval echo ~$USER)/.local/share/darkmod/fms/training_mission/training_mission.pk4"
fi

link_file "tdm_defs01.pk4"
link_file "tdm_sound_ambient03.pk4"
link_file "tdm_textures_door01.pk4"
link_file "tdm_textures_wood01.pk4"
link_file "tdm_env01.pk4"
link_file "tdm_sound_ambient_decls01.pk4"
link_file "tdm_textures_fabric01.pk4"
link_file "tdm_ai_animals01.pk4"
link_file "tdm_fonts01.pk4"
link_file "tdm_sound_sfx01.pk4"
link_file "tdm_textures_glass01.pk4"
link_file "tdm_ai_base01.pk4"
link_file "tdm_game01.pk4"
link_file "tdm_sound_sfx02.pk4"
link_file "tdm_textures_metal01.pk4"
link_file "tdm_version_info.txt"
link_file "tdm_ai_humanoid_builders01.pk4"
link_file "tdm_game02.pk4"
link_file "tdm_sound_vocals01.pk4"
link_file "tdm_textures_nature01.pk4"
#link_file "thedarkmod.x86" # May want to copy this instead
link_file "tdm_ai_humanoid_females01.pk4"
link_file "tdm_gui01.pk4"
link_file "tdm_sound_vocals02.pk4"
link_file "tdm_textures_other01.pk4"
link_file "tdm_ai_humanoid_guards01.pk4"
link_file "tdm_gui_credits01.pk4"
link_file "tdm_sound_vocals03.pk4"
link_file "tdm_textures_paint_paper01.pk4"
link_file "tdm_ai_humanoid_heads01.pk4"
link_file "tdm_sound_vocals04.pk4"
link_file "tdm_textures_plaster01.pk4"
link_file "tdm_ai_humanoid_mages01.pk4"
link_file "tdm_sound_vocals05.pk4"
link_file "tdm_textures_roof01.pk4"

if [ ! -f $(eval echo ~$USER)/.local/share/darkmod/darkmod.ini ]; then
    echo -e "Copying darkmod.ini"
    cp /opt/darkmod/darkmod.ini $(eval echo ~$USER)/.local/share/darkmod/darkmod.ini
fi

if [ ! -f $(eval echo ~$USER)/.local/share/darkmod/thedarkmod.x86 ]; then
    echo -e "Copying darkmod executable"
    cp /opt/darkmod/thedarkmod.x86 $(eval echo ~$USER)/.local/share/darkmod/thedarkmod.x86
    chmod +x $(eval echo ~$USER)/.local/share/darkmod/thedarkmod.x86
fi

$(eval echo ~$USER)/.local/share/darkmod/thedarkmod.x86
