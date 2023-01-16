%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname v2ray-core

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A platform for building proxies to bypass network restrictions.
License:        MIT
URL:            https://github.com/v2fly/v2ray-core
#Source:

BuildRequires:  gcc pkg-config git wget
BuildRequires:  systemd-rpm-macros

%description
A platform for building proxies to bypass network restrictions.

%prep
git clone --depth=1 %{url} .

wget https://go.dev/dl/$(curl https://go.dev/VERSION?m=text).linux-amd64.tar.gz
tar xf go*.tar.gz

%build
export PATH="$(pwd)/go/bin:$PATH"
go build -o v2ray ./main

%install
install -pDm755 v2ray %{buildroot}%{_bindir}/v2ray
install -pDm644 release/config/systemd/system/v2ray.service %{buildroot}/usr/lib/systemd/system/v2ray.service
install -pDm644 release/config/systemd/system/v2ray@.service %{buildroot}/usr/lib/systemd/system/v2ray@.service
install -pDm644 release/config/*.json -t %{buildroot}/etc/v2ray/

%check

%files
%{_bindir}/v2ray
/usr/lib/systemd/system/v2ray.service
/usr/lib/systemd/system/v2ray@.service
/etc/v2ray/

%changelog
