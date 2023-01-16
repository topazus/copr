%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname python

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        an interpreted high-level general-purpose programming language.
License:        MIT
URL:            https://www.python.org/
Source:         https://github.com/python/cpython/archive/main/cpython-main.tar.gz

BuildRequires:  gcc gcc-c++ make
BuildRequires:  bzip2 bzip2-devel ncurses-devel gdbm-devel gdbm-devel openssl-devel libuuid-devel readline-devel zlib-devel libffi-devel sqlite-devel

%description
Python is an interpreted high-level general-purpose programming language.

%prep
%autosetup -n cpython-main -p1

%build
./configure --prefix=%{buildroot}/opt/python \
    --enable-optimizations \
    --without-ensurepip \
    --with-lto
make

%install
mkdir -p %{buildroot}/opt/python
make install

%check


%files
%license LICENSE*
%doc README*
/opt/python/*

%changelog
