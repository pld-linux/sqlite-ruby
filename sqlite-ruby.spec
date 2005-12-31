%define tarname sqlite-ruby
Summary:	SQLite module for Ruby
Summary(pl):	Modu³ SQLite dla jêzyka Ruby
Name:		sqlite-ruby
Version:	2.2.1
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/1825/%{name}-%{version}.tar.bz2
# Source0-md5:	935caede77d829cc6ec3e73d8844edf2
Source1:	setup.rb
URL:		http://sqlite-ruby.rubyforge.org
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	sqlite-devel
%{?ruby_mod_ver_requires_eq}
Obsoletes:	ruby-sqlite
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SQLite module for Ruby.

%description -l pl
Modu³ SQLite dla jêzyka Ruby.

%prep
%setup -q
install %{SOURCE1} .
echo sqlite-api.c > ext/MANIFEST

%build
ruby setup.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_sitearchdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_sitearchdir}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO doc 
%attr(755,root,root) %{ruby_sitearchdir}/*
%{ruby_rubylibdir}/sqlite.rb
%{ruby_rubylibdir}/sqlite
