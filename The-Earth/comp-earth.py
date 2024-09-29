import spiceypy as spice
import datetime as dt
import math as math
import numpy as np

date_today = dt.dt.today()
date_today = date_today.strftime("%Y-%m-%dT00:00:00")
earth_id = 399
sun_id = 10

spice.furnsh("../kernels/lsk/naif0012.tls.txt")
spice.furnsh("../kernels/spk/de432s.bsp")
spice.furnsh("../kernels/pck/gm_de431.bsp")

et_today_midnight = spice.utc2et(date_today)
earth_state_wrt_sun, earth_sun_light_time = spice.spkgeo(targ=earth_id, et=et_today_midnight, 
                                                            ref="ECLIPJ2000", obs=sun_id)

earth_sun_distance = math.sqrt(earth_state_wrt_sun[0] ** 2.0
                               + earth_state_wrt_sun[1] ** 2.0
                               + earth_state_wrt_sun[2] ** 2.0)

earth_sun_distance_au = spice.convrt(earth_sun_distance, "km", "au")

earth_state_wrt_sun = np.array(earth_state_wrt_sun)
earth_sun_distance = np.linage.norm(earth_state_wrt_sun[:3])
earth_orb_speed_wrt_sun = np.linalg.norm(earth_state_wrt_sun[3:])

_, GM_SUN = spice.bodvcd(bodyid=10, item="GM", maxn=1)
v_orb_func = lambda gm, r: np.sqrt(gm/r)

