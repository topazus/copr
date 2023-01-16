
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname ruby
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        an interpreted object-oriented programming language often used for web development
License:        GPL
URL:            https://github.com/ruby/ruby
Source:         https://cache.ruby-lang.org/pub/ruby/snapshot/snapshot-master.tar.xz

BuildRequires: gcc-c++ make pkg-config
BuildRequires: automake autoconf bison ruby


%description
Ruby is an interpreted object-oriented programming language often used for web development. It also offers many scripting features to process plain text and serialized files, or manage system tasks. It is simple, straightforward, and extensible.

%prep
%autosetup -n snapshot-master -p1

%build
./autogen.sh

./configure \
    --prefix=%{buildroot}%{_prefix}/local \
    --enable-shared \
    --disable-rpath \
    --with-dbm-type=gdbm_compat
make

%install
make install


%if %{with check}
%check
make check
%endif

%files
%license LICENSE*
%doc README.md

%changelog
