Summary: 	Utilities for the XFce Desktop Environment
Name: 		xfce-utils
Version: 	3.90.0
Release: 	1
License:	GPL
URL: 		http://www.xfce.org/
Source0: 	http://belnet.dl.sourceforge.net/sourceforge/xfce/%{name}-%{version}.tar.gz
# Source0-md5:	e82ae701185d0b7365bbe943fe6af855
Group: 		X11/Applications
Requires:	libxfcegui4 >= 0.0.22
Requires:	libxfce4mcs >= 0.0.3
Requires:	xfce-mcs-manager
BuildRequires: 	libxfcegui4-devel >= 0.0.22
BuildRequires:	libxfce4mcs-devel >= 0.0.3
BuildRequires:	xfce-mcs-manager-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-utils contains utilities for the XFce Desktop Environment

%prep
%setup -q

%build
rm -f missing
glib-gettextize --copy --force
intltoolize --copy --force
%configure --enable-gdm
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog NEWS INSTALL COPYING AUTHORS
%{_bindir}/*
%{_libdir}/xfce4/mcs-plugins/*
%{_datadir}/*
%config(noreplace) %{_sysconfdir}/*
