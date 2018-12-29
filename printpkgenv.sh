#!/bin/bash

grep_function() {
    { declare -f "$1" || declare -f package; } 2>/dev/null | grep -E "$2"
}

extract_function_variable() {
	# $1: function name
	# $2: variable name
	# $3: multivalued
	# $4: name of output var

	local funcname=$1 attr=$2 isarray=$3 outputvar=$4 attr_regex= decl= r=1

	if (( isarray )); then
		printf -v attr_regex '^[[:space:]]* %s\+?=\(' "$2"
	else
		printf -v attr_regex '^[[:space:]]* %s\+?=[^(]' "$2"
	fi

	# this function requires extglob - save current status to restore later
	local shellopts=$(shopt -p extglob)
	shopt -s extglob

    #declare -f $funcname
	while read -r; do
		# strip leading whitespace and any usage of declare
		decl=${REPLY##*([[:space:]])}
		# printf "${decl/#$attr/$outputvar}"
		eval "${decl/#$attr/$outputvar}"

		# entering this loop at all means we found a match, so notify the caller.
		r=0
	done < <(grep_function "$funcname" "$attr_regex")

	eval "$shellopts"

	return $r
}


set +e
env -i
source "$1" || true
echo "pkgname=(" "${pkgname[@]}" ")"
echo "makedepends=(" "${makedepends[@]}" ")"

overrides=(provides depends)
# echo "Len =" "${#pkgname[@]}"
if [[ -n "${2// }" ]]; then
    echo "# We are going to process split"
    extract_function_variable "package_$2" "depends" 1 depends
    extract_function_variable "package_$2" "provides" 1 provides
fi

echo "provides=(" "${provides[@]}" ")"
echo "depends=(" "${depends[@]}" ")"

exit 0
