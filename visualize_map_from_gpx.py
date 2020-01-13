import trackanimation
import gpxpy
import gpxpy.gpx
from trackanimation.animation import AnimationTrack

input_directory = "routes/"
gpx_file = open(input_directory + "Lunch_Run.gpx", 'r')
gpx = gpxpy.parse(gpx_file)
lapse_time = (gpx.tracks[0].segments[0].points[-1].time - gpx.tracks[0].segments[0].points[0].time).total_seconds()/16
ibiza_trk = trackanimation.read_track(input_directory)
ibiza_trk = ibiza_trk.time_video_normalize(time=int(lapse_time), framerate=10)
fig = AnimationTrack(df_points=ibiza_trk, dpi=50, bg_map=True, map_transparency=0.8)

fig.make_video(output_file='simple-example3', framerate=10, linewidth=3.0)