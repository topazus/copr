use v5.36;
my @a=qw(aa bb);
say @a;
foreach (@a){
    say;
}
foreach my $x (@a){
    say $x;
}
sub square{
    my $num=shift;
    return $num*$num;
}
say square(2,4);