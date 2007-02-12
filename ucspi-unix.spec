Summary:	UNIX-domain socket client-server command-line tools
Summary(pl.UTF-8):	Klient i serwer command-line do gniazdek lokalnych
Name:		ucspi-unix
Version:	0.36
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://untroubled.org/ucspi-unix/%{name}-%{version}.tar.gz
# Source0-md5:	759407949912ccb860808ae2205e8a1a
URL:		http://untroubled.org/ucspi-unix/
BuildRequires:	bglibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unixclient and unixserver are command-line tools for building UNIX
domain client-server applications. unixclient connects to a UNIX
domain socket and runs a program of your choice. unixserver creates a
UNIX domain socket, waits for incoming connections and, for each
connection, runs a program of your choice.

unixclient and unixserver conform to UCSPI, the UNIX Client-Server
Program Interface, using UNIX domain sockets. UCSPI tools are
available for several different networks.

%description -l pl.UTF-8
unixclient i unixserver to narzędzia obsługiwane z linii poleceń do
tworzenia aplikacji klient-serwer używających gniazdek lokalnych (UNIX
domain). unixclient łączy się z gniazdkiem lokalnym i uruchamia podany
program. unixserver tworzy gniazdko lokalne, czeka na przychodzące
połączenia, i dla każdego połączenia uruchamia podany program.

unixclient i unixserver są zgodne z UCSPI - UNIX Client-Server Program
Interface. Narzędzia UCSPI są dostępne dla kilku różnych sieci.

%prep
%setup -q

%build
echo '%{__cc} %{rpmcflags} -Wall -I%{_includedir}/bglibs' > conf-cc
echo '%{__cc} %{rpmldflags} -L%{_libdir}/bglibs' > conf-ld
echo '%{_bindir}' > conf-bin
echo '%{_mandir}' > conf-man

%{__make} programs

echo "$RPM_BUILD_ROOT%{_bindir}" > conf-bin
echo "$RPM_BUILD_ROOT%{_mandir}" > conf-man

%{__make} installer

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}}

./installer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS PROTOCOL README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
