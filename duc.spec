Name:          duc
Version:       1.4.5
Release:       1%{?dist}
Summary:       Library and suite of tools for inspecting disk usage
License:       LGPL-3.0-only
URL:           https://github.com/zevv/duc
Source0:       %{url}/archive/tags/%{version}-rc1.tar.gz

BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: pango-devel
BuildRequires: glfw-devel
BuildRequires: ncurses-devel
BuildRequires: cairo-devel
BuildRequires: sqlite-devel
BuildRequires: tokyocabinet-devel

%description
Duc is a collection of tools for indexing, inspecting and visualizing disk usage.
Duc maintains a database of accumulated sizes of directories of the file system, and allows you to query this database with some tools, or create fancy graphs showing you where your bytes are.

%prep
%autosetup -n duc-tags-%{version}-rc1 -p1

%build
# generate the configure script when it is not available
autoreconf --install
%configure --enable-opengl \
    --disable-x11 \
    --enable-cairo \
    --with-db-backend=sqlite3
make %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/duc
%{_mandir}/man1/duc.1*

%changelog
