
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname dte
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A small, configurable console text editor
License:        GPL2
URL:            https://gitlab.com/craigbarnes/dte
Source:         https://gitlab.com/craigbarnes/dte/-/archive/master/dte-master.tar.gz

BuildRequires: gcc-c++ make pkg-config desktop-file-utils

%description
A small and easy to use console text editor.

%prep
%autosetup -n %{appname}-master -p1

%build
make V=1

%install
make install-bin V=1 prefix=%{buildroot}%{_prefix}

gzip --best docs/{dte.1,dterc.5,dte-syntax.5}
install -pDm644 docs/dte.1.gz %{buildroot}%{_mandir}/man1/dte.1.gz
install -pDm644 docs/{dterc.5.gz,dte-syntax.5.gz} -t %{buildroot}%{_mandir}/man5

install -pDm644 completion.bash %{buildroot}%{_datadir}/bash-completion/completions/dte
install -pDm644 dte.desktop %{buildroot}%{_datadir}/applications/dte.desktop

%if %{with check}
%check
make check
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop

%{_datadir}/bash-completion/completions/dte
%{_mandir}/man1/dte.1.gz
%{_mandir}/man5/dte-syntax.5.gz
%{_mandir}/man5/dterc.5.gz

%changelog
