import spiceypy as spice
import datetime as dt

date_today = dt.dt.today()
date_today = date_today.strftime("%Y-%m-%dT00:00:00")
earth_id = 399
sun_id = 10

spice.furnsh("../kernels/lsk/naif0012.tls.txt")
spice.furnsh("../kernels/spk/de432s.bsp")

et_today_midnight = spice.utc2et(date_today)
earth_state_wrt_sun, earth_sun_light_time = spice.spkgeo(targ=earth_id, et=et_today_midnight, 
                                                            ref="ECLIPJ2000", obs=sun_id)

