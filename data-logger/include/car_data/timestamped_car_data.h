#pragma once
#include "car_data/car_data.h"
#include <boost/timer/timer.hpp>
namespace deepf1
{
	struct timestamped_udp_data {
		UDPPacket* data;
		boost::timer::cpu_times timestamp;
	}; 
	typedef struct timestamped_udp_data timestamped_udp_data_t;
}