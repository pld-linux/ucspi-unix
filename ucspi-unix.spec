Summary:	UNIX-domain socket client-server command-line tools
Summary(pl):	Klient i serwer command-line do gniazdek lokalnych
Name:		ucspi-unix
Version:	0.34
Release:	2
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	http://untroubled.org/ucspi-unix/%{name}-%{version}.tar.gz
URL:		http://untroubled.org/ucspi-unix/
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
%{__make} CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install_prefix=$RPM_BUILD_ROOT install

gzip -9nf ChangeLog NEWS PROTOCOL README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.gz NEWS.gz PROTOCOL.gz README.gz TODO.gz
%attr(755,root,root) %{_bindir}/*
