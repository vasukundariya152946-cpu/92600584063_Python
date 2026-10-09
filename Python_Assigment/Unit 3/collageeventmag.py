from registration import registration_part,part
from scheduling import schedule_event
from repoting import generate_report
registration_part("vasu")
registration_part("vishal")
registration_part("deep")
event =schedule_event(
    "College Annual Function",
    "15 October2026",
 "10:00 AM")
generate_report(event,part)
