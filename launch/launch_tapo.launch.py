from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    ld = LaunchDescription()

    # Kitchen Camera C200_9D046F
    ip_address_kit = DeclareLaunchArgument(
        "kit_ip_address",
        default_value="192.168.0.237",
        description="IP address for the kitchen camera"
    )
    username_kit = DeclareLaunchArgument(
        "kit_username",
        default_value="Kitchen",
        description="Username for the kitchen camera"
    )
    pub_topic_name_kit = DeclareLaunchArgument(
        "kit_pub_topic_name",
        default_value="/camera_kitchen/color/image_raw",
        description="Publish topic name for the kitchen camera"
    )

    ld.add_action(ip_address_kit)
    ld.add_action(username_kit)
    ld.add_action(pub_topic_name_kit)

    tapo_node_kitchen = Node(
        package="tapo_cam_ros_wrapper",
        executable="tapo_node",
        name="kitchen_cam",
        parameters=[
            {"ip_address": LaunchConfiguration("kit_ip_address")},
            {"username": LaunchConfiguration("kit_username")},
            {"pub_topic_name": LaunchConfiguration("kit_pub_topic_name")}
        ]
    )
    #
    ld.add_action(tapo_node_kitchen)
    #E4C
    # Living Room Camera C200_9D00E4
    ip_address_liv = DeclareLaunchArgument(
        "liv_ip_address",
        default_value="192.168.0.196",
        description="IP address for the living room camera"
    )
    username_liv = DeclareLaunchArgument(
        "liv_username",
        default_value="Living_room",
        description="Username for the living room camera"
    )
    pub_topic_name_liv = DeclareLaunchArgument(
        "liv_pub_topic_name",
        default_value="/camera_living_room/color/image_raw",
        description="Publish topic name for the living room camera"
    )

    ld.add_action(ip_address_liv)
    ld.add_action(username_liv)
    ld.add_action(pub_topic_name_liv)

    tapo_node_living_room = Node(
        package="tapo_cam_ros_wrapper",
        executable="tapo_node",
        name="living_room_cam",
        parameters=[
            {"ip_address": LaunchConfiguration("liv_ip_address")},
            {"username": LaunchConfiguration("liv_username")},
            {"pub_topic_name": LaunchConfiguration("liv_pub_topic_name")}
        ]
    )

    ld.add_action(tapo_node_living_room)

    # Dining Room Camera C200_9CF817   0E4
    ip_address_din = DeclareLaunchArgument(
        "din_ip_address",
        default_value="192.168.0.157",
        description="IP address for the dining room camera"
    )
    username_din = DeclareLaunchArgument(
        "din_username",
        default_value="Dining",
        description="Username for the dining room camera"
    )
    pub_topic_name_din = DeclareLaunchArgument(
        "din_pub_topic_name",
        default_value="/camera_dining_room/color/image_raw",
        description="Publish topic name for the dining room camera"
    )

    ld.add_action(ip_address_din)
    ld.add_action(username_din)
    ld.add_action(pub_topic_name_din)

    tapo_node_dining_room = Node(
        package="tapo_cam_ros_wrapper",
        executable="tapo_node",
        name="dining_room_cam",
        parameters=[
            {"ip_address": LaunchConfiguration("din_ip_address")},
            {"username": LaunchConfiguration("din_username")},
            {"pub_topic_name": LaunchConfiguration("din_pub_topic_name")}
        ]
    )

    ld.add_action(tapo_node_dining_room)

    # Bedroom Camera C200_9CFE4C   F817
    ip_address_bed = DeclareLaunchArgument(
        "bed_ip_address",
        default_value="192.168.0.149",
        description="IP address for the bedroom camera"
    )
    username_bed = DeclareLaunchArgument(
        "bed_username",
        default_value="Bedroom",
        description="Username for the bedroom camera"
    )
    pub_topic_name_bed = DeclareLaunchArgument(
        "bed_pub_topic_name",
        default_value="/camera_bedroom_room/color/image_raw",
        description="Publish topic name for the bedroom camera"
    )

    ld.add_action(ip_address_bed)
    ld.add_action(username_bed)
    ld.add_action(pub_topic_name_bed)

    tapo_node_bed_room = Node(
        package="tapo_cam_ros_wrapper",
        executable="tapo_node",
        name="bed_room_cam",
        parameters=[
            {"ip_address": LaunchConfiguration("bed_ip_address")},
            {"username": LaunchConfiguration("bed_username")},
            {"pub_topic_name": LaunchConfiguration("bed_pub_topic_name")}
        ]
    )

    ld.add_action(tapo_node_bed_room)

    return ld
