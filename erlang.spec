%global debug_package %{nil}

Name:           erlang
Version:        25.2
Release:        1%{?dist}
Summary:        Erlang/OTP
License:        MIT
URL:            https://www.erlang.org/
Source:         https://github.com/erlang/otp/releases/download/OTP-%{version}/otp_src_%{version}.tar.gz

BuildRequires:  gcc make perl
BuildRequires:  ncurses-devel openssl-devel

%description
Erlang is a programming language and runtime system for building massively scalable soft real-time systems with requirements on high availability.

OTP is a set of Erlang libraries, which consists of the Erlang runtime system, a number of ready-to-use components mainly written in Erlang, and a set of design principles for Erlang programs. Learn more about Erlang and OTP.

%prep
%autosetup -n otp_src_%{version}

%build
%configure
%make_build

%install
export QA_RPATHS=$[ 0x0001|0x0002 ]
%make_install

make install-docs DESTDIR=%{buildroot}

%check

%files
/usr/bin/ct_run
/usr/bin/dialyzer
/usr/bin/epmd
/usr/bin/erl
/usr/bin/erlc
/usr/bin/escript
/usr/bin/run_erl
/usr/bin/to_erl
/usr/bin/typer

%dir /usr/lib64/erlang/
/usr/lib64/erlang/*

%changelog
