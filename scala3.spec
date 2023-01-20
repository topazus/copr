%global debug_package %{nil}
%define sys_jdk 0
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname scala3

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A next-generation compiler for Scala
License:        ASL 2.0
URL:            https://github.com/lampepfl/dotty
#Source:

BuildRequires:  pkg-config sbt wget git

Requires:       java-17-openjdk

%description
A next-generation compiler for Scala

%prep
git clone --depth=1 %{url} .
%if !%sys_jdk
wget https://download.oracle.com/java/17/latest/jdk-17_linux-x64_bin.tar.gz
tar xvf jdk-17_linux-x64_bin.tar.gz -C $HOME
mv $HOME/jdk-*/ $HOME/jdk
%endif

%build
export JAVA_HOME=$HOME/jdk
export PATH=$JAVA_HOME/bin
sbt dist/packArchive

%install
mkdir -p %{buildroot}/opt/scala3
cp -a dist/target/pack/* %{buildroot}/opt/scala3

rm %{buildroot}/opt/scala3/bin/*.bat

#mkdir -p %{buildroot}/etc/profile.d/
# add path
#echo "export PATH=$PATH:/opt/scala3/bin" > %{buildroot}/etc/profile.d/scala3.sh

%check

%files
%dir /opt/scala3
/opt/scala3/*

%ghost /usr/bin/scala3
%ghost /usr/bin/scalac3
%ghost /usr/bin/scala3doc
%post
ln -s /opt/scala3/bin/scala3 /usr/bin/scala3
ln -s /opt/scala3/bin/scalac3 /usr/bin/scalac3
ln -s /opt/scala3/bin/scala3doc /usr/bin/scala3doc

%changelog
