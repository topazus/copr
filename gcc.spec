%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname gcc

Name:           %{appname}
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        GNU Compiler Collection (GCC)
License:        GPL
URL:            http://gcc.gnu.org/
Source:					http://ftp.tsukuba.wide.ad.jp/software/gcc/snapshots/LATEST-13/gcc-13-20230108.tar.xz

BuildRequires:  gcc gcc-c++ make
BuildRequires:  zlib-devel bison flex gmp-devel mpfr-devel libmpc-devel python3-devel
BuildRequires:  dblatex dejagnu docbook5-style-xsl binutils-devel elfutils-devel
BuildRequires:  gcc-gnat gdb glibc-static hostname libgnat
BuildRequires:  libgphobos-static python3-sphinx sharutils

%description
Powerful yet simple to use screenshot software.

%prep
%autosetup -n gcc-13-20230108

%build
./configure \
	--enable-languages=c,c++ \
	--prefix=/opt/gcc \
	--enable-checking=release --with-system-zlib \
	--without-isl --disable-multilib
make %{?_smp_mflags}

%install
make install

%check

%files
/opt/gcc/

%changelog
