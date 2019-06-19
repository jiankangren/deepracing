/*
 * f1_datagrab_handler.h
 *
 *  Created on: Dec 5, 2018
 *      Author: ttw2xk
 */

#ifndef INCLUDE_UDP_LOGGING_F1_2018_DATAGRAB_HANDLER_H_
#define INCLUDE_UDP_LOGGING_F1_2018_DATAGRAB_HANDLER_H_
#include "f1_datalogger/car_data/timestamped_car_data.h"
#include <string>
namespace deepf1
{

class IF12018DataGrabHandler
{
public:
  IF12018DataGrabHandler() = default;
  virtual ~IF12018DataGrabHandler() = default;
  virtual void handleData(const deepf1::twenty_eighteen::TimestampedPacketCarSetupData& data) = 0;
  virtual void handleData(const deepf1::twenty_eighteen::TimestampedPacketCarStatusData& data) = 0;
  virtual void handleData(const deepf1::twenty_eighteen::TimestampedPacketCarTelemetryData& data) = 0;
  virtual void handleData(const deepf1::twenty_eighteen::TimestampedPacketEventData& data) = 0;
  virtual void handleData(const deepf1::twenty_eighteen::TimestampedPacketLapData& data) = 0;
  virtual void handleData(const deepf1::twenty_eighteen::TimestampedPacketMotionData& data) = 0;
  virtual void handleData(const deepf1::twenty_eighteen::TimestampedPacketParticipantsData& data) = 0;
  virtual void handleData(const deepf1::twenty_eighteen::TimestampedPacketSessionData& data) = 0;
  virtual bool isReady() = 0;
  virtual void init(const std::string& host, unsigned int port, const deepf1::TimePoint& begin) = 0;

};

} /* namespace deepf1 */

#endif /* INCLUDE_UDP_LOGGING_F1_DATAGRAB_HANDLER_H_ */
