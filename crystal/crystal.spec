%global debug_package %{nil}

Name:           crystal
Version:        1.6.2
Release:        1%{?dist}
Summary:        The Crystal Programming Language
License:        Apache
URL:            https://github.com/crystal-lang/crystal
Source:         https://github.com/crystal-lang/crystal/archive/%{version}.tar.gz

BuildRequires:  gcc make
BuildRequires:  libevent-devel pcre-devel gc-devel openssl-devel zlib-devel libyaml-devel
BuildRequires:  llvm14-devel llvm14-static wget tar

%description
Crystal is a general-purpose, object-oriented programming language.
With syntax inspired by Ruby, it is a compiled language with static
type-checking,serving both, humans and computers.

%prep
%autosetup -n %{name}-%{version} -p1
wget https://github.com/crystal-lang/crystal/releases/download/%{version}/crystal-%{version}-1-linux-x86_64.tar.gz
tar xf crystal-%{version}-1-linux-x86_64.tar.gz

%build
export CRYSTAL="$(pwd)/crystal-%{version}-1/bin/crystal"
make

%install
install -pDm644 .build/crystal %{buildroot}%{_bindir}/%{appname}

install -pDm644 man/crystal.1 %{buildroot}%{_datadir}/man/man1/crystal.1.gz
mkdir -p %{buildroot}%{_datadir}/doc/crystal/
cp -r samples/ %{buildroot}%{_datadir}/doc/crystal
install -pDm644 etc/completion.bash %{buildroot}%{_datadir}/bash-completion/completions/*
install -pDm644 etc/completion.zsh %{buildroot}%{_datadir}/zsh/site-functions/*

%check

%files
%{_bindir}/%{appname}
%{_datadir}/man/man1/crystal.1.gz
%{_datadir}/doc/crystal/*
%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/*

%changelog
