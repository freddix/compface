Summary:	Image from/to X-Face conversion utilities
Name:		compface
Version:	1.5.2
Release:	1
Epoch:		1
License:	MIT
Group:		Applications/Graphics
Source0:	http://ftp.xemacs.org/pub/xemacs/aux/%{name}-%{version}.tar.gz
# Source0-md5:	62f4f79c0861ad292ba3cf77b4c48319
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compface provides utilities to convert from/to X-Face format, a 48x48
bitmap format used to carry thumbnails of email authors in a mail
header.

%package devel
Summary:	Image from/to X-Face conversion libraries
Group:		Development/Libraries

%description devel
Compface provides a library to convert from/to X-Face format, a 48x48
bitmap format used to carry thumbnails of email authors in a mail
header.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{man1,man3},%{_libdir},%{_includedir}}

install compface $RPM_BUILD_ROOT%{_bindir}
install uncompface $RPM_BUILD_ROOT%{_bindir}
install compface.1 $RPM_BUILD_ROOT%{_mandir}/man1
install compface.3 $RPM_BUILD_ROOT%{_mandir}/man3
install libcompface.a $RPM_BUILD_ROOT%{_libdir}
install compface.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/compface.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libcompface.a
%{_includedir}/compface.h
%{_mandir}/man3/compface.3*

