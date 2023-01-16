%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname vifm

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A file manager with curses interface
License:        GPL 2.0
URL:            https://github.com/vifm/vifm
#Source:

BuildRequires:  gcc-c++ make pkg-config automake ncurses-devel
BuildRequires:  libX11-devel gtk+-devel
BuildRequires:  desktop-file-utils libappstream-glib git

%description
Vifm is a file manager with curses interface, which provides Vi[m]-like environment for managing objects within file systems, extended with some useful ideas from mutt.

%prep
git clone --depth=1 https://github.com/vifm/vifm .

%build
./scripts/fix-timestamps
#./configure --prefix=%{_prefix}
%configure
%make_build

%install
%make_install

#rm %{buildroot}%{_prefix}/etc/vifm/colors/Default-256.vifm

%check


%files
%{_bindir}/vifm
%{_bindir}/vifm-convert-dircolors
%{_bindir}/vifm-pause
%{_bindir}/vifm-screen-split
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/vifm.png
/etc/vifm/colors/Default-256.vifm

%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/_*
%{_datadir}/man/man1/*.1.gz

%dir %{_datadir}/doc/vifm
%{_datadir}/doc/vifm/*
%dir %{_datadir}/vifm
%{_datadir}/vifm/*

%changelog
