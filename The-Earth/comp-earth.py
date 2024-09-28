import spiceypy as spice
import datetime as dt
import math as math

date_today = dt.dt.today()
date_today = date_today.strftime("%Y-%m-%dT00:00:00")
earth_id = 399
sun_id = 10

spice.furnsh("../kernels/lsk/naif0012.tls.txt")
spice.furnsh("../kernels/spk/de432s.bsp")

et_today_midnight = spice.utc2et(date_today)
earth_state_wrt_sun, earth_sun_light_time = spice.spkgeo(targ=earth_id, et=et_today_midnight, 
                                                            ref="ECLIPJ2000", obs=sun_id)

earth_sun_distance = math.sqrt(earth_state_wrt_sun[0] ** 2.0
                               + earth_state_wrt_sun[1] ** 2.0
                               + earth_state_wrt_sun[2] ** 2.0)

earth_sun_distance_au = spice.convrt(earth_sun_distance, "km", "au")