#!/usr/bin/env bash

. /usr/share/makepkg/util/message.sh
colorize

Detect_CPU=$(gcc -c -Q -march=native --help=target | grep march | awk '{print $2}' | head -1)

msg "Detected CPU architecture: $Detect_CPU"

cat << EOF

    Available CPU microarchitectures:

    1) AMD Opteron/Athlon64/Hammer/K8
    2) AMD Opteron/Athlon64/Hammer/K8 with SSE3
    3) AMD 61xx/7x50/PhenomX3/X4/II/K10
    4) AMD Family 10h (Barcelona)
    5) AMD Family 14h (Bobcat)
    6) AMD Family 16h (Jaguar)
    7) AMD Family 15h (Bulldozer)
    8) AMD Family 15h (Piledriver)
    9) AMD Family 15h (Steamroller)
   10) AMD Family 15h (Excavator)
   11) AMD Family 17h (Zen)
   12) AMD Family 17h (Zen 2)
   13) AMD Family 19h (Zen 3)
   14) AMD Family 19h (Zen 4)
   15) AMD Family 19h (Zen 5)
   20) Intel P4 / older Netburst based Xeon
   21) Intel Core 2 and newer Core 2 Xeons (Xeon 51xx and 53xx)
   22) Intel Atom
   23) Intel 1st Gen Core i3/i5/i7-family (Nehalem)
   24) Intel 1.5 Gen Core i3/i5/i7-family (Westmere)
   25) Intel Silvermont
   26) Intel Goldmont (Apollo Lake and Denverton)
   27) Intel Goldmont Plus (Gemini Lake)
   28) Intel 2nd Gen Core i3/i5/i7-family (Sandybridge)
   29) Intel 3rd Gen Core i3/i5/i7-family (Ivybridge)
   30) Intel 4th Gen Core i3/i5/i7-family (Haswell)
   31) Intel 5th Gen Core i3/i5/i7-family (Broadwell)
   32) Intel 6th Gen Core i3/i5/i7-family (Skylake)
   33) Intel 6th Gen Core i7/i9-family (Skylake X)
   34) Intel 8th Gen Core i3/i5/i7-family (Cannon Lake)
   35) Intel 8th Gen Core i7/i9-family (Ice Lake)
   36) Xeon processors in the Cascade Lake family
   37) Intel Xeon (Cooper Lake)
   38) Intel 3rd Gen 10nm++ i3/i5/i7/i9-family (Tiger Lake)
   39) Intel Sapphire Rapids
   40) Intel Rocket Lake
   41) Intel Alder Lake
   42) Intel Raptor Lake
   43) Intel Meteor Lake
   44) Intel Emerald Rapids

   98) Intel-Native optimizations autodetected by GCC
   99) AMD-Native optimizations autodetected by GCC

    0) Generic x64 (default)
    
EOF

sleep 1
answer=$1

case $answer in
     1) Microarchitecture=CONFIG_MK8 ;;
     2) Microarchitecture=CONFIG_MK8SSE3 ;;
     3) Microarchitecture=CONFIG_MK10 ;;
     4) Microarchitecture=CONFIG_MBARCELONA ;;
     5) Microarchitecture=CONFIG_MBOBCAT ;;
     6) Microarchitecture=CONFIG_MJAGUAR ;;
     7) Microarchitecture=CONFIG_MBULLDOZER ;;
     8) Microarchitecture=CONFIG_MPILEDRIVER ;;
     9) Microarchitecture=CONFIG_MSTEAMROLLER ;;
    10) Microarchitecture=CONFIG_MEXCAVATOR ;;
    11) Microarchitecture=CONFIG_MZEN ;;
    12) Microarchitecture=CONFIG_MZEN2 ;;
    13) Microarchitecture=CONFIG_MZEN3 ;;
    14) Microarchitecture=CONFIG_MZEN4 ;;
    15) Microarchitecture=CONFIG_MZEN5 ;;
    20) Microarchitecture=CONFIG_MPSC ;;
    21) Microarchitecture=CONFIG_MCORE2 ;;
    22) Microarchitecture=CONFIG_MATOM ;;
    23) Microarchitecture=CONFIG_MNEHALEM ;;
    24) Microarchitecture=CONFIG_MWESTMERE ;;
    25) Microarchitecture=CONFIG_MSILVERMONT ;;
    26) Microarchitecture=CONFIG_MGOLDMONT ;;
    27) Microarchitecture=CONFIG_MGOLDMONTPLUS ;;
    28) Microarchitecture=CONFIG_MSANDYBRIDGE ;;
    29) Microarchitecture=CONFIG_MIVYBRIDGE ;;
    30) Microarchitecture=CONFIG_MHASWELL ;;
    31) Microarchitecture=CONFIG_MBROADWELL ;;
    32) Microarchitecture=CONFIG_MSKYLAKE ;;
    33) Microarchitecture=CONFIG_MSKYLAKEX ;;
    34) Microarchitecture=CONFIG_MCANNONLAKE ;;
    35) Microarchitecture=CONFIG_MICELAKE ;;
    36) Microarchitecture=CONFIG_MCASCADELAKE ;;
    37) Microarchitecture=CONFIG_MCOOPERLAKE ;;
    38) Microarchitecture=CONFIG_MTIGERLAKE ;;
    39) Microarchitecture=CONFIG_MSAPPHIRERAPIDS ;;
    40) Microarchitecture=CONFIG_MROCKETLAKE ;;
    41) Microarchitecture=CONFIG_MALDERLAKE ;;
    42) Microarchitecture=CONFIG_MRAPTORLAKE ;;
    43) Microarchitecture=CONFIG_MMETEORLAKE ;;
    44) Microarchitecture=CONFIG_MEMERALDRAPIDS ;;
    98) Microarchitecture=CONFIG_MNATIVE_INTEL ;;
    99) Microarchitecture=CONFIG_MNATIVE_AMD ;;
     *) default=CONFIG_GENERIC_CPU ;;
esac

warning "According to PKGBUILD variable _microarchitecture, your choice is $answer"
msg "Building this package for microarchitecture: $Microarchitecture$default"
sleep 5

_defaultmicro=$(grep ^CONFIG_LOCALVERSION .config)
if [ -z "${default}" ]; then
    _localversion=$(echo ${Microarchitecture,,} | sed -e 's/config_m/-/g')
    sed -e "s|^$_defaultmicro|CONFIG_LOCALVERSION=\"$_localversion\"|g" -i .config
    sed -e 's|^CONFIG_GENERIC_CPU=y|# CONFIG_GENERIC_CPU is not set|g' -i .config
    sed -e "s|^# $Microarchitecture is not set|$Microarchitecture=y|g" -i .config
fi

echo
