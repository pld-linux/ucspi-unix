Name: ucspi-unix
Summary: UNIX-domain socket client-server command-line tools
Version: 0.34
Release: 1
Copyright: GPL
Group:          Networking/Daemons
Group(de):      Netzwerkwesen/Server
Group(pl):      Sieciowe/Serwery
Source: http://em.ca/~bruceg/ucspi-unix/%{version}/ucspi-unix-%{version}.tar.gz
BuildRoot: %{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL: http://em.ca/~bruceg/ucspi-unix/
Packager: Bruce Guenter <bruceg@em.ca>

%description
unixclient and unixserver are command-line tools for building UNIX
domain client-server applications.  unixclient connects to a UNIX domain
socket and runs a program of your choice.  unixserver creates a UNIX
domain socket, waits for incoming connections and, for each connection,
runs a program of your choice.

unixclient and unixserver conform to UCSPI, the UNIX Client-Server
Program Interface, using UNIX domain sockets.  UCSPI tools are available
for several different networks.

%prep
%setup

%build
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_FLAGS -s"

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install_prefix=$RPM_BUILD_ROOT install
gzip -9nf COPYING ChangeLog NEWS PROTOCOL README TODO

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc COPYING.gz ChangeLog.gz NEWS.gz PROTOCOL.gz README.gz TODO.gz
/usr/bin/*
