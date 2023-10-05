if [[ $FLAVOUR == "1" ]]; then
    FLAVOURNAME="Mocha";
elif [[ $FLAVOUR == "2" ]]; then
    FLAVOURNAME="Macchiato";
elif [[ $FLAVOUR == "3" ]]; then
    FLAVOURNAME="Frappe";
elif [[ $FLAVOUR == "4" ]]; then
    FLAVOURNAME="Latte";
else echo "Not a valid flavour name" && exit;
fi

if [[ $ACCENT == "1" ]]; then

    if [[ $FLAVOUR == "1" ]]; then
        ACCENTCOLOR="245,224,220"
    elif [[ $FLAVOUR == "2" ]]; then
        ACCENTCOLOR="244,219,214"
    elif [[ $FLAVOUR == "3" ]]; then
        ACCENTCOLOR="242,213,207"
    elif [[ $FLAVOUR == "4" ]]; then
        ACCENTCOLOR="220,138,120"
    fi
    ACCENTNAME="Rosewater"
elif [[ $ACCENT == "2" ]]; then
    if [[ $FLAVOUR == "1" ]]; then
        ACCENTCOLOR="242,205,205"
    elif [[ $FLAVOUR == "2" ]]; then
        ACCENTCOLOR="240,198,198"
    elif [[ $FLAVOUR == "3" ]]; then
        ACCENTCOLOR="238,190,190"
    elif [[ $FLAVOUR == "4" ]]; then
        ACCENTCOLOR="221,120,120"
    fi
    ACCENTNAME="Flamingo"
elif [[ $ACCENT == "3" ]]; then
    if [[ $FLAVOUR == "1" ]]; then
        ACCENTCOLOR="245,194,231"
    elif [[ $FLAVOUR == "2" ]]; then
        ACCENTCOLOR="245,189,230"
    elif [[ $FLAVOUR == "3" ]]; then
        ACCENTCOLOR="244,184,228"
    elif [[ $FLAVOUR == "4" ]]; then
        ACCENTCOLOR="234,118,203"
    fi
    ACCENTNAME="Pink"
elif [[ $ACCENT == "4" ]]; then
    if [[ $FLAVOUR == "1" ]]; then
        ACCENTCOLOR="203,166,247"
    elif [[ $FLAVOUR == "2" ]]; then
        ACCENTCOLOR="198,160,246"
    elif [[ $FLAVOUR == "3" ]]; then
        ACCENTCOLOR="202,158,230"
    elif [[ $FLAVOUR == "4" ]]; then
        ACCENTCOLOR="136,57,239"
    fi
    ACCENTNAME="Mauve"
elif [[ $ACCENT == "5" ]]; then
    if [[ $FLAVOUR == "1" ]]; then
        ACCENTCOLOR="243,139,168"
    elif [[ $FLAVOUR == "2" ]]; then
        ACCENTCOLOR="237,135,150"
    elif [[ $FLAVOUR == "3" ]]; then
        ACCENTCOLOR="231,130,132"
    elif [[ $FLAVOUR == "4" ]]; then
        ACCENTCOLOR="210,15,57"
    fi
    ACCENTNAME="Red"
elif [[ $ACCENT == "6" ]]; then
    if [[ $FLAVOUR == "1" ]]; then
        ACCENTCOLOR="235,160,172"
    elif [[ $FLAVOUR == "2" ]]; then
        ACCENTCOLOR="238,153,160"
    elif [[ $FLAVOUR == "3" ]]; then
        ACCENTCOLOR="234,153,156"
    elif [[ $FLAVOUR == "4" ]]; then
        ACCENTCOLOR="230,69,83"
    fi
    ACCENTNAME="Maroon"
elif [[ $ACCENT == "7" ]]; then
    if [[ $FLAVOUR == "1" ]]; then
        ACCENTCOLOR="250,179,135"
    elif [[ $FLAVOUR == "2" ]]; then
        ACCENTCOLOR="245,169,127"
    elif [[ $FLAVOUR == "3" ]]; then
        ACCENTCOLOR="239,159,118"
    elif [[ $FLAVOUR == "4" ]]; then
        ACCENTCOLOR="254,100,11"
    fi
    ACCENTNAME="Peach"
elif [[ $ACCENT == "8" ]]; then
    if [[ $FLAVOUR == "1" ]]; then
        ACCENTCOLOR="249,226,175"
    elif [[ $FLAVOUR == "2" ]]; then
        ACCENTCOLOR="238,212,159"
    elif [[ $FLAVOUR == "3" ]]; then
        ACCENTCOLOR="229,200,144"
    elif [[ $FLAVOUR == "4" ]]; then
        ACCENTCOLOR="223,142,29"
    fi
    ACCENTNAME="Yellow"
elif [[ $ACCENT == "9" ]]; then
    if [[ $FLAVOUR == "1" ]]; then
        ACCENTCOLOR="166,227,161"
    elif [[ $FLAVOUR == "2" ]]; then
        ACCENTCOLOR="166,218,149"
    elif [[ $FLAVOUR == "3" ]]; then
        ACCENTCOLOR="166,209,137"
    elif [[ $FLAVOUR == "4" ]]; then
        ACCENTCOLOR="64,160,43"
    fi
    ACCENTNAME="Green"
elif [[ $ACCENT == "10" ]]; then
    if [[ $FLAVOUR == "1" ]]; then
        ACCENTCOLOR="148,226,213"
    elif [[ $FLAVOUR == "2" ]]; then
        ACCENTCOLOR="139,213,202"
    elif [[ $FLAVOUR == "3" ]]; then
        ACCENTCOLOR="129,200,190"
    elif [[ $FLAVOUR == "4" ]]; then
        ACCENTCOLOR="23,146,153"
    fi
    ACCENTNAME="Teal"
elif [[ $ACCENT == "11" ]]; then
    if [[ $FLAVOUR == "1" ]]; then
        ACCENTCOLOR="137,220,235"
    elif [[ $FLAVOUR == "2" ]]; then
        ACCENTCOLOR="145,215,227"
    elif [[ $FLAVOUR == "3" ]]; then
        ACCENTCOLOR="153,209,219"
    elif [[ $FLAVOUR == "4" ]]; then
        ACCENTCOLOR="4,165,229"
    fi
    ACCENTNAME="Sky"
elif [[ $ACCENT == "12" ]]; then
    if [[ $FLAVOUR == "1" ]]; then
        ACCENTCOLOR="116,199,236"
    elif [[ $FLAVOUR == "2" ]]; then
        ACCENTCOLOR="125,196,228"
    elif [[ $FLAVOUR == "3" ]]; then
        ACCENTCOLOR="133,193,220"
    elif [[ $FLAVOUR == "4" ]]; then
        ACCENTCOLOR="32,159,181"
    fi
    ACCENTNAME="Sapphire"
elif [[ $ACCENT == "13" ]]; then
    if [[ $FLAVOUR == "1" ]]; then
        ACCENTCOLOR="137,180,250"
    elif [[ $FLAVOUR == "2" ]]; then
        ACCENTCOLOR="138,173,244"
    elif [[ $FLAVOUR == "3" ]]; then
        ACCENTCOLOR="140,170,238"
    elif [[ $FLAVOUR == "4" ]]; then
        ACCENTCOLOR="30,102,245"
    fi
    ACCENTNAME="Blue"
elif [[ $ACCENT == "14" ]]; then
    if [[ $FLAVOUR == "1" ]]; then
        ACCENTCOLOR="180,190,254"
    elif [[ $FLAVOUR == "2" ]]; then
        ACCENTCOLOR="183,189,248"
    elif [[ $FLAVOUR == "3" ]]; then
        ACCENTCOLOR="186,187,241"
    elif [[ $FLAVOUR == "4" ]]; then
        ACCENTCOLOR="114,135,253"
    fi
    ACCENTNAME="Lavender"
else echo "Not a valid accent" && exit
fi

if [[ $FLAVOUR == "1" ]]; then
    MANTLECOLOR=#181825
elif [[ $FLAVOUR == "2" ]]; then
    MANTLECOLOR=#1e2030
elif [[ $FLAVOUR == "3" ]]; then
    MANTLECOLOR=#292c3c
elif [[ $FLAVOUR == "4" ]]; then
    MANTLECOLOR=#e6e9ef
fi
