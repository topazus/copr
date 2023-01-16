%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname kotlin-native

Name:           kotlin-native-git
Version:        1.7.10
Release:        1%{?dist}
Summary:        A modern programming language that makes developers happier
License:        APACHE-2.0
URL:            https://github.com/JetBrains/kotlin
Source:         https://github.com/JetBrains/kotlin/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc make git

%description
A modern programming language that makes developers happier.

%prep
%autosetup -n kotlin-%{version}
echo "kotlin.native.enabled=true
kotlin.build.isObsoleteJdkOverrideEnabled=true" >> local.properties

cd $HOME && wget https://download.oracle.com/java/17/latest/jdk-17_linux-x64_bin.tar.gz
tar xf jdk-*.tar.gz
mv $HOME/jdk-*/ $HOME/jdk

%build
export JAVA_HOME=$HOME/jdk
export PATH=$PATH:$JAVA_HOME/bin
./gradlew :kotlin-native:dist :kotlin-native:distPlatformLibs

%install
install -pDm755 kotlin-native/dist/bin/kotlinc-native %{buildroot}/kotlinc-native
install -pDm755 kotlin-native/dist/bin/konanc %{buildroot}/konanc
install -pDm755 kotlin-native/dist/bin/cinterop %{buildroot}/cinterop
install -pDm755 kotlin-native/dist/bin/run_konan %{buildroot}/run_konan

%check

%files

%changelog
