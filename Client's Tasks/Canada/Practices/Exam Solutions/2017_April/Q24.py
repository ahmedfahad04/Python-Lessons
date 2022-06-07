def displayOrbitInfo(heights, velocities, acceleration, periods):

    print("%11s %14s %20s %16s"%("Height (km) |","Velocity (m/s) |","Acceleration (m/s^2) |", "Period (seconds)"))
    for h,v,a,p in zip(heights, velocities, acceleration, periods):
        print("%11d | %14.2f | %20.4f | %16.2f" % (h/1000,v,a,p))


displayOrbitInfo([160000,164000,168000],[7817.26,7814.87,8912.48],[9.3586,9.35447,9.25417],[5246.54,5253.36,5258.6978])

