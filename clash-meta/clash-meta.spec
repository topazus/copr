%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname clash-meta

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Another Clash Kernel
License:        MIT
URL:            https://github.com/MetaCubeX/Clash.Meta
#Source:
Source1:        https://raw.githubusercontent.com/topazus/copr/main/clash-meta/clash-meta.service
Source2:        https://github.com/Dreamacro/maxmind-geoip/releases/download/20221212/Country.mmdb

BuildRequires:  gcc pkg-config git wget

%description
Another Clash Kernel

%prep
git clone --depth=1 %{url} .

wget https://go.dev/dl/$(curl https://go.dev/VERSION?m=text).linux-amd64.tar.gz
tar xf go*.tar.gz

%build
export PATH="$(pwd)/go/bin:$PATH"
go build

%install
install -pDm755 clash %{buildroot}%{_bindir}/clash-meta
install -pDm644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/clash-meta.service
mkdir -p %{buildroot}/etc/clash-meta
install -pDm644 %{SOURCE2} %{buildroot}/etc/clash-meta/Country.mmdb

%check

%files
%{_bindir}/clash-meta
/usr/lib/systemd/system/clash-meta.service
/etc/clash-meta/Country.mmdb

%changelog
