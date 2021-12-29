### Edit below to set desired ranges for pH and electrical conductivity ###

# Desired range for pH
range_ph_high = 6.7
range_ph_low = 6.3
# pH range that will immediately cause a pH correction
range_ph_high_danger = 6.8
range_ph_low_danger = 6.2
### Edit below to set the IDs for Conditions and Actions ###
condition_id_measurement_ph_id = "{b330e643}"  # Condition: measurement, last, pH Input

action_id_pump_1_acid = "{7d6ce8fc}"  # Action: Pump 1 (Acid)
action_id_pump_2_base = "{4aca1ce5}"  # Action: Pump 2 (Base)

action_id_email_notification = "{ae690f71}"  # Action: Email Notification

### DO NOT EDIT BELOW THIS LINE UNLESS YOU KNOW WHAT YOU ARE DOING ###
import time

# self.logger.info("{}".format(range_ph_high_danger))
if 'notify_ph' not in self.variables:  # Initiate pH notification timer
    self.variables['notify_ph'] = 0
if 'notify_none' not in self.variables:  # Initiate None measurement notification timer
    self.variables['notify_none'] = 0
measure_ph = self.condition(condition_id_measurement_ph_id)
self.message="pH is : {}. Dispensing 1 ml acid".format(measure_ph)
# self.logger.info("Conditional check. pH: {}".format(measure_ph))
if measure_ph is None:
    self.message += "\nWarning: No pH Measurement! Check sensor!"
    if self.variables['notify_none'] < time.time():  # Only notify every 8 hours#
        self.variables['notify_none'] = time.time() + 28800  # 8 hours
        self.run_action(action_id_email_notification, message=self.message)  # Email alert
    return

# First check if pH is dangerously low or high, and adjust if it is
if measure_ph < range_ph_low_danger:  # pH dangerously low, add base (pH up)
    msg = "pH is dangerously low: {}. Should be > {}. Dispensing 1 ml base".format(measure_ph, range_ph_low_danger)
    self.logger.info(msg)
    self.message += msg
    self.run_action(action_id_pump_2_base)  # Dispense 1 ml base (pH up)
if measure_ph > range_ph_high_danger:  # pH dangerously high, add acid (pH down)
    msg = "pH is dangerously high: {}. Should be < {}. Dispensing 1 ml acid".format(measure_ph, range_ph_high_danger)
    self.logger.info(msg)
    self.message += msg
    self.run_action(action_id_pump_1_acid)  # Dispense 1 ml acid (pH down)
