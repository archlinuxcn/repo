#!/bin/bash

# Clear symlinks
cd /usr/lib/ccache/bin
for file in {*-,}{c++,cc,clang,clang++,g++,gcc}{,-[0-9]*}
do
    if [[ -L $file ]]
    then
        rm "/usr/lib/ccache/bin/$file"
    fi
done

# Recreate synlinks
cd /usr/bin
for file in {*-,}{c++,cc,clang,clang++,g++,gcc}{,-[0-9]*}
do
    if [[ -x $file ]]
    then
        ret=`pacman -Qqo "/usr/bin/$file" | grep -e gcc -e clang`
        if [[ $ret ]]
        then
            ln -s /usr/bin/ccache "/usr/lib/ccache/bin/$file"
        fi
    fi
done

# Update nvcc
{
    [ -f "/usr/lib/ccache/bin/nvcc-ccache" ] && rm "/usr/lib/ccache/bin/nvcc-ccache"
    if [[ -f /opt/cuda/bin/nvcc ]]
    then
        echo -e "#!/bin/sh -\n/usr/bin/ccache /opt/cuda/bin/nvcc \"\$@\"" > /usr/lib/ccache/bin/nvcc-ccache
        chmod 755 /usr/lib/ccache/bin/nvcc-ccache
    fi
}
