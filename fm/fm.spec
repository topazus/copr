%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname fm
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A terminal based file manager
License:        MIT
URL:            https://github.com/knipferrc/fm
Source:         https://github.com/knipferrc/fm/archive/main/%{appname}-main.tar.gz

BuildRequires: gcc-c++ make pkg-config git wget

%description
A terminal based file manager

%prep
%autosetup -n %{appname}-main -p1

mkdir -p $HOME/go-env
wget -O- https://golang.org/dl/go1.16.5.linux-amd64.tar.gz | tar xvzf - -C $HOME/go-env
export PATH=$HOME/go-env/go/bin:$PATH

%build
$HOME/go-env/go/bin/go build -v

%install
install -pDm755 fm %{buildroot}%{_bindir}/fm

install -pDm644 assets/logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/fm.svg

%if %{with check}
%check

%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/icons/hicolor/scalable/apps/fm.svg

%changelog
