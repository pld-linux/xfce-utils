
%define		_snap 20040806

Summary:	Utilities for the XFce Desktop Environment
Summary(pl):	Narzêdzia dla ¶rodowiska XFce
Name:		xfce-utils
Version:	4.2.0
Release:	0.%{_snap}.1
License:	GPL
Group:		X11/Applications
Source0:	http://ep09.pld-linux.org/~havner/xfce4/%{name}-%{_snap}.tar.bz2
# Source0-md5:	09e1c1cdd04af06c64bef36965394c00
Source1:	xfce4-xsession.desktop
Patch0:		%{name}-gxmessage.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkhtml-devel
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce-mcs-manager-devel >= %{version}
Requires:	gxmessage
Requires:	libxfce4mcs >= %{version}
Requires:	libxfcegui4 >= %{version}
Requires:	xfce-mcs-manager >= %{version}
Conflicts:	xfce4-session < 0.1.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-utils contains utilities for the XFce Desktop Environment.

%description -l pl
xfce-utils zawiera narzêdzia dla ¶rodowiska XFce.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-gdm \
	--enable-gtkhtml
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/mcs-plugins/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_datadir}/xfce4/COPYING*
rm -f $RPM_BUILD_ROOT%{_datadir}/xfce4/{BSD,LGPL,GPL}*
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/X11/{dm,gdm,wmsession.d}
rm -f $RPM_BUILD_ROOT%{_datadir}/xsessions/xfce.desktop

install -d $RPM_BUILD_ROOT%{_datadir}/xsessions
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/xfce4.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xinitrc

%{_desktopdir}/xfce-taskbar-settings.desktop

%{_datadir}/xfce4/AUTHORS
%lang(az) %{_datadir}/xfce4/AUTHORS.az
%lang(ca) %{_datadir}/xfce4/AUTHORS.ca
%lang(de) %{_datadir}/xfce4/AUTHORS.de
%lang(es) %{_datadir}/xfce4/AUTHORS.es
%lang(fr) %{_datadir}/xfce4/AUTHORS.fr
%lang(it) %{_datadir}/xfce4/AUTHORS.it
%lang(lt) %{_datadir}/xfce4/AUTHORS.lt
%lang(vi) %{_datadir}/xfce4/AUTHORS.vi
%{_datadir}/xfce4/AUTHORS.html
%lang(az) %{_datadir}/xfce4/AUTHORS.html.az
%lang(ca) %{_datadir}/xfce4/AUTHORS.html.ca
%lang(de) %{_datadir}/xfce4/AUTHORS.html.de
%lang(es) %{_datadir}/xfce4/AUTHORS.html.es
%lang(fr) %{_datadir}/xfce4/AUTHORS.html.fr
%lang(it) %{_datadir}/xfce4/AUTHORS.html.it
%{_datadir}/xfce4/INFO
%{_datadir}/xfce4/INFO.html
%lang(ca) %{_datadir}/xfce4/INFO.ca
%lang(es) %{_datadir}/xfce4/INFO.es
%lang(fr) %{_datadir}/xfce4/INFO.fr
%lang(it) %{_datadir}/xfce4/INFO.it
%lang(vi) %{_datadir}/xfce4/INFO.vi
%lang(ca) %{_datadir}/xfce4/INFO.html.ca
%lang(de) %{_datadir}/xfce4/INFO.html.de
%lang(es) %{_datadir}/xfce4/INFO.html.es
%lang(fr) %{_datadir}/xfce4/INFO.html.fr
%lang(it) %{_datadir}/xfce4/INFO.html.it
%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/xfce.css
%{_datadir}/xfce4/doc/C
%lang(fr) %{_datadir}/xfce4/doc/fr
%lang(it) %{_datadir}/xfce4/doc/it
%{_iconsdir}/hicolor/*/*/*

%{_datadir}/apps/switchdesk/Xclients.xfce4
%{_datadir}/xsessions/xfce4.desktop
