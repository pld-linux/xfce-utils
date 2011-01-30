Summary:	Utilities for the Xfce Desktop Environment
Summary(pl.UTF-8):	Narzędzia dla środowiska Xfce
Name:		xfce-utils
Version:	4.6.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	5d23407700d7e8c9751e17a5bc955109
Source1:	xfce4-xsession.desktop
Patch0:		%{name}-gxmessage.patch
URL:		http://www.xfce.org/projects/xfce-utils/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.62
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.6.0
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	gxmessage
Requires:	libxfcegui4 >= %{version}
Requires:	which
Requires:	xfce4-dirs >= 4.6
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

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/X11/{dm,gdm,wmsession.d}
rm -f $RPM_BUILD_ROOT%{_datadir}/xsessions/xfce.desktop

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

# switchdesk provides Xclients.Xfce4
rm -rf $RPM_BUILD_ROOT%{_datadir}/apps

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
%dir %{_libdir}/xfce4/xfconf-migration
%attr(755,root,root) %{_libdir}/xfce4/xfconf-migration/xfconf-migration-4.6.pl
%{_sysconfdir}/xdg/autostart/xfconf-migration-4.6.desktop
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/Xft.xrdb
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/xinitrc
%{_datadir}/dbus-1/services/*.service
%{_datadir}/xfce4/AUTHORS
%{_datadir}/xfce4/INFO
%lang(ca) %{_datadir}/xfce4/INFO.ca
%lang(de) %{_datadir}/xfce4/INFO.de
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

%{_datadir}/xfce4/doc/xfce*.css
%{_datadir}/xfce4/doc/xfce-mouse.png
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*.jpg
%{_datadir}/xfce4/doc/C/images/*.png
%lang(fr) %{_datadir}/xfce4/doc/fr/*.html
%lang(it) %{_datadir}/xfce4/doc/it/*.html

%{_iconsdir}/hicolor/*/*/*

%{_datadir}/xsessions/xfce4.desktop
