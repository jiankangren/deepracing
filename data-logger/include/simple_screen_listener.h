#pragma once

//#include "car_data/timestamped_image_data.h"
#include <memory>
#include "screen_video_capture.h"
#include <vector>
namespace deepf1
{
	
	class simple_screen_listener
	{
	public:
		simple_screen_listener(std::shared_ptr<const boost::timer::cpu_timer> timer,
			cv::Rect2d capture_area, 
			std::string application,
			unsigned int length = 10);
		~simple_screen_listener();
		void init_images(int num_rows, int num_columns);
		void listen();
		std::vector<timestamped_image_data_t> get_data();
		void stop() {
			running = false;
		}
	private:
		bool running;
		unsigned int length;
		std::shared_ptr<const boost::timer::cpu_timer> timer;
		std::vector<timestamped_image_data_t> dataz;
		std::shared_ptr<screen_video_capture> svc;
		cv::Rect2d capture_area;
	};

}