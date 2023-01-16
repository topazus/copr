%global debug_package %{nil}
%global appname nim

Name:           %{appname}
Version:        1.4.8
Release:        1%{?dist}
Summary:        A statically typed compiled systems programming language
License:        MIT
URL:            https://nim-lang.org/
Source:         https://nim-lang.org/download/nim-%{version}.tar.xz

BuildRequires: gcc make git

Requires: pcre openssl

%description
Nim is a statically typed compiled systems programming language. It combines successful concepts from mature languages like Python, Ada and Modula. Its design focuses on efficiency, expressiveness, and elegance (in that order of priority).

%prep
%autosetup -n nim-%{version} -p1

%build
bash build.sh
bin/nim c koch
./koch boot -d:release
./koch tools

%install
install -Dpm 0755 bin/* -t %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_prefix}/lib/nim %{buildroot}%{_includedir}

cp -a lib compiler %{buildroot}%{_prefix}/lib/nim

install -Dpm 0644 config/* -t %{buildroot}%{_sysconfdir}/nim

# completions
install -Dpm 0644 tools/nim.bash-completion %{buildroot}%{_datadir}/bash-completion/completions/nim
install -Dpm 0644 tools/nim.zsh-completion %{buildroot}%{_datadir}/zsh/site-functions/_nim

install -Dpm 0644 dist/nimble/nimble.bash-completion %{buildroot}%{_datadir}/bash-completion/completions/nimble
install -Dpm 0644 dist/nimble/nimble.zsh-completion %{buildroot}%{_datadir}/zsh/site-functions/_nimble

%check

%files
%license copying.txt
%{_bindir}/nim*
%{_bindir}/testament

%{_prefix}/lib/nim/*

%dir %{_sysconfdir}/nim
%{_sysconfdir}/nim/config.nims
%{_sysconfdir}/nim/nim.cfg
%{_sysconfdir}/nim/nimdoc.cfg
%{_sysconfdir}/nim/nimdoc.tex.cfg
%{_sysconfdir}/nim/rename.rules.cfg

%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/_*

%changelog
