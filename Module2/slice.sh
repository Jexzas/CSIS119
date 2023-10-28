theStr="Howdy! Come here often?"
sub1=${theStr:0:3}
sub2=${theStr:7:10}
sub3=${theStr:22:1}
echo "$sub1 $sub2 $sub3"
#outputs "How Come here ?"