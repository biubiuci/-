// Generated by gencpp from file as_arm_description/CheckCollisionValidRequest.msg
// DO NOT EDIT!


#ifndef AS_ARM_DESCRIPTION_MESSAGE_CHECKCOLLISIONVALIDREQUEST_H
#define AS_ARM_DESCRIPTION_MESSAGE_CHECKCOLLISIONVALIDREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace as_arm_description
{
template <class ContainerAllocator>
struct CheckCollisionValidRequest_
{
  typedef CheckCollisionValidRequest_<ContainerAllocator> Type;

  CheckCollisionValidRequest_()
    : values()  {
    }
  CheckCollisionValidRequest_(const ContainerAllocator& _alloc)
    : values(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> _values_type;
  _values_type values;





  typedef boost::shared_ptr< ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator> const> ConstPtr;

}; // struct CheckCollisionValidRequest_

typedef ::as_arm_description::CheckCollisionValidRequest_<std::allocator<void> > CheckCollisionValidRequest;

typedef boost::shared_ptr< ::as_arm_description::CheckCollisionValidRequest > CheckCollisionValidRequestPtr;
typedef boost::shared_ptr< ::as_arm_description::CheckCollisionValidRequest const> CheckCollisionValidRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator1> & lhs, const ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator2> & rhs)
{
  return lhs.values == rhs.values;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator1> & lhs, const ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace as_arm_description

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b9163d7c678dcd669317e43e46b63d96";
  }

  static const char* value(const ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb9163d7c678dcd66ULL;
  static const uint64_t static_value2 = 0x9317e43e46b63d96ULL;
};

template<class ContainerAllocator>
struct DataType< ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "as_arm_description/CheckCollisionValidRequest";
  }

  static const char* value(const ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# joint names\n"
"# string[] names\n"
"# joint values\n"
"float64[] values\n"
;
  }

  static const char* value(const ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.values);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CheckCollisionValidRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::as_arm_description::CheckCollisionValidRequest_<ContainerAllocator>& v)
  {
    s << indent << "values[]" << std::endl;
    for (size_t i = 0; i < v.values.size(); ++i)
    {
      s << indent << "  values[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.values[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // AS_ARM_DESCRIPTION_MESSAGE_CHECKCOLLISIONVALIDREQUEST_H