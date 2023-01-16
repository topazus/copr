%global debug_package %{nil}
%define build_timestamp %(date +%Y.%m.%d)
%define is_git 1

Name:           jetbrains-jre-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Runtime environment based on OpenJDK for running IntelliJ Platform-based products on Windows, macOS, and Linux
License:        GPL
URL:            https://github.com/JetBrains/JetBrainsRuntime
Source:         https://cache-redirector.jetbrains.com/intellij-jbr/jbr_jcef-17.0.5-linux-x64-b759.1.tar.gz

Conflicts:      jetbrains-jre

BuildRequires:  pkg-config

# build jetbrains jre from source
%if %is_git
%if 0%{?fedora}
BuildRequires:  alsa-lib-devel
%elif 0%{?suse_version}
BuildRequires:  alsa-devel
%endif

BuildRequires:  autoconf make gcc gcc-c++ git wget zip unzip
BuildRequires:  fontconfig-devel cups-devel libXtst-devel
BuildRequires:  libXt-devel libXrender-devel libXrandr-devel libXi-devel
%endif

%description
JetBrains Runtime is a fork of OpenJDK available for Windows, Mac OS X, and Linux. It includes a number enhancements in font rendering, HiDPI support, ligatures, performance improvements, and bugfixes.

%prep
%if %is_git
git clone --branch=main --depth=1 https://github.com/JetBrains/JetBrainsRuntime.git .
wget https://download.oracle.com/java/19/latest/jdk-19_linux-x64_bin.tar.gz
tar xf jdk-19_linux-x64_bin.tar.gz
mv jdk-19*/ jdk-19
%else
%autosetup -n jbr_jcef-*
%endif

%build
%if %is_git
export JAVA_HOME=$(pwd)/jdk-19
export PATH=$JAVA_HOME/bin:$PATH
sh ./configure
make images JOBS=$(nproc --all)
%endif

%install
mkdir -p %{buildroot}%{_libdir}/jvm/jetbrains-jre
%if %is_git
cp -r build/linux-x86_64-server-release/images/jdk/* %{buildroot}%{_libdir}/jvm/jetbrains-jre
%else
cd jbr_jcef-*/
# solve rpath error
#export QA_RPATHS=$[ 0x0001 | 0x002 ]
cp -r * %{buildroot}%{_libdir}/jvm/jetbrains-jre
%endif

%check


%files
%dir %{_libdir}/jvm/jetbrains-jre
%{_libdir}/jvm/jetbrains-jre/*

%changelog
