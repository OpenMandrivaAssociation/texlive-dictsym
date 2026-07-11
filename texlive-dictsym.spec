%global tl_name dictsym
%global tl_revision 78251

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	DictSym font and macro package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/dictsym
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dictsym.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dictsym.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(psnfss)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This directory contains the DictSym Type1 font designed by Georg
Verweyen and all files required to use it with LaTeX on the Unix or PC
platforms. The font provides a number of symbols commonly used in
dictionaries. The accompanying macro package makes the symbols
accessible as LaTeX commands.

