%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname elvish
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Elvish = Expressive Programming Language + Versatile Interactive Shell
License:        BSD
URL:            https://github.com/elves/elvish
Source:         https://github.com/elves/elvish/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ make pkg-config golang git wget


%description
Elvish is an expressive programming language and a versatile interactive shell, combined into one seamless package. It runs on Linux, BSDs, macOS and Windows.

%prep
%autosetup -n %{appname}-master -p1

mkdir -p $HOME/go-env
wget -O- https://golang.org/dl/go1.16.5.linux-amd64.tar.gz | tar xvzf - -C $HOME/go-env

%build
$HOME/go-env/go/bin/go build ./cmd/elvish

%install
install -pDm755 elvish %{buildroot}%{_bindir}/elvish

%if %{with check}
%check
$HOME/go-env/go/bin/go test $(shell ./tools/run-race.sh) ./...
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%changelog
