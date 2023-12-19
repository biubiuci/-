// Generated by gencpp from file blueprintlab_reachsystem_ros_messages/generic.msg
// DO NOT EDIT!


#ifndef BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES_MESSAGE_GENERIC_H
#define BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES_MESSAGE_GENERIC_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace blueprintlab_reachsystem_ros_messages
{
template <class ContainerAllocator>
struct generic_
{
  typedef generic_<ContainerAllocator> Type;

  generic_()
    : stamp()
    , device_id(0)
    , packet_id(0)
    , data()  {
    }
  generic_(const ContainerAllocator& _alloc)
    : stamp()
    , device_id(0)
    , packet_id(0)
    , data(_alloc)  {
  (void)_alloc;
    }



   typedef ros::Time _stamp_type;
  _stamp_type stamp;

   typedef uint8_t _device_id_type;
  _device_id_type device_id;

   typedef uint8_t _packet_id_type;
  _packet_id_type packet_id;

   typedef std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> _data_type;
  _data_type data;





  typedef boost::shared_ptr< ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator> const> ConstPtr;

}; // struct generic_

typedef ::blueprintlab_reachsystem_ros_messages::generic_<std::allocator<void> > generic;

typedef boost::shared_ptr< ::blueprintlab_reachsystem_ros_messages::generic > genericPtr;
typedef boost::shared_ptr< ::blueprintlab_reachsystem_ros_messages::generic const> genericConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator1> & lhs, const ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator2> & rhs)
{
  return lhs.stamp == rhs.stamp &&
    lhs.device_id == rhs.device_id &&
    lhs.packet_id == rhs.packet_id &&
    lhs.data == rhs.data;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator1> & lhs, const ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace blueprintlab_reachsystem_ros_messages

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3d9227290a2d905fa3823529454d5aa2";
  }

  static const char* value(const ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3d9227290a2d905fULL;
  static const uint64_t static_value2 = 0xa3823529454d5aa2ULL;
};

template<class ContainerAllocator>
struct DataType< ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator> >
{
  static const char* value()
  {
    return "blueprintlab_reachsystem_ros_messages/generic";
  }

  static const char* value(const ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator> >
{
  static const char* value()
  {
    return "time stamp\n"
"uint8 device_id\n"
"uint8 packet_id\n"
"float32[] data\n"
;
  }

  static const char* value(const ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.stamp);
      stream.next(m.device_id);
      stream.next(m.packet_id);
      stream.next(m.data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct generic_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::blueprintlab_reachsystem_ros_messages::generic_<ContainerAllocator>& v)
  {
    s << indent << "stamp: ";
    Printer<ros::Time>::stream(s, indent + "  ", v.stamp);
    s << indent << "device_id: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.device_id);
    s << indent << "packet_id: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.packet_id);
    s << indent << "data[]" << std::endl;
    for (size_t i = 0; i < v.data.size(); ++i)
    {
      s << indent << "  data[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.data[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // BLUEPRINTLAB_REACHSYSTEM_ROS_MESSAGES_MESSAGE_GENERIC_H