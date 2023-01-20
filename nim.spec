%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname nim

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A statically typed compiled systems programming language
License:        MIT
URL:            https://github.com/nim-lang/Nim
#Source:

BuildRequires:  gcc make git

Requires:       pcre openssl

%description
Nim is a statically typed compiled systems programming language.

%prep
git clone --depth=1 %{url} .

%build
./build_all.sh


%install
./koch install %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -pDm755 bin/nim* -t %{buildroot}%{_bindir}

#for x in nim nimble nimgrep nimpretty nimsuggest; do
#  install -pDm755 bin/$x %{buildroot}%{_bindir}/$x
#done

mkdir -p %{buildroot}/usr/lib/nim %{buildroot}%{_includedir}

cp -r %{buildroot}/nim/lib %{buildroot}/nim/compiler %{buildroot}/usr/lib/nim

install -pDm644 config/* -t %{buildroot}%{_sysconfdir}/nim

# completions
install -pDm644 tools/nim.bash-completion %{buildroot}%{_datadir}/bash-completion/completions/nim
install -pDm644 tools/nim.zsh-completion %{buildroot}%{_datadir}/zsh/site-functions/_nim

install -pDm644 dist/nimble/nimble.bash-completion %{buildroot}%{_datadir}/bash-completion/completions/nimble
install -pDm644 dist/nimble/nimble.zsh-completion %{buildroot}%{_datadir}/zsh/site-functions/_nimble

rm -rf %{buildroot}/nim

%check

%files
%{_bindir}/nim*

/usr/lib/nim/

/etc/nim/

%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/_*

%changelog
