Summary:	C library intended for use on embedded systems
Summary(pl):	Biblioteka C przeznaczona dla systemów wbudowanych
Name:		newlib
Version:	1.14.0
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	ftp://sources.redhat.com/pub/newlib/%{name}-%{version}.tar.gz
# Source0-md5:	3fa663f131b355d3adb24ead4df678f2
URL:		http://sources.redhat.com/newlib/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Newlib is a C library intended for use on embedded systems. It is a
conglomeration of several library parts, all under free software
licenses that make them easily usable on embedded products.

%description -l pl
Newlib to biblioteka C przeznaczona dla systemów wbudowanych. Jest
po³±czeniem kilku czê¶ci biblioteki, wszystkich na wolnych licencjach
pozwalaj±cych na ³atwe u¿ycie w produktach wbudowanych.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure

cd etc
%{__aclocal}
%{__autoconf}
%configure
cd ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog MAINTAINERS README README-maintainer-mode
%{_infodir}/configure.info*
%{_infodir}/standards.info*
