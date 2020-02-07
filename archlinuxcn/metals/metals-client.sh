#!/bin/bash

set -e

declare -r _INSTALL_DIR='/usr/share/java/metals'
declare _CP="$_INSTALL_DIR/lib:$_INSTALL_DIR/metals"

# This is an ordered array of JDK paths to attempt to use if
# METALS_JDK_PATH is unset. They are based off of the default
# installation locations of the various JDKs in Arch Linux.
#
# We only explicitly try known working versions, at the time of
# writing that is >= 8 and <= 11. We prefer newer versions to older
# ones.
declare -r -a _JAVA_ARCH_PACKAGE_PATHS=('/usr/lib/jvm/java-11-openjdk/bin'
                                        '/usr/lib/jvm/java-10-openjdk/bin'
                                        '/usr/lib/jvm/java-8-openjdk/jre/bin'
                                       )

function ensure_comaptible_jdk {
    local -r _LEN="${#_JAVA_ARCH_PACKAGE_PATHS[@]}"
    local _INDEX=0
    local _PACKAGE_PATH

    if [ -n "$METALS_JDK_PATH" ]
    then
        if [ -d "$METALS_JDK_PATH" ]
        then
            if [ -x "${METALS_JDK_PATH}/java" ]
            then
                export PATH="$METALS_JDK_PATH:$PATH"
                return 0
            else
                echo "Directory specified at METALS_JDK_PATH=${METALS_JDK_PATH} does not contain an executable file named \"java\"." 1>&2
                exit 1
            fi
        else
            echo "METALS_JDK_PATH value set in environment, but $METALS_JDK_PATH is not a directory." 1>&2
            exit 2
        fi
    else
        while [ $_INDEX -lt "$_LEN" ]
        do
            _PACKAGE_PATH="${_JAVA_ARCH_PACKAGE_PATHS[$_INDEX]}"
            if [ -d "$_PACKAGE_PATH" ]
            then
                export PATH="$_PACKAGE_PATH:$PATH"
                return 0
            else
                _INDEX=$((_INDEX + 1))
                continue
            fi
        done
        echo 'Unable to find a Java >=8 and <=11 environment to use with certainty. To use Metals you should have a JDK >=8 and <=11 installed. Attempting to use the current environment.' 1>&2
    fi
}

function build_cp {
    while read -r name
    do
        _CP="$name:$_CP"
    done <<< "$(find "$_INSTALL_DIR"/jars -regex '.*\.jar')"
}

function main {
    ensure_comaptible_jdk

    build_cp

    # Echo out the full path to the Java binary we will use.
    echo "Java binary selected: $(command -v java)" 1>&2

    # Java options taken from metals-emacs documentation
    # https://scalameta.org/metals/docs/editors/emacs.HTML
    exec java -XX:+UseG1GC -XX:+UseStringDeduplication -Xss4m -Xms100m -Dmetals.client="$_METALS_CLIENT" -cp "$_CP" scala.meta.metals.Main "$@"
}

main "$@"
