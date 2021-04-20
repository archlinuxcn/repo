#!/bin/bash

java_=$(source PKGBUILD && echo $java_)

if ! tmpdir=$(mktemp --directory --tmpdir graalvm-test.XXXX); then
    exit
fi
cd -- "$tmpdir" || exit
function cleanup {
    cd / || exit
    rm -rf -- "$tmpdir"
}
trap cleanup EXIT
PATH=/usr/lib/jvm/java-${java_}-graalvm/bin/:$(systemd-path search-binaries-default)

printf '%s\n' 'Testing polyglot R, JavaScript, Python, Ruby, and Java...'

cat > test.R << 'EOF'
jsPlus = eval.polyglot('js', '(function(s1, s2) { return s1 + s2; })')
pythonPlus = eval.polyglot('python', 'lambda s1, s2: s1 + s2')
rubyOne = eval.polyglot('ruby', '1')
pythonOne = eval.polyglot('python', '1')
rOne = 1
jvmPrint = java.type("java.lang.System")$out$println
jvmPrint(pythonPlus(jsPlus(rubyOne, pythonOne), rOne))
EOF

rThree=$(Rscript --polyglot --jvm test.R) || exit
if [[ $rThree != 3 ]]; then
    printf 'expected 3, got %q\n' "$rThree"
    exit 1
fi

printf '%s\n' 'Testing native image...'

cat > Test.java << 'EOF'
public class Test {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}
EOF
javac Test.java || exit
native-image Test > /dev/null || exit

helloWorld=$(./test) || exit
if [[ $helloWorld != 'Hello, world!' ]]; then
    printf 'expected "Hello, world!", got %q\n' "$helloWorld"
    exit 1
fi

printf '%s\n' 'Testing Espresso...'

# reusing the same Test.java / Test.class
helloWorld=$(java -truffle Test) || exit
if [[ $helloWorld != 'Hello, world!' ]]; then
    printf 'expected "Hello, world!", got %q\n' "$helloWorld"
    exit 1
fi

printf '%s\n' 'Testing GraalWASM...'

PATH=$PATH:/usr/lib/emscripten

cat > hello.c << 'EOF'
#include <stdio.h>

int main() {
  printf("Hello, WASM!\n");
  return 0;
}
EOF
emcc -o hello.wasm hello.c 2>/dev/null || exit

helloWorld=$(wasm --Builtins=wasi_snapshot_preview1 hello.wasm) || exit
if [[ $helloWorld != 'Hello, WASM!' ]]; then
    printf 'expected "Hello, WASM!", got %q\n' "$helloWorld"
    exit 1
fi

printf '%s\n' 'Done.'
