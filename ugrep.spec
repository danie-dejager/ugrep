Name:           ugrep
Version:        7.4.1
Release:        1%{?dist}
Summary:        Faster, user-friendly, and compatible grep replacement
License:        BSD-3-Clause
URL:            https://github.com/Genivia/ugrep
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pcre2-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  xz-devel
BuildRequires:  lz4-devel
BuildRequires:  libzstd-devel

%global debug_package %{nil}

%description
Ultra fast grep with interactive TUI, fuzzy search, boolean queries, hexdumps
and more: search file systems, source code, text, binary files, archives
(cpio/tar/pax/zip), compressed files (gz/Z/bz2/lzma/xz/lz4/zstd), documents
etc.  A faster, user-friendly and compatible grep replacement.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%check
%make_build test

%files
%license LICENSE.txt
%{_bindir}/ug
%{_bindir}/ug+
%{_bindir}/ugrep
%{_bindir}/ugrep+
%{_mandir}/man1/ug.1*
%{_mandir}/man1/ugrep.1*
%{_datadir}/ugrep
%{_bindir}/ugrep-indexer
%{_datadir}/bash-completion/completions/ugrep-indexer
%{_datadir}/fish/vendor_completions.d/ugrep-indexer.fish
%{_mandir}/man1/ugrep-indexer.1.gz
%{_datadir}/zsh/site-functions/_ugrep-indexer
/usr/share/bash-completion/completions/ug
/usr/share/bash-completion/completions/ug+
/usr/share/bash-completion/completions/ugrep
/usr/share/bash-completion/completions/ugrep+
/usr/share/fish/vendor_completions.d/ug+.fish
/usr/share/fish/vendor_completions.d/ug.fish
/usr/share/fish/vendor_completions.d/ugrep+.fish
/usr/share/fish/vendor_completions.d/ugrep.fish
/usr/share/zsh/site-functions/_ug
/usr/share/zsh/site-functions/_ug+
/usr/share/zsh/site-functions/_ugrep
/usr/share/zsh/site-functions/_ugrep+

%changelog
* Fri Apr 25 2025 - Danie de Jager - 7.4.1-1
* Wed Jul 17 2024 - Danie de Jager - 6.2.0-1
* Fri Feb 16 2024 - Danie de Jager - 5.0.0-1
* Sun Jan 28 2024 - Danie de Jager - 4.5.2-1
- Initial Build on AL2023
