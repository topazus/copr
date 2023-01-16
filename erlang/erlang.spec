%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname erlang

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        a programming language and runtime system for building massively scalable soft real-time systems
License:        ASL 2.0
URL:            https://www.erlang.org
Source:         https://github.com/erlang/otp/archive/master/otp-master.tar.gz

BuildRequires:  gcc gcc-c++ flex make autoconf pkg-config
BuildRequires:  openssl-devel systemd-devel
BuildRequires:  m4 ncurses-devel zlib-devel lksctp-tools-devel

Requires:       lksctp-tools

%description
Erlang is a programming language and runtime system for building massively scalable soft real-time systems with requirements on high availability.

OTP is a set of Erlang libraries, which consists of the Erlang runtime system, a number of ready-to-use components mainly written in Erlang, and a set of design principles for Erlang programs.

%prep
%autosetup -n otp-master -p1

%build
./otp_build autoconf
####  ./configure --prefix=%{buildroot}%{_prefix}
%configure --enable-shared-zlib --enable-sctp --enable-systemd --disable-silent-rules \
    --enable-smp-support \
    --without-common_test \
	--without-debugger \
	--without-dialyzer \
	--without-et \
	--without-megaco \
	--without-observer \
	--without-reltool \
	--without-wx
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%check


%files
%license LICENSE*
%doc README.md

%changelog
