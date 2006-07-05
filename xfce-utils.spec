# Conditional build:
%bcond_with	gtkhtml		# build with gtkhtml support
#
Summary:	Utilities for the Xfce Desktop Environment
Summary(pl):	Narzędzia dla środowiska Xfce
Name:		xfce-utils
Version:	4.2.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.us.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	8028266d03c5bae7c7ccbddd6656ea97
Source1:	xfce4-xsession.desktop
Patch0:		%{name}-locale-names.patch
Patch1:		%{name}-gxmessage.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbh-devel >= 1.0
BuildRequires:	gettext-devel
%{?with_gtkhtml:BuildRequires:	gtkhtml-devel}
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	xfce4-dev-tools
Requires:	gxmessage
Requires:	libxfce4mcs >= %{version}
Requires:	libxfcegui4 >= %{version}
Requires:	xfce-mcs-manager >= %{version}
Conflicts:	xfce4-session < 0.1.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-utils contains utilities for the Xfce Desktop Environment.

%description -l pl
xfce-utils zawiera narzędzia dla środowiska Xfce.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{pt_PT,pt}.po

%build
%{__libtoolize}
%{__aclocal} -I %{_datadir}/xfce4/dev-tools/m4macros
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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/xinitrc

%{_desktopdir}/xfce-taskbar-settings.desktop

%{_datadir}/xfce4/AUTHORS
%lang(az) %{_datadir}/xfce4/AUTHORS.az
%lang(ca) %{_datadir}/xfce4/AUTHORS.ca
%lang(de) %{_datadir}/xfce4/AUTHORS.de
%lang(es) %{_datadir}/xfce4/AUTHORS.es
%lang(eu) %{_datadir}/xfce4/AUTHORS.eu
%lang(fi) %{_datadir}/xfce4/AUTHORS.fi
%lang(fr) %{_datadir}/xfce4/AUTHORS.fr
%lang(he) %{_datadir}/xfce4/AUTHORS.he
%lang(it) %{_datadir}/xfce4/AUTHORS.it
%lang(ja) %{_datadir}/xfce4/AUTHORS.ja
%lang(lt) %{_datadir}/xfce4/AUTHORS.lt
%lang(ro) %{_datadir}/xfce4/AUTHORS.ro
%lang(ru) %{_datadir}/xfce4/AUTHORS.ru
%lang(sk) %{_datadir}/xfce4/AUTHORS.sk
%lang(uk) %{_datadir}/xfce4/AUTHORS.uk
%lang(vi) %{_datadir}/xfce4/AUTHORS.vi
%lang(zh_TW) %{_datadir}/xfce4/AUTHORS.zh_TW
%{_datadir}/xfce4/AUTHORS.html
%lang(az) %{_datadir}/xfce4/AUTHORS.html.az
%lang(ca) %{_datadir}/xfce4/AUTHORS.html.ca
%lang(de) %{_datadir}/xfce4/AUTHORS.html.de
%lang(es) %{_datadir}/xfce4/AUTHORS.html.es
%lang(eu) %{_datadir}/xfce4/AUTHORS.html.eu
%lang(fi) %{_datadir}/xfce4/AUTHORS.html.fi
%lang(fr) %{_datadir}/xfce4/AUTHORS.html.fr
%lang(it) %{_datadir}/xfce4/AUTHORS.html.it
%lang(ja) %{_datadir}/xfce4/AUTHORS.html.ja
%lang(lt) %{_datadir}/xfce4/AUTHORS.html.lt
%lang(ro) %{_datadir}/xfce4/AUTHORS.html.ro
%lang(ru) %{_datadir}/xfce4/AUTHORS.html.ru
%lang(sk) %{_datadir}/xfce4/AUTHORS.html.sk
%lang(vi) %{_datadir}/xfce4/AUTHORS.html.vi
%lang(zh_TW) %{_datadir}/xfce4/AUTHORS.html.zh_TW
%{_datadir}/xfce4/INFO
%{_datadir}/xfce4/INFO.html
%lang(ca) %{_datadir}/xfce4/INFO.ca
%lang(es) %{_datadir}/xfce4/INFO.es
%lang(fi) %{_datadir}/xfce4/INFO.fi
%lang(fr) %{_datadir}/xfce4/INFO.fr
%lang(it) %{_datadir}/xfce4/INFO.it
%lang(ja) %{_datadir}/xfce4/INFO.ja
%lang(lt) %{_datadir}/xfce4/INFO.lt
%lang(ro) %{_datadir}/xfce4/INFO.ro
%lang(ru) %{_datadir}/xfce4/INFO.ru
%lang(uk) %{_datadir}/xfce4/INFO.uk
%lang(vi) %{_datadir}/xfce4/INFO.vi
%lang(ca) %{_datadir}/xfce4/INFO.html.ca
%lang(de) %{_datadir}/xfce4/INFO.html.de
%lang(es) %{_datadir}/xfce4/INFO.html.es
%lang(fi) %{_datadir}/xfce4/INFO.html.fi
%lang(fr) %{_datadir}/xfce4/INFO.html.fr
%lang(it) %{_datadir}/xfce4/INFO.html.it
%lang(ja) %{_datadir}/xfce4/INFO.html.ja
%lang(lt) %{_datadir}/xfce4/INFO.html.lt
%lang(ro) %{_datadir}/xfce4/INFO.html.ro
%lang(ru) %{_datadir}/xfce4/INFO.html.ru
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
%{_datadir}/xfce4/doc/xfce-rtl.css
%{_datadir}/xfce4/doc/xfce-mouse.png
%{_datadir}/xfce4/doc/C/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*
%lang(he) %{_datadir}/xfce4/doc/he/*
%{_iconsdir}/hicolor/*/*/*

%{_datadir}/apps/switchdesk/Xclients.xfce4
%{_datadir}/xsessions/xfce4.desktop
