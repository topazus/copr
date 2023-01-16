%global debug_package %{nil}

Name:           gdu
Version:        5.12.1
Release:        1%{?dist}
Summary:        Disk usage analyzer with console interface written in Go
License:        MIT
URL:            https://github.com/dundee/gdu
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ make git wget

%if 0%{?rhel} < 9 || 0%{?fedora} <= 33
%else
BuildRequires:  golang >= 1.16
%endif

%description
Gdu is intended primarily for SSD disks where it can fully utilize parallel processing. However HDDs work as well, but the performance gain is not so huge.

%prep
%autosetup -p1

%if 0%{?rhel} < 9 || 0%{?fedora} <= 33
mkdir -p $HOME/go-env
wget -O- https://golang.org/dl/go1.16.5.linux-amd64.tar.gz | tar xvzf - -C $HOME/go-env
%endif

%build
%if 0%{?rhel} < 9 || 0%{?fedora} <= 33
GO111MODULE=on CGO_ENABLED=0 $HOME/go-env/go/bin/go build \
    -trimpath \
    -buildmode=pie \
    -mod=readonly \
    -modcacherw \
    -ldflags \
    "-s -w \
    -X 'github.com/dundee/gdu/v5/build.Version=%{version}' \
    -X 'github.com/dundee/gdu/v5/build.User=topazus' \
    -X 'github.com/dundee/gdu/v5/build.Time=$(LC_ALL=en_US.UTF-8 date)'" \
    -o %{name} \
    github.com/dundee/gdu/v5/cmd/gdu
%else
GO111MODULE=on CGO_ENABLED=0 go build \
    -trimpath \
    -buildmode=pie \
    -mod=readonly \
    -modcacherw \
    -o %{name} \
    "-s -w \
    -X 'github.com/dundee/gdu/v5/build.Version=$(git describe)' \
    -X 'github.com/dundee/gdu/v5/build.User=$(id -u -n)' \
    -X 'github.com/dundee/gdu/v5/build.Time=$(LC_ALL=en_US.UTF-8 date)'" \
    github.com/dundee/gdu/v5/cmd/gdu
%endif

%install
install -pDm755 %{name} %{buildroot}%{_bindir}/%{name}
install -pDm644 gdu.1 %{buildroot}%{_mandir}/man1/%{name}.1

%check
%if 0%{?rhel} < 9 || 0%{?fedora} <= 33
$HOME/go-env/go/bin/go test -v ./...
%else
make test
%endif

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
