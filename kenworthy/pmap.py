# How to apply PMs and parallaxes over time. You need to transform
# the coordinate over time with apply_space_motion, specifying obstime,
# and transform to GCRS to get geocentric coordinates
def pmap(c,dates):
	from astropy.coordinates import SkyCoord, GCRS
	from astropy.time import Time
	import astropy.units as u

	# make a copy of the input object and make it infinitely distant
	cfar = SkyCoord(c.ra, c.dec, frame=c.frame,
		pm_dec = 0. * u.mas/u.year,
	    distance = 1000000*u.parsec,
	    pm_ra_cosdec = 0. * u.mas/u.year,
	    radial_velocity=0.*u.km/u.s)

	c.obstime = dates[0]
	cfar.obstime = dates[0]

	cn = c.apply_space_motion(dates)
	cn_geo = cn.transform_to(GCRS)

	cfarn = cfar.apply_space_motion(dates)
	cfarn_geo = cfarn.transform_to(GCRS)

	t1 = SkyCoord(cn_geo.ra,cn_geo.dec,frame='icrs')
	dra, ddec = (t1[0]).spherical_offsets_to(t1)

	t1far = SkyCoord(cfarn_geo.ra,cfarn_geo.dec,frame='icrs')
	drafar, ddecfar = (t1far[0]).spherical_offsets_to(t1far)

	return(dra-drafar, ddec-ddecfar)


if __name__ == '__main__':
	import matplotlib.pyplot as plt
	import numpy as np
	from astropy import units as u
	from astropy.coordinates import SkyCoord
	from astropy.time import Time


	def draw_pm(star, epochs, title, ax, star_rest_frame=0):

		(dx, dy) = pmap(star, ee)

		dx = dx.to(u.mas).value
		dy = dy.to(u.mas).value

		if (star_rest_frame):
			dx = -dx
			dy = -dy
			title = "STAR REST FRAME: "+title

		ax.plot(dx, dy, color = 'orange', lw=1, zorder=-5)

		viewside = np.max([np.max(np.abs(dx)), np.max(np.abs(dy))]) * 1.1

		ax.set(xlabel='delta RA [mas]', ylabel='delta Dec [mas]',
			xlim=(viewside, -viewside),
			ylim=(-viewside, viewside)
			)

		for (i, e) in enumerate(epochs):
			if (i%20)==False:
				et=f'{e.jyear:.2f}'
				ax.text(dx[i],dy[i],et)
				ax.scatter(dx[i], dy[i], 5, color = 'blue')


		ax.text(0.98, 0.05, title, ha='right', va='bottom', transform=ax.transAxes, fontweight='bold')


	epochs = np.linspace(2020,2023,50)
	ee = Time(epochs, format='jyear')

	# times = ['2010-01-01T00:00:00',
	# 		'2010-02-01T00:00:00',
	# 		'2010-03-01T00:00:00',
	# 		'2010-04-01T00:00:00',
	# 		'2010-05-01T00:00:00',
	# 		'2010-06-01T00:00:00',
	# 		'2010-07-01T00:00:00',
	# 		'2010-08-01T00:00:00',
	# 		'2010-09-01T00:00:00',
	# 		'2010-10-01T00:00:00',
	# 		'2010-11-01T00:00:00',
	# 		'2010-12-01T00:00:00',
	# 		'2011-01-01T00:00:00',
	# 		'2011-02-01T00:00:00',
	# 		'2011-03-01T00:00:00',
	# 		'2011-04-01T00:00:00',
	# 		'2011-05-01T00:00:00',
	# 		'2011-06-01T00:00:00',
	# 		'2011-07-01T00:00:00',
	# 		'2011-08-01T00:00:00',
	# 		'2011-09-01T00:00:00',
	# 		'2011-10-01T00:00:00',
	# 		'2011-11-01T00:00:00',
	# 		'2011-12-01T00:00:00',
	# 		]
	# ee = Time(times, format='isot', scale='utc')


	star_name = "Fomalhaut"
	ra = "22 57 39.04"
	dec = "-29 37 20.0"
	rv = 6.5
	pm_ra  = 329.22
	pm_dec = -164.21
	plx = 130.08 # parallax (marscec)

	fomal = SkyCoord(ra, dec, unit=(u.hourangle, u.deg), frame='icrs',
	    pm_dec = pm_dec * u.mas/u.year,
	    distance = (1000./plx)*u.parsec,
	    pm_ra_cosdec = pm_ra * u.mas/u.year,
	    radial_velocity=rv*u.km/u.s)


	fig,axes = plt.subplots(2,2,figsize=(8,8))
	ax = axes.flatten()

	draw_pm(fomal, ee, star_name, ax[0])

	star_name = "North Ecliptic Pole"
	ra = "18 00 00.00"
	dec = "66 33 38.55"
	dec = "89 00 00"
	rv = 0.0
	pm_ra  = 0.0
	pm_dec = 0.0
	plx = 100.0 # parallax (marscec)

	nec = SkyCoord(ra, dec, unit=(u.hourangle, u.deg), frame='icrs',
	    pm_dec = pm_dec * u.mas/u.year,
	    distance = (1000./plx)*u.parsec,
	    pm_ra_cosdec = pm_ra * u.mas/u.year,
	    radial_velocity=rv*u.km/u.s)

	draw_pm(nec , ee, star_name, ax[1])

	star_name = "HD 37484"
	ra = "05 37 39.6"
	dec = "-28 37 34.6"
	rv = 23.27
	pm_ra  = 24.29
	pm_dec = -4.06
	plx = 17.61 # parallax (marscec)
	hd37 = SkyCoord(ra, dec, unit=(u.hourangle, u.deg), frame='icrs',
	    pm_dec = pm_dec * u.mas/u.year,
	    distance = (1000./plx)*u.parsec,
	    pm_ra_cosdec = pm_ra * u.mas/u.year,
	    radial_velocity=rv*u.km/u.s)

	draw_pm(hd37, ee, star_name, ax[2])


	star_name = "HD 106906"
	ra = "12 17 53.2"
	dec = "-55 58 32."
	rv = 8.4
	pm_ra  = -38.79
	pm_dec = -12.21
	plx = 10.86 # parallax (marscec)
	hd10 = SkyCoord(ra, dec, unit=(u.hourangle, u.deg), frame='icrs',
	    pm_dec = pm_dec * u.mas/u.year,
	    distance = (1000./plx)*u.parsec,
	    pm_ra_cosdec = pm_ra * u.mas/u.year,
	    radial_velocity=rv*u.km/u.s)

	draw_pm(hd10, ee, star_name, ax[3])


	plt.show()

