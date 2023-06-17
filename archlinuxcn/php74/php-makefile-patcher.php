<?php
if (!isset($argv, $argc)) {
    echo "No command line args provided\n";
    exit(1);
}
if ($argc < 2) {
    echo "Not all command line args provided\n";
    exit(2);
}
$filename = $argv[1];
$fileContent = @file_get_contents($filename);
if (!strlen($fileContent)) {
    echo "No file contents of $filename\n";
    exit(3);
}
$matches = array();
$match = preg_match("/^(?P<line>(?P<definition>PHP_MODULES[\s\t]+=[\s\t]+)(?P<expression>.*)$)/m", $fileContent, $matches);
if (!$match) {
    echo "No PHP_MODULES in $filename\n";
    exit (4);
}
$expression = explode(' ', $matches['expression']);
function sortByPrio($a, $b) {
    $aPrio = 999;
    $bPrio = 999;
    $priorities = array('/openssl/i'=> 0, '@\/xml\.@i'=>1, '@\/pdo\.@i'=>2, '@\/dom\.@i'=>3, '/mysqlnd/i'=>4);
    foreach ($priorities as $regex => $prio) {
        if (preg_match($regex, $a) && $prio < $aPrio) {
            $aPrio = $prio;
        }
        if (preg_match($regex, $b) && $prio < $bPrio) {
            $bPrio = $prio;
        }
    }
    if ($aPrio == $bPrio) {
        return 0;
    }
    return $aPrio > $bPrio ? 1: -1;
}
usort($expression, 'sortByPrio');
$expression = $matches['definition'].join (' ', $expression)."\n";
$fileContent = str_replace($matches['line'], $expression, $fileContent);
if (!file_put_contents($filename, $fileContent)) {
    echo "Failed to write to $filename\n";
    exit(5);
}
exit(0);
