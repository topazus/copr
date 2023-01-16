%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname htop

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        an interactive process viewer
License:        GPLv2+
URL:            https://github.com/htop-dev/htop
#Source:

BuildRequires:  gcc make pkg-config automake autoconf
BuildRequires:  ncurses-devel desktop-file-utils git libcap-devel libnl3-devel

%if 0%{?fedora}
BuildRequires:  lm_sensors-devel
%elif 0%{?suse_version}
BuildRequires:  libsensors4-devel
%endif

%description
htop is a cross-platform interactive process viewer.

%prep
git clone --depth=1 https://github.com/htop-dev/htop.git .

%build
./autogen.sh

%configure \
  --enable-affinity \
  --enable-capabilities \
  --enable-delayacct \
  --enable-openvz \
  --enable-sensors \
  --enable-unicode \
  --enable-vserver

%make_build

%install
%make_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%{_bindir}/%{appname}
%{_datadir}/pixmaps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/applications/*.desktop
%{_datadir}/man/man1/htop.1*

%changelog
