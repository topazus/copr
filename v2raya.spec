%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname v2raya

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A Linux web GUI client of Project V which supports V2Ray, Xray, SS, SSR, Trojan and Pingtunnel
License:        AGPL-3.0
Url:            https://github.com/v2rayA/v2rayA
#Source0:

BuildRequires:  nodejs git wget
%if 0%{?fedora}
BuildRequires:  yarnpkg
%elif 0%{?suse_version}
BuildRequires:  yarn
%endif
Requires:       v2ray-core-git

%description
A Linux web GUI client of Project V which supports V2Ray, Xray, SS, SSR, Trojan and Pingtunnel

%prep
git clone --depth=1 %{url} .

wget --quiet https://go.dev/dl/$(curl https://go.dev/VERSION?m=text).linux-amd64.tar.gz
tar xf go*.tar.gz -C $HOME

%build
# build gui
cd gui/
yarn --check-files
OUTPUT_DIR=../service/server/router/web yarn build

# build core
cd ../service/
export PATH=$HOME/go/bin:$PATH
go build -o v2raya

%install
install -pDm 755 service/v2raya %{buildroot}/usr/bin/v2raya
mkdir -p %{buildroot}/etc/v2raya/
install -pDm 644 install/universal/v2raya.desktop %{buildroot}/usr/share/applications/v2raya.desktop
install -pDm 644 install/universal/v2raya.service %{buildroot}/usr/lib/systemd/system/v2raya.service
install -pDm 644 install/universal/v2raya-lite.service %{buildroot}/usr/lib/systemd/user/v2raya-lite.service
install -pDm 644 gui/public/img/icons/android-chrome-512x512.png %{buildroot}/usr/share/icons/hicolor/512x512/apps/v2raya.png

%files
%{_sysconfdir}/v2raya/
%{_bindir}/v2raya
%{_prefix}/lib/systemd/system/v2raya.service
%{_prefix}/lib/systemd/user/v2raya-lite.service
%{_datadir}/applications/v2raya.desktop
%{_datadir}/icons/hicolor/512x512/apps/v2raya.png

%changelog
