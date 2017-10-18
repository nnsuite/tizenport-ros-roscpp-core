Name:           ros-kinetic-cpp-common
Version:        0.6.5
Release:        0
Summary:        ROS roscpp core package
Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/roscpp_core
Source0:        %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  pkgconfig(console_bridge)
Requires:       libconsole-bridge0
Requires:       pkgconfig(console_bridge)

%description
cpp_common contains C++ code for doing things that are not necessarily ROS
related, but are useful for multiple packages. This includes things like the
ROS_DEPRECATED and ROS_FORCE_INLINE macros, as well as code for getting
backtraces. This package is a component of roscpp.

%package    -n  ros-kinetic-roscpp-traits
Summary:        ROS cpp traits package
Group:          Development/Libraries
BuildRequires:  gcc-c++
BuildRequires:  ros-kinetic-catkin

%description -n ros-kinetic-roscpp-traits
This package is a traits component of roscpp.

%package    -n  ros-kinetic-rostime
Summary:        ROS time package
Group:          Development/Libraries
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  pkgconfig(console_bridge)
Requires:       libconsole-bridge0
Requires:       ros-kinetic-cpp-common

%description -n ros-kinetic-rostime
This package is a time component of roscpp.

%package    -n  ros-kinetic-roscpp-serialization
Summary:        ROS cpp serialization package
Group:          Development/Libraries
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  pkgconfig(console_bridge)
Requires:       ros-kinetic-cpp-common
Requires:       ros-kinetic-roscpp-traits
Requires:       ros-kinetic-rostime
Requires:       libconsole-bridge0

%description -n ros-kinetic-roscpp-serialization
This package is a serialization component of roscpp.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%{__ros_setup}

pushd cpp_common
%{__ros_build}
popd

pushd roscpp_traits
%{__ros_build}
popd

pushd rostime
%{__ros_build}
popd

pushd roscpp_serialization
%{__ros_build}
popd

%install
%{__ros_setup}

pushd cpp_common
%{__ros_install}
popd

pushd roscpp_traits
%{__ros_install}
popd

pushd rostime
%{__ros_install}
popd

pushd roscpp_serialization
%{__ros_install}
popd

%files -f cpp_common/build/install_manifest.txt
%manifest %{name}.manifest
%defattr(-,root,root)

%files -n ros-kinetic-roscpp-traits -f roscpp_traits/build/install_manifest.txt
%manifest %{name}.manifest
%defattr(-,root,root)

%files -n ros-kinetic-rostime -f rostime/build/install_manifest.txt
%manifest %{name}.manifest
%defattr(-,root,root)

%files -n ros-kinetic-roscpp-serialization -f roscpp_serialization/build/install_manifest.txt
%manifest %{name}.manifest
%defattr(-,root,root)

