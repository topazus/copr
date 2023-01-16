%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname nnn

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        n³ The unorthodox terminal file manager
License:        BSD-2-Clause
URL:            https://github.com/jarun/nnn
Source:         https://github.com/jarun/nnn/archive/master/%{appname}-master.tar.gz

BuildRequires:  make gcc
BuildRequires:  ncurses-devel readline-devel
BuildRequires:  desktop-file-utils

%description
nnn (n³) is a full-featured terminal file manager. It's tiny and nearly 0-config with an incredible speed.

%prep
git clone --depth=1 https://github.com/jarun/nnn .

%build
make

%install
make install PREFIX=%{buildroot}%{_prefix}

make install-desktop PREFIX=%{buildroot}%{_prefix}

install -pDm644 misc/auto-completion/bash/nnn-completion.bash %{buildroot}%{_datadir}/bash-completion/completions/nnn
install -pDm644 misc/auto-completion/zsh/_nnn %{buildroot}%{_datadir}/zsh/site-functions/_nnn
install -pDm644 misc/auto-completion/fish/nnn.fish %{buildroot}%{_datadir}/fish/vendor_completion.d/nnn.fish

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/64x64/apps/nnn.png
%{_datadir}/icons/hicolor/scalable/apps/nnn.svg

%{_datadir}/man/man1/nnn.1.gz
%{_datadir}/bash-completion/completions/nnn
%{_datadir}/zsh/site-functions/_nnn
%{_datadir}/fish/vendor_completion.d/nnn.fish

%changelog
