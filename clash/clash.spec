%global debug_package %{nil}

Name:           clash
Version:        1.12.0
Release:        1%{?dist}
Summary:        A rule-based tunnel in Go
License:        GPL
URL:            https://github.com/Dreamacro/clash
Source0:        %{url}/archive/%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/topazus/fedora-copr/main/clash/clash.service
Source2:        https://github.com/Dreamacro/maxmind-geoip/releases/download/20221212/Country.mmdb

BuildRequires:  pkg-config wget

%description
A rule-based tunnel in Go.

%prep
%autosetup -n %{name}-%{version}

# download golang
wget https://go.dev/dl/go1.19.4.linux-amd64.tar.gz -O $HOME
tar xvf $HOME/go*.tar.gz -C $HOME/go

%build
export PATH=$PATH:$HOME/go/bin
go build

%install
install -pDm755 clash %{buildroot}%{_bindir}/%{name}
install -pDm644 %{SOURCE1} %{buildroot}/etc/systemd/system/clash.service

%check

%files
%{_bindir}/%{name}
/etc/systemd/system/clash.service


%changelog
