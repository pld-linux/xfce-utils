Summary: 	Utilities for the XFce Desktop Environment
Summary(pl):	Narzędzia dla środowiska XFce
Name: 		xfce-utils
Version: 	3.90.0
Release: 	1
License:	GPL
Group: 		X11/Applications
Source0: 	http://dl.sourceforge.net/xfce/%{name}-%{version}.tar.gz
# Source0-md5:	e82ae701185d0b7365bbe943fe6af855
URL: 		http://www.xfce.org/
BuildRequires:	intltool
BuildRequires:	libxfce4mcs-devel >= 0.0.3
BuildRequires: 	libxfcegui4-devel >= 0.0.22
BuildRequires:	xfce-mcs-manager-devel
Requires:	libxfce4mcs >= 0.0.3
Requires:	libxfcegui4 >= 0.0.22
Requires:	xfce-mcs-manager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-utils contains utilities for the XFce Desktop Environment.

%description -l pl
xfce-utils zawiera narzędzia dla środowiska XFce.

%prep
%setup -q

%build
rm -f missing
glib-gettextize --copy --force
intltoolize --copy --force
%configure \
	--enable-gdm

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/mcs-plugins/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/X11/gdm/Sessions/XFce4
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/X11/wmsession.d/10XFce4
%dir %{_sysconfdir}/xfce4
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xinitrc
%{_datadir}/xfce4/AUTHORS
%lang(ca) %{_datadir}/xfce4/AUTHORS.ca
%lang(de) %{_datadir}/xfce4/AUTHORS.de
%{_datadir}/xfce4/AUTHORS.html
%lang(ca) %{_datadir}/xfce4/AUTHORS.html.ca
%lang(de) %{_datadir}/xfce4/AUTHORS.html.de
%{_datadir}/xfce4/BSD
%{_datadir}/xfce4/COPYING
%{_datadir}/xfce4/GPL
%{_datadir}/xfce4/INFO
%{_datadir}/xfce4/INFO.html
%lang(ca) %{_datadir}/xfce4/INFO.html.ca
%lang(de) %{_datadir}/xfce4/INFO.html.de
%{_datadir}/xfce4/LGPL
%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/xfce.css
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*

%{_datadir}/apps/switchdesk/Xclients.xfce4
