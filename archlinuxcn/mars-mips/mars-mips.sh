#!/bin/bash
java -Dswing.crossplatformlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel \
     -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true \
     -jar /usr/share/java/mars-mips/Mars.jar "$@"
