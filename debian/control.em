Source: @(CATKIN_PACKAGE_PREFIX)roscpp-core
Section: misc
Priority: extra
Maintainer: Troy Straszheim <straszheim@@willowgarage.com>
Build-Depends: debhelper (>= 7), cmake, gcc, make, catkin
Homepage: <insert the upstream URL, if relevant>

Package: @(CATKIN_PACKAGE_PREFIX)roscpp-core
Architecture: any
Depends: ${misc:Depends}
Description: <insert up to 60 chars description>
 <insert long description, indented with spaces>
X-ROS-Pkg-Name: roscpp_core
X-ROS-Pkg-Depends: catkin, genmsg, gencpp
X-ROS-System-Depends: