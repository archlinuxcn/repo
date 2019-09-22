#!/bin/sh

GenPatch()
{
    diff -ruN reg_tmp/ reg_tmp_fixed/ > reg.patch
}

Extract()
{
    rm -rf reg_tmp_fixed && \
    mkdir reg_tmp_fixed && \
    tar xvjf reg_files.tar.bz2 -C reg_tmp_fixed
}

GenSrcInfo()
{
    makepkg --printsrcinfo > .SRCINFO
}

Clean()
{
    git clean -xfd
}

Tar()
{
    cd reg_tmp && \
    tar -cvjSf reg_files.tar.bz2 * && \
    mv reg_files.tar.bz2 ../ && \
    cd ../
}

HelpApp()
{
    echo " Extra Commands:"
    echo " -p/--patch          Generate patch files between reg_tmp/ and reg_tmp_fixed/"
    echo " -e/--extract        Extract reg files from reg_files.tar.bz2 to dir reg_tmp_fixed/"
    echo " -g/--gen            Generate AUR package info to .SRCINFO"
    echo " -c/--clean          Clean files which not track by git"
    echo " -t/--tar            Package reg files and modify the md5 value in PKGBUILD"
    echo " -h/--help           Show program help info"
}

if [ -z $1 ]; then
    # Default generate AUR package info
    GenSrcInfo
    exit 0
fi
case $1 in
    "-p" | "--patch")
        GenPatch
    ;;
    "-e" | "--extract")
        Extract
    ;;
    "-g" | "--gen")
        GenSrcInfo
    ;;
    "-c" | "--clean")
        Clean
    ;;
    "-t" | "--tar")
        Tar
    ;;
    "-h" | "--help")
        HelpApp
    ;;
    *)
        echo -e "\033[31mgen: unrecognized option '$1' \033[0m"
        echo "Use -h|--help to get help"
        exit 1
    ;;
esac
exit 0
