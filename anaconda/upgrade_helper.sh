#!/bin/bash

echo "update pkgver in PKGBUILD"
read

echo "Downloading files (checks will fail)"
makepkg --verifysource
CARCH=x86 makepkg --verifysource

source PKGBUILD
anaconda_x86_64=Anaconda3-${pkgver}-Linux-x86_64.sh
anaconda_x86=Anaconda3-${pkgver}-Linux-x86.sh
cp $anaconda_x86_64 ${anaconda_x86_64}.old
cp $anaconda_x86 ${anaconda_x86}.old

echo "Modify $anaconda_x86 and $anaconda_x86_64"
read

diff -u ${anaconda_x86_64}.old $anaconda_x86_64 > installer_sh_x86_64.patch
diff -u ${anaconda_x86}.old $anaconda_x86 > installer_sh_x86.patch

mv -f ${anaconda_x86_64}.old $anaconda_x86_64
mv -f ${anaconda_x86}.old $anaconda_x86

echo "Clean installer_sh_x86_64.patch and installer_sh_x86.patch (update header and remove tail)"
read

updpkgsums
sha256sum $anaconda_x86
echo "update sha256sum for $anaconda_x86 in PKGBUILD"
read
BREAK_EARLY=1 makepkg
grep CONDA_INSTALL= installer_sh_x86_64.patch
echo "Edit conda_install patch to have correct conda version in header"
read

cd pkg/anaconda/opt/anaconda/
conda_install=`ls -1 pkgs/conda-3.*/lib/python*/site-packages/conda/install.py`
cp $conda_install ${conda_install}.old
echo "Trying patch as is:"
patch -p1 < ../../../../conda_install.patch

diff -u ${conda_install}.old ${conda_install} > ../../../../conda_install.patch

cd -

echo "Check conda_install.patch and update header"

read
updpkgsums
grep CONDA_INSTALL= installer_sh_x86_64.patch
grep PYTHON= installer_sh_x86_64.patch
echo "Update _pythonver and _condaver in PKGBUILD"
read

echo "upgrading srcinfo"
mksrcinfo
echo "Done"
