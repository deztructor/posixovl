Summary: Overlay filesystem to get POSIX features on non-POSIX filesystems
Name: posixovl
Version: 0.0.0
Release: 1
License: GPL2
Group: System Environment/Libraries
URL: http://sourceforge.net/projects/posixovl/
Source0: %{name}-%{version}.tar.bz2
Requires: fuse >= 2.6.5
BuildRequires: pkgconfig(fuse) >= 2.6.5
BuildRequires: libattr-devel

%description
A FUSE filesystem that provides POSIX functionality - UNIX-style
permissions, ownership, special files - for filesystems that do not
have such, e.g. vfat. It is a modern equivalent of the UMSDOS fs.

%prep
%setup -q -n %{name}-%{version}/posixovl

%build
./autogen.sh
%configure
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%{_sbindir}/mount.posixovl
%{_mandir}/man1/posixovl.1.gz

