Summary:	Utilities for the XFce Desktop Environment
Summary(pl):	Narzêdzia dla ¶rodowiska XFce
Name:		xfce-utils
Version:	4.0.4
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	34fe286ed9aa48e7d76e1c07904b0ecf
Source1:	xfce4-xsession.desktop
URL:		http://www.xfce.org/
BuildRequires:	automake
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce-mcs-manager-devel >= %{version}
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
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--enable-gdm
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/mcs-plugins/*.{la,a}
rm -rf $RPM_BUILD_ROOT%{_datadir}/xfce4/doc/fr
rm -f $RPM_BUILD_ROOT%{_datadir}/xfce4/COPYING.{html,vi}

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
%{_datadir}/xfce4/AUTHORS
%lang(az) %{_datadir}/xfce4/AUTHORS.az
%lang(ca) %{_datadir}/xfce4/AUTHORS.ca
%lang(de) %{_datadir}/xfce4/AUTHORS.de
%lang(es) %{_datadir}/xfce4/AUTHORS.es
%lang(fr) %{_datadir}/xfce4/AUTHORS.fr
%lang(vi) %{_datadir}/xfce4/AUTHORS.vi
%{_datadir}/xfce4/AUTHORS.html
%lang(az) %{_datadir}/xfce4/AUTHORS.html.az
%lang(ca) %{_datadir}/xfce4/AUTHORS.html.ca
%lang(de) %{_datadir}/xfce4/AUTHORS.html.de
%lang(es) %{_datadir}/xfce4/AUTHORS.html.es
%lang(fr) %{_datadir}/xfce4/AUTHORS.html.fr
%{_datadir}/xfce4/BSD
%{_datadir}/xfce4/COPYING
%{_datadir}/xfce4/GPL
%{_datadir}/xfce4/INFO
%{_datadir}/xfce4/INFO.html
%lang(ca) %{_datadir}/xfce4/INFO.ca
%lang(fr) %{_datadir}/xfce4/INFO.fr
%lang(vi) %{_datadir}/xfce4/INFO.vi
%lang(ca) %{_datadir}/xfce4/INFO.html.ca
%lang(de) %{_datadir}/xfce4/INFO.html.de
%lang(fr) %{_datadir}/xfce4/INFO.html.fr
%{_datadir}/xfce4/LGPL
%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/xfce.css
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*

%{_datadir}/apps/switchdesk/Xclients.xfce4
%{_datadir}/xsessions/xfce4.desktop
