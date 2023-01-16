
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname julia

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A high-level, high-performance dynamic language for technical computing
License:        MIT
URL:            https://github.com/JuliaLang/julia
Source:         https://github.com/JuliaLang/julia/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ gcc-gfortran pkg-config
BuildRequires:  python3-devel perl openblas-devel pcre2-devel libgit2-devel openlibm-devel dSFMT-devel

%if 0%{?__isa_bits} == 64
BuildRequires:  suitesparse64_-devel
%else
BuildRequires:  suitesparse-devel
%endif

BuildRequires:  pcre2-devel gmp-devel libgit2-devel curl libssh2-devel mbedtls-devel utf8proc-devel libunwind-devel libatomic

%description
Julia is a high-level, high-performance dynamic language for technical computing.

%prep
%autosetup -n %{appname}-master -p1



%build
make release

%install
make DESTDIR=%{buildroot} install

%check

%file
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%changelog
