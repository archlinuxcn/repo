#!/bin/bash

set -e

declare -r _INSTALL_DIR='/usr/share/java/metals'
declare -r _UTIL_DIR="${_INSTALL_DIR}/util"
declare _CP="$_INSTALL_DIR/lib:$_INSTALL_DIR/metals"

# This is an ordered array of JDK paths to attempt to use if
# METALS_JDK_PATH is unset. They are based off of the default
# installation locations of the various JDKs in Arch Linux.
#
# We only explicitly try known working versions, at the time of
# writing that is >= 8 and <= 17. We prefer newer versions to older
# ones.
declare -r -a _JAVA_ARCH_PACKAGE_PATHS=('/usr/lib/jvm/java-17-openjdk/bin'
                                        '/usr/lib/jvm/java-16-openjdk/bin'
                                        '/usr/lib/jvm/java-15-openjdk/bin'
                                        '/usr/lib/jvm/java-14-openjdk/bin'
                                        '/usr/lib/jvm/java-13-openjdk/bin'
                                        '/usr/lib/jvm/java-12-openjdk/bin'
                                        '/usr/lib/jvm/java-11-openjdk/bin'
                                        '/usr/lib/jvm/java-10-openjdk/bin'
                                        '/usr/lib/jvm/java-8-openjdk/jre/bin'
                                       )
declare -r -a _DEFAULT_METALS_JAVA_OPTS=('-XX:MaxHeapFreeRatio=20' '-XX:MinHeapFreeRatio=5' '-XX:MaxRAMPercentage=25.0')

# The _actual_ metals options will be put here after
# setup_metals_java_opts is run.
declare -a _METALS_JAVA_OPTS

# Used in conjunction with _DEFAULT_METALS_JAVA_OPTS to determine
# which java options to are supported. Not used or set if
# METALS_JAVA_OPTS is explicitly set.
declare _JRE_VERSION

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

function determine_jre_version {
    pushd "$_UTIL_DIR" &>/dev/null
    _JRE_VERSION="$(java JREMajorVersion)"
    popd &>/dev/null
    readonly _JRE_VERSION
    echo "JRE version determined to be ${_JRE_VERSION}" 1>&2
}

function setup_metals_java_opts {
    if [ -n "$METALS_JAVA_OPTS" ]
    then
        read -r -a _METALS_JAVA_OPTS <<< "$METALS_JAVA_OPTS"
        echo "Found METALS_JAVA_OPTS: ${_METALS_JAVA_OPTS[*]}" 1>&2
    else
        _METALS_JAVA_OPTS+=("${_DEFAULT_METALS_JAVA_OPTS[@]}")

        determine_jre_version

        if [ "$_JRE_VERSION" -gt 9 ]
        then
            _METALS_JAVA_OPTS+=("${_DEFAULT_JDK_10_PLUS_OPTS[@]}")
        fi

        echo "Using default METALS_JAVA_OPTS: ${_METALS_JAVA_OPTS[*]}" 1>&2
    fi

    readonly -a _METALS_JAVA_OPTS
}

function main {
    ensure_comaptible_jdk

    build_cp

    # Echo out the full path to the Java binary we will use.
    echo "Java binary selected: $(command -v java)" 1>&2

    setup_metals_java_opts

    if [ -z "$_METALS_CLIENT" ]
    then
        exec java "${_METALS_JAVA_OPTS[@]}" -cp "$_CP" scala.meta.metals.Main "$@"
    else
        exec java "${_METALS_JAVA_OPTS[@]}" -Dmetals.client="$_METALS_CLIENT" -cp "$_CP" scala.meta.metals.Main "$@"
    fi
}

main "$@"
