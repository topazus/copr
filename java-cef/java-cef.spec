
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname java-cef
%bcond_without check

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Java Chromium Embedded Framework (JCEF)
License:        BSD
URL:            https://bitbucket.org/chromiumembedded/java-cef
Source:         https://github.com/chromiumembedded/java-cef/archive/master/java-cef-master.tar.gz

BuildRequires: gcc-c++ cmake pkg-config meson ninja-build git wget

Requires: java-11-openjdk


%description
The Java Chromium Embedded Framework (JCEF) is a simple framework for embedding Chromium-based browsers in other applications using the Java programming language.

%prep
%autosetup -n %{appname}-master -p1
mkdir -p $HOME/java-env
wget -O- https://cache-redirector.jetbrains.com/intellij-jbr/jbr_jcef-11_0_11-linux-x64-b1504.8.tar.gz | tar xvzf - -C $HOME/java-env

%build
mkdir build && cd build
export JAVA_HOME=$HOME/java-env/jbr
cmake .. -GNinja -DCMAKE_INSTALL_PREFIX=%{buildroot}%{_prefix}
ninja
cd ../tools
./compile.sh linux64
./make_distrib.sh linux64

%install
install -d %{buildroot}/opt/java-jcef
mv binary_distrib/linux64 %{buildroot}/opt/java-jcef

%if %{with check}
%check
cd tools
./run.sh
%endif

%files
%license LICENSE*
%doc README.md

%changelog
