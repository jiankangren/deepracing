cmake_minimum_required(VERSION 3.15)
project(f1_datalogger_ros)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rosidl_default_runtime REQUIRED)
find_package(image_transport REQUIRED)
find_package(laser_geometry REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(f1_datalogger_msgs REQUIRED)

#Provides imported targets for f1_datalogger, armadillo, Boost, Eigen3, and Opencv
find_package(f1_datalogger_provider REQUIRED)

find_package(cv_bridge REQUIRED)
if(WIN32)
  find_package(vJoy_plusplus REQUIRED)
endif()

include_directories(include)
add_library(f1_msg_utils src/utils/f1_msg_utils.cpp)
ament_target_dependencies(f1_msg_utils cv_bridge f1_datalogger sensor_msgs std_msgs f1_datalogger_msgs rclcpp rosidl_default_runtime)
target_link_libraries(f1_msg_utils
 f1_datalogger::f1_datalogger_udp_utils
 Eigen3::Eigen
 Boost::system
 Boost::regex
)

add_executable(tf_updater src/tf_updater.cpp)
ament_target_dependencies(tf_updater rclcpp f1_datalogger_msgs tf2_ros tf2)
target_link_libraries(tf_updater
 f1_msg_utils
 Eigen3::Eigen
)

add_executable(path_converter src/path_converter.cpp)
ament_target_dependencies(path_converter rclcpp geometry_msgs nav_msgs f1_datalogger_msgs)
target_link_libraries(path_converter
 Eigen3::Eigen
)

add_executable(ros_rebroadcaster src/ros_rebroadcaster.cpp)
ament_target_dependencies(ros_rebroadcaster cv_bridge f1_datalogger image_transport sensor_msgs std_msgs f1_datalogger_msgs)
target_link_libraries(ros_rebroadcaster
 f1_msg_utils
 f1_datalogger::f1_datalogger
 Eigen3::Eigen
 ${ARMADILLO_LIBRARIES}
 ${cv_bridge_LIBRARIES}
)
#target_include_directories(ros_rebroadcaster PRIVATE ${cv_bridge_INCLUDE_DIRS})


 ament_export_libraries(f1_msg_utils)
 ament_export_dependencies(ament_cmake)
 ament_export_dependencies(rcl)
 ament_export_dependencies(image_tools)
 ament_export_dependencies(laser_geometry)
 ament_export_dependencies(f1_datalogger_msgs)
 ament_export_dependencies(f1_datalogger_provider)
 #ament_export_dependencies(f1_datalogger)
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()
install(TARGETS
    ros_rebroadcaster
    f1_msg_utils
    tf_updater
    path_converter
    DESTINATION lib/${PROJECT_NAME}
)
install(
  DIRECTORY include/
  DESTINATION include
)
install(DIRECTORY
  launch/
  DESTINATION share/${PROJECT_NAME}/
)
ament_package()
