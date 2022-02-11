import numpy as np
from astropy.stats import sigma_clip
def rebinclip(t, f, tedges):
    tc_bin = np.array([])
    fc_bin = np.array([])
    fsigc_bin = np.array([])
    fc_npoi = np.array([])

    t_lower = tedges[:-1]
    t_upper = tedges[1:]
    t_midpoint = (t_lower+t_upper)/2.

    for t_mid, t_low, t_high in zip(t_midpoint, t_lower, t_upper):
        # select points from flux that have
        selpoints = ((t > t_low) * (t < t_high))
        fluxsel = f[selpoints]
        #fluxesel = flux_c[np.where(np.abs(time_c-t)<(dt/2))]
        if (fluxsel.size > 3):
        #    print('time {} has {} points'.format(t_mid, fluxsel.size))

            meanflux = sigma_clip(fluxsel, sigma=3, maxiters=2, masked=True)
            meane = np.ma.mean(meanflux)
            if np.isfinite(meane):
                tc_bin = np.append(tc_bin, t_mid)
                fc_bin = np.append(fc_bin, np.ma.mean(meanflux))
                fsigc_bin = np.append(fsigc_bin, np.ma.std(meanflux))
                fc_npoi = np.append(fc_npoi, np.sum(selpoints))

    return (tc_bin, fc_bin, fsigc_bin, fc_npoi)





# epochs for rebinned flux
t_rebin = np.arange(t_plot_start_epoch, t_plot_end_epoch, 0.05)

