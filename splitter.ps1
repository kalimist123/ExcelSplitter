# Copyright (c) 2012, Bryan O'Connell
# License: http://bryanoconnell.blogspot.com/p/licenses.html 
# Purpose: Extract all of the worksheets from an Excel file into separate files.
[CmdletBinding()]
Param ( 
    [Parameter(Mandatory=$true,Position=0)] 
    [string]$filepath,
    [Parameter(Mandatory=$true,Position=1)] 
    [ValidateSet("csv","txt","xls","html")] 
    [string]$output_type 
)


#-----------------------------------------------------------------------------#


# Figures out and returns the 'XlFileFormat Enumeration' ID for the specified format.
# http://msdn.microsoft.com/en-us/library/office/bb241279%28v=office.12%29.aspx 
# NOTE: The code being used for 'xls' is actually a 'text' type, but it seemed
# to work the best for splitting the worksheets into separate Excel files.
function GetOutputFileFormatID 
{ 
Param([string]$fomat_name) 
    $Result = 0 
    switch($fomat_name) 
    { 
        "csv" {$Result = 6} 
        "txt" {$Result = 20} 
        "xls" {$Result = 21} 
        "html" {$Result = 44} 
        default {$Result = 51} 
    } 
    
    return $Result 
}

$Path = $PSScriptRoot +'\'

$filepath = $Path+ $filepath

#-----------------------------------------------------------------------------# 
$Excel = New-Object -ComObject "Excel.Application" 
$Excel.Visible = $false #Runs Excel in the background. 
$Excel.DisplayAlerts = $false #Supress alert messages. 
$Workbook = $Excel.Workbooks.open($filepath) 
#Loop through the Workbook and extract each Worksheet
#     in the specified file type. 
if ($Workbook.Worksheets.Count -gt 0) { 
    write-Output "Now processing: $WorkbookName" 
    
    $FileFormat = GetOutputFileFormatID($output_type) 
    #Strip off the Excel extension. 
    $WorkbookName = $filepath -replace ".xlsx", "" #Post 2007 extension
    $WorkbookName = $WorkbookName -replace ".xls", "" #Pre 2007 extension 
    $Worksheet = $Workbook.Worksheets.item(1) 
    foreach($Worksheet in $Workbook.Worksheets) { 
        $ExtractedFileName = $WorkbookName + "_worksheet_" + $Worksheet.Name + "." + $output_type 
        $Worksheet.SaveAs($ExtractedFileName, $FileFormat) 
        write-Output "Created file: $ExtractedFileName" 
    } 
} 
#Clean up & close the main Excel objects. 
$Workbook.Close() 
$Excel.Quit()