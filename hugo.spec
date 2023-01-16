%if 0%{?fedora} == 35
%global _missing_build_ids_terminate_build 0
%endif

%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname hugo

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        World’s fastest framework for building websites

License:        MIT
URL:            https://github.com/gohugoio/hugo
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires: golang git gcc-c++ curl wget
BuildRequires: libsass-devel

%description
The world’s fastest framework for building websites.

%prep
git clone --depth=1 %{url} .
mkdir -p $HOME/go-env
wget "https://dl.google.com/go/$(curl https://go.dev/VERSION?m=text).linux-amd64.tar.gz"
tar xf go*.tar.gz -C $HOME/go-env

%build
$HOME/go-env/go/bin/go build -v -tags extended

./hugo gen man
./hugo gen autocomplete --completionfile hugo-completion

%install
install -pDm755 %{appname} %{buildroot}%{_bindir}/%{appname}

install -pDm644 man/* -t %{buildroot}%{_mandir}/man1
install -pDm644 hugo-completion %{buildroot}%{_datadir}/bash-completion/completions/hugo

%check

%files
%license LICENSE
%doc README.md
%{_bindir}/%{appname}
%{_mandir}/man1/*
%{_datadir}/bash-completion/completions/hugo

%changelog
