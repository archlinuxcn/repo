#!/bin/sh

SCRIPT_DIR=`dirname "$0"`
DAPHNE_BIN=/usr/share/daphne.bin
DAPHNE_SHARE=~/.daphne
DAPHNE_DATA=/usr/share/daphne

echo "Singe Launcher : Script dir is $SCRIPT_DIR"
cd "$SCRIPT_DIR"

# point to our linked libs that user may not have
LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH

if [ -z $1 ] ; then
	echo "Specify a game to try: timegal"
	exit
fi


#strace -o strace.txt \
./$DAPHNE_BIN singe vldp \
-framefile $DAPHNE_SHARE/singe/$1/$1.txt \
-script $DAPHNE_SHARE/singe/$1/$1.singe \
-homedir $DAPHNE_SHARE \
-datadir $DAPHNE_DATA \
-blank_searches \
-min_seek_delay 1000 \
-seek_frames_per_ms 20 \
-sound_buffer 2048 \
-noserversend \
-x 640 \
-y 480

#-bank 0 11111001 \
#-bank 1 00100111 \

EXIT_CODE=$?

if [ "$EXIT_CODE" -ne "0" ] ; then
	if [ "$EXIT_CODE" -eq "127" ]; then
		echo ""
		echo "Daphne failed to start."
		echo "This is probably due to a library problem."
		echo "Run ./daphne.bin directly to see which libraries are missing."
		echo ""
	else
		echo "DaphneLoader failed with an unknown exit code : $EXIT_CODE."
	fi
fi


