#
# TODO:
# - gabriel-passphrase.patch:
#   ssh_userauth_autopubkey from libssh takes two arguments. The second one is
#   public key passphrase. This patch asumes that passphrase is empty so it
#   won't work with encrypted public keys. It should call pinentry or something.
#   I have no idea.
Summary:	Secure remote D-Bus
Summary(pl.UTF-8):	Bezpieczny zdalny D-Bus
Name:		gabriel
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/gabriel/%{name}-%{version}.tar.gz
# Source0-md5:	136d971aaf4917c31bfdc25c3f713091
# Very ugly hack. See TODO file.
Patch0:		%{name}-passphrase.patch
URL:		http://gabriel.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	libssh-devel
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Secure remote D-Bus.

%description -l pl.UTF-8
Bezpieczny zdalny D-Bus.

%prep
%setup -q

%patch0 -p0

%build
# Is it correct?
%{__aclocal}
%{__autoconf}
%{__automake}

CPPFLAGS=-I/usr/include/glib-2.0
%configure
%{__make}
%{__make} -C client

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install client/gabriel $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README server/gabriel-server-start server/gabriel-server-stop server/gabriel-dbus.conf
%attr(755,root,root) %{_bindir}/gabriel
