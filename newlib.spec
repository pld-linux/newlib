Summary:	C library intended for use on embedded systems
Summary(pl.UTF-8):	Biblioteka C przeznaczona dla systemów wbudowanych
Name:		newlib
Version:	2.0.0
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	ftp://sources.redhat.com/pub/newlib/%{name}-%{version}.tar.gz
# Source0-md5:	e3e936235e56d6a28afb2a7f98b1a635
URL:		http://sources.redhat.com/newlib/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# use single prefix as multilib is supported inside
%define		newlibdir	/usr/lib/newlib
%define		_exec_prefix	%{newlibdir}
%define		tooldir		%{_exec_prefix}/%{_target_alias}

%description
Newlib is a C library intended for use on embedded systems. It is a
conglomeration of several library parts, all under free software
licenses that make them easily usable on embedded products.

%description -l pl.UTF-8
Newlib to biblioteka C przeznaczona dla systemów wbudowanych. Jest
połączeniem kilku części biblioteki, wszystkich na wolnych licencjach
pozwalających na łatwe użycie w produktach wbudowanych.

%prep
%setup -q

%build
%configure \
	--with-newlib

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# common gnu-standards files
%{__rm} $RPM_BUILD_ROOT%{_infodir}/{configure,standards}.info*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING.LIBGLOSS COPYING.NEWLIB ChangeLog MAINTAINERS newlib/{NEWS,README}
%dir %{newlibdir}
%dir %{tooldir}
%{tooldir}/include
%dir %{tooldir}/lib
%{tooldir}/lib/libc.a
%{tooldir}/lib/libg.a
%{tooldir}/lib/libm.a
