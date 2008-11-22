#
# Conditional build:
%bcond_with	gtkhtml		# build with gtkhtml support
#
Summary:	Utilities for the Xfce Desktop Environment
Summary(pl.UTF-8):	Narzędzia dla środowiska Xfce
Name:		xfce-utils
Version:	4.4.3
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	6d6ae1f048e1dc1348ad050498af5a18
Source1:	xfce4-xsession.desktop
Patch0:		%{name}-locale-names.patch
Patch1:		%{name}-gxmessage.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.62
BuildRequires:	gettext-devel
%{?with_gtkhtml:BuildRequires:	gtkhtml-devel}
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	xfce4-dev-tools >= 4.4.0.1
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	gxmessage
Requires:	libxfce4mcs >= %{version}
Requires:	libxfcegui4 >= %{version}
Requires:	which
Requires:	xfce-mcs-manager >= %{version}
Requires:	xlockmore
Requires:	xorg-app-xrdb
Conflicts:	xfce4-session < 0.1.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-utils contains utilities for the Xfce Desktop Environment.

%description -l pl.UTF-8
xfce-utils zawiera narzędzia dla środowiska Xfce.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{nb_NO,nb}.po
mv -f po/{pt_PT,pt}.po

%build
%{__libtoolize}
%{__aclocal}
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
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/X11/{dm,gdm,wmsession.d}
rm -f $RPM_BUILD_ROOT%{_datadir}/xsessions/xfce.desktop

# switchdesk provides Xclients.Xfce4
rm -rf $RPM_BUILD_ROOT%{_datadir}/apps

install -d $RPM_BUILD_ROOT%{_datadir}/xsessions
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/xfce4.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/Xft.xrdb
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/xinitrc
%{_datadir}/dbus-1/services/*.service
%{_datadir}/xfce4/AUTHORS
%{_datadir}/xfce4/INFO
%lang(ca) %{_datadir}/xfce4/INFO.ca
%lang(es) %{_datadir}/xfce4/INFO.es
%lang(fi) %{_datadir}/xfce4/INFO.fi
%lang(fr) %{_datadir}/xfce4/INFO.fr
%lang(it) %{_datadir}/xfce4/INFO.it
%lang(ja) %{_datadir}/xfce4/INFO.ja
%lang(ru) %{_datadir}/xfce4/INFO.ru
%lang(uk) %{_datadir}/xfce4/INFO.uk
%lang(vi) %{_datadir}/xfce4/INFO.vi
%{_datadir}/xfce4/COPYING
%{_datadir}/xfce4/BSD
%{_datadir}/xfce4/LGPL
%{_datadir}/xfce4/GPL

%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/xfce*.css
%{_datadir}/xfce4/doc/xfce-mouse.png
%{_datadir}/xfce4/doc/C/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*
%lang(it) %{_datadir}/xfce4/doc/it/*
%{_iconsdir}/hicolor/*/*/*

%{_datadir}/xsessions/xfce4.desktop
