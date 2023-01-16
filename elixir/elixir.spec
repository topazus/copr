%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname elixir

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A dynamic, functional language designed for building scalable and maintainable applications
License:        APACHE
URL:            https://github.com/elixir-lang/elixir
Source:         https://github.com/elixir-lang/elixir/archive/master/%{appname}-master.tar.gz

BuildRequires:  erlang pkg-config make


%description
Elixir is a dynamic, functional language designed for building scalable and maintainable applications.

%prep
%autosetup -n %{appname}-master -p1

%build
make

%install
make install PREFIX=%{buildroot}%{_prefix}

%check


%files
%license LICENSE*
%doc README.md
%{_bindir}/elixir
%{_bindir}/elixirc
%{_bindir}/iex
%{_bindir}/mix

%{_prefix}/lib/elixir/bin/elixir
%{_prefix}/lib/elixir/bin/elixirc
%{_prefix}/lib/elixir/bin/iex
%{_prefix}/lib/elixir/bin/mix
%{_prefix}/lib/elixir/lib/

%{_mandir}/man1/elixir.1.gz
%{_mandir}/man1/elixirc.1.gz
%{_mandir}/man1/iex.1.gz
%{_mandir}/man1/mix.1.gz

%changelog
