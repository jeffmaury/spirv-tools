%global commit 5834719fc17d4735fce0102738b87b70255cfd5f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20171023
%global gitrel .%{commit_date}.git%{shortcommit}

Name:           spirv-tools
Version:        2016.7
Release:        0.1%{?gitrel}%{?dist}
Summary:        API and commands for processing SPIR-V modules

License:        ASL 2.0
URL:            https://github.com/KhronosGroup
Source0:        %url/SPIRV-Tools/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
Patch0:         SPIRV-Tools_staticlib.patch

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  python2-devel
BuildRequires:  python-simplejson
BuildRequires:  spirv-headers-devel

%description
The package includes an assembler, binary module parser,
disassembler, and validator for SPIR-V..

%package        devel
Summary:        Development files for %{name}

%description    devel
The SPIR-V Tool library contains all of the implementation details
driving the SPIR-V assembler, binary module parser, disassembler and
validator, and is used in the standalone tools whilst also enabling
integration into other code bases directly.

%prep
%autosetup -p1 -n SPIRV-Tools-%{commit}

%build
%__mkdir_p %_target_platform
pushd %_target_platform
%cmake3 -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
        -DSPIRV-Headers_SOURCE_DIR=%{_prefix} ..
%{make_build}
popd

%install
%{make_install} -C %_target_platform

%files devel
%license LICENSE
%doc README.md CHANGES
%{_bindir}/spirv-as
%{_bindir}/spirv-cfg
%{_bindir}/spirv-dis
%{_bindir}/spirv-lesspipe.sh
%{_bindir}/spirv-link
%{_bindir}/spirv-opt
%{_bindir}/spirv-stats
%{_bindir}/spirv-val
%{_includedir}/spirv-tools/
%{_libdir}/libSPIRV-Tools-link.a
%{_libdir}/libSPIRV-Tools-opt.a
%{_libdir}/libSPIRV-Tools.a

%changelog
* Thu Jul 13 2017 Leigh Scott <leigh123linux@googlemail.com> - 2016.7-0.1.20171023.git5834719
- First build

