%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname groovy

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A powerful multi-faceted programming language for the JVM platform
License:        ASL 2.0
URL:            https://github.com/apache/groovy
#Source:         https://github.com/apache/groovy/archive/master/groovy-master.tar.gz

BuildRequires:  make autoconf pkg-config unzip wget
BuildRequires:  graphviz
#BuildRequires:  java-17-openjdk

%description
Apache Groovy is a powerful, optionally typed and dynamic language, with static-typing and static compilation capabilities, for the Java platform aimed at improving developer productivity thanks to a concise, familiar and easy to learn syntax.

%prep
git clone --depth=1 https://github.com/apache/groovy .

cd $HOME && wget https://download.oracle.com/java/17/latest/jdk-17_linux-x64_bin.tar.gz
tar xf jdk-*.tar.gz
mv $HOME/jdk-*/ $HOME/jdk

%build
export JAVA_HOME=$HOME/jdk
./gradlew clean dist

%install
unzip subprojects/groovy-binary/build/distributions/apache-groovy-binary-*.zip \
    -d %{buildroot}/opt
mv %{buildroot}/opt/groovy-* %{buildroot}/opt/%{name}

mkdir -p %{buildroot}/etc/profile.d/
# add path
echo 'export GROOVY_HOME=/opt/groovy
export PATH=$PATH:$GROOVY_HOME/bin
' > %{buildroot}/etc/profile.d/groovy.sh

%check


%files
/opt/groovy/*
/etc/profile.d/groovy.sh

%changelog
