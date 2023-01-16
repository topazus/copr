mkdir -p $1 && touch $1/$1.spec
rust2rpm $1 - > $1/$1.spec
