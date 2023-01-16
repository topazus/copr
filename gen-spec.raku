my @a1=['jetbrains-idea/idea','jetbrains-clion/clion','jetbrains-pycharm/pycharm',
'comma-ide/comma-ide','jetbrains-jre/jetbrains-jre','flutter','rakudo','zig','groovy','scala3'];
sub f($x){ "https://raw.githubusercontent.com/topazus/fedora-copr/main/$x.spec" }
my $res=map(&f,@a1);
say $res.join("\n");

@a1.map(->$x {"https://raw.githubusercontent.com/topazus/fedora-copr/main/$x.spec"});

my $a2=['alacritty','archey4','chez-scheme','clifm','fzf','flutter','bottom','alacritty','rakudo','zig'];
