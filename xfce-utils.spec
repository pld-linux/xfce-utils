#
%bcond_without	gtkhtml		# build without gtkhtml support
#
Summary:	Utilities for the XFce Desktop Environment
Summary(pl):	Narzêdzia dla ¶rodowiska XFce
Name:		xfce-utils
Version:	4.1.99.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c88e6e06df41579e8c67c75ec2f2fa37
Source1:	xfce4-xsession.desktop
Patch0:		%{name}-gxmessage.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%{?with_gtkhtml:BuildRequires:	gtkhtml-devel}
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= 4.1.3
BuildRequires:	libxfcegui4-devel >= 4.1.27
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce-mcs-manager-devel >= 4.1.3
Requires:	gxmessage
Requires:	libxfce4mcs >= 4.1.3
Requires:	libxfcegui4 >= 4.1.27
Requires:	xfce-mcs-manager >= 4.1.3
Conflicts:	xfce4-session < 0.1.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-utils contains utilities for the XFce Desktop Environment.

%description -l pl
xfce-utils zawiera narzêdzia dla ¶rodowiska XFce.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	%{?with_gtkhtml:--enable-gtkhtml} \
	--enable-gdm
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/mcs-plugins/*.{la,a}
#rm -f $RPM_BUILD_ROOT%{_datadir}/xfce4/COPYING*
#rm -f $RPM_BUILD_ROOT%{_datadir}/xfce4/{BSD,LGPL,GPL}*
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
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/xinitrc

%{_desktopdir}/xfce-taskbar-settings.desktop

%{_datadir}/xfce4/AUTHORS
%lang(az) %{_datadir}/xfce4/AUTHORS.az
%lang(ca) %{_datadir}/xfce4/AUTHORS.ca
%lang(de) %{_datadir}/xfce4/AUTHORS.de
%lang(es) %{_datadir}/xfce4/AUTHORS.es
%lang(fr) %{_datadir}/xfce4/AUTHORS.fr
%lang(he) %{_datadir}/xfce4/AUTHORS.he
%lang(it) %{_datadir}/xfce4/AUTHORS.it
%lang(lt) %{_datadir}/xfce4/AUTHORS.lt
%lang(ru) %{_datadir}/xfce4/AUTHORS.ru
%lang(sk) %{_datadir}/xfce4/AUTHORS.sk
%lang(vi) %{_datadir}/xfce4/AUTHORS.vi
%{_datadir}/xfce4/AUTHORS.html
%lang(az) %{_datadir}/xfce4/AUTHORS.html.az
%lang(ca) %{_datadir}/xfce4/AUTHORS.html.ca
%lang(de) %{_datadir}/xfce4/AUTHORS.html.de
%lang(es) %{_datadir}/xfce4/AUTHORS.html.es
%lang(fr) %{_datadir}/xfce4/AUTHORS.html.fr
%lang(it) %{_datadir}/xfce4/AUTHORS.html.it
%lang(ru) %{_datadir}/xfce4/AUTHORS.html.ru
%lang(sk) %{_datadir}/xfce4/AUTHORS.html.sk
%lang(vi) %{_datadir}/xfce4/AUTHORS.html.vi
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
%{_datadir}/xfce4/COPYING
%{_datadir}/xfce4/COPYING.html
%lang(vi) %{_datadir}/xfce4/COPYING.vi
%{_datadir}/xfce4/BSD
%{_datadir}/xfce4/BSD.html
%{_datadir}/xfce4/LGPL
%{_datadir}/xfce4/LGPL.html
%{_datadir}/xfce4/GPL
%{_datadir}/xfce4/GPL.html

%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/xfce.css
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*.png
%lang(fr) %{_datadir}/xfce4/doc/fr/*.html
%lang(fr) %{_datadir}/xfce4/doc/fr/images/*.png
%lang(it) %{_datadir}/xfce4/doc/it/*.html
%lang(it) %{_datadir}/xfce4/doc/it/images/*.png
%{_iconsdir}/hicolor/*/*/*

%{_datadir}/apps/switchdesk/Xclients.xfce4
%{_datadir}/xsessions/xfce4.desktop
