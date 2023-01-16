%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname fastfetch

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Like neofetch, but much faster because written in C.
License:        ASL
URL:            https://github.com/LinusDierheimer/fastfetch
#Source:

BuildRequires:  gcc-c++ cmake git
BuildRequires:  glibc-devel

Requires:       glibc

%description
Like neofetch, but much faster because written in C.

%prep
git clone --depth=1 %{url} .

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%check

%files
/usr/bin/fastfetch
/usr/bin/flashfetch
/etc/fastfetch/config.conf
/usr/share/bash-completion/completions/fastfetch
/usr/share/fastfetch/
/usr/share/licenses/fastfetch/LICENSE

%changelog
