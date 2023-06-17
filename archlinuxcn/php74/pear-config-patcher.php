<?php
if (!isset($argv, $argc)) {
    echo "No command line args provided\n";
    exit(1);
}
if ($argc < 3) {
    echo "Not all command line args provided\n";
    exit(2);
}
$targetFile = $confFile = $argv[1];
$varPath = $argv[2];

$data = '';
$file = fopen($confFile, "r");

if ($file !== false) {
    while(!feof($file)) {
        $line = fgets($file);
        $serialized = @unserialize($line);
        if (is_array($serialized)) {
            $serialized['temp_dir'] = "{$varPath}/temp";
            $serialized['cache_dir'] = "{$varPath}/cache";
            $serialized['download_dir'] = "{$varPath}/download";
            $serialized['metadata_dir'] = "{$varPath}/metadata";
            $data .= @serialize($serialized);
            $data .= "\n";
        } else {
            $data .= $line;
        }
    }
    fclose($file);
    if (false !== file_put_contents($targetFile, $data)) {
        echo "Written to $targetFile\n";
    } else {
        echo "Failed to write to $targetFile\n";
        exit(3);
    }
} else {
    echo "File was not found {$confFile}\n";
    exit(4);
}
exit(0);
