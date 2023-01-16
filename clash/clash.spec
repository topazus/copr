%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname clash

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A rule-based tunnel in Go
License:        GPL
URL:            https://github.com/Dreamacro/clash
#Source0:
Source1:        https://raw.githubusercontent.com/topazus/copr/main/clash/clash.service
Source2:        https://github.com/Dreamacro/maxmind-geoip/releases/download/20221212/Country.mmdb

BuildRequires:  pkg-config wget

%description
A rule-based tunnel in Go.

%prep
git clone --depth=1 %{url} .

wget --quiet https://go.dev/dl/$(curl https://go.dev/VERSION?m=text).linux-amd64.tar.gz
tar xf go*.tar.gz -C $HOME

%build
export PATH=$PATH:$HOME/go/bin
go build

%install
install -pDm755 clash %{buildroot}%{_bindir}/%{appname}
install -pDm644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/clash.service
mkdir -p %{buildroot}/etc/clash
install -pDm644 %{SOURCE2} %{buildroot}/etc/clash/Country.mmdb

%check

%files
%{_bindir}/%{appname}
/etc/systemd/system/clash.service


%changelog
