Summary:	UNIX-domain socket client-server command-line tools
Summary(pl):	Klient i serwer command-line do gniazdek lokalnych
Name:		ucspi-unix
Version:	0.36
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://untroubled.org/ucspi-unix/%{name}-%{version}.tar.gz
# Source0-md5:	759407949912ccb860808ae2205e8a1a
URL:		http://untroubled.org/ucspi-unix/
BuildRequires:	bglibs
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

%description -l pl
unixclient i unixserver to narzêdzia obs³ugiwane z linii poleceñ do
tworzenia aplikacji klient-serwer u¿ywaj±cych gniazdek lokalnych (UNIX
domain). unixclient ³±czy siê z gniazdkiem lokalnym i uruchamia podany
program. unixserver tworzy gniazdko lokalne, czeka na przychodz±ce
po³±czenia, i dla ka¿dego po³±czenia uruchamia podany program.

unixclient i unixserver s± zgodne z UCSPI - UNIX Client-Server Program
Interface. Narzêdzia UCSPI s± dostêpne dla kilku ró¿nych sieci.

%prep
%setup -q

%build
echo '%{__cc} %{rpmcflags} -Wall -I/usr/lib/bglibs/include' > conf-cc
echo '%{__cc} %{rpmldflags} -L/usr/lib/bglibs/lib' > conf-ld
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
