#!/usr/bin/bash

test_results() {
    cmd="$1"; shift
    expected="$1"
    tmpfile=$(mktemp)
    
    for file in sample*; do
        "${cmd}" "${file}" >> "$tmpfile" 
    done

    diff -b -u --color=always "$expected" "$tmpfile"
    rm "$tmpfile"
}

run_tests() {
    cmd="./$1"; shift
    expected=("${@}")

    test_results "$cmd" "${expected[@]}"
    printf "\n"
}

for exec in "$@"; do 
    name=$(echo "$exec" | rev | cut -d . -f2- | rev)
    
    expected_file="${name}_expected.txt"
    
    if [ -f "$expected_file" ]; then
        run_tests "$exec" "$expected_file"
    else 
        printf "Expected file '%s' not found for '%s'. Skipping tests.\n" "$expected_file" "$exec"
    fi
done

