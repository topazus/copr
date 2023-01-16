%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname folly

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        An open-source C++ library developed and used at Facebook
License:        ASL
URL:            https://github.com/facebook/folly
#Source:

BuildRequires:  gcc-c++ cmake
BuildRequires:  double-conversion-devel libevent-devel libsodium-devel
BuildRequires:  openssl-devel fmt-devel
BuildRequires:  libtool libzstd-devel libdwarf-devel libunwind-devel
BuildRequires:  snappy-devel xz-devel glog-devel zlib-devel
%if 0%{?fedora}
BuildRequires:  boost-devel lz4-static ninja-build lz4-devel
%elif 0%{?suse_version}
BuildRequires:  ninja
BuildRequires:  libboost_context-devel
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  gflags-devel gflags-devel-static liblz4-devel
%endif

%description
An open-source C++ library developed and used at Facebook.

%prep
git clone --depth=1 %{url} .

%build
%if 0%{?fedora}
%cmake -G Ninja -DCMAKE_BUILD_TYPE=Release
%cmake_build
%elif 0%{?suse_version}
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build
%endif

%install
%if 0%{?fedora}
%cmake_install
%elif 0%{?suse_version}
%cmake_install
%endif

%check

%files
/usr/include/folly/
/usr/lib64/libfolly*
/usr/lib64/pkgconfig/

/usr/lib/cmake/folly/folly-config.cmake
/usr/lib/cmake/folly/folly-targets-release.cmake
/usr/lib/cmake/folly/folly-targets.cmake

%changelog
