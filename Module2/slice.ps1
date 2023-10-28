$TheStr = "Howdy! Come here often?"
$str1 = $TheStr.Substring(0, 3)
$str2 = $TheStr.Substring(7, 9)
$str3 = $TheStr.Substring(22, 1)
Write-Host "$str1 $str2 $str3"
# Prints "How Come here ?"