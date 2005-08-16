# TODO:
# - rc scripts
# - check files section
# - check BR and R section
#
# Conditional build:
%bcond_with     efence		# link with Electric Fence to find memory problems
%bcond_with	mysql		# include MySQL user accounts support
%bcond_with	pgsql		# include PostgreSQL user accounts suppor
%bcond_with	sqlite3		# include SQLite3 user accounts support
Summary:	PvPGN - free software that emulates a Blizzard Battle.net server
Summary(pl):	PvPGN - wolne opgramowanie kt�re emuluje serwer Blizzarda Battle.net
Name:		pvpgn
Version:	1.7.7
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://download.berlios.de/pvpgn/%{name}-%{version}.tar.bz2
# Source0-md5:	465e18b04ca903eca7e2973a2d557e46
URL:		http://pvpgn.berlios.de/
BuildRequires:	zlib-devel
%{?with_mysql:BuildRequires:      mysql-devel}
%{?with_pgsql:BuildRequires:      postgresql-devel}
%{?with_sqlite3:BuildRequires:      sqlite3-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PvPGN (Player vs Player Gaming Network) is free software that emulates
a Blizzard Battle.net server. It currently supports all Battle.net
games, such as StarCraft, Diablo II, and Warcraft III, and gives you
the power to run your own server, manage your own users, run your own
tournaments, etc.

%description -l pl
PvPGN (Player vs Player Gaming Network) to wolne oprogramowanie kt�re
emuluje serwer Blizzarda Battle.net. Obecnie wspiera wszystkie gry
Battle.net, takie jak StarCraft, Diablo II oraz Warcraft III, daje ci
mo�liwo�� uruchomienia w�asnego serwera, zarz�dania u�ytkownikami,
grania w�asnych rozgrywek itp.

%prep
%setup -q

%build
cd src
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd src
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CREDITS IGNOREME NEWS README README.ALPHA README.DEV TODO UPDATE version-history.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*