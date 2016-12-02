# copied from: http://mdmetric.com/tech/M-thead%20600.htm

from collections import defaultdict


class Thread(object):
    __slots__ = ["major_diameter_max", "major_diameter_min", "pitch_diameter_max", "pitch_diameter_min",
                 "minor_diameter_max", "minor_diameter_min", "thread_class", "diameter", "pitch"]

    def __init__(self, major_diameter_max, major_diameter_min, pitch_diameter_max, pitch_diameter_min,
                 minor_diameter_max, minor_diameter_min, thread_class, diameter, pitch):
        # type: (float, float, float, float, float, float) -> object
        self.major_diameter_max = major_diameter_max
        self.major_diameter_min = major_diameter_min
        self.pitch_diameter_max = pitch_diameter_max
        self.pitch_diameter_min = pitch_diameter_min
        self.minor_diameter_max = minor_diameter_max
        self.minor_diameter_min = minor_diameter_min
        self.thread_class = thread_class
        self.diameter = diameter
        self.pitch = pitch


thread = defaultdict(lambda: defaultdict(dict))

thread["6g"][0.25][0.075] = Thread(major_diameter_max=0.25, major_diameter_min=0.235, pitch_diameter_max=0.201,
                                   pitch_diameter_min=0.187, minor_diameter_max=0.16, minor_diameter_min=0.14,
                                   thread_class="6g", diameter=0.25, pitch=0.075)
thread["6g"][0.3][0.08] = Thread(major_diameter_max=0.3, major_diameter_min=0.284, pitch_diameter_max=0.248,
                                 pitch_diameter_min=0.234, minor_diameter_max=0.204, minor_diameter_min=0.183,
                                 thread_class="6g", diameter=0.3, pitch=0.08)
thread["6g"][0.3][0.09] = Thread(major_diameter_max=0.3, major_diameter_min=0.283, pitch_diameter_max=0.242,
                                 pitch_diameter_min=0.226, minor_diameter_max=0.192, minor_diameter_min=0.17,
                                 thread_class="6g", diameter=0.3, pitch=0.09)
thread["6g"][0.35][0.09] = Thread(major_diameter_max=0.35, major_diameter_min=0.333, pitch_diameter_max=0.292,
                                  pitch_diameter_min=0.277, minor_diameter_max=0.242, minor_diameter_min=0.22,
                                  thread_class="6g", diameter=0.35, pitch=0.09)
thread["6g"][0.4][0.1] = Thread(major_diameter_max=0.4, major_diameter_min=0.382, pitch_diameter_max=0.335,
                                pitch_diameter_min=0.319, minor_diameter_max=0.28, minor_diameter_min=0.256,
                                thread_class="6g", diameter=0.4, pitch=0.1)
thread["6g"][0.45][0.1] = Thread(major_diameter_max=0.45, major_diameter_min=0.432, pitch_diameter_max=0.385,
                                 pitch_diameter_min=0.369, minor_diameter_max=0.33, minor_diameter_min=0.306,
                                 thread_class="6g", diameter=0.45, pitch=0.1)
thread["6g"][0.5][0.125] = Thread(major_diameter_max=0.5, major_diameter_min=0.479, pitch_diameter_max=0.419,
                                  pitch_diameter_min=0.401, minor_diameter_max=0.35, minor_diameter_min=0.322,
                                  thread_class="6g", diameter=0.5, pitch=0.125)
thread["6g"][0.55][0.125] = Thread(major_diameter_max=0.55, major_diameter_min=0.529, pitch_diameter_max=0.469,
                                   pitch_diameter_min=0.451, minor_diameter_max=0.4, minor_diameter_min=0.372,
                                   thread_class="6g", diameter=0.55, pitch=0.125)
thread["6g"][0.6][0.15] = Thread(major_diameter_max=0.6, major_diameter_min=0.576, pitch_diameter_max=0.503,
                                 pitch_diameter_min=0.483, minor_diameter_max=0.42, minor_diameter_min=0.388,
                                 thread_class="6g", diameter=0.6, pitch=0.15)
thread["6g"][0.7][0.175] = Thread(major_diameter_max=0.7, major_diameter_min=0.673, pitch_diameter_max=0.586,
                                  pitch_diameter_min=0.564, minor_diameter_max=0.49, minor_diameter_min=0.454,
                                  thread_class="6g", diameter=0.7, pitch=0.175)
thread["6g"][0.8][0.2] = Thread(major_diameter_max=0.8, major_diameter_min=0.77, pitch_diameter_max=0.67,
                                pitch_diameter_min=0.646, minor_diameter_max=0.56, minor_diameter_min=0.52,
                                thread_class="6g", diameter=0.8, pitch=0.2)
thread["6g"][0.9][0.225] = Thread(major_diameter_max=0.9, major_diameter_min=0.867, pitch_diameter_max=0.754,
                                  pitch_diameter_min=0.728, minor_diameter_max=0.63, minor_diameter_min=0.586,
                                  thread_class="6g", diameter=0.9, pitch=0.225)
thread["6g"][1][0.25] = Thread(major_diameter_max=0.982, major_diameter_min=0.915, pitch_diameter_max=0.82,
                               pitch_diameter_min=0.767, minor_diameter_max=0.711, minor_diameter_min=0.613,
                               thread_class="6g", diameter=1, pitch=0.25)
thread["6g"][1][0.2] = Thread(major_diameter_max=0.983, major_diameter_min=0.927, pitch_diameter_max=0.853,
                              pitch_diameter_min=0.805, minor_diameter_max=0.766, minor_diameter_min=0.682,
                              thread_class="6g", diameter=1, pitch=0.2)
thread["6g"][1.1][0.25] = Thread(major_diameter_max=1.082, major_diameter_min=1.015, pitch_diameter_max=0.92,
                                 pitch_diameter_min=0.867, minor_diameter_max=0.811, minor_diameter_min=0.713,
                                 thread_class="6g", diameter=1.1, pitch=0.25)
thread["6g"][1.1][0.2] = Thread(major_diameter_max=1.083, major_diameter_min=1.027, pitch_diameter_max=0.953,
                                pitch_diameter_min=0.905, minor_diameter_max=0.866, minor_diameter_min=0.782,
                                thread_class="6g", diameter=1.1, pitch=0.2)
thread["6g"][1.2][0.25] = Thread(major_diameter_max=1.182, major_diameter_min=1.115, pitch_diameter_max=1.02,
                                 pitch_diameter_min=0.967, minor_diameter_max=0.911, minor_diameter_min=0.813,
                                 thread_class="6g", diameter=1.2, pitch=0.25)
thread["6g"][1.2][0.2] = Thread(major_diameter_max=1.183, major_diameter_min=1.127, pitch_diameter_max=1.053,
                                pitch_diameter_min=1.005, minor_diameter_max=0.966, minor_diameter_min=0.882,
                                thread_class="6g", diameter=1.2, pitch=0.2)
thread["6g"][1.4][0.3] = Thread(major_diameter_max=1.383, major_diameter_min=1.308, pitch_diameter_max=1.253,
                                pitch_diameter_min=1.193, minor_diameter_max=1.166, minor_diameter_min=1.07,
                                thread_class="6g", diameter=1.4, pitch=0.3)
thread["6g"][1.4][0.2] = Thread(major_diameter_max=1.383, major_diameter_min=1.327, pitch_diameter_max=1.253,
                                pitch_diameter_min=1.205, minor_diameter_max=1.166, minor_diameter_min=1.082,
                                thread_class="6g", diameter=1.4, pitch=0.2)
thread["6g"][1.6][0.35] = Thread(major_diameter_max=1.581, major_diameter_min=1.496, pitch_diameter_max=1.354,
                                 pitch_diameter_min=1.291, minor_diameter_max=1.202, minor_diameter_min=1.075,
                                 thread_class="6g", diameter=1.6, pitch=0.35)
thread["6g"][1.6][0.3] = Thread(major_diameter_max=1.582, major_diameter_min=1.507, pitch_diameter_max=1.387,
                                pitch_diameter_min=1.342, minor_diameter_max=1.257, minor_diameter_min=1.157,
                                thread_class="6g", diameter=1.6, pitch=0.3)
thread["6g"][1.6][0.2] = Thread(major_diameter_max=1.583, major_diameter_min=1.527, pitch_diameter_max=1.453,
                                pitch_diameter_min=1.403, minor_diameter_max=1.366, minor_diameter_min=1.28,
                                thread_class="6g", diameter=1.6, pitch=0.2)
thread["6g"][1.7][0.35] = Thread(major_diameter_max=1.681, major_diameter_min=1.596, pitch_diameter_max=1.454,
                                 pitch_diameter_min=1.391, minor_diameter_max=1.302, minor_diameter_min=1.175,
                                 thread_class="6g", diameter=1.7, pitch=0.35)
thread["6g"][1.8][0.35] = Thread(major_diameter_max=1.781, major_diameter_min=1.696, pitch_diameter_max=1.554,
                                 pitch_diameter_min=1.491, minor_diameter_max=1.402, minor_diameter_min=1.275,
                                 thread_class="6g", diameter=1.8, pitch=0.35)
thread["6g"][1.8][0.2] = Thread(major_diameter_max=1.783, major_diameter_min=1.727, pitch_diameter_max=1.653,
                                pitch_diameter_min=1.603, minor_diameter_max=1.566, minor_diameter_min=1.48,
                                thread_class="6g", diameter=1.8, pitch=0.2)
thread["6g"][2][0.4] = Thread(major_diameter_max=1.981, major_diameter_min=1.886, pitch_diameter_max=1.721,
                              pitch_diameter_min=1.654, minor_diameter_max=1.548, minor_diameter_min=1.408,
                              thread_class="6g", diameter=2, pitch=0.4)
thread["6g"][2][0.25] = Thread(major_diameter_max=1.982, major_diameter_min=1.915, pitch_diameter_max=1.82,
                               pitch_diameter_min=1.764, minor_diameter_max=1.711, minor_diameter_min=1.61,
                               thread_class="6g", diameter=2, pitch=0.25)
thread["6g"][2.2][0.45] = Thread(major_diameter_max=2.18, major_diameter_min=2.08, pitch_diameter_max=1.888,
                                 pitch_diameter_min=1.817, minor_diameter_max=1.693, minor_diameter_min=1.54,
                                 thread_class="6g", diameter=2.2, pitch=0.45)
thread["6g"][2.2][0.25] = Thread(major_diameter_max=2.182, major_diameter_min=2.115, pitch_diameter_max=2.02,
                                 pitch_diameter_min=1.964, minor_diameter_max=1.911, minor_diameter_min=1.81,
                                 thread_class="6g", diameter=2.2, pitch=0.25)
thread["6g"][2.3][0.45] = Thread(major_diameter_max=2.28, major_diameter_min=2.18, pitch_diameter_max=1.988,
                                 pitch_diameter_min=1.917, minor_diameter_max=1.793, minor_diameter_min=1.64,
                                 thread_class="6g", diameter=2.3, pitch=0.45)
thread["6g"][2.3][0.4] = Thread(major_diameter_max=2.281, major_diameter_min=2.186, pitch_diameter_max=2.021,
                                pitch_diameter_min=1.954, minor_diameter_max=1.848, minor_diameter_min=1.708,
                                thread_class="6g", diameter=2.3, pitch=0.4)
thread["6g"][2.5][0.45] = Thread(major_diameter_max=2.48, major_diameter_min=2.38, pitch_diameter_max=2.188,
                                 pitch_diameter_min=2.117, minor_diameter_max=1.993, minor_diameter_min=1.84,
                                 thread_class="6g", diameter=2.5, pitch=0.45)
thread["6g"][2.5][0.35] = Thread(major_diameter_max=2.481, major_diameter_min=2.396, pitch_diameter_max=2.254,
                                 pitch_diameter_min=2.191, minor_diameter_max=2.102, minor_diameter_min=1.975,
                                 thread_class="6g", diameter=2.5, pitch=0.35)
thread["6g"][2.6][0.45] = Thread(major_diameter_max=2.58, major_diameter_min=2.48, pitch_diameter_max=2.288,
                                 pitch_diameter_min=2.217, minor_diameter_max=2.093, minor_diameter_min=1.94,
                                 thread_class="6g", diameter=2.6, pitch=0.45)
thread["6g"][3][0.5] = Thread(major_diameter_max=2.98, major_diameter_min=2.874, pitch_diameter_max=2.655,
                              pitch_diameter_min=2.58, minor_diameter_max=2.439, minor_diameter_min=2.272,
                              thread_class="6g", diameter=3, pitch=0.5)
thread["6g"][3][0.35] = Thread(major_diameter_max=2.981, major_diameter_min=2.896, pitch_diameter_max=2.754,
                               pitch_diameter_min=2.687, minor_diameter_max=2.602, minor_diameter_min=2.471,
                               thread_class="6g", diameter=3, pitch=0.35)
thread["6g"][3.5][0.6] = Thread(major_diameter_max=3.479, major_diameter_min=3.354, pitch_diameter_max=3.089,
                                pitch_diameter_min=3.004, minor_diameter_max=2.829, minor_diameter_min=2.635,
                                thread_class="6g", diameter=3.5, pitch=0.6)
thread["6g"][3.5][0.35] = Thread(major_diameter_max=3.481, major_diameter_min=3.396, pitch_diameter_max=3.254,
                                 pitch_diameter_min=3.187, minor_diameter_max=3.102, minor_diameter_min=2.971,
                                 thread_class="6g", diameter=3.5, pitch=0.35)
thread["6g"][4][0.7] = Thread(major_diameter_max=3.978, major_diameter_min=3.838, pitch_diameter_max=3.523,
                              pitch_diameter_min=3.433, minor_diameter_max=3.22, minor_diameter_min=3.002,
                              thread_class="6g", diameter=4, pitch=0.7)
thread["6g"][4][0.5] = Thread(major_diameter_max=3.98, major_diameter_min=3.874, pitch_diameter_max=3.655,
                              pitch_diameter_min=3.58, minor_diameter_max=3.439, minor_diameter_min=3.272,
                              thread_class="6g", diameter=4, pitch=0.5)
thread["6g"][4.5][0.75] = Thread(major_diameter_max=4.478, major_diameter_min=4.338, pitch_diameter_max=3.991,
                                 pitch_diameter_min=3.901, minor_diameter_max=3.666, minor_diameter_min=3.439,
                                 thread_class="6g", diameter=4.5, pitch=0.75)
thread["6g"][4.5][0.5] = Thread(major_diameter_max=4.48, major_diameter_min=4.374, pitch_diameter_max=4.155,
                                pitch_diameter_min=4.08, minor_diameter_max=3.939, minor_diameter_min=3.772,
                                thread_class="6g", diameter=4.5, pitch=0.5)
thread["6g"][5][0.8] = Thread(major_diameter_max=4.976, major_diameter_min=4.826, pitch_diameter_max=4.456,
                              pitch_diameter_min=4.361, minor_diameter_max=4.11, minor_diameter_min=3.869,
                              thread_class="6g", diameter=5, pitch=0.8)
thread["6g"][5][0.5] = Thread(major_diameter_max=4.98, major_diameter_min=4.874, pitch_diameter_max=4.655,
                              pitch_diameter_min=4.58, minor_diameter_max=4.439, minor_diameter_min=4.272,
                              thread_class="6g", diameter=5, pitch=0.5)
thread["6g"][5.5][0.5] = Thread(major_diameter_max=5.48, major_diameter_min=5.374, pitch_diameter_max=5.155,
                                pitch_diameter_min=5.065, minor_diameter_max=4.939, minor_diameter_min=4.757,
                                thread_class="6g", diameter=5.5, pitch=0.5)
thread["6g"][6][1] = Thread(major_diameter_max=5.974, major_diameter_min=5.794, pitch_diameter_max=5.324,
                            pitch_diameter_min=5.212, minor_diameter_max=4.891, minor_diameter_min=4.596,
                            thread_class="6g", diameter=6, pitch=1)
thread["6g"][6][0.8] = Thread(major_diameter_max=5.976, major_diameter_min=5.826, pitch_diameter_max=5.456,
                              pitch_diameter_min=5.376, minor_diameter_max=5.11, minor_diameter_min=4.884,
                              thread_class="6g", diameter=6, pitch=0.8)
thread["6g"][6][0.75] = Thread(major_diameter_max=5.978, major_diameter_min=5.838, pitch_diameter_max=5.491,
                               pitch_diameter_min=5.391, minor_diameter_max=5.166, minor_diameter_min=4.929,
                               thread_class="6g", diameter=6, pitch=0.75)
thread["6g"][6][0.7] = Thread(major_diameter_max=5.978, major_diameter_min=5.838, pitch_diameter_max=5.523,
                              pitch_diameter_min=5.428, minor_diameter_max=5.22, minor_diameter_min=4.997,
                              thread_class="6g", diameter=6, pitch=0.7)
thread["6g"][6][0.5] = Thread(major_diameter_max=5.98, major_diameter_min=5.874, pitch_diameter_max=5.655,
                              pitch_diameter_min=5.57, minor_diameter_max=5.439, minor_diameter_min=5.262,
                              thread_class="6g", diameter=6, pitch=0.5)
thread["6g"][7][1] = Thread(major_diameter_max=6.974, major_diameter_min=6.794, pitch_diameter_max=6.324,
                            pitch_diameter_min=6.212, minor_diameter_max=5.891, minor_diameter_min=5.596,
                            thread_class="6g", diameter=7, pitch=1)
thread["6g"][7][0.75] = Thread(major_diameter_max=6.978, major_diameter_min=6.838, pitch_diameter_max=6.491,
                               pitch_diameter_min=6.391, minor_diameter_max=6.166, minor_diameter_min=5.929,
                               thread_class="6g", diameter=7, pitch=0.75)
thread["6g"][7][0.5] = Thread(major_diameter_max=6.98, major_diameter_min=6.874, pitch_diameter_max=6.655,
                              pitch_diameter_min=6.57, minor_diameter_max=6.439, minor_diameter_min=6.262,
                              thread_class="6g", diameter=7, pitch=0.5)
thread["6g"][8][1.25] = Thread(major_diameter_max=7.972, major_diameter_min=7.76, pitch_diameter_max=7.16,
                               pitch_diameter_min=7.042, minor_diameter_max=6.619, minor_diameter_min=6.272,
                               thread_class="6g", diameter=8, pitch=1.25)
thread["6g"][8][1] = Thread(major_diameter_max=7.974, major_diameter_min=7.794, pitch_diameter_max=7.324,
                            pitch_diameter_min=7.212, minor_diameter_max=6.891, minor_diameter_min=6.596,
                            thread_class="6g", diameter=8, pitch=1)
thread["6g"][8][0.8] = Thread(major_diameter_max=7.976, major_diameter_min=7.826, pitch_diameter_max=7.456,
                              pitch_diameter_min=7.35, minor_diameter_max=7.11, minor_diameter_min=6.858,
                              thread_class="6g", diameter=8, pitch=0.8)
thread["6g"][8][0.75] = Thread(major_diameter_max=7.978, major_diameter_min=7.838, pitch_diameter_max=7.491,
                               pitch_diameter_min=7.391, minor_diameter_max=7.166, minor_diameter_min=6.929,
                               thread_class="6g", diameter=8, pitch=0.75)
thread["6g"][8][0.5] = Thread(major_diameter_max=7.98, major_diameter_min=7.874, pitch_diameter_max=7.655,
                              pitch_diameter_min=7.57, minor_diameter_max=7.439, minor_diameter_min=7.262,
                              thread_class="6g", diameter=8, pitch=0.5)
thread["6g"][9][1.25] = Thread(major_diameter_max=8.972, major_diameter_min=8.76, pitch_diameter_max=8.16,
                               pitch_diameter_min=8.042, minor_diameter_max=7.619, minor_diameter_min=7.272,
                               thread_class="6g", diameter=9, pitch=1.25)
thread["6g"][9][1] = Thread(major_diameter_max=8.974, major_diameter_min=8.794, pitch_diameter_max=8.324,
                            pitch_diameter_min=8.212, minor_diameter_max=7.891, minor_diameter_min=7.596,
                            thread_class="6g", diameter=9, pitch=1)
thread["6g"][9][0.75] = Thread(major_diameter_max=8.978, major_diameter_min=8.838, pitch_diameter_max=8.491,
                               pitch_diameter_min=8.391, minor_diameter_max=8.166, minor_diameter_min=7.929,
                               thread_class="6g", diameter=9, pitch=0.75)
thread["6g"][9][0.5] = Thread(major_diameter_max=8.98, major_diameter_min=8.874, pitch_diameter_max=8.655,
                              pitch_diameter_min=8.57, minor_diameter_max=8.439, minor_diameter_min=8.262,
                              thread_class="6g", diameter=9, pitch=0.5)
thread["6g"][10][1.5] = Thread(major_diameter_max=9.968, major_diameter_min=9.732, pitch_diameter_max=8.994,
                               pitch_diameter_min=8.862, minor_diameter_max=8.344, minor_diameter_min=7.938,
                               thread_class="6g", diameter=10, pitch=1.5)
thread["6g"][10][1.25] = Thread(major_diameter_max=9.972, major_diameter_min=9.76, pitch_diameter_max=9.16,
                                pitch_diameter_min=9.042, minor_diameter_max=8.619, minor_diameter_min=8.272,
                                thread_class="6g", diameter=10, pitch=1.25)
thread["6g"][10][1.12] = Thread(major_diameter_max=9.973, major_diameter_min=9.783, pitch_diameter_max=9.246,
                                pitch_diameter_min=9.128, minor_diameter_max=8.761, minor_diameter_min=8.438,
                                thread_class="6g", diameter=10, pitch=1.12)
thread["6g"][10][1] = Thread(major_diameter_max=9.974, major_diameter_min=9.794, pitch_diameter_max=9.324,
                             pitch_diameter_min=9.212, minor_diameter_max=8.891, minor_diameter_min=8.596,
                             thread_class="6g", diameter=10, pitch=1)
thread["6g"][10][0.75] = Thread(major_diameter_max=9.978, major_diameter_min=9.838, pitch_diameter_max=9.491,
                                pitch_diameter_min=9.391, minor_diameter_max=9.166, minor_diameter_min=8.929,
                                thread_class="6g", diameter=10, pitch=0.75)
thread["6g"][10][0.5] = Thread(major_diameter_max=9.98, major_diameter_min=9.874, pitch_diameter_max=9.655,
                               pitch_diameter_min=9.57, minor_diameter_max=9.439, minor_diameter_min=9.262,
                               thread_class="6g", diameter=10, pitch=0.5)
thread["6g"][11][1.5] = Thread(major_diameter_max=10.97, major_diameter_min=10.73, pitch_diameter_max=9.994,
                               pitch_diameter_min=9.862, minor_diameter_max=9.344, minor_diameter_min=8.938,
                               thread_class="6g", diameter=11, pitch=1.5)
thread["6g"][11][1] = Thread(major_diameter_max=10.97, major_diameter_min=10.79, pitch_diameter_max=10.32,
                             pitch_diameter_min=10.21, minor_diameter_max=9.891, minor_diameter_min=9.596,
                             thread_class="6g", diameter=11, pitch=1)
thread["6g"][11][0.75] = Thread(major_diameter_max=10.98, major_diameter_min=10.84, pitch_diameter_max=10.49,
                                pitch_diameter_min=10.39, minor_diameter_max=10.166, minor_diameter_min=9.929,
                                thread_class="6g", diameter=11, pitch=0.75)
thread["6g"][11][0.5] = Thread(major_diameter_max=10.98, major_diameter_min=10.87, pitch_diameter_max=10.66,
                               pitch_diameter_min=10.57, minor_diameter_max=10.439, minor_diameter_min=10.262,
                               thread_class="6g", diameter=11, pitch=0.5)
thread["6g"][12][1.75] = Thread(major_diameter_max=11.97, major_diameter_min=11.7, pitch_diameter_max=10.83,
                                pitch_diameter_min=10.68, minor_diameter_max=10.072, minor_diameter_min=9.601,
                                thread_class="6g", diameter=12, pitch=1.75)
thread["6g"][12][1.5] = Thread(major_diameter_max=11.97, major_diameter_min=11.73, pitch_diameter_max=10.99,
                               pitch_diameter_min=10.85, minor_diameter_max=10.344, minor_diameter_min=9.93,
                               thread_class="6g", diameter=12, pitch=1.5)
thread["6g"][12][1.25] = Thread(major_diameter_max=11.97, major_diameter_min=11.76, pitch_diameter_max=11.16,
                                pitch_diameter_min=11.03, minor_diameter_max=10.619, minor_diameter_min=10.258,
                                thread_class="6g", diameter=12, pitch=1.25)
thread["6g"][12][1] = Thread(major_diameter_max=11.97, major_diameter_min=11.79, pitch_diameter_max=11.32,
                             pitch_diameter_min=11.21, minor_diameter_max=10.891, minor_diameter_min=10.59,
                             thread_class="6g", diameter=12, pitch=1)
thread["6g"][12][0.75] = Thread(major_diameter_max=11.98, major_diameter_min=11.84, pitch_diameter_max=11.49,
                                pitch_diameter_min=11.39, minor_diameter_max=11.166, minor_diameter_min=10.923,
                                thread_class="6g", diameter=12, pitch=0.75)
thread["6g"][12][0.5] = Thread(major_diameter_max=11.98, major_diameter_min=11.87, pitch_diameter_max=11.66,
                               pitch_diameter_min=11.57, minor_diameter_max=11.439, minor_diameter_min=11.257,
                               thread_class="6g", diameter=12, pitch=0.5)
thread["6g"][14][2] = Thread(major_diameter_max=13.96, major_diameter_min=13.68, pitch_diameter_max=12.66,
                             pitch_diameter_min=12.5, minor_diameter_max=11.797, minor_diameter_min=11.271,
                             thread_class="6g", diameter=14, pitch=2)
thread["6g"][14][1.5] = Thread(major_diameter_max=13.97, major_diameter_min=13.73, pitch_diameter_max=12.99,
                               pitch_diameter_min=12.85, minor_diameter_max=12.344, minor_diameter_min=11.93,
                               thread_class="6g", diameter=14, pitch=1.5)
thread["6g"][14][1.25] = Thread(major_diameter_max=13.97, major_diameter_min=13.76, pitch_diameter_max=13.16,
                                pitch_diameter_min=13.03, minor_diameter_max=12.619, minor_diameter_min=12.258,
                                thread_class="6g", diameter=14, pitch=1.25)
thread["6g"][14][1] = Thread(major_diameter_max=13.97, major_diameter_min=13.79, pitch_diameter_max=13.32,
                             pitch_diameter_min=13.21, minor_diameter_max=12.891, minor_diameter_min=12.59,
                             thread_class="6g", diameter=14, pitch=1)
thread["6g"][14][0.75] = Thread(major_diameter_max=13.98, major_diameter_min=13.84, pitch_diameter_max=13.49,
                                pitch_diameter_min=13.39, minor_diameter_max=13.166, minor_diameter_min=12.923,
                                thread_class="6g", diameter=14, pitch=0.75)
thread["6g"][14][0.5] = Thread(major_diameter_max=13.98, major_diameter_min=13.87, pitch_diameter_max=13.66,
                               pitch_diameter_min=13.57, minor_diameter_max=13.439, minor_diameter_min=13.257,
                               thread_class="6g", diameter=14, pitch=0.5)
thread["6g"][15][1.5] = Thread(major_diameter_max=14.97, major_diameter_min=14.73, pitch_diameter_max=13.99,
                               pitch_diameter_min=13.85, minor_diameter_max=13.344, minor_diameter_min=12.93,
                               thread_class="6g", diameter=15, pitch=1.5)
thread["6g"][15][1] = Thread(major_diameter_max=14.97, major_diameter_min=14.79, pitch_diameter_max=14.32,
                             pitch_diameter_min=14.21, minor_diameter_max=13.891, minor_diameter_min=13.59,
                             thread_class="6g", diameter=15, pitch=1)
thread["6g"][16][2] = Thread(major_diameter_max=15.96, major_diameter_min=15.68, pitch_diameter_max=14.66,
                             pitch_diameter_min=14.5, minor_diameter_max=13.797, minor_diameter_min=13.271,
                             thread_class="6g", diameter=16, pitch=2)
thread["6g"][16][1.6] = Thread(major_diameter_max=15.97, major_diameter_min=15.76, pitch_diameter_max=14.93,
                               pitch_diameter_min=14.82, minor_diameter_max=14.236, minor_diameter_min=13.838,
                               thread_class="6g", diameter=16, pitch=1.6)
thread["6g"][16][1.5] = Thread(major_diameter_max=15.97, major_diameter_min=15.73, pitch_diameter_max=14.99,
                               pitch_diameter_min=14.85, minor_diameter_max=14.344, minor_diameter_min=13.93,
                               thread_class="6g", diameter=16, pitch=1.5)
thread["6g"][16][1.25] = Thread(major_diameter_max=15.97, major_diameter_min=15.76, pitch_diameter_max=15.16,
                                pitch_diameter_min=15.03, minor_diameter_max=14.619, minor_diameter_min=14.258,
                                thread_class="6g", diameter=16, pitch=1.25)
thread["6g"][16][1] = Thread(major_diameter_max=15.97, major_diameter_min=15.79, pitch_diameter_max=15.32,
                             pitch_diameter_min=15.21, minor_diameter_max=14.891, minor_diameter_min=14.59,
                             thread_class="6g", diameter=16, pitch=1)
thread["6g"][16][0.75] = Thread(major_diameter_max=15.98, major_diameter_min=15.84, pitch_diameter_max=15.49,
                                pitch_diameter_min=15.39, minor_diameter_max=15.166, minor_diameter_min=14.923,
                                thread_class="6g", diameter=16, pitch=0.75)
thread["6g"][16][0.5] = Thread(major_diameter_max=15.98, major_diameter_min=15.87, pitch_diameter_max=15.66,
                               pitch_diameter_min=15.57, minor_diameter_max=15.439, minor_diameter_min=15.257,
                               thread_class="6g", diameter=16, pitch=0.5)
thread["6g"][17][1.5] = Thread(major_diameter_max=16.97, major_diameter_min=16.73, pitch_diameter_max=15.99,
                               pitch_diameter_min=15.85, minor_diameter_max=15.344, minor_diameter_min=14.93,
                               thread_class="6g", diameter=17, pitch=1.5)
thread["6g"][17][1] = Thread(major_diameter_max=16.97, major_diameter_min=16.79, pitch_diameter_max=16.32,
                             pitch_diameter_min=16.21, minor_diameter_max=15.891, minor_diameter_min=15.59,
                             thread_class="6g", diameter=17, pitch=1)
thread["6g"][18][2.5] = Thread(major_diameter_max=17.96, major_diameter_min=17.62, pitch_diameter_max=16.33,
                               pitch_diameter_min=16.16, minor_diameter_max=15.252, minor_diameter_min=14.624,
                               thread_class="6g", diameter=18, pitch=2.5)
thread["6g"][18][2] = Thread(major_diameter_max=17.96, major_diameter_min=17.68, pitch_diameter_max=16.66,
                             pitch_diameter_min=16.5, minor_diameter_max=15.797, minor_diameter_min=15.271,
                             thread_class="6g", diameter=18, pitch=2)
thread["6g"][18][1.5] = Thread(major_diameter_max=17.97, major_diameter_min=17.73, pitch_diameter_max=16.99,
                               pitch_diameter_min=16.85, minor_diameter_max=16.344, minor_diameter_min=15.93,
                               thread_class="6g", diameter=18, pitch=1.5)
thread["6g"][18][1.25] = Thread(major_diameter_max=17.97, major_diameter_min=17.76, pitch_diameter_max=17.16,
                                pitch_diameter_min=17.03, minor_diameter_max=16.619, minor_diameter_min=16.258,
                                thread_class="6g", diameter=18, pitch=1.25)
thread["6g"][18][1] = Thread(major_diameter_max=17.97, major_diameter_min=17.79, pitch_diameter_max=17.32,
                             pitch_diameter_min=17.21, minor_diameter_max=16.891, minor_diameter_min=16.59,
                             thread_class="6g", diameter=18, pitch=1)
thread["6g"][18][0.75] = Thread(major_diameter_max=17.98, major_diameter_min=17.84, pitch_diameter_max=17.49,
                                pitch_diameter_min=17.39, minor_diameter_max=17.166, minor_diameter_min=16.923,
                                thread_class="6g", diameter=18, pitch=0.75)
thread["6g"][18][0.5] = Thread(major_diameter_max=17.98, major_diameter_min=17.87, pitch_diameter_max=17.66,
                               pitch_diameter_min=17.57, minor_diameter_max=17.439, minor_diameter_min=17.257,
                               thread_class="6g", diameter=18, pitch=0.5)
thread["6g"][20][2.5] = Thread(major_diameter_max=19.96, major_diameter_min=19.62, pitch_diameter_max=18.33,
                               pitch_diameter_min=18.16, minor_diameter_max=17.252, minor_diameter_min=16.624,
                               thread_class="6g", diameter=20, pitch=2.5)
thread["6g"][20][2] = Thread(major_diameter_max=19.96, major_diameter_min=19.68, pitch_diameter_max=18.66,
                             pitch_diameter_min=18.5, minor_diameter_max=17.797, minor_diameter_min=17.271,
                             thread_class="6g", diameter=20, pitch=2)
thread["6g"][20][1.5] = Thread(major_diameter_max=19.97, major_diameter_min=19.73, pitch_diameter_max=18.99,
                               pitch_diameter_min=18.85, minor_diameter_max=18.344, minor_diameter_min=17.93,
                               thread_class="6g", diameter=20, pitch=1.5)
thread["6g"][20][1] = Thread(major_diameter_max=19.97, major_diameter_min=19.79, pitch_diameter_max=19.32,
                             pitch_diameter_min=19.21, minor_diameter_max=18.891, minor_diameter_min=18.59,
                             thread_class="6g", diameter=20, pitch=1)
thread["6g"][20][0.75] = Thread(major_diameter_max=19.98, major_diameter_min=19.84, pitch_diameter_max=19.49,
                                pitch_diameter_min=19.39, minor_diameter_max=19.166, minor_diameter_min=18.923,
                                thread_class="6g", diameter=20, pitch=0.75)
thread["6g"][20][0.5] = Thread(major_diameter_max=19.98, major_diameter_min=19.87, pitch_diameter_max=19.66,
                               pitch_diameter_min=19.57, minor_diameter_max=19.439, minor_diameter_min=19.257,
                               thread_class="6g", diameter=20, pitch=0.5)
thread["6g"][22][3] = Thread(major_diameter_max=21.95, major_diameter_min=21.58, pitch_diameter_max=20,
                             pitch_diameter_min=19.82, minor_diameter_max=18.704, minor_diameter_min=17.97,
                             thread_class="6g", diameter=22, pitch=3)
thread["6g"][22][2.5] = Thread(major_diameter_max=21.96, major_diameter_min=21.62, pitch_diameter_max=20.33,
                               pitch_diameter_min=20.16, minor_diameter_max=19.252, minor_diameter_min=18.624,
                               thread_class="6g", diameter=22, pitch=2.5)
thread["6g"][22][2] = Thread(major_diameter_max=21.96, major_diameter_min=21.68, pitch_diameter_max=20.66,
                             pitch_diameter_min=20.5, minor_diameter_max=19.797, minor_diameter_min=19.271,
                             thread_class="6g", diameter=22, pitch=2)
thread["6g"][22][1.5] = Thread(major_diameter_max=21.97, major_diameter_min=21.73, pitch_diameter_max=20.99,
                               pitch_diameter_min=20.85, minor_diameter_max=20.344, minor_diameter_min=19.93,
                               thread_class="6g", diameter=22, pitch=1.5)
thread["6g"][22][1] = Thread(major_diameter_max=21.97, major_diameter_min=21.79, pitch_diameter_max=21.32,
                             pitch_diameter_min=21.21, minor_diameter_max=20.891, minor_diameter_min=20.59,
                             thread_class="6g", diameter=22, pitch=1)
thread["6g"][22][0.75] = Thread(major_diameter_max=21.98, major_diameter_min=21.84, pitch_diameter_max=21.49,
                                pitch_diameter_min=21.39, minor_diameter_max=21.166, minor_diameter_min=20.923,
                                thread_class="6g", diameter=22, pitch=0.75)
thread["6g"][22][0.5] = Thread(major_diameter_max=21.98, major_diameter_min=21.87, pitch_diameter_max=21.66,
                               pitch_diameter_min=21.57, minor_diameter_max=21.439, minor_diameter_min=21.257,
                               thread_class="6g", diameter=22, pitch=0.5)
thread["6g"][24][3] = Thread(major_diameter_max=23.95, major_diameter_min=23.58, pitch_diameter_max=22,
                             pitch_diameter_min=21.8, minor_diameter_max=20.704, minor_diameter_min=19.955,
                             thread_class="6g", diameter=24, pitch=3)
thread["6g"][24][2.5] = Thread(major_diameter_max=23.96, major_diameter_min=23.62, pitch_diameter_max=22.33,
                               pitch_diameter_min=22.14, minor_diameter_max=21.252, minor_diameter_min=20.604,
                               thread_class="6g", diameter=24, pitch=2.5)
thread["6g"][24][2] = Thread(major_diameter_max=23.96, major_diameter_min=23.68, pitch_diameter_max=22.66,
                             pitch_diameter_min=22.49, minor_diameter_max=21.797, minor_diameter_min=21.261,
                             thread_class="6g", diameter=24, pitch=2)
thread["6g"][24][1.5] = Thread(major_diameter_max=23.97, major_diameter_min=23.73, pitch_diameter_max=22.99,
                               pitch_diameter_min=22.84, minor_diameter_max=22.344, minor_diameter_min=21.92,
                               thread_class="6g", diameter=24, pitch=1.5)
thread["6g"][24][1] = Thread(major_diameter_max=23.97, major_diameter_min=23.79, pitch_diameter_max=23.32,
                             pitch_diameter_min=23.2, minor_diameter_max=22.891, minor_diameter_min=22.583,
                             thread_class="6g", diameter=24, pitch=1)
thread["6g"][24][0.75] = Thread(major_diameter_max=23.98, major_diameter_min=23.84, pitch_diameter_max=23.49,
                                pitch_diameter_min=23.38, minor_diameter_max=23.166, minor_diameter_min=22.917,
                                thread_class="6g", diameter=24, pitch=0.75)
thread["6g"][25][2] = Thread(major_diameter_max=24.96, major_diameter_min=24.68, pitch_diameter_max=23.66,
                             pitch_diameter_min=23.49, minor_diameter_max=22.797, minor_diameter_min=22.261,
                             thread_class="6g", diameter=25, pitch=2)
thread["6g"][25][1.5] = Thread(major_diameter_max=24.97, major_diameter_min=24.73, pitch_diameter_max=23.99,
                               pitch_diameter_min=23.84, minor_diameter_max=23.344, minor_diameter_min=22.92,
                               thread_class="6g", diameter=25, pitch=1.5)
thread["6g"][25][1] = Thread(major_diameter_max=24.97, major_diameter_min=24.79, pitch_diameter_max=24.32,
                             pitch_diameter_min=24.2, minor_diameter_max=23.891, minor_diameter_min=23.583,
                             thread_class="6g", diameter=25, pitch=1)
thread["6g"][26][1.5] = Thread(major_diameter_max=25.97, major_diameter_min=25.73, pitch_diameter_max=24.99,
                               pitch_diameter_min=24.84, minor_diameter_max=24.344, minor_diameter_min=23.92,
                               thread_class="6g", diameter=26, pitch=1.5)
thread["6g"][27][3] = Thread(major_diameter_max=26.95, major_diameter_min=26.58, pitch_diameter_max=25,
                             pitch_diameter_min=24.8, minor_diameter_max=23.704, minor_diameter_min=22.955,
                             thread_class="6g", diameter=27, pitch=3)
thread["6g"][27][2] = Thread(major_diameter_max=26.96, major_diameter_min=26.68, pitch_diameter_max=25.66,
                             pitch_diameter_min=25.49, minor_diameter_max=24.797, minor_diameter_min=24.261,
                             thread_class="6g", diameter=27, pitch=2)
thread["6g"][27][1.5] = Thread(major_diameter_max=26.97, major_diameter_min=26.73, pitch_diameter_max=25.99,
                               pitch_diameter_min=25.84, minor_diameter_max=25.344, minor_diameter_min=24.92,
                               thread_class="6g", diameter=27, pitch=1.5)
thread["6g"][27][1] = Thread(major_diameter_max=26.97, major_diameter_min=26.79, pitch_diameter_max=26.32,
                             pitch_diameter_min=26.2, minor_diameter_max=25.891, minor_diameter_min=25.583,
                             thread_class="6g", diameter=27, pitch=1)
thread["6g"][27][0.75] = Thread(major_diameter_max=26.98, major_diameter_min=26.84, pitch_diameter_max=26.49,
                                pitch_diameter_min=26.38, minor_diameter_max=26.166, minor_diameter_min=25.917,
                                thread_class="6g", diameter=27, pitch=0.75)
thread["6g"][28][2] = Thread(major_diameter_max=27.96, major_diameter_min=27.68, pitch_diameter_max=26.66,
                             pitch_diameter_min=26.49, minor_diameter_max=25.797, minor_diameter_min=25.261,
                             thread_class="6g", diameter=28, pitch=2)
thread["6g"][28][1.5] = Thread(major_diameter_max=27.97, major_diameter_min=27.73, pitch_diameter_max=26.99,
                               pitch_diameter_min=26.84, minor_diameter_max=26.344, minor_diameter_min=25.92,
                               thread_class="6g", diameter=28, pitch=1.5)
thread["6g"][28][1] = Thread(major_diameter_max=27.97, major_diameter_min=27.79, pitch_diameter_max=27.32,
                             pitch_diameter_min=27.2, minor_diameter_max=26.891, minor_diameter_min=26.583,
                             thread_class="6g", diameter=28, pitch=1)
thread["6g"][30][3.5] = Thread(major_diameter_max=29.95, major_diameter_min=29.52, pitch_diameter_max=27.67,
                               pitch_diameter_min=27.46, minor_diameter_max=26.158, minor_diameter_min=25.306,
                               thread_class="6g", diameter=30, pitch=3.5)
thread["6g"][30][3] = Thread(major_diameter_max=29.95, major_diameter_min=29.58, pitch_diameter_max=28,
                             pitch_diameter_min=27.8, minor_diameter_max=26.704, minor_diameter_min=25.955,
                             thread_class="6g", diameter=30, pitch=3)
thread["6g"][30][2.5] = Thread(major_diameter_max=29.96, major_diameter_min=29.62, pitch_diameter_max=28.33,
                               pitch_diameter_min=28.14, minor_diameter_max=27.252, minor_diameter_min=26.604,
                               thread_class="6g", diameter=30, pitch=2.5)
thread["6g"][30][2] = Thread(major_diameter_max=29.96, major_diameter_min=29.68, pitch_diameter_max=28.66,
                             pitch_diameter_min=28.49, minor_diameter_max=27.797, minor_diameter_min=27.261,
                             thread_class="6g", diameter=30, pitch=2)
thread["6g"][30][1.5] = Thread(major_diameter_max=29.97, major_diameter_min=29.73, pitch_diameter_max=28.99,
                               pitch_diameter_min=28.84, minor_diameter_max=28.344, minor_diameter_min=27.92,
                               thread_class="6g", diameter=30, pitch=1.5)
thread["6g"][30][1] = Thread(major_diameter_max=29.97, major_diameter_min=29.79, pitch_diameter_max=29.32,
                             pitch_diameter_min=29.2, minor_diameter_max=28.891, minor_diameter_min=28.583,
                             thread_class="6g", diameter=30, pitch=1)
thread["6g"][30][0.75] = Thread(major_diameter_max=29.98, major_diameter_min=29.84, pitch_diameter_max=29.49,
                                pitch_diameter_min=29.38, minor_diameter_max=29.166, minor_diameter_min=28.917,
                                thread_class="6g", diameter=30, pitch=0.75)
thread["6g"][32][2] = Thread(major_diameter_max=31.96, major_diameter_min=31.68, pitch_diameter_max=30.66,
                             pitch_diameter_min=30.49, minor_diameter_max=29.797, minor_diameter_min=29.261,
                             thread_class="6g", diameter=32, pitch=2)
thread["6g"][32][1.5] = Thread(major_diameter_max=31.97, major_diameter_min=31.73, pitch_diameter_max=30.99,
                               pitch_diameter_min=30.84, minor_diameter_max=30.344, minor_diameter_min=29.92,
                               thread_class="6g", diameter=32, pitch=1.5)
thread["6g"][33][3.5] = Thread(major_diameter_max=32.97, major_diameter_min=32.54, pitch_diameter_max=30.7,
                               pitch_diameter_min=30.48, minor_diameter_max=29.179, minor_diameter_min=28.327,
                               thread_class="6g", diameter=33, pitch=3.5)
thread["6g"][33][3] = Thread(major_diameter_max=32.95, major_diameter_min=32.58, pitch_diameter_max=31,
                             pitch_diameter_min=30.8, minor_diameter_max=29.704, minor_diameter_min=28.955,
                             thread_class="6g", diameter=33, pitch=3)
thread["6g"][33][2] = Thread(major_diameter_max=32.96, major_diameter_min=32.68, pitch_diameter_max=31.66,
                             pitch_diameter_min=31.49, minor_diameter_max=30.797, minor_diameter_min=30.261,
                             thread_class="6g", diameter=33, pitch=2)
thread["6g"][33][1.5] = Thread(major_diameter_max=32.97, major_diameter_min=32.73, pitch_diameter_max=31.99,
                               pitch_diameter_min=31.84, minor_diameter_max=31.344, minor_diameter_min=30.92,
                               thread_class="6g", diameter=33, pitch=1.5)
thread["6g"][33][1] = Thread(major_diameter_max=32.97, major_diameter_min=32.79, pitch_diameter_max=32.32,
                             pitch_diameter_min=32.2, minor_diameter_max=31.891, minor_diameter_min=31.583,
                             thread_class="6g", diameter=33, pitch=1)
thread["6g"][33][0.75] = Thread(major_diameter_max=32.98, major_diameter_min=32.84, pitch_diameter_max=32.49,
                                pitch_diameter_min=32.38, minor_diameter_max=32.166, minor_diameter_min=31.917,
                                thread_class="6g", diameter=33, pitch=0.75)
thread["6g"][35][1.5] = Thread(major_diameter_max=34.97, major_diameter_min=34.73, pitch_diameter_max=33.99,
                               pitch_diameter_min=33.84, minor_diameter_max=33.344, minor_diameter_min=32.92,
                               thread_class="6g", diameter=35, pitch=1.5)
thread["6g"][36][4] = Thread(major_diameter_max=35.94, major_diameter_min=35.47, pitch_diameter_max=33.34,
                             pitch_diameter_min=33.12, minor_diameter_max=31.61, minor_diameter_min=30.654,
                             thread_class="6g", diameter=36, pitch=4)
thread["6g"][36][3] = Thread(major_diameter_max=35.95, major_diameter_min=35.58, pitch_diameter_max=34,
                             pitch_diameter_min=33.8, minor_diameter_max=32.704, minor_diameter_min=31.955,
                             thread_class="6g", diameter=36, pitch=3)
thread["6g"][36][2] = Thread(major_diameter_max=35.96, major_diameter_min=35.68, pitch_diameter_max=34.66,
                             pitch_diameter_min=34.49, minor_diameter_max=33.797, minor_diameter_min=33.261,
                             thread_class="6g", diameter=36, pitch=2)
thread["6g"][36][1.5] = Thread(major_diameter_max=35.97, major_diameter_min=35.73, pitch_diameter_max=34.99,
                               pitch_diameter_min=34.84, minor_diameter_max=34.344, minor_diameter_min=33.92,
                               thread_class="6g", diameter=36, pitch=1.5)
thread["6g"][36][1] = Thread(major_diameter_max=35.97, major_diameter_min=35.79, pitch_diameter_max=35.32,
                             pitch_diameter_min=35.2, minor_diameter_max=34.891, minor_diameter_min=34.583,
                             thread_class="6g", diameter=36, pitch=1)
thread["6g"][38][1.5] = Thread(major_diameter_max=37.97, major_diameter_min=37.73, pitch_diameter_max=36.99,
                               pitch_diameter_min=36.84, minor_diameter_max=36.344, minor_diameter_min=35.92,
                               thread_class="6g", diameter=38, pitch=1.5)
thread["6g"][39][4] = Thread(major_diameter_max=38.94, major_diameter_min=38.47, pitch_diameter_max=36.34,
                             pitch_diameter_min=36.12, minor_diameter_max=34.61, minor_diameter_min=33.654,
                             thread_class="6g", diameter=39, pitch=4)
thread["6g"][39][3] = Thread(major_diameter_max=38.95, major_diameter_min=38.58, pitch_diameter_max=37,
                             pitch_diameter_min=36.8, minor_diameter_max=35.704, minor_diameter_min=34.955,
                             thread_class="6g", diameter=39, pitch=3)
thread["6g"][39][2] = Thread(major_diameter_max=38.96, major_diameter_min=38.68, pitch_diameter_max=37.66,
                             pitch_diameter_min=37.49, minor_diameter_max=36.797, minor_diameter_min=36.261,
                             thread_class="6g", diameter=39, pitch=2)
thread["6g"][39][1.5] = Thread(major_diameter_max=38.97, major_diameter_min=38.73, pitch_diameter_max=37.99,
                               pitch_diameter_min=37.84, minor_diameter_max=37.344, minor_diameter_min=36.92,
                               thread_class="6g", diameter=39, pitch=1.5)
thread["6g"][39][1] = Thread(major_diameter_max=38.97, major_diameter_min=38.79, pitch_diameter_max=38.32,
                             pitch_diameter_min=38.2, minor_diameter_max=37.891, minor_diameter_min=37.583,
                             thread_class="6g", diameter=39, pitch=1)
thread["6g"][40][3] = Thread(major_diameter_max=39.95, major_diameter_min=39.58, pitch_diameter_max=38,
                             pitch_diameter_min=37.8, minor_diameter_max=36.704, minor_diameter_min=35.955,
                             thread_class="6g", diameter=40, pitch=3)
thread["6g"][40][2.5] = Thread(major_diameter_max=39.96, major_diameter_min=39.62, pitch_diameter_max=38.33,
                               pitch_diameter_min=38.14, minor_diameter_max=37.252, minor_diameter_min=36.604,
                               thread_class="6g", diameter=40, pitch=2.5)
thread["6g"][40][2] = Thread(major_diameter_max=39.96, major_diameter_min=39.68, pitch_diameter_max=38.66,
                             pitch_diameter_min=38.49, minor_diameter_max=37.797, minor_diameter_min=37.261,
                             thread_class="6g", diameter=40, pitch=2)
thread["6g"][40][1.5] = Thread(major_diameter_max=39.97, major_diameter_min=39.73, pitch_diameter_max=38.99,
                               pitch_diameter_min=38.84, minor_diameter_max=38.344, minor_diameter_min=37.92,
                               thread_class="6g", diameter=40, pitch=1.5)
thread["6g"][42][4.5] = Thread(major_diameter_max=41.94, major_diameter_min=41.44, pitch_diameter_max=39.01,
                               pitch_diameter_min=38.78, minor_diameter_max=37.066, minor_diameter_min=36.006,
                               thread_class="6g", diameter=42, pitch=4.5)
thread["6g"][42][4] = Thread(major_diameter_max=41.94, major_diameter_min=41.47, pitch_diameter_max=39.34,
                             pitch_diameter_min=39.12, minor_diameter_max=37.61, minor_diameter_min=36.654,
                             thread_class="6g", diameter=42, pitch=4)
thread["6g"][42][3] = Thread(major_diameter_max=41.95, major_diameter_min=41.58, pitch_diameter_max=40,
                             pitch_diameter_min=39.8, minor_diameter_max=38.704, minor_diameter_min=37.955,
                             thread_class="6g", diameter=42, pitch=3)
thread["6g"][42][2] = Thread(major_diameter_max=41.96, major_diameter_min=41.68, pitch_diameter_max=40.66,
                             pitch_diameter_min=40.49, minor_diameter_max=39.797, minor_diameter_min=39.261,
                             thread_class="6g", diameter=42, pitch=2)
thread["6g"][42][1.5] = Thread(major_diameter_max=41.97, major_diameter_min=41.73, pitch_diameter_max=40.99,
                               pitch_diameter_min=40.84, minor_diameter_max=40.344, minor_diameter_min=39.92,
                               thread_class="6g", diameter=42, pitch=1.5)
thread["6g"][42][1] = Thread(major_diameter_max=41.97, major_diameter_min=41.79, pitch_diameter_max=41.32,
                             pitch_diameter_min=41.2, minor_diameter_max=40.891, minor_diameter_min=40.583,
                             thread_class="6g", diameter=42, pitch=1)
thread["6g"][45][4.5] = Thread(major_diameter_max=44.94, major_diameter_min=44.44, pitch_diameter_max=42.01,
                               pitch_diameter_min=41.78, minor_diameter_max=40.066, minor_diameter_min=39.006,
                               thread_class="6g", diameter=45, pitch=4.5)
thread["6g"][45][4] = Thread(major_diameter_max=44.94, major_diameter_min=44.47, pitch_diameter_max=42.34,
                             pitch_diameter_min=42.12, minor_diameter_max=40.61, minor_diameter_min=39.654,
                             thread_class="6g", diameter=45, pitch=4)
thread["6g"][45][3] = Thread(major_diameter_max=44.95, major_diameter_min=44.58, pitch_diameter_max=43,
                             pitch_diameter_min=42.8, minor_diameter_max=41.704, minor_diameter_min=40.955,
                             thread_class="6g", diameter=45, pitch=3)
thread["6g"][45][2] = Thread(major_diameter_max=44.96, major_diameter_min=44.68, pitch_diameter_max=43.66,
                             pitch_diameter_min=43.49, minor_diameter_max=42.797, minor_diameter_min=42.261,
                             thread_class="6g", diameter=45, pitch=2)
thread["6g"][45][1.5] = Thread(major_diameter_max=44.97, major_diameter_min=44.73, pitch_diameter_max=43.99,
                               pitch_diameter_min=43.84, minor_diameter_max=43.344, minor_diameter_min=42.92,
                               thread_class="6g", diameter=45, pitch=1.5)
thread["6g"][45][1] = Thread(major_diameter_max=44.97, major_diameter_min=44.79, pitch_diameter_max=44.32,
                             pitch_diameter_min=44.2, minor_diameter_max=43.891, minor_diameter_min=43.583,
                             thread_class="6g", diameter=45, pitch=1)
thread["6g"][48][5] = Thread(major_diameter_max=47.93, major_diameter_min=47.4, pitch_diameter_max=44.68,
                             pitch_diameter_min=44.43, minor_diameter_max=42.516, minor_diameter_min=41.351,
                             thread_class="6g", diameter=48, pitch=5)
thread["6g"][48][4] = Thread(major_diameter_max=47.94, major_diameter_min=47.47, pitch_diameter_max=45.34,
                             pitch_diameter_min=45.11, minor_diameter_max=43.61, minor_diameter_min=42.642,
                             thread_class="6g", diameter=48, pitch=4)
thread["6g"][48][3] = Thread(major_diameter_max=47.95, major_diameter_min=47.58, pitch_diameter_max=46,
                             pitch_diameter_min=45.79, minor_diameter_max=44.704, minor_diameter_min=43.943,
                             thread_class="6g", diameter=48, pitch=3)
thread["6g"][48][2] = Thread(major_diameter_max=47.96, major_diameter_min=47.68, pitch_diameter_max=46.66,
                             pitch_diameter_min=46.48, minor_diameter_max=45.797, minor_diameter_min=45.251,
                             thread_class="6g", diameter=48, pitch=2)
thread["6g"][48][1.5] = Thread(major_diameter_max=47.97, major_diameter_min=47.73, pitch_diameter_max=46.99,
                               pitch_diameter_min=46.83, minor_diameter_max=46.344, minor_diameter_min=45.91,
                               thread_class="6g", diameter=48, pitch=1.5)
thread["6g"][50][4] = Thread(major_diameter_max=49.94, major_diameter_min=49.47, pitch_diameter_max=47.34,
                             pitch_diameter_min=47.11, minor_diameter_max=45.61, minor_diameter_min=44.642,
                             thread_class="6g", diameter=50, pitch=4)
thread["6g"][50][3] = Thread(major_diameter_max=49.95, major_diameter_min=49.58, pitch_diameter_max=48,
                             pitch_diameter_min=47.79, minor_diameter_max=46.704, minor_diameter_min=45.943,
                             thread_class="6g", diameter=50, pitch=3)
thread["6g"][50][2] = Thread(major_diameter_max=49.96, major_diameter_min=49.68, pitch_diameter_max=48.66,
                             pitch_diameter_min=48.48, minor_diameter_max=47.797, minor_diameter_min=47.251,
                             thread_class="6g", diameter=50, pitch=2)
thread["6g"][50][1.5] = Thread(major_diameter_max=49.97, major_diameter_min=49.73, pitch_diameter_max=48.99,
                               pitch_diameter_min=48.83, minor_diameter_max=48.344, minor_diameter_min=47.91,
                               thread_class="6g", diameter=50, pitch=1.5)
thread["6g"][52][5] = Thread(major_diameter_max=51.93, major_diameter_min=51.4, pitch_diameter_max=48.68,
                             pitch_diameter_min=48.45, minor_diameter_max=46.516, minor_diameter_min=45.365,
                             thread_class="6g", diameter=52, pitch=5)
thread["6g"][52][4] = Thread(major_diameter_max=51.94, major_diameter_min=51.47, pitch_diameter_max=49.34,
                             pitch_diameter_min=49.11, minor_diameter_max=47.61, minor_diameter_min=46.642,
                             thread_class="6g", diameter=52, pitch=4)
thread["6g"][52][3] = Thread(major_diameter_max=51.95, major_diameter_min=51.58, pitch_diameter_max=50,
                             pitch_diameter_min=49.79, minor_diameter_max=48.704, minor_diameter_min=47.943,
                             thread_class="6g", diameter=52, pitch=3)
thread["6g"][52][2] = Thread(major_diameter_max=51.96, major_diameter_min=51.68, pitch_diameter_max=50.66,
                             pitch_diameter_min=50.48, minor_diameter_max=49.797, minor_diameter_min=49.251,
                             thread_class="6g", diameter=52, pitch=2)
thread["6g"][52][1.5] = Thread(major_diameter_max=51.97, major_diameter_min=51.73, pitch_diameter_max=50.99,
                               pitch_diameter_min=50.83, minor_diameter_max=50.344, minor_diameter_min=49.91,
                               thread_class="6g", diameter=52, pitch=1.5)
thread["6g"][55][4] = Thread(major_diameter_max=54.94, major_diameter_min=54.47, pitch_diameter_max=52.34,
                             pitch_diameter_min=52.11, minor_diameter_max=50.61, minor_diameter_min=49.642,
                             thread_class="6g", diameter=55, pitch=4)
thread["6g"][55][3] = Thread(major_diameter_max=54.95, major_diameter_min=54.58, pitch_diameter_max=53,
                             pitch_diameter_min=52.79, minor_diameter_max=51.704, minor_diameter_min=50.943,
                             thread_class="6g", diameter=55, pitch=3)
thread["6g"][55][2] = Thread(major_diameter_max=54.96, major_diameter_min=54.68, pitch_diameter_max=53.66,
                             pitch_diameter_min=53.48, minor_diameter_max=52.797, minor_diameter_min=52.251,
                             thread_class="6g", diameter=55, pitch=2)
thread["6g"][55][1.5] = Thread(major_diameter_max=54.97, major_diameter_min=54.73, pitch_diameter_max=53.99,
                               pitch_diameter_min=53.83, minor_diameter_max=53.344, minor_diameter_min=52.91,
                               thread_class="6g", diameter=55, pitch=1.5)
thread["6g"][56][5.5] = Thread(major_diameter_max=55.93, major_diameter_min=55.37, pitch_diameter_max=52.35,
                               pitch_diameter_min=52.09, minor_diameter_max=49.971, minor_diameter_min=48.7,
                               thread_class="6g", diameter=56, pitch=5.5)
thread["6g"][56][4] = Thread(major_diameter_max=55.94, major_diameter_min=55.47, pitch_diameter_max=53.34,
                             pitch_diameter_min=53.11, minor_diameter_max=51.61, minor_diameter_min=50.642,
                             thread_class="6g", diameter=56, pitch=4)
thread["6g"][56][3] = Thread(major_diameter_max=55.95, major_diameter_min=55.58, pitch_diameter_max=54,
                             pitch_diameter_min=53.79, minor_diameter_max=52.704, minor_diameter_min=51.943,
                             thread_class="6g", diameter=56, pitch=3)
thread["6g"][56][2] = Thread(major_diameter_max=55.96, major_diameter_min=55.68, pitch_diameter_max=54.66,
                             pitch_diameter_min=54.48, minor_diameter_max=53.797, minor_diameter_min=53.251,
                             thread_class="6g", diameter=56, pitch=2)
thread["6g"][56][1.5] = Thread(major_diameter_max=55.97, major_diameter_min=55.73, pitch_diameter_max=54.99,
                               pitch_diameter_min=54.83, minor_diameter_max=54.344, minor_diameter_min=53.91,
                               thread_class="6g", diameter=56, pitch=1.5)
thread["6g"][56][1] = Thread(major_diameter_max=55.97, major_diameter_min=55.79, pitch_diameter_max=55.32,
                             pitch_diameter_min=55.18, minor_diameter_max=54.891, minor_diameter_min=54.568,
                             thread_class="6g", diameter=56, pitch=1)
thread["6g"][58][4] = Thread(major_diameter_max=57.94, major_diameter_min=57.47, pitch_diameter_max=55.34,
                             pitch_diameter_min=55.11, minor_diameter_max=53.61, minor_diameter_min=52.642,
                             thread_class="6g", diameter=58, pitch=4)
thread["6g"][58][3] = Thread(major_diameter_max=57.95, major_diameter_min=57.58, pitch_diameter_max=56,
                             pitch_diameter_min=55.79, minor_diameter_max=54.704, minor_diameter_min=53.943,
                             thread_class="6g", diameter=58, pitch=3)
thread["6g"][58][2] = Thread(major_diameter_max=57.96, major_diameter_min=57.68, pitch_diameter_max=56.66,
                             pitch_diameter_min=56.48, minor_diameter_max=55.797, minor_diameter_min=55.251,
                             thread_class="6g", diameter=58, pitch=2)
thread["6g"][58][1.5] = Thread(major_diameter_max=57.97, major_diameter_min=57.73, pitch_diameter_max=56.99,
                               pitch_diameter_min=56.83, minor_diameter_max=56.344, minor_diameter_min=55.91,
                               thread_class="6g", diameter=58, pitch=1.5)
thread["6g"][60][5.5] = Thread(major_diameter_max=59.93, major_diameter_min=59.37, pitch_diameter_max=56.35,
                               pitch_diameter_min=56.09, minor_diameter_max=53.971, minor_diameter_min=52.7,
                               thread_class="6g", diameter=60, pitch=5.5)
thread["6g"][60][4] = Thread(major_diameter_max=59.94, major_diameter_min=59.47, pitch_diameter_max=57.34,
                             pitch_diameter_min=57.11, minor_diameter_max=55.61, minor_diameter_min=54.642,
                             thread_class="6g", diameter=60, pitch=4)
thread["6g"][60][3] = Thread(major_diameter_max=59.95, major_diameter_min=59.58, pitch_diameter_max=58,
                             pitch_diameter_min=57.79, minor_diameter_max=56.704, minor_diameter_min=55.943,
                             thread_class="6g", diameter=60, pitch=3)
thread["6g"][60][2] = Thread(major_diameter_max=59.96, major_diameter_min=59.68, pitch_diameter_max=58.66,
                             pitch_diameter_min=58.48, minor_diameter_max=57.797, minor_diameter_min=57.251,
                             thread_class="6g", diameter=60, pitch=2)
thread["6g"][60][1.5] = Thread(major_diameter_max=59.97, major_diameter_min=59.73, pitch_diameter_max=58.99,
                               pitch_diameter_min=58.83, minor_diameter_max=58.344, minor_diameter_min=57.91,
                               thread_class="6g", diameter=60, pitch=1.5)
thread["6g"][60][1] = Thread(major_diameter_max=59.97, major_diameter_min=59.79, pitch_diameter_max=59.32,
                             pitch_diameter_min=59.18, minor_diameter_max=58.891, minor_diameter_min=58.568,
                             thread_class="6g", diameter=60, pitch=1)
thread["6g"][62][4] = Thread(major_diameter_max=61.94, major_diameter_min=61.47, pitch_diameter_max=59.34,
                             pitch_diameter_min=59.11, minor_diameter_max=57.61, minor_diameter_min=56.642,
                             thread_class="6g", diameter=62, pitch=4)
thread["6g"][62][3] = Thread(major_diameter_max=61.95, major_diameter_min=61.58, pitch_diameter_max=60,
                             pitch_diameter_min=59.79, minor_diameter_max=58.704, minor_diameter_min=57.943,
                             thread_class="6g", diameter=62, pitch=3)
thread["6g"][62][2] = Thread(major_diameter_max=61.96, major_diameter_min=61.68, pitch_diameter_max=60.66,
                             pitch_diameter_min=60.48, minor_diameter_max=59.797, minor_diameter_min=59.251,
                             thread_class="6g", diameter=62, pitch=2)
thread["6g"][62][1.5] = Thread(major_diameter_max=61.97, major_diameter_min=61.73, pitch_diameter_max=60.99,
                               pitch_diameter_min=60.83, minor_diameter_max=60.344, minor_diameter_min=59.91,
                               thread_class="6g", diameter=62, pitch=1.5)
thread["6g"][63][1.5] = Thread(major_diameter_max=62.97, major_diameter_min=62.73, pitch_diameter_max=61.99,
                               pitch_diameter_min=61.83, minor_diameter_max=61.344, minor_diameter_min=60.91,
                               thread_class="6g", diameter=63, pitch=1.5)
thread["6g"][64][6] = Thread(major_diameter_max=63.92, major_diameter_min=63.32, pitch_diameter_max=60.02,
                             pitch_diameter_min=59.74, minor_diameter_max=57.425, minor_diameter_min=56.047,
                             thread_class="6g", diameter=64, pitch=6)
thread["6g"][64][5.5] = Thread(major_diameter_max=63.93, major_diameter_min=63.37, pitch_diameter_max=60.35,
                               pitch_diameter_min=60.09, minor_diameter_max=57.971, minor_diameter_min=56.7,
                               thread_class="6g", diameter=64, pitch=5.5)
thread["6g"][64][4] = Thread(major_diameter_max=63.94, major_diameter_min=63.47, pitch_diameter_max=61.34,
                             pitch_diameter_min=61.11, minor_diameter_max=59.61, minor_diameter_min=58.642,
                             thread_class="6g", diameter=64, pitch=4)
thread["6g"][64][3] = Thread(major_diameter_max=63.95, major_diameter_min=63.58, pitch_diameter_max=62,
                             pitch_diameter_min=61.79, minor_diameter_max=60.704, minor_diameter_min=59.943,
                             thread_class="6g", diameter=64, pitch=3)
thread["6g"][64][2] = Thread(major_diameter_max=63.96, major_diameter_min=63.68, pitch_diameter_max=62.66,
                             pitch_diameter_min=62.48, minor_diameter_max=61.797, minor_diameter_min=61.251,
                             thread_class="6g", diameter=64, pitch=2)
thread["6g"][64][1.5] = Thread(major_diameter_max=63.97, major_diameter_min=63.73, pitch_diameter_max=62.99,
                               pitch_diameter_min=62.83, minor_diameter_max=62.344, minor_diameter_min=61.91,
                               thread_class="6g", diameter=64, pitch=1.5)
thread["6g"][64][1] = Thread(major_diameter_max=63.97, major_diameter_min=63.79, pitch_diameter_max=63.32,
                             pitch_diameter_min=63.18, minor_diameter_max=62.891, minor_diameter_min=62.568,
                             thread_class="6g", diameter=64, pitch=1)
thread["6g"][65][4] = Thread(major_diameter_max=64.94, major_diameter_min=64.47, pitch_diameter_max=62.34,
                             pitch_diameter_min=62.11, minor_diameter_max=60.61, minor_diameter_min=59.642,
                             thread_class="6g", diameter=65, pitch=4)
thread["6g"][65][3] = Thread(major_diameter_max=64.95, major_diameter_min=64.58, pitch_diameter_max=63,
                             pitch_diameter_min=62.79, minor_diameter_max=61.704, minor_diameter_min=60.943,
                             thread_class="6g", diameter=65, pitch=3)
thread["6g"][65][2] = Thread(major_diameter_max=64.96, major_diameter_min=64.68, pitch_diameter_max=63.66,
                             pitch_diameter_min=63.48, minor_diameter_max=62.797, minor_diameter_min=62.251,
                             thread_class="6g", diameter=65, pitch=2)
thread["6g"][65][1.5] = Thread(major_diameter_max=64.97, major_diameter_min=64.73, pitch_diameter_max=63.99,
                               pitch_diameter_min=63.83, minor_diameter_max=63.344, minor_diameter_min=62.91,
                               thread_class="6g", diameter=65, pitch=1.5)
thread["6g"][68][6] = Thread(major_diameter_max=67.92, major_diameter_min=67.32, pitch_diameter_max=64.02,
                             pitch_diameter_min=63.74, minor_diameter_max=61.425, minor_diameter_min=60.047,
                             thread_class="6g", diameter=68, pitch=6)
thread["6g"][68][4] = Thread(major_diameter_max=67.94, major_diameter_min=67.47, pitch_diameter_max=65.34,
                             pitch_diameter_min=65.11, minor_diameter_max=63.61, minor_diameter_min=62.642,
                             thread_class="6g", diameter=68, pitch=4)
thread["6g"][68][3] = Thread(major_diameter_max=67.95, major_diameter_min=67.58, pitch_diameter_max=66,
                             pitch_diameter_min=65.79, minor_diameter_max=64.704, minor_diameter_min=63.943,
                             thread_class="6g", diameter=68, pitch=3)
thread["6g"][68][2] = Thread(major_diameter_max=67.96, major_diameter_min=67.68, pitch_diameter_max=66.66,
                             pitch_diameter_min=66.48, minor_diameter_max=65.797, minor_diameter_min=65.251,
                             thread_class="6g", diameter=68, pitch=2)
thread["6g"][68][1.5] = Thread(major_diameter_max=67.97, major_diameter_min=67.73, pitch_diameter_max=66.99,
                               pitch_diameter_min=66.83, minor_diameter_max=66.344, minor_diameter_min=65.91,
                               thread_class="6g", diameter=68, pitch=1.5)
thread["6g"][68][1] = Thread(major_diameter_max=67.97, major_diameter_min=67.79, pitch_diameter_max=67.32,
                             pitch_diameter_min=67.18, minor_diameter_max=66.891, minor_diameter_min=66.568,
                             thread_class="6g", diameter=68, pitch=1)
thread["6g"][70][6] = Thread(major_diameter_max=69.92, major_diameter_min=69.32, pitch_diameter_max=66.02,
                             pitch_diameter_min=65.74, minor_diameter_max=63.425, minor_diameter_min=62.047,
                             thread_class="6g", diameter=70, pitch=6)
thread["6g"][70][4] = Thread(major_diameter_max=69.94, major_diameter_min=69.47, pitch_diameter_max=67.34,
                             pitch_diameter_min=67.11, minor_diameter_max=65.61, minor_diameter_min=64.642,
                             thread_class="6g", diameter=70, pitch=4)
thread["6g"][70][3] = Thread(major_diameter_max=69.95, major_diameter_min=69.58, pitch_diameter_max=68,
                             pitch_diameter_min=67.79, minor_diameter_max=66.704, minor_diameter_min=65.943,
                             thread_class="6g", diameter=70, pitch=3)
thread["6g"][70][2] = Thread(major_diameter_max=69.96, major_diameter_min=69.68, pitch_diameter_max=68.66,
                             pitch_diameter_min=68.48, minor_diameter_max=67.797, minor_diameter_min=67.251,
                             thread_class="6g", diameter=70, pitch=2)
thread["6g"][70][1.5] = Thread(major_diameter_max=69.97, major_diameter_min=69.73, pitch_diameter_max=68.99,
                               pitch_diameter_min=68.83, minor_diameter_max=68.344, minor_diameter_min=67.91,
                               thread_class="6g", diameter=70, pitch=1.5)
thread["6g"][72][6] = Thread(major_diameter_max=71.92, major_diameter_min=71.32, pitch_diameter_max=68.02,
                             pitch_diameter_min=67.74, minor_diameter_max=65.425, minor_diameter_min=64.047,
                             thread_class="6g", diameter=72, pitch=6)
thread["6g"][72][4] = Thread(major_diameter_max=71.94, major_diameter_min=71.47, pitch_diameter_max=69.34,
                             pitch_diameter_min=69.11, minor_diameter_max=67.61, minor_diameter_min=66.642,
                             thread_class="6g", diameter=72, pitch=4)
thread["6g"][72][3] = Thread(major_diameter_max=71.95, major_diameter_min=71.58, pitch_diameter_max=70,
                             pitch_diameter_min=69.79, minor_diameter_max=68.704, minor_diameter_min=67.943,
                             thread_class="6g", diameter=72, pitch=3)
thread["6g"][72][2] = Thread(major_diameter_max=71.96, major_diameter_min=71.68, pitch_diameter_max=70.66,
                             pitch_diameter_min=70.48, minor_diameter_max=69.797, minor_diameter_min=69.251,
                             thread_class="6g", diameter=72, pitch=2)
thread["6g"][72][1.5] = Thread(major_diameter_max=71.97, major_diameter_min=71.73, pitch_diameter_max=70.99,
                               pitch_diameter_min=70.83, minor_diameter_max=70.344, minor_diameter_min=69.91,
                               thread_class="6g", diameter=72, pitch=1.5)
thread["6g"][72][1] = Thread(major_diameter_max=71.97, major_diameter_min=71.79, pitch_diameter_max=71.32,
                             pitch_diameter_min=71.18, minor_diameter_max=70.891, minor_diameter_min=70.568,
                             thread_class="6g", diameter=72, pitch=1)
thread["6g"][75][6] = Thread(major_diameter_max=74.92, major_diameter_min=74.32, pitch_diameter_max=71.02,
                             pitch_diameter_min=70.74, minor_diameter_max=68.425, minor_diameter_min=67.047,
                             thread_class="6g", diameter=75, pitch=6)
thread["6g"][75][4] = Thread(major_diameter_max=74.94, major_diameter_min=74.47, pitch_diameter_max=72.34,
                             pitch_diameter_min=72.11, minor_diameter_max=70.61, minor_diameter_min=69.642,
                             thread_class="6g", diameter=75, pitch=4)
thread["6g"][75][3] = Thread(major_diameter_max=74.95, major_diameter_min=74.58, pitch_diameter_max=73,
                             pitch_diameter_min=72.79, minor_diameter_max=71.704, minor_diameter_min=70.943,
                             thread_class="6g", diameter=75, pitch=3)
thread["6g"][75][2] = Thread(major_diameter_max=74.96, major_diameter_min=74.68, pitch_diameter_max=73.66,
                             pitch_diameter_min=73.48, minor_diameter_max=72.797, minor_diameter_min=72.251,
                             thread_class="6g", diameter=75, pitch=2)
thread["6g"][75][1.5] = Thread(major_diameter_max=74.97, major_diameter_min=74.73, pitch_diameter_max=73.99,
                               pitch_diameter_min=73.83, minor_diameter_max=73.344, minor_diameter_min=72.91,
                               thread_class="6g", diameter=75, pitch=1.5)
thread["6g"][76][6] = Thread(major_diameter_max=75.92, major_diameter_min=75.32, pitch_diameter_max=72.02,
                             pitch_diameter_min=71.74, minor_diameter_max=69.425, minor_diameter_min=68.047,
                             thread_class="6g", diameter=76, pitch=6)
thread["6g"][76][4] = Thread(major_diameter_max=75.94, major_diameter_min=75.47, pitch_diameter_max=73.34,
                             pitch_diameter_min=73.11, minor_diameter_max=71.61, minor_diameter_min=70.642,
                             thread_class="6g", diameter=76, pitch=4)
thread["6g"][76][3] = Thread(major_diameter_max=75.95, major_diameter_min=75.58, pitch_diameter_max=74,
                             pitch_diameter_min=73.79, minor_diameter_max=72.704, minor_diameter_min=71.943,
                             thread_class="6g", diameter=76, pitch=3)
thread["6g"][76][2] = Thread(major_diameter_max=75.96, major_diameter_min=75.68, pitch_diameter_max=74.66,
                             pitch_diameter_min=74.48, minor_diameter_max=73.797, minor_diameter_min=73.251,
                             thread_class="6g", diameter=76, pitch=2)
thread["6g"][76][1.5] = Thread(major_diameter_max=75.97, major_diameter_min=75.73, pitch_diameter_max=74.99,
                               pitch_diameter_min=74.83, minor_diameter_max=74.344, minor_diameter_min=73.91,
                               thread_class="6g", diameter=76, pitch=1.5)
thread["6g"][76][1] = Thread(major_diameter_max=75.97, major_diameter_min=75.79, pitch_diameter_max=75.32,
                             pitch_diameter_min=75.18, minor_diameter_max=74.891, minor_diameter_min=74.568,
                             thread_class="6g", diameter=76, pitch=1)
thread["6g"][78][2] = Thread(major_diameter_max=77.96, major_diameter_min=77.68, pitch_diameter_max=76.66,
                             pitch_diameter_min=76.48, minor_diameter_max=75.797, minor_diameter_min=75.251,
                             thread_class="6g", diameter=78, pitch=2)
thread["6g"][80][6] = Thread(major_diameter_max=79.92, major_diameter_min=79.32, pitch_diameter_max=76.02,
                             pitch_diameter_min=75.74, minor_diameter_max=73.425, minor_diameter_min=72.047,
                             thread_class="6g", diameter=80, pitch=6)
thread["6g"][80][4] = Thread(major_diameter_max=79.94, major_diameter_min=79.34, pitch_diameter_max=77.34,
                             pitch_diameter_min=77.11, minor_diameter_max=75.61, minor_diameter_min=74.642,
                             thread_class="6g", diameter=80, pitch=4)
thread["6g"][80][3] = Thread(major_diameter_max=79.95, major_diameter_min=79.58, pitch_diameter_max=78,
                             pitch_diameter_min=77.79, minor_diameter_max=76.704, minor_diameter_min=75.943,
                             thread_class="6g", diameter=80, pitch=3)
thread["6g"][80][2] = Thread(major_diameter_max=79.96, major_diameter_min=79.68, pitch_diameter_max=78.66,
                             pitch_diameter_min=78.48, minor_diameter_max=77.797, minor_diameter_min=77.251,
                             thread_class="6g", diameter=80, pitch=2)
thread["6g"][80][1.5] = Thread(major_diameter_max=79.97, major_diameter_min=79.73, pitch_diameter_max=78.99,
                               pitch_diameter_min=78.83, minor_diameter_max=78.344, minor_diameter_min=77.91,
                               thread_class="6g", diameter=80, pitch=1.5)
thread["6g"][80][1] = Thread(major_diameter_max=79.97, major_diameter_min=79.79, pitch_diameter_max=79.32,
                             pitch_diameter_min=79.18, minor_diameter_max=78.891, minor_diameter_min=78.568,
                             thread_class="6g", diameter=80, pitch=1)
thread["6g"][82][2] = Thread(major_diameter_max=81.96, major_diameter_min=81.68, pitch_diameter_max=80.66,
                             pitch_diameter_min=80.48, minor_diameter_max=79.797, minor_diameter_min=79.251,
                             thread_class="6g", diameter=82, pitch=2)
thread["6g"][85][6] = Thread(major_diameter_max=84.92, major_diameter_min=84.32, pitch_diameter_max=81.02,
                             pitch_diameter_min=80.74, minor_diameter_max=78.425, minor_diameter_min=77.047,
                             thread_class="6g", diameter=85, pitch=6)
thread["6g"][85][4] = Thread(major_diameter_max=84.94, major_diameter_min=84.47, pitch_diameter_max=82.34,
                             pitch_diameter_min=82.11, minor_diameter_max=80.61, minor_diameter_min=79.642,
                             thread_class="6g", diameter=85, pitch=4)
thread["6g"][85][3] = Thread(major_diameter_max=84.95, major_diameter_min=84.58, pitch_diameter_max=83,
                             pitch_diameter_min=82.79, minor_diameter_max=81.704, minor_diameter_min=80.943,
                             thread_class="6g", diameter=85, pitch=3)
thread["6g"][85][2] = Thread(major_diameter_max=84.96, major_diameter_min=84.68, pitch_diameter_max=83.66,
                             pitch_diameter_min=83.48, minor_diameter_max=82.797, minor_diameter_min=82.251,
                             thread_class="6g", diameter=85, pitch=2)
thread["6g"][85][1.5] = Thread(major_diameter_max=84.97, major_diameter_min=84.73, pitch_diameter_max=83.99,
                               pitch_diameter_min=83.83, minor_diameter_max=83.344, minor_diameter_min=82.91,
                               thread_class="6g", diameter=85, pitch=1.5)
thread["6g"][90][6] = Thread(major_diameter_max=89.92, major_diameter_min=89.32, pitch_diameter_max=86.02,
                             pitch_diameter_min=85.74, minor_diameter_max=83.425, minor_diameter_min=82.047,
                             thread_class="6g", diameter=90, pitch=6)
thread["6g"][90][4] = Thread(major_diameter_max=89.94, major_diameter_min=89.47, pitch_diameter_max=87.34,
                             pitch_diameter_min=87.11, minor_diameter_max=85.61, minor_diameter_min=84.642,
                             thread_class="6g", diameter=90, pitch=4)
thread["6g"][90][3] = Thread(major_diameter_max=89.95, major_diameter_min=89.58, pitch_diameter_max=88,
                             pitch_diameter_min=87.79, minor_diameter_max=86.704, minor_diameter_min=85.943,
                             thread_class="6g", diameter=90, pitch=3)
thread["6g"][90][2] = Thread(major_diameter_max=89.96, major_diameter_min=89.68, pitch_diameter_max=88.66,
                             pitch_diameter_min=88.48, minor_diameter_max=87.797, minor_diameter_min=87.251,
                             thread_class="6g", diameter=90, pitch=2)
thread["6g"][90][1.5] = Thread(major_diameter_max=89.97, major_diameter_min=89.73, pitch_diameter_max=88.99,
                               pitch_diameter_min=88.83, minor_diameter_max=88.344, minor_diameter_min=87.91,
                               thread_class="6g", diameter=90, pitch=1.5)
thread["6g"][95][6] = Thread(major_diameter_max=94.92, major_diameter_min=94.32, pitch_diameter_max=91.02,
                             pitch_diameter_min=90.72, minor_diameter_max=88.425, minor_diameter_min=87.027,
                             thread_class="6g", diameter=95, pitch=6)
thread["6g"][95][4] = Thread(major_diameter_max=94.94, major_diameter_min=94.47, pitch_diameter_max=92.34,
                             pitch_diameter_min=92.09, minor_diameter_max=90.61, minor_diameter_min=89.628,
                             thread_class="6g", diameter=95, pitch=4)
thread["6g"][95][3] = Thread(major_diameter_max=94.95, major_diameter_min=94.58, pitch_diameter_max=93,
                             pitch_diameter_min=92.78, minor_diameter_max=91.704, minor_diameter_min=90.931,
                             thread_class="6g", diameter=95, pitch=3)
thread["6g"][95][2] = Thread(major_diameter_max=94.96, major_diameter_min=94.68, pitch_diameter_max=93.66,
                             pitch_diameter_min=93.47, minor_diameter_max=92.797, minor_diameter_min=92.241,
                             thread_class="6g", diameter=95, pitch=2)
thread["6g"][95][1.5] = Thread(major_diameter_max=94.97, major_diameter_min=94.73, pitch_diameter_max=93.99,
                               pitch_diameter_min=93.81, minor_diameter_max=93.344, minor_diameter_min=92.89,
                               thread_class="6g", diameter=95, pitch=1.5)
thread["6g"][100][6] = Thread(major_diameter_max=99.92, major_diameter_min=99.32, pitch_diameter_max=96.02,
                              pitch_diameter_min=95.72, minor_diameter_max=93.425, minor_diameter_min=92.027,
                              thread_class="6g", diameter=100, pitch=6)
thread["6g"][100][4] = Thread(major_diameter_max=99.94, major_diameter_min=99.47, pitch_diameter_max=97.34,
                              pitch_diameter_min=97.09, minor_diameter_max=95.61, minor_diameter_min=94.628,
                              thread_class="6g", diameter=100, pitch=4)
thread["6g"][100][3] = Thread(major_diameter_max=99.95, major_diameter_min=99.58, pitch_diameter_max=98,
                              pitch_diameter_min=97.78, minor_diameter_max=96.704, minor_diameter_min=95.931,
                              thread_class="6g", diameter=100, pitch=3)
thread["6g"][100][2] = Thread(major_diameter_max=99.96, major_diameter_min=99.68, pitch_diameter_max=98.66,
                              pitch_diameter_min=98.47, minor_diameter_max=97.797, minor_diameter_min=97.241,
                              thread_class="6g", diameter=100, pitch=2)
thread["6g"][100][1.5] = Thread(major_diameter_max=99.97, major_diameter_min=99.73, pitch_diameter_max=98.99,
                                pitch_diameter_min=98.81, minor_diameter_max=98.344, minor_diameter_min=97.89,
                                thread_class="6g", diameter=100, pitch=1.5)
thread["6g"][105][6] = Thread(major_diameter_max=104.9, major_diameter_min=104.3, pitch_diameter_max=101,
                              pitch_diameter_min=100.7, minor_diameter_max=98.425, minor_diameter_min=97.027,
                              thread_class="6g", diameter=105, pitch=6)
thread["6g"][105][4] = Thread(major_diameter_max=104.9, major_diameter_min=104.5, pitch_diameter_max=102.3,
                              pitch_diameter_min=102.1, minor_diameter_max=100.61, minor_diameter_min=99.628,
                              thread_class="6g", diameter=105, pitch=4)
thread["6g"][105][3] = Thread(major_diameter_max=105, major_diameter_min=104.6, pitch_diameter_max=103,
                              pitch_diameter_min=102.8, minor_diameter_max=101.7, minor_diameter_min=100.93,
                              thread_class="6g", diameter=105, pitch=3)
thread["6g"][105][2] = Thread(major_diameter_max=105, major_diameter_min=104.7, pitch_diameter_max=103.7,
                              pitch_diameter_min=103.5, minor_diameter_max=102.8, minor_diameter_min=102.24,
                              thread_class="6g", diameter=105, pitch=2)
thread["6g"][105][1.5] = Thread(major_diameter_max=105, major_diameter_min=104.7, pitch_diameter_max=104,
                                pitch_diameter_min=103.8, minor_diameter_max=103.34, minor_diameter_min=102.89,
                                thread_class="6g", diameter=105, pitch=1.5)
thread["6g"][110][6] = Thread(major_diameter_max=109.9, major_diameter_min=109.3, pitch_diameter_max=106,
                              pitch_diameter_min=105.7, minor_diameter_max=103.43, minor_diameter_min=102.03,
                              thread_class="6g", diameter=110, pitch=6)
thread["6g"][110][4] = Thread(major_diameter_max=109.9, major_diameter_min=109.5, pitch_diameter_max=107.3,
                              pitch_diameter_min=107.1, minor_diameter_max=105.61, minor_diameter_min=104.63,
                              thread_class="6g", diameter=110, pitch=4)
thread["6g"][110][3] = Thread(major_diameter_max=110, major_diameter_min=109.6, pitch_diameter_max=108,
                              pitch_diameter_min=107.8, minor_diameter_max=106.7, minor_diameter_min=105.93,
                              thread_class="6g", diameter=110, pitch=3)
thread["6g"][110][2] = Thread(major_diameter_max=110, major_diameter_min=109.7, pitch_diameter_max=108.7,
                              pitch_diameter_min=108.5, minor_diameter_max=107.8, minor_diameter_min=107.24,
                              thread_class="6g", diameter=110, pitch=2)
thread["6g"][110][1.5] = Thread(major_diameter_max=110, major_diameter_min=109.7, pitch_diameter_max=109,
                                pitch_diameter_min=108.8, minor_diameter_max=108.34, minor_diameter_min=107.89,
                                thread_class="6g", diameter=110, pitch=1.5)
thread["6g"][115][6] = Thread(major_diameter_max=114.9, major_diameter_min=114.3, pitch_diameter_max=111,
                              pitch_diameter_min=110.7, minor_diameter_max=108.43, minor_diameter_min=107.03,
                              thread_class="6g", diameter=115, pitch=6)
thread["6g"][115][4] = Thread(major_diameter_max=114.9, major_diameter_min=114.5, pitch_diameter_max=112.3,
                              pitch_diameter_min=112.1, minor_diameter_max=110.61, minor_diameter_min=109.63,
                              thread_class="6g", diameter=115, pitch=4)
thread["6g"][115][3] = Thread(major_diameter_max=115, major_diameter_min=114.6, pitch_diameter_max=113,
                              pitch_diameter_min=112.8, minor_diameter_max=111.7, minor_diameter_min=110.93,
                              thread_class="6g", diameter=115, pitch=3)
thread["6g"][115][2] = Thread(major_diameter_max=115, major_diameter_min=114.7, pitch_diameter_max=113.7,
                              pitch_diameter_min=113.5, minor_diameter_max=112.8, minor_diameter_min=112.24,
                              thread_class="6g", diameter=115, pitch=2)
thread["6g"][115][1.5] = Thread(major_diameter_max=115, major_diameter_min=114.7, pitch_diameter_max=114,
                                pitch_diameter_min=113.8, minor_diameter_max=113.34, minor_diameter_min=112.89,
                                thread_class="6g", diameter=115, pitch=1.5)
thread["6g"][120][6] = Thread(major_diameter_max=119.9, major_diameter_min=119.3, pitch_diameter_max=116,
                              pitch_diameter_min=115.7, minor_diameter_max=113.43, minor_diameter_min=112.03,
                              thread_class="6g", diameter=120, pitch=6)
thread["6g"][120][4] = Thread(major_diameter_max=119.9, major_diameter_min=119.5, pitch_diameter_max=117.3,
                              pitch_diameter_min=117.1, minor_diameter_max=115.61, minor_diameter_min=114.63,
                              thread_class="6g", diameter=120, pitch=4)
thread["6g"][120][3] = Thread(major_diameter_max=120, major_diameter_min=119.6, pitch_diameter_max=118,
                              pitch_diameter_min=117.8, minor_diameter_max=116.7, minor_diameter_min=115.93,
                              thread_class="6g", diameter=120, pitch=3)
thread["6g"][120][2] = Thread(major_diameter_max=120, major_diameter_min=119.7, pitch_diameter_max=118.7,
                              pitch_diameter_min=118.5, minor_diameter_max=117.8, minor_diameter_min=117.24,
                              thread_class="6g", diameter=120, pitch=2)
thread["6g"][120][1.5] = Thread(major_diameter_max=120, major_diameter_min=119.7, pitch_diameter_max=119,
                                pitch_diameter_min=118.8, minor_diameter_max=118.34, minor_diameter_min=117.89,
                                thread_class="6g", diameter=120, pitch=1.5)
thread["6g"][125][8] = Thread(major_diameter_max=124.9, major_diameter_min=124.2, pitch_diameter_max=119.7,
                              pitch_diameter_min=119.4, minor_diameter_max=116.24, minor_diameter_min=114.44,
                              thread_class="6g", diameter=125, pitch=8)
thread["6g"][125][6] = Thread(major_diameter_max=124.9, major_diameter_min=124.3, pitch_diameter_max=121,
                              pitch_diameter_min=120.7, minor_diameter_max=118.43, minor_diameter_min=117.03,
                              thread_class="6g", diameter=125, pitch=6)
thread["6g"][125][4] = Thread(major_diameter_max=124.9, major_diameter_min=124.5, pitch_diameter_max=122.3,
                              pitch_diameter_min=122.1, minor_diameter_max=120.61, minor_diameter_min=119.63,
                              thread_class="6g", diameter=125, pitch=4)
thread["6g"][125][3] = Thread(major_diameter_max=125, major_diameter_min=124.6, pitch_diameter_max=123,
                              pitch_diameter_min=122.8, minor_diameter_max=121.7, minor_diameter_min=120.93,
                              thread_class="6g", diameter=125, pitch=3)
thread["6g"][125][2] = Thread(major_diameter_max=125, major_diameter_min=124.7, pitch_diameter_max=123.7,
                              pitch_diameter_min=123.5, minor_diameter_max=122.8, minor_diameter_min=122.24,
                              thread_class="6g", diameter=125, pitch=2)
thread["6g"][125][1.5] = Thread(major_diameter_max=125, major_diameter_min=124.7, pitch_diameter_max=124,
                                pitch_diameter_min=123.8, minor_diameter_max=123.34, minor_diameter_min=122.89,
                                thread_class="6g", diameter=125, pitch=1.5)
thread["6g"][130][8] = Thread(major_diameter_max=129.9, major_diameter_min=129.2, pitch_diameter_max=124.7,
                              pitch_diameter_min=124.4, minor_diameter_max=121.24, minor_diameter_min=119.44,
                              thread_class="6g", diameter=130, pitch=8)
thread["6g"][130][6] = Thread(major_diameter_max=129.9, major_diameter_min=129.3, pitch_diameter_max=126,
                              pitch_diameter_min=125.7, minor_diameter_max=123.43, minor_diameter_min=122.03,
                              thread_class="6g", diameter=130, pitch=6)
thread["6g"][130][4] = Thread(major_diameter_max=129.9, major_diameter_min=129.5, pitch_diameter_max=127.3,
                              pitch_diameter_min=127.1, minor_diameter_max=125.61, minor_diameter_min=124.63,
                              thread_class="6g", diameter=130, pitch=4)
thread["6g"][130][3] = Thread(major_diameter_max=130, major_diameter_min=129.6, pitch_diameter_max=128,
                              pitch_diameter_min=127.8, minor_diameter_max=126.7, minor_diameter_min=125.93,
                              thread_class="6g", diameter=130, pitch=3)
thread["6g"][130][2] = Thread(major_diameter_max=130, major_diameter_min=129.7, pitch_diameter_max=128.7,
                              pitch_diameter_min=128.5, minor_diameter_max=127.8, minor_diameter_min=127.24,
                              thread_class="6g", diameter=130, pitch=2)
thread["6g"][130][1.5] = Thread(major_diameter_max=130, major_diameter_min=129.7, pitch_diameter_max=129,
                                pitch_diameter_min=128.8, minor_diameter_max=128.34, minor_diameter_min=127.89,
                                thread_class="6g", diameter=130, pitch=1.5)
thread["6g"][135][6] = Thread(major_diameter_max=134.9, major_diameter_min=134.3, pitch_diameter_max=131,
                              pitch_diameter_min=130.7, minor_diameter_max=128.43, minor_diameter_min=127.03,
                              thread_class="6g", diameter=135, pitch=6)
thread["6g"][135][4] = Thread(major_diameter_max=134.9, major_diameter_min=134.5, pitch_diameter_max=132.3,
                              pitch_diameter_min=132.1, minor_diameter_max=130.61, minor_diameter_min=129.63,
                              thread_class="6g", diameter=135, pitch=4)
thread["6g"][135][3] = Thread(major_diameter_max=135, major_diameter_min=134.6, pitch_diameter_max=133,
                              pitch_diameter_min=132.8, minor_diameter_max=131.7, minor_diameter_min=130.93,
                              thread_class="6g", diameter=135, pitch=3)
thread["6g"][135][2] = Thread(major_diameter_max=135, major_diameter_min=134.7, pitch_diameter_max=133.7,
                              pitch_diameter_min=133.5, minor_diameter_max=132.8, minor_diameter_min=132.24,
                              thread_class="6g", diameter=135, pitch=2)
thread["6g"][135][1.5] = Thread(major_diameter_max=135, major_diameter_min=134.7, pitch_diameter_max=134,
                                pitch_diameter_min=133.8, minor_diameter_max=133.34, minor_diameter_min=132.89,
                                thread_class="6g", diameter=135, pitch=1.5)
thread["6g"][140][8] = Thread(major_diameter_max=139.9, major_diameter_min=139.2, pitch_diameter_max=134.7,
                              pitch_diameter_min=134.4, minor_diameter_max=131.24, minor_diameter_min=129.44,
                              thread_class="6g", diameter=140, pitch=8)
thread["6g"][140][6] = Thread(major_diameter_max=139.9, major_diameter_min=139.3, pitch_diameter_max=136,
                              pitch_diameter_min=135.7, minor_diameter_max=133.43, minor_diameter_min=132.03,
                              thread_class="6g", diameter=140, pitch=6)
thread["6g"][140][4] = Thread(major_diameter_max=139.9, major_diameter_min=139.5, pitch_diameter_max=137.3,
                              pitch_diameter_min=137.1, minor_diameter_max=135.61, minor_diameter_min=134.63,
                              thread_class="6g", diameter=140, pitch=4)
thread["6g"][140][3] = Thread(major_diameter_max=140, major_diameter_min=139.6, pitch_diameter_max=138,
                              pitch_diameter_min=137.8, minor_diameter_max=136.7, minor_diameter_min=135.93,
                              thread_class="6g", diameter=140, pitch=3)
thread["6g"][140][2] = Thread(major_diameter_max=140, major_diameter_min=139.7, pitch_diameter_max=138.7,
                              pitch_diameter_min=138.5, minor_diameter_max=137.8, minor_diameter_min=137.24,
                              thread_class="6g", diameter=140, pitch=2)
thread["6g"][140][1.5] = Thread(major_diameter_max=140, major_diameter_min=139.7, pitch_diameter_max=139,
                                pitch_diameter_min=138.8, minor_diameter_max=138.34, minor_diameter_min=137.89,
                                thread_class="6g", diameter=140, pitch=1.5)
thread["6g"][145][6] = Thread(major_diameter_max=144.9, major_diameter_min=144.3, pitch_diameter_max=141,
                              pitch_diameter_min=140.7, minor_diameter_max=138.43, minor_diameter_min=137.03,
                              thread_class="6g", diameter=145, pitch=6)
thread["6g"][145][4] = Thread(major_diameter_max=144.9, major_diameter_min=144.5, pitch_diameter_max=142.3,
                              pitch_diameter_min=142.1, minor_diameter_max=140.61, minor_diameter_min=139.63,
                              thread_class="6g", diameter=145, pitch=4)
thread["6g"][145][3] = Thread(major_diameter_max=145, major_diameter_min=144.6, pitch_diameter_max=143,
                              pitch_diameter_min=142.8, minor_diameter_max=141.7, minor_diameter_min=140.93,
                              thread_class="6g", diameter=145, pitch=3)
thread["6g"][145][2] = Thread(major_diameter_max=145, major_diameter_min=144.7, pitch_diameter_max=143.7,
                              pitch_diameter_min=143.5, minor_diameter_max=142.8, minor_diameter_min=142.24,
                              thread_class="6g", diameter=145, pitch=2)
thread["6g"][145][1.5] = Thread(major_diameter_max=145, major_diameter_min=144.7, pitch_diameter_max=144,
                                pitch_diameter_min=143.8, minor_diameter_max=143.34, minor_diameter_min=142.89,
                                thread_class="6g", diameter=145, pitch=1.5)
thread["6g"][150][8] = Thread(major_diameter_max=149.9, major_diameter_min=149.2, pitch_diameter_max=144.7,
                              pitch_diameter_min=144.4, minor_diameter_max=141.24, minor_diameter_min=139.44,
                              thread_class="6g", diameter=150, pitch=8)
thread["6g"][150][6] = Thread(major_diameter_max=149.9, major_diameter_min=149.3, pitch_diameter_max=146,
                              pitch_diameter_min=145.7, minor_diameter_max=143.43, minor_diameter_min=142.03,
                              thread_class="6g", diameter=150, pitch=6)
thread["6g"][150][4] = Thread(major_diameter_max=149.9, major_diameter_min=149.5, pitch_diameter_max=147.3,
                              pitch_diameter_min=147.1, minor_diameter_max=145.61, minor_diameter_min=144.63,
                              thread_class="6g", diameter=150, pitch=4)
thread["6g"][150][3] = Thread(major_diameter_max=150, major_diameter_min=149.6, pitch_diameter_max=148,
                              pitch_diameter_min=147.8, minor_diameter_max=146.7, minor_diameter_min=145.93,
                              thread_class="6g", diameter=150, pitch=3)
thread["6g"][150][2] = Thread(major_diameter_max=150, major_diameter_min=149.7, pitch_diameter_max=148.7,
                              pitch_diameter_min=148.5, minor_diameter_max=147.8, minor_diameter_min=147.24,
                              thread_class="6g", diameter=150, pitch=2)
thread["6g"][150][1.5] = Thread(major_diameter_max=150, major_diameter_min=149.7, pitch_diameter_max=149,
                                pitch_diameter_min=148.8, minor_diameter_max=148.34, minor_diameter_min=147.89,
                                thread_class="6g", diameter=150, pitch=1.5)
thread["6g"][155][6] = Thread(major_diameter_max=154.9, major_diameter_min=154.3, pitch_diameter_max=151,
                              pitch_diameter_min=150.7, minor_diameter_max=148.43, minor_diameter_min=147.03,
                              thread_class="6g", diameter=155, pitch=6)
thread["6g"][155][4] = Thread(major_diameter_max=154.9, major_diameter_min=154.5, pitch_diameter_max=152.3,
                              pitch_diameter_min=152.1, minor_diameter_max=150.61, minor_diameter_min=149.63,
                              thread_class="6g", diameter=155, pitch=4)
thread["6g"][155][3] = Thread(major_diameter_max=155, major_diameter_min=154.6, pitch_diameter_max=153,
                              pitch_diameter_min=152.8, minor_diameter_max=151.7, minor_diameter_min=150.93,
                              thread_class="6g", diameter=155, pitch=3)
thread["6g"][155][2] = Thread(major_diameter_max=155, major_diameter_min=154.7, pitch_diameter_max=153.7,
                              pitch_diameter_min=153.5, minor_diameter_max=152.8, minor_diameter_min=152.24,
                              thread_class="6g", diameter=155, pitch=2)
thread["6g"][160][8] = Thread(major_diameter_max=159.9, major_diameter_min=159.2, pitch_diameter_max=154.7,
                              pitch_diameter_min=154.4, minor_diameter_max=151.24, minor_diameter_min=149.44,
                              thread_class="6g", diameter=160, pitch=8)
thread["6g"][160][6] = Thread(major_diameter_max=159.9, major_diameter_min=159.3, pitch_diameter_max=156,
                              pitch_diameter_min=155.7, minor_diameter_max=153.43, minor_diameter_min=152.03,
                              thread_class="6g", diameter=160, pitch=6)
thread["6g"][160][4] = Thread(major_diameter_max=159.9, major_diameter_min=159.5, pitch_diameter_max=157.3,
                              pitch_diameter_min=157.1, minor_diameter_max=155.61, minor_diameter_min=154.63,
                              thread_class="6g", diameter=160, pitch=4)
thread["6g"][160][3] = Thread(major_diameter_max=160, major_diameter_min=159.6, pitch_diameter_max=158,
                              pitch_diameter_min=157.8, minor_diameter_max=156.7, minor_diameter_min=155.93,
                              thread_class="6g", diameter=160, pitch=3)
thread["6g"][160][2] = Thread(major_diameter_max=160, major_diameter_min=159.7, pitch_diameter_max=158.7,
                              pitch_diameter_min=158.5, minor_diameter_max=157.8, minor_diameter_min=157.24,
                              thread_class="6g", diameter=160, pitch=2)
thread["6g"][165][6] = Thread(major_diameter_max=164.9, major_diameter_min=164.3, pitch_diameter_max=161,
                              pitch_diameter_min=160.7, minor_diameter_max=158.43, minor_diameter_min=157.03,
                              thread_class="6g", diameter=165, pitch=6)
thread["6g"][165][4] = Thread(major_diameter_max=164.9, major_diameter_min=164.5, pitch_diameter_max=162.3,
                              pitch_diameter_min=162.1, minor_diameter_max=160.61, minor_diameter_min=159.63,
                              thread_class="6g", diameter=165, pitch=4)
thread["6g"][165][3] = Thread(major_diameter_max=165, major_diameter_min=164.6, pitch_diameter_max=163,
                              pitch_diameter_min=162.8, minor_diameter_max=161.7, minor_diameter_min=160.93,
                              thread_class="6g", diameter=165, pitch=3)
thread["6g"][165][2] = Thread(major_diameter_max=165, major_diameter_min=164.7, pitch_diameter_max=163.7,
                              pitch_diameter_min=163.5, minor_diameter_max=162.8, minor_diameter_min=162.24,
                              thread_class="6g", diameter=165, pitch=2)
thread["6g"][170][8] = Thread(major_diameter_max=169.9, major_diameter_min=169.2, pitch_diameter_max=164.7,
                              pitch_diameter_min=164.4, minor_diameter_max=161.24, minor_diameter_min=159.44,
                              thread_class="6g", diameter=170, pitch=8)
thread["6g"][170][6] = Thread(major_diameter_max=169.9, major_diameter_min=169.3, pitch_diameter_max=166,
                              pitch_diameter_min=165.7, minor_diameter_max=163.43, minor_diameter_min=162.03,
                              thread_class="6g", diameter=170, pitch=6)
thread["6g"][170][4] = Thread(major_diameter_max=169.9, major_diameter_min=169.5, pitch_diameter_max=167.3,
                              pitch_diameter_min=167.1, minor_diameter_max=165.61, minor_diameter_min=164.63,
                              thread_class="6g", diameter=170, pitch=4)
thread["6g"][170][3] = Thread(major_diameter_max=170, major_diameter_min=169.6, pitch_diameter_max=168,
                              pitch_diameter_min=167.8, minor_diameter_max=166.7, minor_diameter_min=165.93,
                              thread_class="6g", diameter=170, pitch=3)
thread["6g"][170][2] = Thread(major_diameter_max=170, major_diameter_min=169.7, pitch_diameter_max=168.7,
                              pitch_diameter_min=168.5, minor_diameter_max=167.8, minor_diameter_min=167.24,
                              thread_class="6g", diameter=170, pitch=2)
thread["6g"][175][6] = Thread(major_diameter_max=174.9, major_diameter_min=174.3, pitch_diameter_max=171,
                              pitch_diameter_min=170.7, minor_diameter_max=168.43, minor_diameter_min=167.03,
                              thread_class="6g", diameter=175, pitch=6)
thread["6g"][175][4] = Thread(major_diameter_max=174.9, major_diameter_min=174.5, pitch_diameter_max=172.3,
                              pitch_diameter_min=172.1, minor_diameter_max=170.61, minor_diameter_min=169.63,
                              thread_class="6g", diameter=175, pitch=4)
thread["6g"][175][3] = Thread(major_diameter_max=175, major_diameter_min=174.6, pitch_diameter_max=173,
                              pitch_diameter_min=172.8, minor_diameter_max=171.7, minor_diameter_min=170.93,
                              thread_class="6g", diameter=175, pitch=3)
thread["6g"][175][2] = Thread(major_diameter_max=175, major_diameter_min=174.7, pitch_diameter_max=173.7,
                              pitch_diameter_min=173.5, minor_diameter_max=172.8, minor_diameter_min=172.24,
                              thread_class="6g", diameter=175, pitch=2)
thread["6g"][180][8] = Thread(major_diameter_max=179.9, major_diameter_min=179.2, pitch_diameter_max=174.7,
                              pitch_diameter_min=174.4, minor_diameter_max=171.24, minor_diameter_min=169.44,
                              thread_class="6g", diameter=180, pitch=8)
thread["6g"][180][6] = Thread(major_diameter_max=179.9, major_diameter_min=179.3, pitch_diameter_max=176,
                              pitch_diameter_min=175.7, minor_diameter_max=173.43, minor_diameter_min=172.03,
                              thread_class="6g", diameter=180, pitch=6)
thread["6g"][180][4] = Thread(major_diameter_max=179.9, major_diameter_min=179.5, pitch_diameter_max=177.3,
                              pitch_diameter_min=177.1, minor_diameter_max=175.61, minor_diameter_min=174.63,
                              thread_class="6g", diameter=180, pitch=4)
thread["6g"][180][3] = Thread(major_diameter_max=180, major_diameter_min=179.6, pitch_diameter_max=178,
                              pitch_diameter_min=177.8, minor_diameter_max=176.7, minor_diameter_min=175.93,
                              thread_class="6g", diameter=180, pitch=3)
thread["6g"][180][2] = Thread(major_diameter_max=180, major_diameter_min=179.7, pitch_diameter_max=178.7,
                              pitch_diameter_min=178.5, minor_diameter_max=177.8, minor_diameter_min=177.24,
                              thread_class="6g", diameter=180, pitch=2)
thread["6g"][185][6] = Thread(major_diameter_max=184.9, major_diameter_min=184.3, pitch_diameter_max=181,
                              pitch_diameter_min=180.7, minor_diameter_max=178.43, minor_diameter_min=177.01,
                              thread_class="6g", diameter=185, pitch=6)
thread["6g"][185][4] = Thread(major_diameter_max=184.9, major_diameter_min=184.5, pitch_diameter_max=182.3,
                              pitch_diameter_min=182.1, minor_diameter_max=180.61, minor_diameter_min=179.6,
                              thread_class="6g", diameter=185, pitch=4)
thread["6g"][185][3] = Thread(major_diameter_max=185, major_diameter_min=184.6, pitch_diameter_max=183,
                              pitch_diameter_min=182.8, minor_diameter_max=181.7, minor_diameter_min=180.91,
                              thread_class="6g", diameter=185, pitch=3)
thread["6g"][185][2] = Thread(major_diameter_max=185, major_diameter_min=184.7, pitch_diameter_max=183.7,
                              pitch_diameter_min=183.5, minor_diameter_max=182.8, minor_diameter_min=182.22,
                              thread_class="6g", diameter=185, pitch=2)
thread["6g"][190][8] = Thread(major_diameter_max=189.9, major_diameter_min=189.2, pitch_diameter_max=184.7,
                              pitch_diameter_min=184.3, minor_diameter_max=181.24, minor_diameter_min=179.42,
                              thread_class="6g", diameter=190, pitch=8)
thread["6g"][190][6] = Thread(major_diameter_max=189.9, major_diameter_min=189.3, pitch_diameter_max=186,
                              pitch_diameter_min=185.7, minor_diameter_max=183.43, minor_diameter_min=182.01,
                              thread_class="6g", diameter=190, pitch=6)
thread["6g"][190][4] = Thread(major_diameter_max=189.9, major_diameter_min=189.5, pitch_diameter_max=187.3,
                              pitch_diameter_min=187.1, minor_diameter_max=185.61, minor_diameter_min=184.6,
                              thread_class="6g", diameter=190, pitch=4)
thread["6g"][190][3] = Thread(major_diameter_max=190, major_diameter_min=189.6, pitch_diameter_max=188,
                              pitch_diameter_min=187.8, minor_diameter_max=186.7, minor_diameter_min=185.91,
                              thread_class="6g", diameter=190, pitch=3)
thread["6g"][190][2] = Thread(major_diameter_max=190, major_diameter_min=189.7, pitch_diameter_max=188.7,
                              pitch_diameter_min=188.5, minor_diameter_max=187.8, minor_diameter_min=187.22,
                              thread_class="6g", diameter=190, pitch=2)
thread["6g"][195][6] = Thread(major_diameter_max=194.9, major_diameter_min=194.3, pitch_diameter_max=191,
                              pitch_diameter_min=190.7, minor_diameter_max=188.43, minor_diameter_min=187.01,
                              thread_class="6g", diameter=195, pitch=6)
thread["6g"][195][4] = Thread(major_diameter_max=194.9, major_diameter_min=194.5, pitch_diameter_max=192.3,
                              pitch_diameter_min=192.1, minor_diameter_max=190.61, minor_diameter_min=189.6,
                              thread_class="6g", diameter=195, pitch=4)
thread["6g"][195][3] = Thread(major_diameter_max=195, major_diameter_min=194.6, pitch_diameter_max=193,
                              pitch_diameter_min=192.8, minor_diameter_max=191.7, minor_diameter_min=190.91,
                              thread_class="6g", diameter=195, pitch=3)
thread["6g"][195][2] = Thread(major_diameter_max=195, major_diameter_min=194.7, pitch_diameter_max=193.7,
                              pitch_diameter_min=193.5, minor_diameter_max=192.8, minor_diameter_min=192.22,
                              thread_class="6g", diameter=195, pitch=2)
thread["6g"][200][8] = Thread(major_diameter_max=199.9, major_diameter_min=199.2, pitch_diameter_max=194.7,
                              pitch_diameter_min=194.3, minor_diameter_max=191.24, minor_diameter_min=189.42,
                              thread_class="6g", diameter=200, pitch=8)
thread["6g"][200][6] = Thread(major_diameter_max=199.9, major_diameter_min=199.3, pitch_diameter_max=196,
                              pitch_diameter_min=195.7, minor_diameter_max=193.43, minor_diameter_min=192.01,
                              thread_class="6g", diameter=200, pitch=6)
thread["6g"][200][4] = Thread(major_diameter_max=199.9, major_diameter_min=199.5, pitch_diameter_max=197.3,
                              pitch_diameter_min=197.1, minor_diameter_max=195.61, minor_diameter_min=194.6,
                              thread_class="6g", diameter=200, pitch=4)
thread["6g"][200][3] = Thread(major_diameter_max=200, major_diameter_min=199.6, pitch_diameter_max=198,
                              pitch_diameter_min=197.8, minor_diameter_max=196.7, minor_diameter_min=195.91,
                              thread_class="6g", diameter=200, pitch=3)
thread["6g"][200][2] = Thread(major_diameter_max=200, major_diameter_min=199.7, pitch_diameter_max=198.7,
                              pitch_diameter_min=198.5, minor_diameter_max=197.8, minor_diameter_min=197.22,
                              thread_class="6g", diameter=200, pitch=2)
thread["6g"][205][6] = Thread(major_diameter_max=204.9, major_diameter_min=204.3, pitch_diameter_max=201,
                              pitch_diameter_min=200.7, minor_diameter_max=198.43, minor_diameter_min=197.01,
                              thread_class="6g", diameter=205, pitch=6)
thread["6g"][205][4] = Thread(major_diameter_max=204.9, major_diameter_min=204.5, pitch_diameter_max=202.3,
                              pitch_diameter_min=202.1, minor_diameter_max=200.61, minor_diameter_min=199.6,
                              thread_class="6g", diameter=205, pitch=4)
thread["6g"][205][3] = Thread(major_diameter_max=205, major_diameter_min=204.6, pitch_diameter_max=203,
                              pitch_diameter_min=202.8, minor_diameter_max=201.7, minor_diameter_min=200.91,
                              thread_class="6g", diameter=205, pitch=3)
thread["6g"][205][2] = Thread(major_diameter_max=205, major_diameter_min=204.7, pitch_diameter_max=203.7,
                              pitch_diameter_min=203.5, minor_diameter_max=202.8, minor_diameter_min=202.22,
                              thread_class="6g", diameter=205, pitch=2)
thread["6g"][210][8] = Thread(major_diameter_max=209.9, major_diameter_min=209.2, pitch_diameter_max=204.7,
                              pitch_diameter_min=204.3, minor_diameter_max=201.24, minor_diameter_min=199.42,
                              thread_class="6g", diameter=210, pitch=8)
thread["6g"][210][6] = Thread(major_diameter_max=209.9, major_diameter_min=209.3, pitch_diameter_max=206,
                              pitch_diameter_min=205.7, minor_diameter_max=203.43, minor_diameter_min=202.01,
                              thread_class="6g", diameter=210, pitch=6)
thread["6g"][210][4] = Thread(major_diameter_max=209.9, major_diameter_min=209.5, pitch_diameter_max=207.3,
                              pitch_diameter_min=207.1, minor_diameter_max=205.61, minor_diameter_min=204.6,
                              thread_class="6g", diameter=210, pitch=4)
thread["6g"][210][3] = Thread(major_diameter_max=210, major_diameter_min=209.6, pitch_diameter_max=208,
                              pitch_diameter_min=207.8, minor_diameter_max=206.7, minor_diameter_min=205.91,
                              thread_class="6g", diameter=210, pitch=3)
thread["6g"][210][2] = Thread(major_diameter_max=210, major_diameter_min=209.7, pitch_diameter_max=208.7,
                              pitch_diameter_min=208.5, minor_diameter_max=207.8, minor_diameter_min=207.22,
                              thread_class="6g", diameter=210, pitch=2)
thread["6g"][215][6] = Thread(major_diameter_max=214.9, major_diameter_min=214.3, pitch_diameter_max=211,
                              pitch_diameter_min=210.7, minor_diameter_max=208.43, minor_diameter_min=207.01,
                              thread_class="6g", diameter=215, pitch=6)
thread["6g"][215][4] = Thread(major_diameter_max=214.9, major_diameter_min=214.5, pitch_diameter_max=212.3,
                              pitch_diameter_min=212.1, minor_diameter_max=210.61, minor_diameter_min=209.6,
                              thread_class="6g", diameter=215, pitch=4)
thread["6g"][215][3] = Thread(major_diameter_max=215, major_diameter_min=214.6, pitch_diameter_max=213,
                              pitch_diameter_min=212.8, minor_diameter_max=211.7, minor_diameter_min=210.91,
                              thread_class="6g", diameter=215, pitch=3)
thread["6g"][220][8] = Thread(major_diameter_max=219.9, major_diameter_min=219.2, pitch_diameter_max=214.7,
                              pitch_diameter_min=214.3, minor_diameter_max=211.24, minor_diameter_min=209.42,
                              thread_class="6g", diameter=220, pitch=8)
thread["6g"][220][6] = Thread(major_diameter_max=219.9, major_diameter_min=219.3, pitch_diameter_max=216,
                              pitch_diameter_min=215.7, minor_diameter_max=213.43, minor_diameter_min=212.01,
                              thread_class="6g", diameter=220, pitch=6)
thread["6g"][220][4] = Thread(major_diameter_max=219.9, major_diameter_min=219.5, pitch_diameter_max=217.3,
                              pitch_diameter_min=217.1, minor_diameter_max=215.61, minor_diameter_min=214.6,
                              thread_class="6g", diameter=220, pitch=4)
thread["6g"][220][3] = Thread(major_diameter_max=220, major_diameter_min=219.6, pitch_diameter_max=218,
                              pitch_diameter_min=217.8, minor_diameter_max=216.7, minor_diameter_min=215.91,
                              thread_class="6g", diameter=220, pitch=3)
thread["6g"][220][2] = Thread(major_diameter_max=220, major_diameter_min=219.7, pitch_diameter_max=218.7,
                              pitch_diameter_min=218.5, minor_diameter_max=217.8, minor_diameter_min=217.22,
                              thread_class="6g", diameter=220, pitch=2)
thread["6g"][225][6] = Thread(major_diameter_max=224.9, major_diameter_min=224.5, pitch_diameter_max=221,
                              pitch_diameter_min=220.7, minor_diameter_max=218.43, minor_diameter_min=217.01,
                              thread_class="6g", diameter=225, pitch=6)
thread["6g"][225][4] = Thread(major_diameter_max=224.9, major_diameter_min=224.5, pitch_diameter_max=222.3,
                              pitch_diameter_min=222.1, minor_diameter_max=220.61, minor_diameter_min=219.6,
                              thread_class="6g", diameter=225, pitch=4)
thread["6g"][225][3] = Thread(major_diameter_max=225, major_diameter_min=224.6, pitch_diameter_max=223,
                              pitch_diameter_min=222.8, minor_diameter_max=221.7, minor_diameter_min=220.91,
                              thread_class="6g", diameter=225, pitch=3)
thread["6g"][225][2] = Thread(major_diameter_max=225, major_diameter_min=224.7, pitch_diameter_max=223.7,
                              pitch_diameter_min=223.5, minor_diameter_max=222.8, minor_diameter_min=222.22,
                              thread_class="6g", diameter=225, pitch=2)
thread["6g"][230][6] = Thread(major_diameter_max=229.9, major_diameter_min=229.3, pitch_diameter_max=226,
                              pitch_diameter_min=225.7, minor_diameter_max=223.43, minor_diameter_min=222.01,
                              thread_class="6g", diameter=230, pitch=6)
thread["6g"][230][4] = Thread(major_diameter_max=229.9, major_diameter_min=229.5, pitch_diameter_max=227.3,
                              pitch_diameter_min=227.1, minor_diameter_max=225.61, minor_diameter_min=224.6,
                              thread_class="6g", diameter=230, pitch=4)
thread["6g"][230][3] = Thread(major_diameter_max=230, major_diameter_min=229.6, pitch_diameter_max=228,
                              pitch_diameter_min=227.8, minor_diameter_max=226.7, minor_diameter_min=225.91,
                              thread_class="6g", diameter=230, pitch=3)
thread["6g"][230][2] = Thread(major_diameter_max=230, major_diameter_min=229.7, pitch_diameter_max=228.7,
                              pitch_diameter_min=228.5, minor_diameter_max=227.8, minor_diameter_min=227.22,
                              thread_class="6g", diameter=230, pitch=2)
thread["6g"][235][6] = Thread(major_diameter_max=234.9, major_diameter_min=234.3, pitch_diameter_max=231,
                              pitch_diameter_min=230.7, minor_diameter_max=228.43, minor_diameter_min=226.97,
                              thread_class="6g", diameter=235, pitch=6)
thread["6g"][235][4] = Thread(major_diameter_max=234.9, major_diameter_min=234.5, pitch_diameter_max=232.3,
                              pitch_diameter_min=232.1, minor_diameter_max=230.61, minor_diameter_min=229.6,
                              thread_class="6g", diameter=235, pitch=4)
thread["6g"][235][3] = Thread(major_diameter_max=235, major_diameter_min=234.6, pitch_diameter_max=233,
                              pitch_diameter_min=232.8, minor_diameter_max=231.7, minor_diameter_min=230.91,
                              thread_class="6g", diameter=235, pitch=3)
thread["6g"][240][8] = Thread(major_diameter_max=239.9, major_diameter_min=239.2, pitch_diameter_max=234.7,
                              pitch_diameter_min=234.3, minor_diameter_max=231.24, minor_diameter_min=229.42,
                              thread_class="6g", diameter=240, pitch=8)
thread["6g"][240][6] = Thread(major_diameter_max=239.9, major_diameter_min=239.3, pitch_diameter_max=236,
                              pitch_diameter_min=235.7, minor_diameter_max=233.43, minor_diameter_min=232.01,
                              thread_class="6g", diameter=240, pitch=6)
thread["6g"][240][4] = Thread(major_diameter_max=239.9, major_diameter_min=239.5, pitch_diameter_max=237.3,
                              pitch_diameter_min=237.1, minor_diameter_max=235.61, minor_diameter_min=234.6,
                              thread_class="6g", diameter=240, pitch=4)
thread["6g"][240][3] = Thread(major_diameter_max=240, major_diameter_min=239.6, pitch_diameter_max=238,
                              pitch_diameter_min=237.8, minor_diameter_max=236.7, minor_diameter_min=235.91,
                              thread_class="6g", diameter=240, pitch=3)
thread["6g"][240][2] = Thread(major_diameter_max=240, major_diameter_min=239.7, pitch_diameter_max=238.7,
                              pitch_diameter_min=238.5, minor_diameter_max=237.8, minor_diameter_min=237.22,
                              thread_class="6g", diameter=240, pitch=2)
thread["6g"][245][6] = Thread(major_diameter_max=244.9, major_diameter_min=244.3, pitch_diameter_max=241,
                              pitch_diameter_min=240.7, minor_diameter_max=238.43, minor_diameter_min=237.01,
                              thread_class="6g", diameter=245, pitch=6)
thread["6g"][245][4] = Thread(major_diameter_max=244.9, major_diameter_min=244.5, pitch_diameter_max=242.3,
                              pitch_diameter_min=242.1, minor_diameter_max=240.61, minor_diameter_min=239.6,
                              thread_class="6g", diameter=245, pitch=4)
thread["6g"][245][3] = Thread(major_diameter_max=245, major_diameter_min=244.6, pitch_diameter_max=243,
                              pitch_diameter_min=242.8, minor_diameter_max=241.7, minor_diameter_min=240.91,
                              thread_class="6g", diameter=245, pitch=3)
thread["6g"][245][2] = Thread(major_diameter_max=245, major_diameter_min=244.7, pitch_diameter_max=243.7,
                              pitch_diameter_min=243.5, minor_diameter_max=242.8, minor_diameter_min=242.22,
                              thread_class="6g", diameter=245, pitch=2)
thread["6g"][250][8] = Thread(major_diameter_max=249.9, major_diameter_min=249.2, pitch_diameter_max=244.7,
                              pitch_diameter_min=244.3, minor_diameter_max=241.24, minor_diameter_min=239.42,
                              thread_class="6g", diameter=250, pitch=8)
thread["6g"][250][6] = Thread(major_diameter_max=249.9, major_diameter_min=249.3, pitch_diameter_max=246,
                              pitch_diameter_min=245.7, minor_diameter_max=243.43, minor_diameter_min=242.01,
                              thread_class="6g", diameter=250, pitch=6)
thread["6g"][250][4] = Thread(major_diameter_max=249.9, major_diameter_min=249.5, pitch_diameter_max=247.3,
                              pitch_diameter_min=247.1, minor_diameter_max=245.61, minor_diameter_min=244.6,
                              thread_class="6g", diameter=250, pitch=4)
thread["6g"][250][3] = Thread(major_diameter_max=250, major_diameter_min=249.6, pitch_diameter_max=248,
                              pitch_diameter_min=247.8, minor_diameter_max=246.7, minor_diameter_min=245.91,
                              thread_class="6g", diameter=250, pitch=3)
thread["6g"][250][2] = Thread(major_diameter_max=250, major_diameter_min=249.7, pitch_diameter_max=248.7,
                              pitch_diameter_min=248.5, minor_diameter_max=247.8, minor_diameter_min=247.22,
                              thread_class="6g", diameter=250, pitch=2)
thread["6g"][255][6] = Thread(major_diameter_max=254.9, major_diameter_min=254.3, pitch_diameter_max=251,
                              pitch_diameter_min=250.7, minor_diameter_max=248.43, minor_diameter_min=246.97,
                              thread_class="6g", diameter=255, pitch=6)
thread["6g"][255][4] = Thread(major_diameter_max=254.9, major_diameter_min=254.5, pitch_diameter_max=252.3,
                              pitch_diameter_min=252.1, minor_diameter_max=250.61, minor_diameter_min=249.6,
                              thread_class="6g", diameter=255, pitch=4)
thread["6g"][255][3] = Thread(major_diameter_max=255, major_diameter_min=254.6, pitch_diameter_max=253,
                              pitch_diameter_min=252.8, minor_diameter_max=251.7, minor_diameter_min=250.91,
                              thread_class="6g", diameter=255, pitch=3)
thread["6g"][260][8] = Thread(major_diameter_max=259.9, major_diameter_min=259.2, pitch_diameter_max=254.7,
                              pitch_diameter_min=254.3, minor_diameter_max=251.24, minor_diameter_min=249.42,
                              thread_class="6g", diameter=260, pitch=8)
thread["6g"][260][6] = Thread(major_diameter_max=259.9, major_diameter_min=259.3, pitch_diameter_max=256,
                              pitch_diameter_min=255.7, minor_diameter_max=253.43, minor_diameter_min=252.01,
                              thread_class="6g", diameter=260, pitch=6)
thread["6g"][260][4] = Thread(major_diameter_max=259.9, major_diameter_min=259.5, pitch_diameter_max=257.3,
                              pitch_diameter_min=257.1, minor_diameter_max=255.61, minor_diameter_min=254.6,
                              thread_class="6g", diameter=260, pitch=4)
thread["6g"][260][3] = Thread(major_diameter_max=260, major_diameter_min=259.6, pitch_diameter_max=258,
                              pitch_diameter_min=257.8, minor_diameter_max=256.7, minor_diameter_min=255.91,
                              thread_class="6g", diameter=260, pitch=3)
thread["6g"][265][6] = Thread(major_diameter_max=264.9, major_diameter_min=264.3, pitch_diameter_max=261,
                              pitch_diameter_min=260.7, minor_diameter_max=258.43, minor_diameter_min=257.01,
                              thread_class="6g", diameter=265, pitch=6)
thread["6g"][265][4] = Thread(major_diameter_max=264.9, major_diameter_min=264.5, pitch_diameter_max=262.3,
                              pitch_diameter_min=262.1, minor_diameter_max=260.61, minor_diameter_min=259.6,
                              thread_class="6g", diameter=265, pitch=4)
thread["6g"][265][3] = Thread(major_diameter_max=265, major_diameter_min=264.6, pitch_diameter_max=263,
                              pitch_diameter_min=262.8, minor_diameter_max=261.7, minor_diameter_min=260.91,
                              thread_class="6g", diameter=265, pitch=3)
thread["6g"][270][6] = Thread(major_diameter_max=269.9, major_diameter_min=269.3, pitch_diameter_max=266,
                              pitch_diameter_min=265.7, minor_diameter_max=263.43, minor_diameter_min=262.01,
                              thread_class="6g", diameter=270, pitch=6)
thread["6g"][270][4] = Thread(major_diameter_max=269.9, major_diameter_min=269.5, pitch_diameter_max=267.3,
                              pitch_diameter_min=267.1, minor_diameter_max=265.61, minor_diameter_min=264.6,
                              thread_class="6g", diameter=270, pitch=4)
thread["6g"][270][3] = Thread(major_diameter_max=270, major_diameter_min=269.6, pitch_diameter_max=268,
                              pitch_diameter_min=267.8, minor_diameter_max=266.7, minor_diameter_min=265.91,
                              thread_class="6g", diameter=270, pitch=3)
thread["6g"][275][6] = Thread(major_diameter_max=274.9, major_diameter_min=274.3, pitch_diameter_max=271,
                              pitch_diameter_min=270.7, minor_diameter_max=268.43, minor_diameter_min=267.01,
                              thread_class="6g", diameter=275, pitch=6)
thread["6g"][275][4] = Thread(major_diameter_max=274.9, major_diameter_min=274.5, pitch_diameter_max=272.3,
                              pitch_diameter_min=272.1, minor_diameter_max=270.61, minor_diameter_min=269.6,
                              thread_class="6g", diameter=275, pitch=4)
thread["6g"][275][3] = Thread(major_diameter_max=275, major_diameter_min=274.6, pitch_diameter_max=273,
                              pitch_diameter_min=272.8, minor_diameter_max=271.7, minor_diameter_min=270.91,
                              thread_class="6g", diameter=275, pitch=3)
thread["6g"][280][8] = Thread(major_diameter_max=279.9, major_diameter_min=279.2, pitch_diameter_max=274.7,
                              pitch_diameter_min=274.3, minor_diameter_max=271.24, minor_diameter_min=269.42,
                              thread_class="6g", diameter=280, pitch=8)
thread["6g"][280][6] = Thread(major_diameter_max=279.9, major_diameter_min=279.3, pitch_diameter_max=276,
                              pitch_diameter_min=275.7, minor_diameter_max=273.43, minor_diameter_min=272.01,
                              thread_class="6g", diameter=280, pitch=6)
thread["6g"][280][4] = Thread(major_diameter_max=279.9, major_diameter_min=279.5, pitch_diameter_max=277.3,
                              pitch_diameter_min=277.1, minor_diameter_max=275.61, minor_diameter_min=274.6,
                              thread_class="6g", diameter=280, pitch=4)
thread["6g"][280][3] = Thread(major_diameter_max=280, major_diameter_min=279.6, pitch_diameter_max=278,
                              pitch_diameter_min=277.8, minor_diameter_max=276.7, minor_diameter_min=275.91,
                              thread_class="6g", diameter=280, pitch=3)
thread["6g"][285][6] = Thread(major_diameter_max=284.9, major_diameter_min=284.3, pitch_diameter_max=281,
                              pitch_diameter_min=280.7, minor_diameter_max=278.43, minor_diameter_min=277.01,
                              thread_class="6g", diameter=285, pitch=6)
thread["6g"][285][4] = Thread(major_diameter_max=284.9, major_diameter_min=284.5, pitch_diameter_max=282.3,
                              pitch_diameter_min=282.1, minor_diameter_max=280.61, minor_diameter_min=279.6,
                              thread_class="6g", diameter=285, pitch=4)
thread["6g"][285][3] = Thread(major_diameter_max=285, major_diameter_min=284.6, pitch_diameter_max=283,
                              pitch_diameter_min=282.8, minor_diameter_max=281.7, minor_diameter_min=280.91,
                              thread_class="6g", diameter=285, pitch=3)
thread["6g"][290][6] = Thread(major_diameter_max=289.9, major_diameter_min=289.3, pitch_diameter_max=286,
                              pitch_diameter_min=285.7, minor_diameter_max=283.43, minor_diameter_min=282.01,
                              thread_class="6g", diameter=290, pitch=6)
thread["6g"][290][4] = Thread(major_diameter_max=289.9, major_diameter_min=289.5, pitch_diameter_max=287.3,
                              pitch_diameter_min=287.1, minor_diameter_max=285.61, minor_diameter_min=284.6,
                              thread_class="6g", diameter=290, pitch=4)
thread["6g"][290][3] = Thread(major_diameter_max=290, major_diameter_min=289.6, pitch_diameter_max=288,
                              pitch_diameter_min=287.8, minor_diameter_max=286.7, minor_diameter_min=285.91,
                              thread_class="6g", diameter=290, pitch=3)
thread["6g"][295][6] = Thread(major_diameter_max=294.9, major_diameter_min=294.3, pitch_diameter_max=291,
                              pitch_diameter_min=290.7, minor_diameter_max=288.43, minor_diameter_min=287.01,
                              thread_class="6g", diameter=295, pitch=6)
thread["6g"][295][4] = Thread(major_diameter_max=294.9, major_diameter_min=294.5, pitch_diameter_max=292.3,
                              pitch_diameter_min=292.1, minor_diameter_max=290.61, minor_diameter_min=289.6,
                              thread_class="6g", diameter=295, pitch=4)
thread["6g"][295][3] = Thread(major_diameter_max=295, major_diameter_min=294.6, pitch_diameter_max=293,
                              pitch_diameter_min=292.8, minor_diameter_max=291.7, minor_diameter_min=290.91,
                              thread_class="6g", diameter=295, pitch=3)
thread["6g"][300][8] = Thread(major_diameter_max=299.9, major_diameter_min=299.2, pitch_diameter_max=294.7,
                              pitch_diameter_min=294.3, minor_diameter_max=291.24, minor_diameter_min=289.42,
                              thread_class="6g", diameter=300, pitch=8)
thread["6g"][300][6] = Thread(major_diameter_max=299.9, major_diameter_min=299.3, pitch_diameter_max=296,
                              pitch_diameter_min=295.7, minor_diameter_max=293.43, minor_diameter_min=292.01,
                              thread_class="6g", diameter=300, pitch=6)
thread["6g"][300][4] = Thread(major_diameter_max=299.9, major_diameter_min=299.5, pitch_diameter_max=297.3,
                              pitch_diameter_min=297.1, minor_diameter_max=295.61, minor_diameter_min=294.6,
                              thread_class="6g", diameter=300, pitch=4)
thread["6g"][300][3] = Thread(major_diameter_max=300, major_diameter_min=299.6, pitch_diameter_max=298,
                              pitch_diameter_min=297.8, minor_diameter_max=296.7, minor_diameter_min=295.91,
                              thread_class="6g", diameter=300, pitch=3)
thread["6g"][310][6] = Thread(major_diameter_max=309.9, major_diameter_min=309.3, pitch_diameter_max=306,
                              pitch_diameter_min=305.7, minor_diameter_max=303.43, minor_diameter_min=302.01,
                              thread_class="6g", diameter=310, pitch=6)
thread["6g"][310][4] = Thread(major_diameter_max=309.9, major_diameter_min=309.5, pitch_diameter_max=307.3,
                              pitch_diameter_min=307.1, minor_diameter_max=305.61, minor_diameter_min=304.6,
                              thread_class="6g", diameter=310, pitch=4)
thread["6g"][320][6] = Thread(major_diameter_max=319.9, major_diameter_min=319.3, pitch_diameter_max=316,
                              pitch_diameter_min=315.7, minor_diameter_max=313.43, minor_diameter_min=312.01,
                              thread_class="6g", diameter=320, pitch=6)
thread["6g"][320][4] = Thread(major_diameter_max=319.9, major_diameter_min=319.5, pitch_diameter_max=317.3,
                              pitch_diameter_min=317.1, minor_diameter_max=315.61, minor_diameter_min=314.6,
                              thread_class="6g", diameter=320, pitch=4)
thread["6g"][330][6] = Thread(major_diameter_max=329.9, major_diameter_min=329.3, pitch_diameter_max=326,
                              pitch_diameter_min=325.7, minor_diameter_max=323.43, minor_diameter_min=322.01,
                              thread_class="6g", diameter=330, pitch=6)
thread["6g"][330][4] = Thread(major_diameter_max=329.9, major_diameter_min=329.5, pitch_diameter_max=327.3,
                              pitch_diameter_min=327.1, minor_diameter_max=325.61, minor_diameter_min=324.6,
                              thread_class="6g", diameter=330, pitch=4)
thread["6g"][340][6] = Thread(major_diameter_max=339.9, major_diameter_min=339.3, pitch_diameter_max=336,
                              pitch_diameter_min=335.7, minor_diameter_max=333.43, minor_diameter_min=332.01,
                              thread_class="6g", diameter=340, pitch=6)
thread["6g"][340][4] = Thread(major_diameter_max=339.9, major_diameter_min=339.5, pitch_diameter_max=337.3,
                              pitch_diameter_min=337.1, minor_diameter_max=335.61, minor_diameter_min=334.6,
                              thread_class="6g", diameter=340, pitch=4)
thread["6g"][350][6] = Thread(major_diameter_max=349.9, major_diameter_min=349.3, pitch_diameter_max=346,
                              pitch_diameter_min=345.7, minor_diameter_max=343.43, minor_diameter_min=342.01,
                              thread_class="6g", diameter=350, pitch=6)
thread["6g"][350][4] = Thread(major_diameter_max=349.9, major_diameter_min=349.5, pitch_diameter_max=347.3,
                              pitch_diameter_min=347.1, minor_diameter_max=345.61, minor_diameter_min=344.6,
                              thread_class="6g", diameter=350, pitch=4)
thread["6g"][360][6] = Thread(major_diameter_max=359.9, major_diameter_min=359.3, pitch_diameter_max=356,
                              pitch_diameter_min=355.7, minor_diameter_max=353.43, minor_diameter_min=351.97,
                              thread_class="6g", diameter=360, pitch=6)
thread["6g"][360][4] = Thread(major_diameter_max=359.9, major_diameter_min=359.5, pitch_diameter_max=357.3,
                              pitch_diameter_min=357, minor_diameter_max=355.61, minor_diameter_min=354.58,
                              thread_class="6g", diameter=360, pitch=4)
thread["6g"][370][6] = Thread(major_diameter_max=369.9, major_diameter_min=369.3, pitch_diameter_max=366,
                              pitch_diameter_min=365.7, minor_diameter_max=363.43, minor_diameter_min=361.97,
                              thread_class="6g", diameter=370, pitch=6)
thread["6g"][370][4] = Thread(major_diameter_max=369.9, major_diameter_min=369.5, pitch_diameter_max=367.3,
                              pitch_diameter_min=367, minor_diameter_max=365.61, minor_diameter_min=364.58,
                              thread_class="6g", diameter=370, pitch=4)
thread["6g"][380][6] = Thread(major_diameter_max=379.9, major_diameter_min=379.3, pitch_diameter_max=376,
                              pitch_diameter_min=375.7, minor_diameter_max=373.43, minor_diameter_min=371.97,
                              thread_class="6g", diameter=380, pitch=6)
thread["6g"][380][4] = Thread(major_diameter_max=379.9, major_diameter_min=379.5, pitch_diameter_max=377.3,
                              pitch_diameter_min=377, minor_diameter_max=375.61, minor_diameter_min=374.58,
                              thread_class="6g", diameter=380, pitch=4)
thread["6g"][390][6] = Thread(major_diameter_max=389.9, major_diameter_min=389.3, pitch_diameter_max=386,
                              pitch_diameter_min=385.7, minor_diameter_max=383.43, minor_diameter_min=381.97,
                              thread_class="6g", diameter=390, pitch=6)
thread["6g"][390][4] = Thread(major_diameter_max=389.9, major_diameter_min=389.5, pitch_diameter_max=387.3,
                              pitch_diameter_min=387, minor_diameter_max=385.61, minor_diameter_min=384.58,
                              thread_class="6g", diameter=390, pitch=4)
thread["6g"][400][6] = Thread(major_diameter_max=399.9, major_diameter_min=399.3, pitch_diameter_max=396,
                              pitch_diameter_min=395.7, minor_diameter_max=393.43, minor_diameter_min=391.97,
                              thread_class="6g", diameter=400, pitch=6)
thread["6g"][400][4] = Thread(major_diameter_max=399.9, major_diameter_min=399.5, pitch_diameter_max=397.3,
                              pitch_diameter_min=397, minor_diameter_max=395.61, minor_diameter_min=394.58,
                              thread_class="6g", diameter=400, pitch=4)
thread["6g"][410][6] = Thread(major_diameter_max=409.9, major_diameter_min=409.3, pitch_diameter_max=406,
                              pitch_diameter_min=405.7, minor_diameter_max=403.43, minor_diameter_min=401.97,
                              thread_class="6g", diameter=410, pitch=6)
thread["6g"][420][6] = Thread(major_diameter_max=419.9, major_diameter_min=419.3, pitch_diameter_max=416,
                              pitch_diameter_min=415.7, minor_diameter_max=413.43, minor_diameter_min=411.97,
                              thread_class="6g", diameter=420, pitch=6)
thread["6g"][430][6] = Thread(major_diameter_max=429.9, major_diameter_min=429.3, pitch_diameter_max=426,
                              pitch_diameter_min=425.7, minor_diameter_max=423.43, minor_diameter_min=421.97,
                              thread_class="6g", diameter=430, pitch=6)
thread["6g"][440][6] = Thread(major_diameter_max=439.9, major_diameter_min=439.3, pitch_diameter_max=436,
                              pitch_diameter_min=435.7, minor_diameter_max=433.43, minor_diameter_min=431.97,
                              thread_class="6g", diameter=440, pitch=6)
thread["6g"][450][6] = Thread(major_diameter_max=449.9, major_diameter_min=449.3, pitch_diameter_max=446,
                              pitch_diameter_min=445.7, minor_diameter_max=443.43, minor_diameter_min=441.97,
                              thread_class="6g", diameter=450, pitch=6)
thread["6g"][460][6] = Thread(major_diameter_max=459.9, major_diameter_min=459.3, pitch_diameter_max=456,
                              pitch_diameter_min=455.7, minor_diameter_max=453.43, minor_diameter_min=451.97,
                              thread_class="6g", diameter=460, pitch=6)
thread["6g"][470][6] = Thread(major_diameter_max=469.9, major_diameter_min=469.3, pitch_diameter_max=466,
                              pitch_diameter_min=465.7, minor_diameter_max=463.43, minor_diameter_min=461.97,
                              thread_class="6g", diameter=470, pitch=6)
thread["6g"][480][6] = Thread(major_diameter_max=479.9, major_diameter_min=479.3, pitch_diameter_max=476,
                              pitch_diameter_min=475.7, minor_diameter_max=473.43, minor_diameter_min=471.97,
                              thread_class="6g", diameter=480, pitch=6)
thread["6g"][490][6] = Thread(major_diameter_max=489.9, major_diameter_min=489.3, pitch_diameter_max=486,
                              pitch_diameter_min=485.7, minor_diameter_max=483.43, minor_diameter_min=481.97,
                              thread_class="6g", diameter=490, pitch=6)
thread["6g"][500][6] = Thread(major_diameter_max=499.9, major_diameter_min=499.3, pitch_diameter_max=496,
                              pitch_diameter_min=495.7, minor_diameter_max=493.43, minor_diameter_min=491.97,
                              thread_class="6g", diameter=500, pitch=6)
thread["6g"][510][6] = Thread(major_diameter_max=509.9, major_diameter_min=509.3, pitch_diameter_max=506,
                              pitch_diameter_min=505.7, minor_diameter_max=503.43, minor_diameter_min=501.97,
                              thread_class="6g", diameter=510, pitch=6)
thread["6g"][520][6] = Thread(major_diameter_max=519.9, major_diameter_min=519.3, pitch_diameter_max=516,
                              pitch_diameter_min=515.7, minor_diameter_max=513.43, minor_diameter_min=511.97,
                              thread_class="6g", diameter=520, pitch=6)
thread["6g"][530][6] = Thread(major_diameter_max=529.9, major_diameter_min=529.3, pitch_diameter_max=526,
                              pitch_diameter_min=525.7, minor_diameter_max=523.43, minor_diameter_min=521.97,
                              thread_class="6g", diameter=530, pitch=6)
thread["6g"][540][6] = Thread(major_diameter_max=539.9, major_diameter_min=539.3, pitch_diameter_max=536,
                              pitch_diameter_min=535.7, minor_diameter_max=533.43, minor_diameter_min=531.97,
                              thread_class="6g", diameter=540, pitch=6)
thread["6g"][550][6] = Thread(major_diameter_max=549.9, major_diameter_min=549.3, pitch_diameter_max=546,
                              pitch_diameter_min=545.7, minor_diameter_max=543.43, minor_diameter_min=541.97,
                              thread_class="6g", diameter=550, pitch=6)
thread["6g"][560][6] = Thread(major_diameter_max=559.9, major_diameter_min=559.3, pitch_diameter_max=556,
                              pitch_diameter_min=555.7, minor_diameter_max=553.43, minor_diameter_min=551.97,
                              thread_class="6g", diameter=560, pitch=6)
thread["6g"][570][6] = Thread(major_diameter_max=569.9, major_diameter_min=569.3, pitch_diameter_max=566,
                              pitch_diameter_min=565.7, minor_diameter_max=563.43, minor_diameter_min=561.97,
                              thread_class="6g", diameter=570, pitch=6)
thread["6g"][580][6] = Thread(major_diameter_max=579.9, major_diameter_min=579.3, pitch_diameter_max=576,
                              pitch_diameter_min=575.7, minor_diameter_max=573.43, minor_diameter_min=571.97,
                              thread_class="6g", diameter=580, pitch=6)
thread["6g"][590][6] = Thread(major_diameter_max=589.9, major_diameter_min=589.3, pitch_diameter_max=586,
                              pitch_diameter_min=585.7, minor_diameter_max=583.43, minor_diameter_min=581.97,
                              thread_class="6g", diameter=590, pitch=6)
thread["6g"][600][6] = Thread(major_diameter_max=599.9, major_diameter_min=599.3, pitch_diameter_max=596,
                              pitch_diameter_min=595.7, minor_diameter_max=593.43, minor_diameter_min=591.97,
                              thread_class="6g", diameter=600, pitch=6)

thread["4g6g"][0.25][0.075] = Thread(major_diameter_max=0.250, major_diameter_min=0.235, pitch_diameter_max=0.201,
                                     pitch_diameter_min=0.193, minor_diameter_max=0.160, minor_diameter_min=0.152,
                                     thread_class="4g6g", diameter=0.25, pitch=0.075)
thread["4g6g"][0.3][0.08] = Thread(major_diameter_max=0.300, major_diameter_min=0.284, pitch_diameter_max=0.248,
                                   pitch_diameter_min=0.239, minor_diameter_max=0.204, minor_diameter_min=0.195,
                                   thread_class="4g6g", diameter=0.3, pitch=0.08)
thread["4g6g"][0.3][0.09] = Thread(major_diameter_max=0.300, major_diameter_min=0.283, pitch_diameter_max=0.242,
                                   pitch_diameter_min=0.233, minor_diameter_max=0.192, minor_diameter_min=0.183,
                                   thread_class="4g6g", diameter=0.3, pitch=0.09)
thread["4g6g"][0.35][0.09] = Thread(major_diameter_max=0.350, major_diameter_min=0.333, pitch_diameter_max=0.292,
                                    pitch_diameter_min=0.283, minor_diameter_max=0.242, minor_diameter_min=0.233,
                                    thread_class="4g6g", diameter=0.35, pitch=0.09)
thread["4g6g"][0.4][0.1] = Thread(major_diameter_max=0.400, major_diameter_min=0.382, pitch_diameter_max=0.335,
                                  pitch_diameter_min=0.325, minor_diameter_max=0.280, minor_diameter_min=0.270,
                                  thread_class="4g6g", diameter=0.4, pitch=0.1)
thread["4g6g"][0.45][0.1] = Thread(major_diameter_max=0.450, major_diameter_min=0.432, pitch_diameter_max=0.385,
                                   pitch_diameter_min=0.375, minor_diameter_max=0.330, minor_diameter_min=0.320,
                                   thread_class="4g6g", diameter=0.45, pitch=0.1)
thread["4g6g"][0.5][0.125] = Thread(major_diameter_max=0.500, major_diameter_min=0.479, pitch_diameter_max=0.419,
                                    pitch_diameter_min=0.408, minor_diameter_max=0.350, minor_diameter_min=0.339,
                                    thread_class="4g6g", diameter=0.5, pitch=0.125)
thread["4g6g"][0.55][0.125] = Thread(major_diameter_max=0.550, major_diameter_min=0.529, pitch_diameter_max=0.469,
                                     pitch_diameter_min=0.458, minor_diameter_max=0.400, minor_diameter_min=0.389,
                                     thread_class="4g6g", diameter=0.55, pitch=0.125)
thread["4g6g"][0.6][0.15] = Thread(major_diameter_max=0.600, major_diameter_min=0.576, pitch_diameter_max=0.503,
                                   pitch_diameter_min=0.490, minor_diameter_max=0.420, minor_diameter_min=0.407,
                                   thread_class="4g6g", diameter=0.6, pitch=0.15)
thread["4g6g"][0.7][0.175] = Thread(major_diameter_max=0.700, major_diameter_min=0.673, pitch_diameter_max=0.586,
                                    pitch_diameter_min=0.572, minor_diameter_max=0.490, minor_diameter_min=0.476,
                                    thread_class="4g6g", diameter=0.7, pitch=0.175)
thread["4g6g"][0.8][0.2] = Thread(major_diameter_max=0.800, major_diameter_min=0.770, pitch_diameter_max=0.670,
                                  pitch_diameter_min=0.655, minor_diameter_max=0.560, minor_diameter_min=0.545,
                                  thread_class="4g6g", diameter=0.8, pitch=0.2)
thread["4g6g"][0.9][0.225] = Thread(major_diameter_max=0.900, major_diameter_min=0.867, pitch_diameter_max=0.754,
                                    pitch_diameter_min=0.738, minor_diameter_max=0.630, minor_diameter_min=0.614,
                                    thread_class="4g6g", diameter=0.9, pitch=0.225)
thread["4g6g"][1][0.25] = Thread(major_diameter_max=0.982, major_diameter_min=0.915, pitch_diameter_max=0.820,
                                 pitch_diameter_min=0.787, minor_diameter_max=0.711, minor_diameter_min=0.633,
                                 thread_class="4g6g", diameter=1, pitch=0.25)
thread["4g6g"][1][0.2] = Thread(major_diameter_max=0.983, major_diameter_min=0.927, pitch_diameter_max=0.853,
                                pitch_diameter_min=0.823, minor_diameter_max=0.766, minor_diameter_min=0.700,
                                thread_class="4g6g", diameter=1, pitch=0.2)
thread["4g6g"][1.1][0.25] = Thread(major_diameter_max=1.082, major_diameter_min=1.015, pitch_diameter_max=0.920,
                                   pitch_diameter_min=0.888, minor_diameter_max=0.811, minor_diameter_min=0.734,
                                   thread_class="4g6g", diameter=1.1, pitch=0.25)
thread["4g6g"][1.1][0.2] = Thread(major_diameter_max=1.083, major_diameter_min=1.027, pitch_diameter_max=0.953,
                                  pitch_diameter_min=0.923, minor_diameter_max=0.866, minor_diameter_min=0.800,
                                  thread_class="4g6g", diameter=1.1, pitch=0.2)
thread["4g6g"][1.2][0.25] = Thread(major_diameter_max=1.182, major_diameter_min=1.115, pitch_diameter_max=1.020,
                                   pitch_diameter_min=0.987, minor_diameter_max=0.911, minor_diameter_min=0.833,
                                   thread_class="4g6g", diameter=1.2, pitch=0.25)
thread["4g6g"][1.2][0.2] = Thread(major_diameter_max=1.183, major_diameter_min=1.127, pitch_diameter_max=1.053,
                                  pitch_diameter_min=1.023, minor_diameter_max=0.966, minor_diameter_min=0.900,
                                  thread_class="4g6g", diameter=1.2, pitch=0.2)
thread["4g6g"][1.4][0.3] = Thread(major_diameter_max=1.383, major_diameter_min=1.308, pitch_diameter_max=1.253,
                                  pitch_diameter_min=1.215, minor_diameter_max=1.166, minor_diameter_min=1.092,
                                  thread_class="4g6g", diameter=1.4, pitch=0.3)
thread["4g6g"][1.4][0.2] = Thread(major_diameter_max=1.383, major_diameter_min=1.327, pitch_diameter_max=1.253,
                                  pitch_diameter_min=1.223, minor_diameter_max=1.166, minor_diameter_min=1.100,
                                  thread_class="4g6g", diameter=1.4, pitch=0.2)
thread["4g6g"][1.6][0.35] = Thread(major_diameter_max=1.581, major_diameter_min=1.496, pitch_diameter_max=1.354,
                                   pitch_diameter_min=1.314, minor_diameter_max=1.202, minor_diameter_min=1.098,
                                   thread_class="4g6g", diameter=1.6, pitch=0.35)
thread["4g6g"][1.6][0.3] = Thread(major_diameter_max=1.582, major_diameter_min=1.507, pitch_diameter_max=1.387,
                                  pitch_diameter_min=1.359, minor_diameter_max=1.257, minor_diameter_min=1.174,
                                  thread_class="4g6g", diameter=1.6, pitch=0.3)
thread["4g6g"][1.6][0.2] = Thread(major_diameter_max=1.583, major_diameter_min=1.527, pitch_diameter_max=1.453,
                                  pitch_diameter_min=1.421, minor_diameter_max=1.366, minor_diameter_min=1.298,
                                  thread_class="4g6g", diameter=1.6, pitch=0.2)
thread["4g6g"][1.7][0.35] = Thread(major_diameter_max=1.681, major_diameter_min=1.596, pitch_diameter_max=1.454,
                                   pitch_diameter_min=1.414, minor_diameter_max=1.302, minor_diameter_min=1.198,
                                   thread_class="4g6g", diameter=1.7, pitch=0.35)
thread["4g6g"][1.8][0.35] = Thread(major_diameter_max=1.781, major_diameter_min=1.696, pitch_diameter_max=1.554,
                                   pitch_diameter_min=1.514, minor_diameter_max=1.402, minor_diameter_min=1.298,
                                   thread_class="4g6g", diameter=1.8, pitch=0.35)
thread["4g6g"][1.8][0.2] = Thread(major_diameter_max=1.783, major_diameter_min=1.727, pitch_diameter_max=1.653,
                                  pitch_diameter_min=1.621, minor_diameter_max=1.566, minor_diameter_min=1.498,
                                  thread_class="4g6g", diameter=1.8, pitch=0.2)
thread["4g6g"][2][0.4] = Thread(major_diameter_max=1.981, major_diameter_min=1.886, pitch_diameter_max=1.721,
                                pitch_diameter_min=1.679, minor_diameter_max=1.548, minor_diameter_min=1.433,
                                thread_class="4g6g", diameter=2, pitch=0.4)
thread["4g6g"][2][0.25] = Thread(major_diameter_max=1.982, major_diameter_min=1.915, pitch_diameter_max=1.820,
                                 pitch_diameter_min=1.784, minor_diameter_max=1.711, minor_diameter_min=1.630,
                                 thread_class="4g6g", diameter=2, pitch=0.25)
thread["4g6g"][2.2][0.45] = Thread(major_diameter_max=2.180, major_diameter_min=2.080, pitch_diameter_max=1.888,
                                   pitch_diameter_min=1.843, minor_diameter_max=1.693, minor_diameter_min=1.566,
                                   thread_class="4g6g", diameter=2.2, pitch=0.45)
thread["4g6g"][2.2][0.25] = Thread(major_diameter_max=2.182, major_diameter_min=2.115, pitch_diameter_max=2.020,
                                   pitch_diameter_min=1.984, minor_diameter_max=1.911, minor_diameter_min=1.830,
                                   thread_class="4g6g", diameter=2.2, pitch=0.25)
thread["4g6g"][2.3][0.45] = Thread(major_diameter_max=2.280, major_diameter_min=2.180, pitch_diameter_max=1.988,
                                   pitch_diameter_min=1.943, minor_diameter_max=1.793, minor_diameter_min=1.666,
                                   thread_class="4g6g", diameter=2.3, pitch=0.45)
thread["4g6g"][2.3][0.4] = Thread(major_diameter_max=2.281, major_diameter_min=2.186, pitch_diameter_max=2.021,
                                  pitch_diameter_min=1.979, minor_diameter_max=1.848, minor_diameter_min=1.733,
                                  thread_class="4g6g", diameter=2.3, pitch=0.4)
thread["4g6g"][2.5][0.45] = Thread(major_diameter_max=2.480, major_diameter_min=2.380, pitch_diameter_max=2.188,
                                   pitch_diameter_min=2.143, minor_diameter_max=1.993, minor_diameter_min=1.866,
                                   thread_class="4g6g", diameter=2.5, pitch=0.45)
thread["4g6g"][2.5][0.35] = Thread(major_diameter_max=2.481, major_diameter_min=2.396, pitch_diameter_max=2.254,
                                   pitch_diameter_min=2.214, minor_diameter_max=2.102, minor_diameter_min=1.998,
                                   thread_class="4g6g", diameter=2.5, pitch=0.35)
thread["4g6g"][2.6][0.45] = Thread(major_diameter_max=2.580, major_diameter_min=2.480, pitch_diameter_max=2.288,
                                   pitch_diameter_min=2.243, minor_diameter_max=2.093, minor_diameter_min=1.966,
                                   thread_class="4g6g", diameter=2.6, pitch=0.45)
thread["4g6g"][3][0.5] = Thread(major_diameter_max=2.980, major_diameter_min=2.874, pitch_diameter_max=2.655,
                                pitch_diameter_min=2.607, minor_diameter_max=2.439, minor_diameter_min=2.299,
                                thread_class="4g6g", diameter=3, pitch=0.5)
thread["4g6g"][3][0.35] = Thread(major_diameter_max=2.981, major_diameter_min=2.896, pitch_diameter_max=2.754,
                                 pitch_diameter_min=2.712, minor_diameter_max=2.602, minor_diameter_min=2.496,
                                 thread_class="4g6g", diameter=3, pitch=0.35)
thread["4g6g"][3.5][0.6] = Thread(major_diameter_max=3.479, major_diameter_min=3.354, pitch_diameter_max=3.089,
                                  pitch_diameter_min=3.036, minor_diameter_max=2.829, minor_diameter_min=2.667,
                                  thread_class="4g6g", diameter=3.5, pitch=0.6)
thread["4g6g"][3.5][0.35] = Thread(major_diameter_max=3.481, major_diameter_min=3.396, pitch_diameter_max=3.254,
                                   pitch_diameter_min=3.212, minor_diameter_max=3.102, minor_diameter_min=2.996,
                                   thread_class="4g6g", diameter=3.5, pitch=0.35)
thread["4g6g"][4][0.7] = Thread(major_diameter_max=3.978, major_diameter_min=3.838, pitch_diameter_max=3.523,
                                pitch_diameter_min=3.467, minor_diameter_max=3.220, minor_diameter_min=3.036,
                                thread_class="4g6g", diameter=4, pitch=0.7)
thread["4g6g"][4][0.5] = Thread(major_diameter_max=3.980, major_diameter_min=3.874, pitch_diameter_max=3.655,
                                pitch_diameter_min=3.607, minor_diameter_max=3.439, minor_diameter_min=3.299,
                                thread_class="4g6g", diameter=4, pitch=0.5)
thread["4g6g"][4.5][0.75] = Thread(major_diameter_max=4.478, major_diameter_min=4.338, pitch_diameter_max=3.991,
                                   pitch_diameter_min=3.935, minor_diameter_max=3.666, minor_diameter_min=3.473,
                                   thread_class="4g6g", diameter=4.5, pitch=0.75)
thread["4g6g"][4.5][0.5] = Thread(major_diameter_max=4.480, major_diameter_min=4.374, pitch_diameter_max=4.155,
                                  pitch_diameter_min=4.107, minor_diameter_max=3.939, minor_diameter_min=3.799,
                                  thread_class="4g6g", diameter=4.5, pitch=0.5)
thread["4g6g"][5][0.8] = Thread(major_diameter_max=4.976, major_diameter_min=4.826, pitch_diameter_max=4.456,
                                pitch_diameter_min=4.396, minor_diameter_max=4.110, minor_diameter_min=3.904,
                                thread_class="4g6g", diameter=5, pitch=0.8)
thread["4g6g"][5][0.5] = Thread(major_diameter_max=4.980, major_diameter_min=4.874, pitch_diameter_max=4.655,
                                pitch_diameter_min=4.607, minor_diameter_max=4.439, minor_diameter_min=4.299,
                                thread_class="4g6g", diameter=5, pitch=0.5)
thread["4g6g"][5.5][0.5] = Thread(major_diameter_max=5.480, major_diameter_min=5.374, pitch_diameter_max=5.155,
                                  pitch_diameter_min=5.099, minor_diameter_max=4.939, minor_diameter_min=4.791,
                                  thread_class="4g6g", diameter=5.5, pitch=0.5)
thread["4g6g"][6][1] = Thread(major_diameter_max=5.974, major_diameter_min=5.794, pitch_diameter_max=5.324,
                              pitch_diameter_min=5.253, minor_diameter_max=4.891, minor_diameter_min=4.637,
                              thread_class="4g6g", diameter=6, pitch=1)
thread["4g6g"][6][0.8] = Thread(major_diameter_max=5.976, major_diameter_min=5.826, pitch_diameter_max=5.456,
                                pitch_diameter_min=5.406, minor_diameter_max=5.110, minor_diameter_min=4.914,
                                thread_class="4g6g", diameter=6, pitch=0.8)
thread["4g6g"][6][0.75] = Thread(major_diameter_max=5.978, major_diameter_min=5.838, pitch_diameter_max=5.491,
                                 pitch_diameter_min=5.428, minor_diameter_max=5.166, minor_diameter_min=4.966,
                                 thread_class="4g6g", diameter=6, pitch=0.75)
thread["4g6g"][6][0.7] = Thread(major_diameter_max=5.978, major_diameter_min=5.838, pitch_diameter_max=5.523,
                                pitch_diameter_min=5.463, minor_diameter_max=5.220, minor_diameter_min=5.032,
                                thread_class="4g6g", diameter=6, pitch=0.7)
thread["4g6g"][6][0.5] = Thread(major_diameter_max=5.980, major_diameter_min=5.874, pitch_diameter_max=5.655,
                                pitch_diameter_min=5.602, minor_diameter_max=5.439, minor_diameter_min=5.294,
                                thread_class="4g6g", diameter=6, pitch=0.5)
thread["4g6g"][7][1] = Thread(major_diameter_max=6.974, major_diameter_min=6.794, pitch_diameter_max=6.324,
                              pitch_diameter_min=6.253, minor_diameter_max=5.891, minor_diameter_min=5.637,
                              thread_class="4g6g", diameter=7, pitch=1)
thread["4g6g"][7][0.75] = Thread(major_diameter_max=6.978, major_diameter_min=6.838, pitch_diameter_max=6.491,
                                 pitch_diameter_min=6.428, minor_diameter_max=6.166, minor_diameter_min=5.966,
                                 thread_class="4g6g", diameter=7, pitch=0.75)
thread["4g6g"][7][0.5] = Thread(major_diameter_max=6.980, major_diameter_min=6.874, pitch_diameter_max=6.655,
                                pitch_diameter_min=6.602, minor_diameter_max=6.439, minor_diameter_min=6.294,
                                thread_class="4g6g", diameter=7, pitch=0.5)
thread["4g6g"][8][1.25] = Thread(major_diameter_max=7.972, major_diameter_min=7.760, pitch_diameter_max=7.160,
                                 pitch_diameter_min=7.085, minor_diameter_max=6.619, minor_diameter_min=6.315,
                                 thread_class="4g6g", diameter=8, pitch=1.25)
thread["4g6g"][8][1] = Thread(major_diameter_max=7.974, major_diameter_min=7.794, pitch_diameter_max=7.324,
                              pitch_diameter_min=7.253, minor_diameter_max=6.891, minor_diameter_min=6.637,
                              thread_class="4g6g", diameter=8, pitch=1)
thread["4g6g"][8][0.8] = Thread(major_diameter_max=7.976, major_diameter_min=7.826, pitch_diameter_max=7.456,
                                pitch_diameter_min=7.389, minor_diameter_max=7.110, minor_diameter_min=6.897,
                                thread_class="4g6g", diameter=8, pitch=0.8)
thread["4g6g"][8][0.75] = Thread(major_diameter_max=7.978, major_diameter_min=7.838, pitch_diameter_max=7.491,
                                 pitch_diameter_min=7.428, minor_diameter_max=7.166, minor_diameter_min=6.966,
                                 thread_class="4g6g", diameter=8, pitch=0.75)
thread["4g6g"][8][0.5] = Thread(major_diameter_max=7.980, major_diameter_min=7.874, pitch_diameter_max=7.655,
                                pitch_diameter_min=7.602, minor_diameter_max=7.439, minor_diameter_min=7.294,
                                thread_class="4g6g", diameter=8, pitch=0.5)
thread["4g6g"][9][1.25] = Thread(major_diameter_max=8.972, major_diameter_min=8.760, pitch_diameter_max=8.160,
                                 pitch_diameter_min=8.085, minor_diameter_max=7.619, minor_diameter_min=7.315,
                                 thread_class="4g6g", diameter=9, pitch=1.25)
thread["4g6g"][9][1] = Thread(major_diameter_max=8.974, major_diameter_min=8.794, pitch_diameter_max=8.324,
                              pitch_diameter_min=8.253, minor_diameter_max=7.891, minor_diameter_min=7.637,
                              thread_class="4g6g", diameter=9, pitch=1)
thread["4g6g"][9][0.75] = Thread(major_diameter_max=8.978, major_diameter_min=8.838, pitch_diameter_max=8.491,
                                 pitch_diameter_min=8.428, minor_diameter_max=8.166, minor_diameter_min=7.966,
                                 thread_class="4g6g", diameter=9, pitch=0.75)
thread["4g6g"][9][0.5] = Thread(major_diameter_max=8.980, major_diameter_min=8.874, pitch_diameter_max=8.655,
                                pitch_diameter_min=8.602, minor_diameter_max=8.439, minor_diameter_min=8.294,
                                thread_class="4g6g", diameter=9, pitch=0.5)
thread["4g6g"][10][1.5] = Thread(major_diameter_max=9.968, major_diameter_min=9.732, pitch_diameter_max=8.994,
                                 pitch_diameter_min=8.909, minor_diameter_max=8.344, minor_diameter_min=7.985,
                                 thread_class="4g6g", diameter=10, pitch=1.5)
thread["4g6g"][10][1.25] = Thread(major_diameter_max=9.972, major_diameter_min=9.760, pitch_diameter_max=9.160,
                                  pitch_diameter_min=9.085, minor_diameter_max=8.619, minor_diameter_min=8.315,
                                  thread_class="4g6g", diameter=10, pitch=1.25)
thread["4g6g"][10][1.12] = Thread(major_diameter_max=9.973, major_diameter_min=9.783, pitch_diameter_max=9.246,
                                  pitch_diameter_min=9.171, minor_diameter_max=8.761, minor_diameter_min=8.481,
                                  thread_class="4g6g", diameter=10, pitch=1.12)
thread["4g6g"][10][1] = Thread(major_diameter_max=9.974, major_diameter_min=9.794, pitch_diameter_max=9.324,
                               pitch_diameter_min=9.253, minor_diameter_max=8.891, minor_diameter_min=8.637,
                               thread_class="4g6g", diameter=10, pitch=1)
thread["4g6g"][10][0.75] = Thread(major_diameter_max=9.978, major_diameter_min=9.838, pitch_diameter_max=9.491,
                                  pitch_diameter_min=9.428, minor_diameter_max=9.166, minor_diameter_min=8.966,
                                  thread_class="4g6g", diameter=10, pitch=0.75)
thread["4g6g"][10][0.5] = Thread(major_diameter_max=9.980, major_diameter_min=9.874, pitch_diameter_max=9.655,
                                 pitch_diameter_min=9.602, minor_diameter_max=9.439, minor_diameter_min=9.294,
                                 thread_class="4g6g", diameter=10, pitch=0.5)
thread["4g6g"][11][1.5] = Thread(major_diameter_max=10.968, major_diameter_min=10.732, pitch_diameter_max=9.994,
                                 pitch_diameter_min=9.911, minor_diameter_max=9.344, minor_diameter_min=8.987,
                                 thread_class="4g6g", diameter=11, pitch=1.5)
thread["4g6g"][11][1] = Thread(major_diameter_max=10.974, major_diameter_min=10.794, pitch_diameter_max=10.324,
                               pitch_diameter_min=10.253, minor_diameter_max=9.891, minor_diameter_min=9.637,
                               thread_class="4g6g", diameter=11, pitch=1)
thread["4g6g"][11][0.75] = Thread(major_diameter_max=10.978, major_diameter_min=10.838, pitch_diameter_max=10.491,
                                  pitch_diameter_min=10.428, minor_diameter_max=10.166, minor_diameter_min=9.966,
                                  thread_class="4g6g", diameter=11, pitch=0.75)
thread["4g6g"][11][0.5] = Thread(major_diameter_max=10.980, major_diameter_min=10.874, pitch_diameter_max=10.655,
                                 pitch_diameter_min=10.602, minor_diameter_max=10.439, minor_diameter_min=10.294,
                                 thread_class="4g6g", diameter=11, pitch=0.5)
thread["4g6g"][12][1.75] = Thread(major_diameter_max=11.966, major_diameter_min=11.701, pitch_diameter_max=10.829,
                                  pitch_diameter_min=10.734, minor_diameter_max=10.072, minor_diameter_min=9.656,
                                  thread_class="4g6g", diameter=12, pitch=1.75)
thread["4g6g"][12][1.25] = Thread(major_diameter_max=11.972, major_diameter_min=11.760, pitch_diameter_max=11.160,
                                  pitch_diameter_min=11.075, minor_diameter_max=10.619, minor_diameter_min=10.305,
                                  thread_class="4g6g", diameter=12, pitch=1.25)
thread["4g6g"][12][1] = Thread(major_diameter_max=11.974, major_diameter_min=11.794, pitch_diameter_max=11.324,
                               pitch_diameter_min=11.249, minor_diameter_max=10.891, minor_diameter_min=10.633,
                               thread_class="4g6g", diameter=12, pitch=1)
thread["4g6g"][12][0.75] = Thread(major_diameter_max=11.978, major_diameter_min=11.838, pitch_diameter_max=11.491,
                                  pitch_diameter_min=11.424, minor_diameter_max=11.166, minor_diameter_min=10.962,
                                  thread_class="4g6g", diameter=12, pitch=0.75)
thread["4g6g"][12][0.5] = Thread(major_diameter_max=11.980, major_diameter_min=11.874, pitch_diameter_max=11.655,
                                 pitch_diameter_min=11.598, minor_diameter_max=11.439, minor_diameter_min=11.290,
                                 thread_class="4g6g", diameter=12, pitch=0.5)
thread["4g6g"][14][2] = Thread(major_diameter_max=13.962, major_diameter_min=13.682, pitch_diameter_max=12.663,
                               pitch_diameter_min=12.563, minor_diameter_max=11.797, minor_diameter_min=11.331,
                               thread_class="4g6g", diameter=14, pitch=2)
thread["4g6g"][14][1.5] = Thread(major_diameter_max=13.968, major_diameter_min=13.732, pitch_diameter_max=12.994,
                                 pitch_diameter_min=12.904, minor_diameter_max=12.344, minor_diameter_min=11.980,
                                 thread_class="4g6g", diameter=14, pitch=1.5)
thread["4g6g"][14][1.25] = Thread(major_diameter_max=13.972, major_diameter_min=13.760, pitch_diameter_max=13.160,
                                  pitch_diameter_min=13.075, minor_diameter_max=12.619, minor_diameter_min=12.305,
                                  thread_class="4g6g", diameter=14, pitch=1.25)
thread["4g6g"][14][1] = Thread(major_diameter_max=13.974, major_diameter_min=13.794, pitch_diameter_max=13.324,
                               pitch_diameter_min=13.250, minor_diameter_max=12.891, minor_diameter_min=12.634,
                               thread_class="4g6g", diameter=14, pitch=1)
thread["4g6g"][14][0.75] = Thread(major_diameter_max=13.978, major_diameter_min=13.838, pitch_diameter_max=13.491,
                                  pitch_diameter_min=13.424, minor_diameter_max=13.166, minor_diameter_min=12.962,
                                  thread_class="4g6g", diameter=14, pitch=0.75)
thread["4g6g"][14][0.5] = Thread(major_diameter_max=13.980, major_diameter_min=13.874, pitch_diameter_max=13.655,
                                 pitch_diameter_min=13.598, minor_diameter_max=13.439, minor_diameter_min=13.290,
                                 thread_class="4g6g", diameter=14, pitch=0.5)
thread["4g6g"][15][1.5] = Thread(major_diameter_max=14.968, major_diameter_min=14.732, pitch_diameter_max=13.994,
                                 pitch_diameter_min=13.904, minor_diameter_max=13.344, minor_diameter_min=12.980,
                                 thread_class="4g6g", diameter=15, pitch=1.5)
thread["4g6g"][15][1] = Thread(major_diameter_max=14.974, major_diameter_min=14.794, pitch_diameter_max=14.324,
                               pitch_diameter_min=14.249, minor_diameter_max=13.891, minor_diameter_min=13.633,
                               thread_class="4g6g", diameter=15, pitch=1)
thread["4g6g"][16][2] = Thread(major_diameter_max=15.962, major_diameter_min=15.682, pitch_diameter_max=14.663,
                               pitch_diameter_min=14.563, minor_diameter_max=13.797, minor_diameter_min=13.331,
                               thread_class="4g6g", diameter=16, pitch=2)
thread["4g6g"][16][1.6] = Thread(major_diameter_max=15.968, major_diameter_min=15.756, pitch_diameter_max=14.929,
                                 pitch_diameter_min=14.863, minor_diameter_max=14.236, minor_diameter_min=13.877,
                                 thread_class="4g6g", diameter=16, pitch=1.6)
thread["4g6g"][16][1.5] = Thread(major_diameter_max=15.968, major_diameter_min=15.732, pitch_diameter_max=14.994,
                                 pitch_diameter_min=14.904, minor_diameter_max=14.344, minor_diameter_min=13.980,
                                 thread_class="4g6g", diameter=16, pitch=1.5)
thread["4g6g"][16][1.25] = Thread(major_diameter_max=15.972, major_diameter_min=15.760, pitch_diameter_max=15.160,
                                  pitch_diameter_min=15.075, minor_diameter_max=14.619, minor_diameter_min=14.305,
                                  thread_class="4g6g", diameter=16, pitch=1.25)
thread["4g6g"][16][1] = Thread(major_diameter_max=15.974, major_diameter_min=15.794, pitch_diameter_max=15.324,
                               pitch_diameter_min=15.249, minor_diameter_max=14.891, minor_diameter_min=14.633,
                               thread_class="4g6g", diameter=16, pitch=1)
thread["4g6g"][16][0.75] = Thread(major_diameter_max=15.978, major_diameter_min=15.838, pitch_diameter_max=15.491,
                                  pitch_diameter_min=15.424, minor_diameter_max=15.166, minor_diameter_min=14.962,
                                  thread_class="4g6g", diameter=16, pitch=0.75)
thread["4g6g"][16][0.5] = Thread(major_diameter_max=15.980, major_diameter_min=15.874, pitch_diameter_max=15.655,
                                 pitch_diameter_min=15.599, minor_diameter_max=15.439, minor_diameter_min=15.291,
                                 thread_class="4g6g", diameter=16, pitch=0.5)
thread["4g6g"][17][1.5] = Thread(major_diameter_max=16.968, major_diameter_min=16.732, pitch_diameter_max=15.994,
                                 pitch_diameter_min=15.904, minor_diameter_max=15.344, minor_diameter_min=14.980,
                                 thread_class="4g6g", diameter=17, pitch=1.5)
thread["4g6g"][17][1] = Thread(major_diameter_max=16.974, major_diameter_min=16.794, pitch_diameter_max=16.324,
                               pitch_diameter_min=16.249, minor_diameter_max=15.891, minor_diameter_min=15.633,
                               thread_class="4g6g", diameter=17, pitch=1)
thread["4g6g"][18][2.5] = Thread(major_diameter_max=17.958, major_diameter_min=17.623, pitch_diameter_max=16.334,
                                 pitch_diameter_min=16.228, minor_diameter_max=15.252, minor_diameter_min=14.688,
                                 thread_class="4g6g", diameter=18, pitch=2.5)
thread["4g6g"][18][2] = Thread(major_diameter_max=17.962, major_diameter_min=17.682, pitch_diameter_max=16.663,
                               pitch_diameter_min=16.563, minor_diameter_max=15.797, minor_diameter_min=15.331,
                               thread_class="4g6g", diameter=18, pitch=2)
thread["4g6g"][18][1.5] = Thread(major_diameter_max=17.968, major_diameter_min=17.732, pitch_diameter_max=16.994,
                                 pitch_diameter_min=16.904, minor_diameter_max=16.344, minor_diameter_min=15.980,
                                 thread_class="4g6g", diameter=18, pitch=1.5)
thread["4g6g"][18][1.25] = Thread(major_diameter_max=17.972, major_diameter_min=17.760, pitch_diameter_max=17.160,
                                  pitch_diameter_min=17.075, minor_diameter_max=16.619, minor_diameter_min=16.305,
                                  thread_class="4g6g", diameter=18, pitch=1.25)
thread["4g6g"][18][1] = Thread(major_diameter_max=17.974, major_diameter_min=17.794, pitch_diameter_max=17.324,
                               pitch_diameter_min=17.249, minor_diameter_max=16.891, minor_diameter_min=16.633,
                               thread_class="4g6g", diameter=18, pitch=1)
thread["4g6g"][18][0.75] = Thread(major_diameter_max=17.978, major_diameter_min=17.838, pitch_diameter_max=17.491,
                                  pitch_diameter_min=17.424, minor_diameter_max=17.166, minor_diameter_min=16.962,
                                  thread_class="4g6g", diameter=18, pitch=0.75)
thread["4g6g"][18][0.5] = Thread(major_diameter_max=17.980, major_diameter_min=17.874, pitch_diameter_max=17.655,
                                 pitch_diameter_min=17.599, minor_diameter_max=17.439, minor_diameter_min=17.291,
                                 thread_class="4g6g", diameter=18, pitch=0.5)
thread["4g6g"][20][2.5] = Thread(major_diameter_max=19.958, major_diameter_min=19.623, pitch_diameter_max=18.334,
                                 pitch_diameter_min=18.228, minor_diameter_max=17.252, minor_diameter_min=16.688,
                                 thread_class="4g6g", diameter=20, pitch=2.5)
thread["4g6g"][20][2] = Thread(major_diameter_max=19.962, major_diameter_min=19.682, pitch_diameter_max=18.663,
                               pitch_diameter_min=18.562, minor_diameter_max=17.797, minor_diameter_min=17.330,
                               thread_class="4g6g", diameter=20, pitch=2)
thread["4g6g"][20][1.5] = Thread(major_diameter_max=19.968, major_diameter_min=19.732, pitch_diameter_max=18.994,
                                 pitch_diameter_min=18.904, minor_diameter_max=18.344, minor_diameter_min=17.980,
                                 thread_class="4g6g", diameter=20, pitch=1.5)
thread["4g6g"][20][1] = Thread(major_diameter_max=19.974, major_diameter_min=19.794, pitch_diameter_max=19.324,
                               pitch_diameter_min=19.249, minor_diameter_max=18.891, minor_diameter_min=18.633,
                               thread_class="4g6g", diameter=20, pitch=1)
thread["4g6g"][20][0.75] = Thread(major_diameter_max=19.978, major_diameter_min=19.838, pitch_diameter_max=19.491,
                                  pitch_diameter_min=19.424, minor_diameter_max=19.166, minor_diameter_min=18.962,
                                  thread_class="4g6g", diameter=20, pitch=0.75)
thread["4g6g"][20][0.5] = Thread(major_diameter_max=19.980, major_diameter_min=19.874, pitch_diameter_max=19.655,
                                 pitch_diameter_min=19.599, minor_diameter_max=19.439, minor_diameter_min=19.291,
                                 thread_class="4g6g", diameter=20, pitch=0.5)
thread["4g6g"][22][3] = Thread(major_diameter_max=21.952, major_diameter_min=21.577, pitch_diameter_max=20.003,
                               pitch_diameter_min=19.885, minor_diameter_max=18.704, minor_diameter_min=18.037,
                               thread_class="4g6g", diameter=22, pitch=3)
thread["4g6g"][22][2.5] = Thread(major_diameter_max=21.958, major_diameter_min=21.623, pitch_diameter_max=20.334,
                                 pitch_diameter_min=20.234, minor_diameter_max=19.252, minor_diameter_min=18.694,
                                 thread_class="4g6g", diameter=22, pitch=2.5)
thread["4g6g"][22][2] = Thread(major_diameter_max=21.962, major_diameter_min=21.682, pitch_diameter_max=20.663,
                               pitch_diameter_min=20.563, minor_diameter_max=19.797, minor_diameter_min=19.331,
                               thread_class="4g6g", diameter=22, pitch=2)
thread["4g6g"][22][1.5] = Thread(major_diameter_max=21.968, major_diameter_min=21.732, pitch_diameter_max=20.994,
                                 pitch_diameter_min=20.904, minor_diameter_max=20.344, minor_diameter_min=19.980,
                                 thread_class="4g6g", diameter=22, pitch=1.5)
thread["4g6g"][22][1] = Thread(major_diameter_max=21.974, major_diameter_min=21.794, pitch_diameter_max=21.324,
                               pitch_diameter_min=21.249, minor_diameter_max=20.891, minor_diameter_min=20.633,
                               thread_class="4g6g", diameter=22, pitch=1)
thread["4g6g"][22][0.75] = Thread(major_diameter_max=21.978, major_diameter_min=21.838, pitch_diameter_max=21.491,
                                  pitch_diameter_min=21.424, minor_diameter_max=21.166, minor_diameter_min=20.962,
                                  thread_class="4g6g", diameter=22, pitch=0.75)
thread["4g6g"][22][0.5] = Thread(major_diameter_max=21.980, major_diameter_min=21.874, pitch_diameter_max=21.655,
                                 pitch_diameter_min=21.598, minor_diameter_max=21.439, minor_diameter_min=21.290,
                                 thread_class="4g6g", diameter=22, pitch=0.5)
thread["4g6g"][24][3] = Thread(major_diameter_max=23.952, major_diameter_min=23.557, pitch_diameter_max=22.003,
                               pitch_diameter_min=21.878, minor_diameter_max=20.704, minor_diameter_min=20.030,
                               thread_class="4g6g", diameter=24, pitch=3)
thread["4g6g"][24][2.5] = Thread(major_diameter_max=23.958, major_diameter_min=23.623, pitch_diameter_max=22.334,
                                 pitch_diameter_min=22.214, minor_diameter_max=21.252, minor_diameter_min=20.674,
                                 thread_class="4g6g", diameter=24, pitch=2.5)
thread["4g6g"][24][2] = Thread(major_diameter_max=23.962, major_diameter_min=23.682, pitch_diameter_max=22.663,
                               pitch_diameter_min=22.557, minor_diameter_max=21.797, minor_diameter_min=21.325,
                               thread_class="4g6g", diameter=24, pitch=2)
thread["4g6g"][24][1.5] = Thread(major_diameter_max=23.968, major_diameter_min=23.732, pitch_diameter_max=22.994,
                                 pitch_diameter_min=22.899, minor_diameter_max=22.344, minor_diameter_min=21.975,
                                 thread_class="4g6g", diameter=24, pitch=1.5)
thread["4g6g"][24][1] = Thread(major_diameter_max=23.974, major_diameter_min=23.794, pitch_diameter_max=23.324,
                               pitch_diameter_min=23.244, minor_diameter_max=22.891, minor_diameter_min=22.628,
                               thread_class="4g6g", diameter=24, pitch=1)
thread["4g6g"][24][0.75] = Thread(major_diameter_max=23.978, major_diameter_min=23.838, pitch_diameter_max=23.491,
                                  pitch_diameter_min=23.420, minor_diameter_max=23.166, minor_diameter_min=22.958,
                                  thread_class="4g6g", diameter=24, pitch=0.75)
thread["4g6g"][25][2] = Thread(major_diameter_max=24.962, major_diameter_min=24.682, pitch_diameter_max=23.663,
                               pitch_diameter_min=23.557, minor_diameter_max=22.797, minor_diameter_min=22.325,
                               thread_class="4g6g", diameter=25, pitch=2)
thread["4g6g"][25][1.5] = Thread(major_diameter_max=24.968, major_diameter_min=24.732, pitch_diameter_max=23.994,
                                 pitch_diameter_min=23.899, minor_diameter_max=23.344, minor_diameter_min=22.975,
                                 thread_class="4g6g", diameter=25, pitch=1.5)
thread["4g6g"][25][1] = Thread(major_diameter_max=24.974, major_diameter_min=24.794, pitch_diameter_max=24.324,
                               pitch_diameter_min=24.244, minor_diameter_max=23.891, minor_diameter_min=23.628,
                               thread_class="4g6g", diameter=25, pitch=1)
thread["4g6g"][26][1.5] = Thread(major_diameter_max=25.968, major_diameter_min=25.732, pitch_diameter_max=24.994,
                                 pitch_diameter_min=24.899, minor_diameter_max=24.344, minor_diameter_min=23.975,
                                 thread_class="4g6g", diameter=26, pitch=1.5)
thread["4g6g"][27][3] = Thread(major_diameter_max=26.952, major_diameter_min=26.577, pitch_diameter_max=25.003,
                               pitch_diameter_min=24.878, minor_diameter_max=23.704, minor_diameter_min=23.030,
                               thread_class="4g6g", diameter=27, pitch=3)
thread["4g6g"][27][2] = Thread(major_diameter_max=29.962, major_diameter_min=26.682, pitch_diameter_max=25.663,
                               pitch_diameter_min=25.557, minor_diameter_max=24.797, minor_diameter_min=24.325,
                               thread_class="4g6g", diameter=27, pitch=2)
thread["4g6g"][27][1.5] = Thread(major_diameter_max=26.968, major_diameter_min=26.732, pitch_diameter_max=25.994,
                                 pitch_diameter_min=25.899, minor_diameter_max=25.344, minor_diameter_min=24.975,
                                 thread_class="4g6g", diameter=27, pitch=1.5)
thread["4g6g"][27][1] = Thread(major_diameter_max=26.974, major_diameter_min=26.794, pitch_diameter_max=26.324,
                               pitch_diameter_min=26.244, minor_diameter_max=25.891, minor_diameter_min=25.628,
                               thread_class="4g6g", diameter=27, pitch=1)
thread["4g6g"][27][0.75] = Thread(major_diameter_max=26.978, major_diameter_min=26.838, pitch_diameter_max=26.491,
                                  pitch_diameter_min=26.420, minor_diameter_max=26.166, minor_diameter_min=25.958,
                                  thread_class="4g6g", diameter=27, pitch=0.75)
thread["4g6g"][28][2] = Thread(major_diameter_max=27.962, major_diameter_min=27.682, pitch_diameter_max=26.663,
                               pitch_diameter_min=26.557, minor_diameter_max=25.797, minor_diameter_min=25.325,
                               thread_class="4g6g", diameter=28, pitch=2)
thread["4g6g"][28][1.5] = Thread(major_diameter_max=27.968, major_diameter_min=27.732, pitch_diameter_max=26.994,
                                 pitch_diameter_min=26.899, minor_diameter_max=26.344, minor_diameter_min=25.975,
                                 thread_class="4g6g", diameter=28, pitch=1.5)
thread["4g6g"][28][1] = Thread(major_diameter_max=27.974, major_diameter_min=27.794, pitch_diameter_max=27.324,
                               pitch_diameter_min=27.244, minor_diameter_max=26.891, minor_diameter_min=26.628,
                               thread_class="4g6g", diameter=28, pitch=1)
thread["4g6g"][30][3.5] = Thread(major_diameter_max=29.947, major_diameter_min=29.522, pitch_diameter_max=27.674,
                                 pitch_diameter_min=27.542, minor_diameter_max=26.158, minor_diameter_min=25.386,
                                 thread_class="4g6g", diameter=30, pitch=3.5)
thread["4g6g"][30][3] = Thread(major_diameter_max=29.952, major_diameter_min=29.577, pitch_diameter_max=28.003,
                               pitch_diameter_min=27.878, minor_diameter_max=26.704, minor_diameter_min=26.030,
                               thread_class="4g6g", diameter=30, pitch=3)
thread["4g6g"][30][2.5] = Thread(major_diameter_max=29.958, major_diameter_min=29.623, pitch_diameter_max=28.334,
                                 pitch_diameter_min=28.214, minor_diameter_max=27.252, minor_diameter_min=26.674,
                                 thread_class="4g6g", diameter=30, pitch=2.5)
thread["4g6g"][30][2] = Thread(major_diameter_max=29.962, major_diameter_min=29.682, pitch_diameter_max=28.663,
                               pitch_diameter_min=28.557, minor_diameter_max=27.797, minor_diameter_min=27.325,
                               thread_class="4g6g", diameter=30, pitch=2)
thread["4g6g"][30][1.5] = Thread(major_diameter_max=29.968, major_diameter_min=29.732, pitch_diameter_max=28.994,
                                 pitch_diameter_min=28.899, minor_diameter_max=28.344, minor_diameter_min=27.975,
                                 thread_class="4g6g", diameter=30, pitch=1.5)
thread["4g6g"][30][1] = Thread(major_diameter_max=29.974, major_diameter_min=29.794, pitch_diameter_max=29.324,
                               pitch_diameter_min=29.244, minor_diameter_max=28.891, minor_diameter_min=28.628,
                               thread_class="4g6g", diameter=30, pitch=1)
thread["4g6g"][30][0.75] = Thread(major_diameter_max=29.978, major_diameter_min=29.838, pitch_diameter_max=29.491,
                                  pitch_diameter_min=29.420, minor_diameter_max=29.166, minor_diameter_min=28.958,
                                  thread_class="4g6g", diameter=30, pitch=0.75)
thread["4g6g"][32][2] = Thread(major_diameter_max=31.962, major_diameter_min=31.682, pitch_diameter_max=30.663,
                               pitch_diameter_min=30.557, minor_diameter_max=29.797, minor_diameter_min=29.325,
                               thread_class="4g6g", diameter=32, pitch=2)
thread["4g6g"][32][1.5] = Thread(major_diameter_max=31.968, major_diameter_min=31.732, pitch_diameter_max=30.994,
                                 pitch_diameter_min=30.899, minor_diameter_max=30.344, minor_diameter_min=29.975,
                                 thread_class="4g6g", diameter=32, pitch=1.5)
thread["4g6g"][33][3.5] = Thread(major_diameter_max=32.968, major_diameter_min=32.543, pitch_diameter_max=30.695,
                                 pitch_diameter_min=30.563, minor_diameter_max=29.179, minor_diameter_min=28.407,
                                 thread_class="4g6g", diameter=33, pitch=3.5)
thread["4g6g"][33][3] = Thread(major_diameter_max=32.952, major_diameter_min=32.577, pitch_diameter_max=31.003,
                               pitch_diameter_min=30.878, minor_diameter_max=29.704, minor_diameter_min=29.030,
                               thread_class="4g6g", diameter=33, pitch=3)
thread["4g6g"][33][2] = Thread(major_diameter_max=32.962, major_diameter_min=32.682, pitch_diameter_max=31.663,
                               pitch_diameter_min=31.557, minor_diameter_max=30.797, minor_diameter_min=30.325,
                               thread_class="4g6g", diameter=33, pitch=2)
thread["4g6g"][33][1.5] = Thread(major_diameter_max=32.968, major_diameter_min=32.732, pitch_diameter_max=31.994,
                                 pitch_diameter_min=31.899, minor_diameter_max=31.344, minor_diameter_min=30.975,
                                 thread_class="4g6g", diameter=33, pitch=1.5)
thread["4g6g"][33][1] = Thread(major_diameter_max=32.974, major_diameter_min=32.794, pitch_diameter_max=32.324,
                               pitch_diameter_min=32.244, minor_diameter_max=31.891, minor_diameter_min=31.628,
                               thread_class="4g6g", diameter=33, pitch=1)
thread["4g6g"][33][0.75] = Thread(major_diameter_max=32.978, major_diameter_min=32.838, pitch_diameter_max=32.491,
                                  pitch_diameter_min=32.420, minor_diameter_max=32.166, minor_diameter_min=31.958,
                                  thread_class="4g6g", diameter=33, pitch=0.75)
thread["4g6g"][35][1.5] = Thread(major_diameter_max=34.968, major_diameter_min=34.732, pitch_diameter_max=33.994,
                                 pitch_diameter_min=33.899, minor_diameter_max=33.344, minor_diameter_min=32.975,
                                 thread_class="4g6g", diameter=35, pitch=1.5)
thread["4g6g"][36][4] = Thread(major_diameter_max=35.940, major_diameter_min=35.465, pitch_diameter_max=33.342,
                               pitch_diameter_min=33.202, minor_diameter_max=31.610, minor_diameter_min=30.738,
                               thread_class="4g6g", diameter=36, pitch=4)
thread["4g6g"][36][3] = Thread(major_diameter_max=35.952, major_diameter_min=35.577, pitch_diameter_max=34.003,
                               pitch_diameter_min=33.878, minor_diameter_max=32.704, minor_diameter_min=32.030,
                               thread_class="4g6g", diameter=36, pitch=3)
thread["4g6g"][36][2] = Thread(major_diameter_max=35.962, major_diameter_min=35.682, pitch_diameter_max=34.663,
                               pitch_diameter_min=34.557, minor_diameter_max=33.797, minor_diameter_min=33.325,
                               thread_class="4g6g", diameter=36, pitch=2)
thread["4g6g"][36][1.5] = Thread(major_diameter_max=35.968, major_diameter_min=35.732, pitch_diameter_max=34.994,
                                 pitch_diameter_min=34.899, minor_diameter_max=34.344, minor_diameter_min=33.975,
                                 thread_class="4g6g", diameter=36, pitch=1.5)
thread["4g6g"][36][1] = Thread(major_diameter_max=35.974, major_diameter_min=35.794, pitch_diameter_max=35.324,
                               pitch_diameter_min=35.244, minor_diameter_max=34.891, minor_diameter_min=34.628,
                               thread_class="4g6g", diameter=36, pitch=1)
thread["4g6g"][38][1.5] = Thread(major_diameter_max=37.968, major_diameter_min=37.732, pitch_diameter_max=36.994,
                                 pitch_diameter_min=36.899, minor_diameter_max=36.344, minor_diameter_min=35.975,
                                 thread_class="4g6g", diameter=38, pitch=1.5)
thread["4g6g"][39][4] = Thread(major_diameter_max=38.940, major_diameter_min=38.465, pitch_diameter_max=36.342,
                               pitch_diameter_min=36.202, minor_diameter_max=34.610, minor_diameter_min=33.738,
                               thread_class="4g6g", diameter=39, pitch=4)
thread["4g6g"][39][3] = Thread(major_diameter_max=38.952, major_diameter_min=38.577, pitch_diameter_max=37.003,
                               pitch_diameter_min=36.878, minor_diameter_max=35.704, minor_diameter_min=35.030,
                               thread_class="4g6g", diameter=39, pitch=3)
thread["4g6g"][39][2] = Thread(major_diameter_max=38.962, major_diameter_min=38.682, pitch_diameter_max=37.663,
                               pitch_diameter_min=37.557, minor_diameter_max=36.797, minor_diameter_min=36.325,
                               thread_class="4g6g", diameter=39, pitch=2)
thread["4g6g"][39][1.5] = Thread(major_diameter_max=38.968, major_diameter_min=38.732, pitch_diameter_max=37.994,
                                 pitch_diameter_min=37.899, minor_diameter_max=37.344, minor_diameter_min=36.975,
                                 thread_class="4g6g", diameter=39, pitch=1.5)
thread["4g6g"][39][1] = Thread(major_diameter_max=38.974, major_diameter_min=38.794, pitch_diameter_max=38.324,
                               pitch_diameter_min=38.244, minor_diameter_max=37.891, minor_diameter_min=37.628,
                               thread_class="4g6g", diameter=39, pitch=1)
thread["4g6g"][40][3] = Thread(major_diameter_max=39.952, major_diameter_min=39.577, pitch_diameter_max=38.003,
                               pitch_diameter_min=37.878, minor_diameter_max=36.704, minor_diameter_min=36.030,
                               thread_class="4g6g", diameter=40, pitch=3)
thread["4g6g"][40][2.5] = Thread(major_diameter_max=39.958, major_diameter_min=39.623, pitch_diameter_max=38.334,
                                 pitch_diameter_min=38.215, minor_diameter_max=37.252, minor_diameter_min=36.674,
                                 thread_class="4g6g", diameter=40, pitch=2.5)
thread["4g6g"][40][2] = Thread(major_diameter_max=39.962, major_diameter_min=39.682, pitch_diameter_max=38.663,
                               pitch_diameter_min=38.557, minor_diameter_max=37.797, minor_diameter_min=37.325,
                               thread_class="4g6g", diameter=40, pitch=2)
thread["4g6g"][40][1.5] = Thread(major_diameter_max=39.968, major_diameter_min=39.732, pitch_diameter_max=38.994,
                                 pitch_diameter_min=38.899, minor_diameter_max=38.344, minor_diameter_min=37.975,
                                 thread_class="4g6g", diameter=40, pitch=1.5)
thread["4g6g"][42][4.5] = Thread(major_diameter_max=41.937, major_diameter_min=41.437, pitch_diameter_max=39.014,
                                 pitch_diameter_min=38.864, minor_diameter_max=37.066, minor_diameter_min=36.092,
                                 thread_class="4g6g", diameter=42, pitch=4.5)
thread["4g6g"][42][4] = Thread(major_diameter_max=41.940, major_diameter_min=41.465, pitch_diameter_max=39.342,
                               pitch_diameter_min=39.202, minor_diameter_max=37.610, minor_diameter_min=36.738,
                               thread_class="4g6g", diameter=42, pitch=4)
thread["4g6g"][42][3] = Thread(major_diameter_max=41.952, major_diameter_min=41.577, pitch_diameter_max=40.003,
                               pitch_diameter_min=39.878, minor_diameter_max=38.704, minor_diameter_min=38.030,
                               thread_class="4g6g", diameter=42, pitch=3)
thread["4g6g"][42][2] = Thread(major_diameter_max=41.962, major_diameter_min=41.682, pitch_diameter_max=40.663,
                               pitch_diameter_min=40.557, minor_diameter_max=39.797, minor_diameter_min=39.325,
                               thread_class="4g6g", diameter=42, pitch=2)
thread["4g6g"][42][1.5] = Thread(major_diameter_max=41.968, major_diameter_min=41.732, pitch_diameter_max=40.994,
                                 pitch_diameter_min=40.899, minor_diameter_max=40.344, minor_diameter_min=39.975,
                                 thread_class="4g6g", diameter=42, pitch=1.5)
thread["4g6g"][42][1] = Thread(major_diameter_max=41.974, major_diameter_min=41.794, pitch_diameter_max=41.324,
                               pitch_diameter_min=41.244, minor_diameter_max=40.891, minor_diameter_min=40.628,
                               thread_class="4g6g", diameter=42, pitch=1)
thread["4g6g"][45][4.5] = Thread(major_diameter_max=44.937, major_diameter_min=44.437, pitch_diameter_max=42.014,
                                 pitch_diameter_min=41.864, minor_diameter_max=40.066, minor_diameter_min=39.092,
                                 thread_class="4g6g", diameter=45, pitch=4.5)
thread["4g6g"][45][4] = Thread(major_diameter_max=44.940, major_diameter_min=44.465, pitch_diameter_max=42.342,
                               pitch_diameter_min=42.202, minor_diameter_max=40.610, minor_diameter_min=39.738,
                               thread_class="4g6g", diameter=45, pitch=4)
thread["4g6g"][45][3] = Thread(major_diameter_max=44.952, major_diameter_min=44.577, pitch_diameter_max=43.003,
                               pitch_diameter_min=42.878, minor_diameter_max=41.704, minor_diameter_min=41.030,
                               thread_class="4g6g", diameter=45, pitch=3)
thread["4g6g"][45][2] = Thread(major_diameter_max=44.962, major_diameter_min=44.682, pitch_diameter_max=43.663,
                               pitch_diameter_min=43.557, minor_diameter_max=42.797, minor_diameter_min=42.325,
                               thread_class="4g6g", diameter=45, pitch=2)
thread["4g6g"][45][1.5] = Thread(major_diameter_max=44.968, major_diameter_min=44.732, pitch_diameter_max=43.994,
                                 pitch_diameter_min=43.899, minor_diameter_max=43.344, minor_diameter_min=42.975,
                                 thread_class="4g6g", diameter=45, pitch=1.5)
thread["4g6g"][45][1] = Thread(major_diameter_max=44.974, major_diameter_min=44.794, pitch_diameter_max=44.324,
                               pitch_diameter_min=44.244, minor_diameter_max=43.891, minor_diameter_min=43.628,
                               thread_class="4g6g", diameter=45, pitch=1)
thread["4g6g"][48][5] = Thread(major_diameter_max=47.929, major_diameter_min=47.399, pitch_diameter_max=44.681,
                               pitch_diameter_min=44.521, minor_diameter_max=42.516, minor_diameter_min=41.441,
                               thread_class="4g6g", diameter=48, pitch=5)
thread["4g6g"][48][4] = Thread(major_diameter_max=47.940, major_diameter_min=47.465, pitch_diameter_max=45.342,
                               pitch_diameter_min=45.192, minor_diameter_max=43.610, minor_diameter_min=42.728,
                               thread_class="4g6g", diameter=48, pitch=4)
thread["4g6g"][48][3] = Thread(major_diameter_max=47.952, major_diameter_min=47.577, pitch_diameter_max=46.003,
                               pitch_diameter_min=45.871, minor_diameter_max=44.704, minor_diameter_min=44.023,
                               thread_class="4g6g", diameter=48, pitch=3)
thread["4g6g"][48][2] = Thread(major_diameter_max=47.962, major_diameter_min=47.682, pitch_diameter_max=46.663,
                               pitch_diameter_min=46.551, minor_diameter_max=45.797, minor_diameter_min=45.319,
                               thread_class="4g6g", diameter=48, pitch=2)
thread["4g6g"][48][1.5] = Thread(major_diameter_max=47.968, major_diameter_min=47.732, pitch_diameter_max=46.994,
                                 pitch_diameter_min=46.894, minor_diameter_max=46.344, minor_diameter_min=45.970,
                                 thread_class="4g6g", diameter=48, pitch=1.5)
thread["4g6g"][50][4] = Thread(major_diameter_max=49.940, major_diameter_min=49.465, pitch_diameter_max=47.342,
                               pitch_diameter_min=47.192, minor_diameter_max=45.610, minor_diameter_min=44.728,
                               thread_class="4g6g", diameter=50, pitch=4)
thread["4g6g"][50][3] = Thread(major_diameter_max=49.952, major_diameter_min=49.577, pitch_diameter_max=48.003,
                               pitch_diameter_min=47.871, minor_diameter_max=46.704, minor_diameter_min=46.023,
                               thread_class="4g6g", diameter=50, pitch=3)
thread["4g6g"][50][2] = Thread(major_diameter_max=49.962, major_diameter_min=49.682, pitch_diameter_max=48.663,
                               pitch_diameter_min=48.551, minor_diameter_max=47.797, minor_diameter_min=47.319,
                               thread_class="4g6g", diameter=50, pitch=2)
thread["4g6g"][50][1.5] = Thread(major_diameter_max=49.968, major_diameter_min=49.732, pitch_diameter_max=48.994,
                                 pitch_diameter_min=48.894, minor_diameter_max=48.344, minor_diameter_min=47.970,
                                 thread_class="4g6g", diameter=50, pitch=1.5)
thread["4g6g"][52][5] = Thread(major_diameter_max=51.929, major_diameter_min=51.399, pitch_diameter_max=48.681,
                               pitch_diameter_min=48.531, minor_diameter_max=46.516, minor_diameter_min=45.451,
                               thread_class="4g6g", diameter=52, pitch=5)
thread["4g6g"][52][4] = Thread(major_diameter_max=51.940, major_diameter_min=51.465, pitch_diameter_max=49.342,
                               pitch_diameter_min=49.192, minor_diameter_max=47.610, minor_diameter_min=46.728,
                               thread_class="4g6g", diameter=52, pitch=4)
thread["4g6g"][52][3] = Thread(major_diameter_max=51.952, major_diameter_min=51.577, pitch_diameter_max=50.003,
                               pitch_diameter_min=49.871, minor_diameter_max=48.704, minor_diameter_min=48.023,
                               thread_class="4g6g", diameter=52, pitch=3)
thread["4g6g"][52][2] = Thread(major_diameter_max=51.962, major_diameter_min=51.682, pitch_diameter_max=50.663,
                               pitch_diameter_min=50.551, minor_diameter_max=49.797, minor_diameter_min=49.319,
                               thread_class="4g6g", diameter=52, pitch=2)
thread["4g6g"][52][1.5] = Thread(major_diameter_max=51.968, major_diameter_min=51.732, pitch_diameter_max=50.994,
                                 pitch_diameter_min=50.894, minor_diameter_max=50.344, minor_diameter_min=49.970,
                                 thread_class="4g6g", diameter=52, pitch=1.5)
thread["4g6g"][55][4] = Thread(major_diameter_max=54.940, major_diameter_min=54.465, pitch_diameter_max=52.342,
                               pitch_diameter_min=52.192, minor_diameter_max=50.610, minor_diameter_min=49.728,
                               thread_class="4g6g", diameter=55, pitch=4)
thread["4g6g"][55][3] = Thread(major_diameter_max=54.952, major_diameter_min=54.577, pitch_diameter_max=53.003,
                               pitch_diameter_min=52.871, minor_diameter_max=51.704, minor_diameter_min=51.023,
                               thread_class="4g6g", diameter=55, pitch=3)
thread["4g6g"][55][2] = Thread(major_diameter_max=54.962, major_diameter_min=54.682, pitch_diameter_max=53.663,
                               pitch_diameter_min=53.551, minor_diameter_max=52.797, minor_diameter_min=52.319,
                               thread_class="4g6g", diameter=55, pitch=2)
thread["4g6g"][55][1.5] = Thread(major_diameter_max=54.968, major_diameter_min=54.732, pitch_diameter_max=53.994,
                                 pitch_diameter_min=53.894, minor_diameter_max=53.344, minor_diameter_min=52.970,
                                 thread_class="4g6g", diameter=55, pitch=1.5)
thread["4g6g"][56][5.5] = Thread(major_diameter_max=55.925, major_diameter_min=55.365, pitch_diameter_max=52.353,
                                 pitch_diameter_min=52.183, minor_diameter_max=49.971, minor_diameter_min=48.795,
                                 thread_class="4g6g", diameter=56, pitch=5.5)
thread["4g6g"][56][4] = Thread(major_diameter_max=55.940, major_diameter_min=55.465, pitch_diameter_max=53.342,
                               pitch_diameter_min=53.192, minor_diameter_max=51.610, minor_diameter_min=50.728,
                               thread_class="4g6g", diameter=56, pitch=4)
thread["4g6g"][56][3] = Thread(major_diameter_max=55.952, major_diameter_min=55.577, pitch_diameter_max=54.003,
                               pitch_diameter_min=53.871, minor_diameter_max=52.704, minor_diameter_min=52.023,
                               thread_class="4g6g", diameter=56, pitch=3)
thread["4g6g"][56][2] = Thread(major_diameter_max=55.962, major_diameter_min=55.682, pitch_diameter_max=54.663,
                               pitch_diameter_min=54.551, minor_diameter_max=53.797, minor_diameter_min=53.319,
                               thread_class="4g6g", diameter=56, pitch=2)
thread["4g6g"][56][1.5] = Thread(major_diameter_max=55.968, major_diameter_min=55.732, pitch_diameter_max=54.994,
                                 pitch_diameter_min=54.894, minor_diameter_max=54.344, minor_diameter_min=53.970,
                                 thread_class="4g6g", diameter=56, pitch=1.5)
thread["4g6g"][56][1] = Thread(major_diameter_max=55.974, major_diameter_min=55.794, pitch_diameter_max=55.324,
                               pitch_diameter_min=55.234, minor_diameter_max=54.891, minor_diameter_min=54.618,
                               thread_class="4g6g", diameter=56, pitch=1)
thread["4g6g"][58][4] = Thread(major_diameter_max=57.940, major_diameter_min=57.465, pitch_diameter_max=55.342,
                               pitch_diameter_min=55.192, minor_diameter_max=53.610, minor_diameter_min=52.728,
                               thread_class="4g6g", diameter=58, pitch=4)
thread["4g6g"][58][3] = Thread(major_diameter_max=57.952, major_diameter_min=57.577, pitch_diameter_max=56.003,
                               pitch_diameter_min=55.871, minor_diameter_max=54.704, minor_diameter_min=54.023,
                               thread_class="4g6g", diameter=58, pitch=3)
thread["4g6g"][58][2] = Thread(major_diameter_max=57.962, major_diameter_min=57.682, pitch_diameter_max=56.663,
                               pitch_diameter_min=56.551, minor_diameter_max=55.797, minor_diameter_min=55.319,
                               thread_class="4g6g", diameter=58, pitch=2)
thread["4g6g"][58][1.5] = Thread(major_diameter_max=57.968, major_diameter_min=57.732, pitch_diameter_max=56.994,
                                 pitch_diameter_min=56.894, minor_diameter_max=56.344, minor_diameter_min=55.970,
                                 thread_class="4g6g", diameter=58, pitch=1.5)
thread["4g6g"][60][5.5] = Thread(major_diameter_max=59.925, major_diameter_min=59.365, pitch_diameter_max=56.353,
                                 pitch_diameter_min=56.183, minor_diameter_max=53.971, minor_diameter_min=52.795,
                                 thread_class="4g6g", diameter=60, pitch=5.5)
thread["4g6g"][60][4] = Thread(major_diameter_max=59.940, major_diameter_min=59.465, pitch_diameter_max=57.342,
                               pitch_diameter_min=57.192, minor_diameter_max=55.610, minor_diameter_min=54.728,
                               thread_class="4g6g", diameter=60, pitch=4)
thread["4g6g"][60][3] = Thread(major_diameter_max=59.952, major_diameter_min=59.577, pitch_diameter_max=58.003,
                               pitch_diameter_min=57.871, minor_diameter_max=56.704, minor_diameter_min=56.023,
                               thread_class="4g6g", diameter=60, pitch=3)
thread["4g6g"][60][2] = Thread(major_diameter_max=59.962, major_diameter_min=59.682, pitch_diameter_max=58.663,
                               pitch_diameter_min=58.551, minor_diameter_max=57.797, minor_diameter_min=57.319,
                               thread_class="4g6g", diameter=60, pitch=2)
thread["4g6g"][60][1.5] = Thread(major_diameter_max=59.968, major_diameter_min=59.732, pitch_diameter_max=58.994,
                                 pitch_diameter_min=58.894, minor_diameter_max=58.344, minor_diameter_min=57.970,
                                 thread_class="4g6g", diameter=60, pitch=1.5)
thread["4g6g"][60][1] = Thread(major_diameter_max=59.974, major_diameter_min=59.794, pitch_diameter_max=59.324,
                               pitch_diameter_min=59.234, minor_diameter_max=58.891, minor_diameter_min=58.618,
                               thread_class="4g6g", diameter=60, pitch=1)
thread["4g6g"][62][4] = Thread(major_diameter_max=61.940, major_diameter_min=61.465, pitch_diameter_max=59.342,
                               pitch_diameter_min=59.192, minor_diameter_max=57.610, minor_diameter_min=56.728,
                               thread_class="4g6g", diameter=62, pitch=4)
thread["4g6g"][62][3] = Thread(major_diameter_max=61.952, major_diameter_min=61.577, pitch_diameter_max=60.003,
                               pitch_diameter_min=59.871, minor_diameter_max=58.704, minor_diameter_min=58.023,
                               thread_class="4g6g", diameter=62, pitch=3)
thread["4g6g"][62][2] = Thread(major_diameter_max=61.962, major_diameter_min=61.682, pitch_diameter_max=60.663,
                               pitch_diameter_min=60.551, minor_diameter_max=59.797, minor_diameter_min=59.319,
                               thread_class="4g6g", diameter=62, pitch=2)
thread["4g6g"][62][1.5] = Thread(major_diameter_max=61.968, major_diameter_min=61.732, pitch_diameter_max=60.994,
                                 pitch_diameter_min=60.894, minor_diameter_max=60.344, minor_diameter_min=59.970,
                                 thread_class="4g6g", diameter=62, pitch=1.5)
thread["4g6g"][63][1.5] = Thread(major_diameter_max=62.968, major_diameter_min=62.732, pitch_diameter_max=61.994,
                                 pitch_diameter_min=61.894, minor_diameter_max=61.344, minor_diameter_min=60.970,
                                 thread_class="4g6g", diameter=63, pitch=1.5)
thread["4g6g"][64][6] = Thread(major_diameter_max=63.920, major_diameter_min=63.320, pitch_diameter_max=60.023,
                               pitch_diameter_min=59.843, minor_diameter_max=57.425, minor_diameter_min=56.147,
                               thread_class="4g6g", diameter=64, pitch=6)
thread["4g6g"][64][5.5] = Thread(major_diameter_max=63.925, major_diameter_min=63.365, pitch_diameter_max=60.353,
                                 pitch_diameter_min=60.183, minor_diameter_max=57.971, minor_diameter_min=56.795,
                                 thread_class="4g6g", diameter=64, pitch=5.5)
thread["4g6g"][64][4] = Thread(major_diameter_max=63.940, major_diameter_min=63.465, pitch_diameter_max=61.342,
                               pitch_diameter_min=61.192, minor_diameter_max=59.610, minor_diameter_min=58.728,
                               thread_class="4g6g", diameter=64, pitch=4)
thread["4g6g"][64][3] = Thread(major_diameter_max=63.952, major_diameter_min=63.577, pitch_diameter_max=62.003,
                               pitch_diameter_min=61.871, minor_diameter_max=60.704, minor_diameter_min=60.023,
                               thread_class="4g6g", diameter=64, pitch=3)
thread["4g6g"][64][2] = Thread(major_diameter_max=63.962, major_diameter_min=63.682, pitch_diameter_max=62.663,
                               pitch_diameter_min=62.551, minor_diameter_max=61.797, minor_diameter_min=61.319,
                               thread_class="4g6g", diameter=64, pitch=2)
thread["4g6g"][64][1.5] = Thread(major_diameter_max=63.968, major_diameter_min=63.732, pitch_diameter_max=62.994,
                                 pitch_diameter_min=62.894, minor_diameter_max=62.344, minor_diameter_min=61.970,
                                 thread_class="4g6g", diameter=64, pitch=1.5)
thread["4g6g"][64][1] = Thread(major_diameter_max=63.974, major_diameter_min=63.794, pitch_diameter_max=63.324,
                               pitch_diameter_min=63.234, minor_diameter_max=62.891, minor_diameter_min=62.618,
                               thread_class="4g6g", diameter=64, pitch=1)
thread["4g6g"][65][4] = Thread(major_diameter_max=64.940, major_diameter_min=64.465, pitch_diameter_max=62.342,
                               pitch_diameter_min=62.192, minor_diameter_max=60.610, minor_diameter_min=59.728,
                               thread_class="4g6g", diameter=65, pitch=4)
thread["4g6g"][65][3] = Thread(major_diameter_max=64.952, major_diameter_min=64.577, pitch_diameter_max=63.003,
                               pitch_diameter_min=62.871, minor_diameter_max=61.704, minor_diameter_min=61.023,
                               thread_class="4g6g", diameter=65, pitch=3)
thread["4g6g"][65][2] = Thread(major_diameter_max=64.962, major_diameter_min=64.682, pitch_diameter_max=63.663,
                               pitch_diameter_min=63.551, minor_diameter_max=62.797, minor_diameter_min=62.319,
                               thread_class="4g6g", diameter=65, pitch=2)
thread["4g6g"][65][1.5] = Thread(major_diameter_max=64.968, major_diameter_min=64.732, pitch_diameter_max=63.994,
                                 pitch_diameter_min=63.894, minor_diameter_max=63.344, minor_diameter_min=62.970,
                                 thread_class="4g6g", diameter=65, pitch=1.5)
thread["4g6g"][68][6] = Thread(major_diameter_max=67.920, major_diameter_min=67.320, pitch_diameter_max=64.023,
                               pitch_diameter_min=63.843, minor_diameter_max=61.425, minor_diameter_min=60.147,
                               thread_class="4g6g", diameter=68, pitch=6)
thread["4g6g"][68][4] = Thread(major_diameter_max=67.940, major_diameter_min=67.465, pitch_diameter_max=65.342,
                               pitch_diameter_min=65.192, minor_diameter_max=63.610, minor_diameter_min=62.728,
                               thread_class="4g6g", diameter=68, pitch=4)
thread["4g6g"][68][3] = Thread(major_diameter_max=67.952, major_diameter_min=67.577, pitch_diameter_max=66.003,
                               pitch_diameter_min=65.871, minor_diameter_max=64.704, minor_diameter_min=64.023,
                               thread_class="4g6g", diameter=68, pitch=3)
thread["4g6g"][68][2] = Thread(major_diameter_max=67.962, major_diameter_min=67.682, pitch_diameter_max=66.663,
                               pitch_diameter_min=66.551, minor_diameter_max=65.797, minor_diameter_min=65.319,
                               thread_class="4g6g", diameter=68, pitch=2)
thread["4g6g"][68][1.5] = Thread(major_diameter_max=67.968, major_diameter_min=67.732, pitch_diameter_max=66.994,
                                 pitch_diameter_min=66.894, minor_diameter_max=66.344, minor_diameter_min=65.970,
                                 thread_class="4g6g", diameter=68, pitch=1.5)
thread["4g6g"][68][1] = Thread(major_diameter_max=67.974, major_diameter_min=67.794, pitch_diameter_max=67.324,
                               pitch_diameter_min=67.234, minor_diameter_max=66.891, minor_diameter_min=66.618,
                               thread_class="4g6g", diameter=68, pitch=1)
thread["4g6g"][70][6] = Thread(major_diameter_max=69.920, major_diameter_min=69.320, pitch_diameter_max=66.023,
                               pitch_diameter_min=65.843, minor_diameter_max=63.425, minor_diameter_min=62.147,
                               thread_class="4g6g", diameter=70, pitch=6)
thread["4g6g"][70][4] = Thread(major_diameter_max=69.940, major_diameter_min=69.465, pitch_diameter_max=67.342,
                               pitch_diameter_min=67.192, minor_diameter_max=65.610, minor_diameter_min=64.728,
                               thread_class="4g6g", diameter=70, pitch=4)
thread["4g6g"][70][3] = Thread(major_diameter_max=69.952, major_diameter_min=69.577, pitch_diameter_max=68.003,
                               pitch_diameter_min=67.871, minor_diameter_max=66.704, minor_diameter_min=66.023,
                               thread_class="4g6g", diameter=70, pitch=3)
thread["4g6g"][70][2] = Thread(major_diameter_max=69.962, major_diameter_min=69.682, pitch_diameter_max=68.663,
                               pitch_diameter_min=68.551, minor_diameter_max=67.797, minor_diameter_min=67.319,
                               thread_class="4g6g", diameter=70, pitch=2)
thread["4g6g"][70][1.5] = Thread(major_diameter_max=69.968, major_diameter_min=69.732, pitch_diameter_max=68.994,
                                 pitch_diameter_min=68.894, minor_diameter_max=68.344, minor_diameter_min=67.970,
                                 thread_class="4g6g", diameter=70, pitch=1.5)
thread["4g6g"][72][6] = Thread(major_diameter_max=71.920, major_diameter_min=71.320, pitch_diameter_max=68.023,
                               pitch_diameter_min=67.843, minor_diameter_max=65.425, minor_diameter_min=64.147,
                               thread_class="4g6g", diameter=72, pitch=6)
thread["4g6g"][72][4] = Thread(major_diameter_max=71.940, major_diameter_min=71.465, pitch_diameter_max=69.342,
                               pitch_diameter_min=69.192, minor_diameter_max=67.610, minor_diameter_min=66.728,
                               thread_class="4g6g", diameter=72, pitch=4)
thread["4g6g"][72][3] = Thread(major_diameter_max=71.952, major_diameter_min=71.577, pitch_diameter_max=70.003,
                               pitch_diameter_min=69.871, minor_diameter_max=68.704, minor_diameter_min=68.023,
                               thread_class="4g6g", diameter=72, pitch=3)
thread["4g6g"][72][2] = Thread(major_diameter_max=71.962, major_diameter_min=71.682, pitch_diameter_max=70.663,
                               pitch_diameter_min=70.551, minor_diameter_max=69.797, minor_diameter_min=69.319,
                               thread_class="4g6g", diameter=72, pitch=2)
thread["4g6g"][72][1.5] = Thread(major_diameter_max=71.968, major_diameter_min=71.732, pitch_diameter_max=70.994,
                                 pitch_diameter_min=70.894, minor_diameter_max=70.344, minor_diameter_min=69.970,
                                 thread_class="4g6g", diameter=72, pitch=1.5)
thread["4g6g"][72][1] = Thread(major_diameter_max=71.974, major_diameter_min=71.794, pitch_diameter_max=71.324,
                               pitch_diameter_min=71.234, minor_diameter_max=70.891, minor_diameter_min=70.618,
                               thread_class="4g6g", diameter=72, pitch=1)
thread["4g6g"][75][6] = Thread(major_diameter_max=74.920, major_diameter_min=74.320, pitch_diameter_max=71.023,
                               pitch_diameter_min=70.843, minor_diameter_max=68.425, minor_diameter_min=67.147,
                               thread_class="4g6g", diameter=75, pitch=6)
thread["4g6g"][75][4] = Thread(major_diameter_max=74.940, major_diameter_min=74.465, pitch_diameter_max=72.342,
                               pitch_diameter_min=72.192, minor_diameter_max=70.610, minor_diameter_min=69.728,
                               thread_class="4g6g", diameter=75, pitch=4)
thread["4g6g"][75][3] = Thread(major_diameter_max=74.952, major_diameter_min=74.577, pitch_diameter_max=73.003,
                               pitch_diameter_min=72.871, minor_diameter_max=71.704, minor_diameter_min=71.023,
                               thread_class="4g6g", diameter=75, pitch=3)
thread["4g6g"][75][2] = Thread(major_diameter_max=74.962, major_diameter_min=74.682, pitch_diameter_max=73.663,
                               pitch_diameter_min=73.551, minor_diameter_max=72.797, minor_diameter_min=72.319,
                               thread_class="4g6g", diameter=75, pitch=2)
thread["4g6g"][75][1.5] = Thread(major_diameter_max=74.968, major_diameter_min=74.732, pitch_diameter_max=73.994,
                                 pitch_diameter_min=73.894, minor_diameter_max=73.344, minor_diameter_min=72.970,
                                 thread_class="4g6g", diameter=75, pitch=1.5)
thread["4g6g"][76][6] = Thread(major_diameter_max=75.920, major_diameter_min=75.320, pitch_diameter_max=72.023,
                               pitch_diameter_min=71.843, minor_diameter_max=69.425, minor_diameter_min=68.147,
                               thread_class="4g6g", diameter=76, pitch=6)
thread["4g6g"][76][4] = Thread(major_diameter_max=75.940, major_diameter_min=75.465, pitch_diameter_max=73.342,
                               pitch_diameter_min=73.192, minor_diameter_max=71.610, minor_diameter_min=70.728,
                               thread_class="4g6g", diameter=76, pitch=4)
thread["4g6g"][76][3] = Thread(major_diameter_max=75.952, major_diameter_min=75.577, pitch_diameter_max=74.003,
                               pitch_diameter_min=73.871, minor_diameter_max=72.704, minor_diameter_min=72.023,
                               thread_class="4g6g", diameter=76, pitch=3)
thread["4g6g"][76][2] = Thread(major_diameter_max=75.962, major_diameter_min=75.682, pitch_diameter_max=74.663,
                               pitch_diameter_min=74.551, minor_diameter_max=73.797, minor_diameter_min=73.319,
                               thread_class="4g6g", diameter=76, pitch=2)
thread["4g6g"][76][1.5] = Thread(major_diameter_max=75.968, major_diameter_min=75.732, pitch_diameter_max=74.994,
                                 pitch_diameter_min=74.894, minor_diameter_max=74.344, minor_diameter_min=73.970,
                                 thread_class="4g6g", diameter=76, pitch=1.5)
thread["4g6g"][76][1] = Thread(major_diameter_max=75.974, major_diameter_min=75.794, pitch_diameter_max=75.324,
                               pitch_diameter_min=75.234, minor_diameter_max=74.891, minor_diameter_min=74.618,
                               thread_class="4g6g", diameter=76, pitch=1)
thread["4g6g"][78][2] = Thread(major_diameter_max=77.962, major_diameter_min=77.682, pitch_diameter_max=76.663,
                               pitch_diameter_min=76.551, minor_diameter_max=75.797, minor_diameter_min=75.319,
                               thread_class="4g6g", diameter=78, pitch=2)
thread["4g6g"][80][6] = Thread(major_diameter_max=79.920, major_diameter_min=79.320, pitch_diameter_max=76.023,
                               pitch_diameter_min=75.843, minor_diameter_max=73.425, minor_diameter_min=72.147,
                               thread_class="4g6g", diameter=80, pitch=6)
thread["4g6g"][80][4] = Thread(major_diameter_max=79.940, major_diameter_min=79.340, pitch_diameter_max=77.342,
                               pitch_diameter_min=77.192, minor_diameter_max=75.610, minor_diameter_min=74.728,
                               thread_class="4g6g", diameter=80, pitch=4)
thread["4g6g"][80][3] = Thread(major_diameter_max=79.952, major_diameter_min=79.577, pitch_diameter_max=78.003,
                               pitch_diameter_min=77.871, minor_diameter_max=76.704, minor_diameter_min=76.023,
                               thread_class="4g6g", diameter=80, pitch=3)
thread["4g6g"][80][2] = Thread(major_diameter_max=79.962, major_diameter_min=79.682, pitch_diameter_max=78.663,
                               pitch_diameter_min=78.551, minor_diameter_max=77.797, minor_diameter_min=77.319,
                               thread_class="4g6g", diameter=80, pitch=2)
thread["4g6g"][80][1.5] = Thread(major_diameter_max=79.968, major_diameter_min=79.732, pitch_diameter_max=78.994,
                                 pitch_diameter_min=78.894, minor_diameter_max=78.334, minor_diameter_min=77.970,
                                 thread_class="4g6g", diameter=80, pitch=1.5)
thread["4g6g"][80][1] = Thread(major_diameter_max=79.974, major_diameter_min=79.794, pitch_diameter_max=79.324,
                               pitch_diameter_min=79.234, minor_diameter_max=78.891, minor_diameter_min=78.618,
                               thread_class="4g6g", diameter=80, pitch=1)
thread["4g6g"][82][2] = Thread(major_diameter_max=81.962, major_diameter_min=81.682, pitch_diameter_max=80.663,
                               pitch_diameter_min=80.551, minor_diameter_max=79.797, minor_diameter_min=79.319,
                               thread_class="4g6g", diameter=82, pitch=2)
thread["4g6g"][85][6] = Thread(major_diameter_max=84.920, major_diameter_min=84.320, pitch_diameter_max=81.023,
                               pitch_diameter_min=80.843, minor_diameter_max=78.425, minor_diameter_min=77.147,
                               thread_class="4g6g", diameter=85, pitch=6)
thread["4g6g"][85][4] = Thread(major_diameter_max=84.940, major_diameter_min=84.465, pitch_diameter_max=82.342,
                               pitch_diameter_min=82.192, minor_diameter_max=80.610, minor_diameter_min=79.728,
                               thread_class="4g6g", diameter=85, pitch=4)
thread["4g6g"][85][3] = Thread(major_diameter_max=84.952, major_diameter_min=84.577, pitch_diameter_max=83.003,
                               pitch_diameter_min=82.871, minor_diameter_max=81.704, minor_diameter_min=81.023,
                               thread_class="4g6g", diameter=85, pitch=3)
thread["4g6g"][85][2] = Thread(major_diameter_max=84.962, major_diameter_min=84.682, pitch_diameter_max=83.663,
                               pitch_diameter_min=83.551, minor_diameter_max=82.797, minor_diameter_min=82.319,
                               thread_class="4g6g", diameter=85, pitch=2)
thread["4g6g"][85][1.5] = Thread(major_diameter_max=84.968, major_diameter_min=84.732, pitch_diameter_max=83.994,
                                 pitch_diameter_min=83.894, minor_diameter_max=83.344, minor_diameter_min=82.970,
                                 thread_class="4g6g", diameter=85, pitch=1.5)
thread["4g6g"][90][6] = Thread(major_diameter_max=89.920, major_diameter_min=89.320, pitch_diameter_max=86.023,
                               pitch_diameter_min=85.843, minor_diameter_max=83.425, minor_diameter_min=82.147,
                               thread_class="4g6g", diameter=90, pitch=6)
thread["4g6g"][90][4] = Thread(major_diameter_max=89.940, major_diameter_min=89.465, pitch_diameter_max=87.342,
                               pitch_diameter_min=87.192, minor_diameter_max=85.610, minor_diameter_min=84.728,
                               thread_class="4g6g", diameter=90, pitch=4)
thread["4g6g"][90][3] = Thread(major_diameter_max=89.952, major_diameter_min=89.577, pitch_diameter_max=88.003,
                               pitch_diameter_min=87.871, minor_diameter_max=86.704, minor_diameter_min=86.023,
                               thread_class="4g6g", diameter=90, pitch=3)
thread["4g6g"][90][2] = Thread(major_diameter_max=89.962, major_diameter_min=89.682, pitch_diameter_max=88.663,
                               pitch_diameter_min=88.551, minor_diameter_max=87.797, minor_diameter_min=87.319,
                               thread_class="4g6g", diameter=90, pitch=2)
thread["4g6g"][90][1.5] = Thread(major_diameter_max=89.968, major_diameter_min=89.732, pitch_diameter_max=88.994,
                                 pitch_diameter_min=88.894, minor_diameter_max=88.344, minor_diameter_min=87.970,
                                 thread_class="4g6g", diameter=90, pitch=1.5)
thread["4g6g"][95][6] = Thread(major_diameter_max=94.920, major_diameter_min=94.320, pitch_diameter_max=91.023,
                               pitch_diameter_min=90.833, minor_diameter_max=88.425, minor_diameter_min=87.137,
                               thread_class="4g6g", diameter=95, pitch=6)
thread["4g6g"][95][4] = Thread(major_diameter_max=94.940, major_diameter_min=94.465, pitch_diameter_max=92.342,
                               pitch_diameter_min=92.182, minor_diameter_max=90.610, minor_diameter_min=89.718,
                               thread_class="4g6g", diameter=95, pitch=4)
thread["4g6g"][95][3] = Thread(major_diameter_max=94.952, major_diameter_min=94.577, pitch_diameter_max=93.003,
                               pitch_diameter_min=92.863, minor_diameter_max=91.704, minor_diameter_min=91.015,
                               thread_class="4g6g", diameter=95, pitch=3)
thread["4g6g"][95][2] = Thread(major_diameter_max=94.962, major_diameter_min=94.682, pitch_diameter_max=93.663,
                               pitch_diameter_min=93.545, minor_diameter_max=92.797, minor_diameter_min=92.313,
                               thread_class="4g6g", diameter=95, pitch=2)
thread["4g6g"][95][1.5] = Thread(major_diameter_max=94.968, major_diameter_min=94.732, pitch_diameter_max=93.994,
                                 pitch_diameter_min=93.882, minor_diameter_max=93.344, minor_diameter_min=92.958,
                                 thread_class="4g6g", diameter=95, pitch=1.5)
thread["4g6g"][100][6] = Thread(major_diameter_max=99.920, major_diameter_min=99.320, pitch_diameter_max=96.023,
                                pitch_diameter_min=95.833, minor_diameter_max=93.425, minor_diameter_min=92.137,
                                thread_class="4g6g", diameter=100, pitch=6)
thread["4g6g"][100][4] = Thread(major_diameter_max=99.940, major_diameter_min=99.465, pitch_diameter_max=97.342,
                                pitch_diameter_min=97.182, minor_diameter_max=95.610, minor_diameter_min=94.718,
                                thread_class="4g6g", diameter=100, pitch=4)
thread["4g6g"][100][3] = Thread(major_diameter_max=99.952, major_diameter_min=99.577, pitch_diameter_max=98.003,
                                pitch_diameter_min=97.863, minor_diameter_max=96.704, minor_diameter_min=96.015,
                                thread_class="4g6g", diameter=100, pitch=3)
thread["4g6g"][100][2] = Thread(major_diameter_max=99.962, major_diameter_min=99.682, pitch_diameter_max=98.663,
                                pitch_diameter_min=98.545, minor_diameter_max=97.797, minor_diameter_min=97.313,
                                thread_class="4g6g", diameter=100, pitch=2)
thread["4g6g"][100][1.5] = Thread(major_diameter_max=99.968, major_diameter_min=99.732, pitch_diameter_max=98.994,
                                  pitch_diameter_min=98.882, minor_diameter_max=98.344, minor_diameter_min=97.958,
                                  thread_class="4g6g", diameter=100, pitch=1.5)
thread["4g6g"][105][6] = Thread(major_diameter_max=104.920, major_diameter_min=104.320, pitch_diameter_max=101.023,
                                pitch_diameter_min=100.833, minor_diameter_max=98.425, minor_diameter_min=97.137,
                                thread_class="4g6g", diameter=105, pitch=6)
thread["4g6g"][105][4] = Thread(major_diameter_max=104.940, major_diameter_min=104.465, pitch_diameter_max=102.342,
                                pitch_diameter_min=102.182, minor_diameter_max=100.610, minor_diameter_min=99.718,
                                thread_class="4g6g", diameter=105, pitch=4)
thread["4g6g"][105][3] = Thread(major_diameter_max=104.952, major_diameter_min=104.577, pitch_diameter_max=103.003,
                                pitch_diameter_min=102.863, minor_diameter_max=101.704, minor_diameter_min=101.015,
                                thread_class="4g6g", diameter=105, pitch=3)
thread["4g6g"][105][2] = Thread(major_diameter_max=104.962, major_diameter_min=104.682, pitch_diameter_max=103.663,
                                pitch_diameter_min=103.545, minor_diameter_max=102.797, minor_diameter_min=102.313,
                                thread_class="4g6g", diameter=105, pitch=2)
thread["4g6g"][105][1.5] = Thread(major_diameter_max=104.968, major_diameter_min=104.732, pitch_diameter_max=103.994,
                                  pitch_diameter_min=103.882, minor_diameter_max=103.344, minor_diameter_min=102.958,
                                  thread_class="4g6g", diameter=105, pitch=1.5)
thread["4g6g"][110][6] = Thread(major_diameter_max=109.920, major_diameter_min=109.320, pitch_diameter_max=106.023,
                                pitch_diameter_min=105.833, minor_diameter_max=103.425, minor_diameter_min=102.137,
                                thread_class="4g6g", diameter=110, pitch=6)
thread["4g6g"][110][4] = Thread(major_diameter_max=109.940, major_diameter_min=109.465, pitch_diameter_max=107.342,
                                pitch_diameter_min=107.182, minor_diameter_max=105.610, minor_diameter_min=104.718,
                                thread_class="4g6g", diameter=110, pitch=4)
thread["4g6g"][110][3] = Thread(major_diameter_max=109.952, major_diameter_min=109.577, pitch_diameter_max=108.003,
                                pitch_diameter_min=107.863, minor_diameter_max=106.704, minor_diameter_min=106.015,
                                thread_class="4g6g", diameter=110, pitch=3)
thread["4g6g"][110][2] = Thread(major_diameter_max=109.962, major_diameter_min=109.682, pitch_diameter_max=108.663,
                                pitch_diameter_min=108.545, minor_diameter_max=107.797, minor_diameter_min=107.313,
                                thread_class="4g6g", diameter=110, pitch=2)
thread["4g6g"][110][1.5] = Thread(major_diameter_max=109.968, major_diameter_min=109.732, pitch_diameter_max=108.994,
                                  pitch_diameter_min=108.882, minor_diameter_max=108.344, minor_diameter_min=107.958,
                                  thread_class="4g6g", diameter=110, pitch=1.5)
thread["4g6g"][115][6] = Thread(major_diameter_max=114.920, major_diameter_min=114.320, pitch_diameter_max=111.023,
                                pitch_diameter_min=110.833, minor_diameter_max=108.425, minor_diameter_min=107.137,
                                thread_class="4g6g", diameter=115, pitch=6)
thread["4g6g"][115][4] = Thread(major_diameter_max=114.940, major_diameter_min=114.465, pitch_diameter_max=112.342,
                                pitch_diameter_min=112.182, minor_diameter_max=110.610, minor_diameter_min=109.718,
                                thread_class="4g6g", diameter=115, pitch=4)
thread["4g6g"][115][3] = Thread(major_diameter_max=114.952, major_diameter_min=114.577, pitch_diameter_max=113.003,
                                pitch_diameter_min=112.863, minor_diameter_max=111.704, minor_diameter_min=111.015,
                                thread_class="4g6g", diameter=115, pitch=3)
thread["4g6g"][115][2] = Thread(major_diameter_max=114.962, major_diameter_min=114.682, pitch_diameter_max=113.663,
                                pitch_diameter_min=113.543, minor_diameter_max=112.797, minor_diameter_min=112.311,
                                thread_class="4g6g", diameter=115, pitch=2)
thread["4g6g"][115][1.5] = Thread(major_diameter_max=114.968, major_diameter_min=114.732, pitch_diameter_max=113.994,
                                  pitch_diameter_min=113.882, minor_diameter_max=113.344, minor_diameter_min=112.958,
                                  thread_class="4g6g", diameter=115, pitch=1.5)
thread["4g6g"][120][6] = Thread(major_diameter_max=119.920, major_diameter_min=119.320, pitch_diameter_max=116.023,
                                pitch_diameter_min=115.833, minor_diameter_max=113.425, minor_diameter_min=112.137,
                                thread_class="4g6g", diameter=120, pitch=6)
thread["4g6g"][120][4] = Thread(major_diameter_max=119.940, major_diameter_min=119.465, pitch_diameter_max=117.342,
                                pitch_diameter_min=117.182, minor_diameter_max=115.610, minor_diameter_min=114.718,
                                thread_class="4g6g", diameter=120, pitch=4)
thread["4g6g"][120][3] = Thread(major_diameter_max=119.952, major_diameter_min=119.577, pitch_diameter_max=118.003,
                                pitch_diameter_min=117.863, minor_diameter_max=116.704, minor_diameter_min=116.015,
                                thread_class="4g6g", diameter=120, pitch=3)
thread["4g6g"][120][2] = Thread(major_diameter_max=119.962, major_diameter_min=119.682, pitch_diameter_max=118.663,
                                pitch_diameter_min=118.545, minor_diameter_max=117.797, minor_diameter_min=117.313,
                                thread_class="4g6g", diameter=120, pitch=2)
thread["4g6g"][120][1.5] = Thread(major_diameter_max=119.968, major_diameter_min=119.732, pitch_diameter_max=118.994,
                                  pitch_diameter_min=118.882, minor_diameter_max=118.344, minor_diameter_min=117.958,
                                  thread_class="4g6g", diameter=120, pitch=1.5)
thread["4g6g"][125][8] = Thread(major_diameter_max=124.900, major_diameter_min=124.190, pitch_diameter_max=119.704,
                                pitch_diameter_min=119.492, minor_diameter_max=116.240, minor_diameter_min=114.564,
                                thread_class="4g6g", diameter=125, pitch=8)
thread["4g6g"][125][6] = Thread(major_diameter_max=124.920, major_diameter_min=124.320, pitch_diameter_max=121.023,
                                pitch_diameter_min=120.833, minor_diameter_max=118.425, minor_diameter_min=117.137,
                                thread_class="4g6g", diameter=125, pitch=6)
thread["4g6g"][125][4] = Thread(major_diameter_max=124.940, major_diameter_min=124.465, pitch_diameter_max=122.342,
                                pitch_diameter_min=122.182, minor_diameter_max=120.610, minor_diameter_min=119.718,
                                thread_class="4g6g", diameter=125, pitch=4)
thread["4g6g"][125][3] = Thread(major_diameter_max=124.952, major_diameter_min=124.577, pitch_diameter_max=123.003,
                                pitch_diameter_min=122.863, minor_diameter_max=121.704, minor_diameter_min=121.015,
                                thread_class="4g6g", diameter=125, pitch=3)
thread["4g6g"][125][2] = Thread(major_diameter_max=124.962, major_diameter_min=124.682, pitch_diameter_max=123.663,
                                pitch_diameter_min=123.543, minor_diameter_max=122.797, minor_diameter_min=122.311,
                                thread_class="4g6g", diameter=125, pitch=2)
thread["4g6g"][125][1.5] = Thread(major_diameter_max=124.968, major_diameter_min=124.732, pitch_diameter_max=123.994,
                                  pitch_diameter_min=123.882, minor_diameter_max=123.344, minor_diameter_min=122.958,
                                  thread_class="4g6g", diameter=125, pitch=1.5)
thread["4g6g"][130][8] = Thread(major_diameter_max=129.900, major_diameter_min=129.190, pitch_diameter_max=124.704,
                                pitch_diameter_min=124.492, minor_diameter_max=121.240, minor_diameter_min=119.564,
                                thread_class="4g6g", diameter=130, pitch=8)
thread["4g6g"][130][6] = Thread(major_diameter_max=129.920, major_diameter_min=129.320, pitch_diameter_max=126.023,
                                pitch_diameter_min=125.833, minor_diameter_max=123.425, minor_diameter_min=122.137,
                                thread_class="4g6g", diameter=130, pitch=6)
thread["4g6g"][130][4] = Thread(major_diameter_max=129.940, major_diameter_min=129.465, pitch_diameter_max=127.342,
                                pitch_diameter_min=127.182, minor_diameter_max=125.610, minor_diameter_min=124.718,
                                thread_class="4g6g", diameter=130, pitch=4)
thread["4g6g"][130][3] = Thread(major_diameter_max=129.952, major_diameter_min=129.577, pitch_diameter_max=128.003,
                                pitch_diameter_min=127.863, minor_diameter_max=126.704, minor_diameter_min=126.015,
                                thread_class="4g6g", diameter=130, pitch=3)
thread["4g6g"][130][2] = Thread(major_diameter_max=139.962, major_diameter_min=139.682, pitch_diameter_max=138.663,
                                pitch_diameter_min=138.545, minor_diameter_max=137.797, minor_diameter_min=137.313,
                                thread_class="4g6g", diameter=130, pitch=2)
thread["4g6g"][130][1.5] = Thread(major_diameter_max=129.968, major_diameter_min=129.732, pitch_diameter_max=128.994,
                                  pitch_diameter_min=128.882, minor_diameter_max=128.344, minor_diameter_min=127.958,
                                  thread_class="4g6g", diameter=130, pitch=1.5)
thread["4g6g"][135][6] = Thread(major_diameter_max=134.920, major_diameter_min=134.320, pitch_diameter_max=131.023,
                                pitch_diameter_min=130.833, minor_diameter_max=128.425, minor_diameter_min=127.137,
                                thread_class="4g6g", diameter=135, pitch=6)
thread["4g6g"][135][4] = Thread(major_diameter_max=134.940, major_diameter_min=134.465, pitch_diameter_max=132.342,
                                pitch_diameter_min=132.182, minor_diameter_max=130.610, minor_diameter_min=129.718,
                                thread_class="4g6g", diameter=135, pitch=4)
thread["4g6g"][135][3] = Thread(major_diameter_max=134.952, major_diameter_min=134.577, pitch_diameter_max=133.003,
                                pitch_diameter_min=132.863, minor_diameter_max=131.704, minor_diameter_min=131.015,
                                thread_class="4g6g", diameter=135, pitch=3)
thread["4g6g"][135][2] = Thread(major_diameter_max=134.962, major_diameter_min=134.682, pitch_diameter_max=133.663,
                                pitch_diameter_min=133.543, minor_diameter_max=132.797, minor_diameter_min=132.311,
                                thread_class="4g6g", diameter=135, pitch=2)
thread["4g6g"][135][1.5] = Thread(major_diameter_max=134.968, major_diameter_min=134.732, pitch_diameter_max=133.994,
                                  pitch_diameter_min=133.882, minor_diameter_max=133.344, minor_diameter_min=132.958,
                                  thread_class="4g6g", diameter=135, pitch=1.5)
thread["4g6g"][140][8] = Thread(major_diameter_max=139.900, major_diameter_min=139.190, pitch_diameter_max=134.704,
                                pitch_diameter_min=134.492, minor_diameter_max=131.240, minor_diameter_min=129.564,
                                thread_class="4g6g", diameter=140, pitch=8)
thread["4g6g"][140][6] = Thread(major_diameter_max=139.920, major_diameter_min=139.320, pitch_diameter_max=136.023,
                                pitch_diameter_min=135.833, minor_diameter_max=133.425, minor_diameter_min=132.137,
                                thread_class="4g6g", diameter=140, pitch=6)
thread["4g6g"][140][4] = Thread(major_diameter_max=139.940, major_diameter_min=139.465, pitch_diameter_max=137.342,
                                pitch_diameter_min=137.182, minor_diameter_max=135.610, minor_diameter_min=134.718,
                                thread_class="4g6g", diameter=140, pitch=4)
thread["4g6g"][140][3] = Thread(major_diameter_max=139.952, major_diameter_min=139.577, pitch_diameter_max=138.003,
                                pitch_diameter_min=137.863, minor_diameter_max=136.704, minor_diameter_min=136.015,
                                thread_class="4g6g", diameter=140, pitch=3)
thread["4g6g"][140][2] = Thread(major_diameter_max=139.962, major_diameter_min=139.682, pitch_diameter_max=138.663,
                                pitch_diameter_min=138.545, minor_diameter_max=137.797, minor_diameter_min=137.313,
                                thread_class="4g6g", diameter=140, pitch=2)
thread["4g6g"][140][1.5] = Thread(major_diameter_max=139.968, major_diameter_min=139.732, pitch_diameter_max=138.994,
                                  pitch_diameter_min=138.882, minor_diameter_max=138.344, minor_diameter_min=137.958,
                                  thread_class="4g6g", diameter=140, pitch=1.5)
thread["4g6g"][145][6] = Thread(major_diameter_max=144.920, major_diameter_min=144.320, pitch_diameter_max=141.023,
                                pitch_diameter_min=140.833, minor_diameter_max=138.425, minor_diameter_min=137.137,
                                thread_class="4g6g", diameter=145, pitch=6)
thread["4g6g"][145][4] = Thread(major_diameter_max=144.940, major_diameter_min=144.465, pitch_diameter_max=142.342,
                                pitch_diameter_min=142.182, minor_diameter_max=140.610, minor_diameter_min=139.718,
                                thread_class="4g6g", diameter=145, pitch=4)
thread["4g6g"][145][3] = Thread(major_diameter_max=144.952, major_diameter_min=144.577, pitch_diameter_max=143.003,
                                pitch_diameter_min=142.863, minor_diameter_max=141.704, minor_diameter_min=141.015,
                                thread_class="4g6g", diameter=145, pitch=3)
thread["4g6g"][145][2] = Thread(major_diameter_max=144.962, major_diameter_min=144.682, pitch_diameter_max=143.663,
                                pitch_diameter_min=143.543, minor_diameter_max=142.797, minor_diameter_min=142.311,
                                thread_class="4g6g", diameter=145, pitch=2)
thread["4g6g"][145][1.5] = Thread(major_diameter_max=144.968, major_diameter_min=144.732, pitch_diameter_max=143.994,
                                  pitch_diameter_min=143.882, minor_diameter_max=143.344, minor_diameter_min=142.958,
                                  thread_class="4g6g", diameter=145, pitch=1.5)
thread["4g6g"][150][8] = Thread(major_diameter_max=149.900, major_diameter_min=149.190, pitch_diameter_max=144.704,
                                pitch_diameter_min=144.492, minor_diameter_max=141.240, minor_diameter_min=139.564,
                                thread_class="4g6g", diameter=150, pitch=8)
thread["4g6g"][150][6] = Thread(major_diameter_max=149.920, major_diameter_min=149.320, pitch_diameter_max=146.023,
                                pitch_diameter_min=145.833, minor_diameter_max=143.425, minor_diameter_min=142.137,
                                thread_class="4g6g", diameter=150, pitch=6)
thread["4g6g"][150][4] = Thread(major_diameter_max=149.940, major_diameter_min=149.465, pitch_diameter_max=147.342,
                                pitch_diameter_min=147.182, minor_diameter_max=145.610, minor_diameter_min=144.718,
                                thread_class="4g6g", diameter=150, pitch=4)
thread["4g6g"][150][3] = Thread(major_diameter_max=149.952, major_diameter_min=149.577, pitch_diameter_max=148.003,
                                pitch_diameter_min=147.863, minor_diameter_max=146.704, minor_diameter_min=146.015,
                                thread_class="4g6g", diameter=150, pitch=3)
thread["4g6g"][150][2] = Thread(major_diameter_max=149.962, major_diameter_min=149.682, pitch_diameter_max=148.663,
                                pitch_diameter_min=148.545, minor_diameter_max=147.797, minor_diameter_min=147.313,
                                thread_class="4g6g", diameter=150, pitch=2)
thread["4g6g"][150][1.5] = Thread(major_diameter_max=149.968, major_diameter_min=149.732, pitch_diameter_max=148.994,
                                  pitch_diameter_min=148.882, minor_diameter_max=148.344, minor_diameter_min=147.958,
                                  thread_class="4g6g", diameter=150, pitch=1.5)
thread["4g6g"][155][6] = Thread(major_diameter_max=154.920, major_diameter_min=154.320, pitch_diameter_max=151.023,
                                pitch_diameter_min=150.833, minor_diameter_max=148.425, minor_diameter_min=147.137,
                                thread_class="4g6g", diameter=155, pitch=6)
thread["4g6g"][155][4] = Thread(major_diameter_max=154.940, major_diameter_min=154.465, pitch_diameter_max=152.342,
                                pitch_diameter_min=152.182, minor_diameter_max=150.610, minor_diameter_min=149.718,
                                thread_class="4g6g", diameter=155, pitch=4)
thread["4g6g"][155][3] = Thread(major_diameter_max=154.952, major_diameter_min=154.577, pitch_diameter_max=153.003,
                                pitch_diameter_min=152.863, minor_diameter_max=151.704, minor_diameter_min=151.015,
                                thread_class="4g6g", diameter=155, pitch=3)
thread["4g6g"][155][2] = Thread(major_diameter_max=154.962, major_diameter_min=154.682, pitch_diameter_max=153.663,
                                pitch_diameter_min=153.543, minor_diameter_max=152.797, minor_diameter_min=152.311,
                                thread_class="4g6g", diameter=155, pitch=2)
thread["4g6g"][160][8] = Thread(major_diameter_max=159.900, major_diameter_min=159.190, pitch_diameter_max=154.704,
                                pitch_diameter_min=154.492, minor_diameter_max=151.240, minor_diameter_min=149.564,
                                thread_class="4g6g", diameter=160, pitch=8)
thread["4g6g"][160][6] = Thread(major_diameter_max=159.920, major_diameter_min=159.320, pitch_diameter_max=156.023,
                                pitch_diameter_min=155.833, minor_diameter_max=153.425, minor_diameter_min=152.137,
                                thread_class="4g6g", diameter=160, pitch=6)
thread["4g6g"][160][4] = Thread(major_diameter_max=159.940, major_diameter_min=159.465, pitch_diameter_max=157.342,
                                pitch_diameter_min=157.182, minor_diameter_max=155.610, minor_diameter_min=154.718,
                                thread_class="4g6g", diameter=160, pitch=4)
thread["4g6g"][160][3] = Thread(major_diameter_max=159.952, major_diameter_min=159.577, pitch_diameter_max=158.003,
                                pitch_diameter_min=157.863, minor_diameter_max=156.704, minor_diameter_min=156.015,
                                thread_class="4g6g", diameter=160, pitch=3)
thread["4g6g"][160][2] = Thread(major_diameter_max=159.962, major_diameter_min=159.682, pitch_diameter_max=158.663,
                                pitch_diameter_min=158.543, minor_diameter_max=157.797, minor_diameter_min=157.311,
                                thread_class="4g6g", diameter=160, pitch=2)
thread["4g6g"][165][6] = Thread(major_diameter_max=164.920, major_diameter_min=164.320, pitch_diameter_max=161.023,
                                pitch_diameter_min=160.833, minor_diameter_max=158.425, minor_diameter_min=157.137,
                                thread_class="4g6g", diameter=165, pitch=6)
thread["4g6g"][165][4] = Thread(major_diameter_max=164.940, major_diameter_min=164.465, pitch_diameter_max=162.342,
                                pitch_diameter_min=162.182, minor_diameter_max=160.610, minor_diameter_min=159.718,
                                thread_class="4g6g", diameter=165, pitch=4)
thread["4g6g"][165][3] = Thread(major_diameter_max=164.952, major_diameter_min=164.577, pitch_diameter_max=163.003,
                                pitch_diameter_min=162.863, minor_diameter_max=161.704, minor_diameter_min=161.015,
                                thread_class="4g6g", diameter=165, pitch=3)
thread["4g6g"][165][2] = Thread(major_diameter_max=164.962, major_diameter_min=164.682, pitch_diameter_max=163.663,
                                pitch_diameter_min=163.543, minor_diameter_max=162.797, minor_diameter_min=162.311,
                                thread_class="4g6g", diameter=165, pitch=2)
thread["4g6g"][170][8] = Thread(major_diameter_max=169.900, major_diameter_min=169.190, pitch_diameter_max=164.704,
                                pitch_diameter_min=164.492, minor_diameter_max=161.240, minor_diameter_min=159.564,
                                thread_class="4g6g", diameter=170, pitch=8)
thread["4g6g"][170][6] = Thread(major_diameter_max=169.920, major_diameter_min=169.320, pitch_diameter_max=166.023,
                                pitch_diameter_min=165.833, minor_diameter_max=163.425, minor_diameter_min=162.137,
                                thread_class="4g6g", diameter=170, pitch=6)
thread["4g6g"][170][4] = Thread(major_diameter_max=169.940, major_diameter_min=169.465, pitch_diameter_max=167.342,
                                pitch_diameter_min=167.182, minor_diameter_max=165.610, minor_diameter_min=164.718,
                                thread_class="4g6g", diameter=170, pitch=4)
thread["4g6g"][170][3] = Thread(major_diameter_max=169.952, major_diameter_min=169.577, pitch_diameter_max=168.003,
                                pitch_diameter_min=167.863, minor_diameter_max=166.704, minor_diameter_min=166.015,
                                thread_class="4g6g", diameter=170, pitch=3)
thread["4g6g"][170][2] = Thread(major_diameter_max=169.962, major_diameter_min=169.682, pitch_diameter_max=168.663,
                                pitch_diameter_min=168.543, minor_diameter_max=167.797, minor_diameter_min=167.311,
                                thread_class="4g6g", diameter=170, pitch=2)
thread["4g6g"][175][6] = Thread(major_diameter_max=174.920, major_diameter_min=174.320, pitch_diameter_max=171.023,
                                pitch_diameter_min=170.833, minor_diameter_max=168.425, minor_diameter_min=167.137,
                                thread_class="4g6g", diameter=175, pitch=6)
thread["4g6g"][175][4] = Thread(major_diameter_max=174.940, major_diameter_min=174.465, pitch_diameter_max=172.342,
                                pitch_diameter_min=172.182, minor_diameter_max=170.610, minor_diameter_min=169.718,
                                thread_class="4g6g", diameter=175, pitch=4)
thread["4g6g"][175][3] = Thread(major_diameter_max=174.952, major_diameter_min=174.577, pitch_diameter_max=173.003,
                                pitch_diameter_min=172.862, minor_diameter_max=171.704, minor_diameter_min=171.014,
                                thread_class="4g6g", diameter=175, pitch=3)
thread["4g6g"][175][2] = Thread(major_diameter_max=174.962, major_diameter_min=174.682, pitch_diameter_max=173.663,
                                pitch_diameter_min=173.543, minor_diameter_max=172.797, minor_diameter_min=172.311,
                                thread_class="4g6g", diameter=175, pitch=2)
thread["4g6g"][180][8] = Thread(major_diameter_max=179.900, major_diameter_min=179.190, pitch_diameter_max=174.704,
                                pitch_diameter_min=174.492, minor_diameter_max=171.240, minor_diameter_min=169.564,
                                thread_class="4g6g", diameter=180, pitch=8)
thread["4g6g"][180][6] = Thread(major_diameter_max=179.920, major_diameter_min=179.320, pitch_diameter_max=176.023,
                                pitch_diameter_min=175.833, minor_diameter_max=173.425, minor_diameter_min=172.137,
                                thread_class="4g6g", diameter=180, pitch=6)
thread["4g6g"][180][4] = Thread(major_diameter_max=179.940, major_diameter_min=179.465, pitch_diameter_max=177.342,
                                pitch_diameter_min=177.182, minor_diameter_max=175.610, minor_diameter_min=174.718,
                                thread_class="4g6g", diameter=180, pitch=4)
thread["4g6g"][180][3] = Thread(major_diameter_max=179.952, major_diameter_min=179.577, pitch_diameter_max=178.003,
                                pitch_diameter_min=177.863, minor_diameter_max=176.704, minor_diameter_min=176.015,
                                thread_class="4g6g", diameter=180, pitch=3)
thread["4g6g"][180][2] = Thread(major_diameter_max=179.962, major_diameter_min=179.682, pitch_diameter_max=178.663,
                                pitch_diameter_min=178.543, minor_diameter_max=177.797, minor_diameter_min=177.311,
                                thread_class="4g6g", diameter=180, pitch=2)
thread["4g6g"][185][6] = Thread(major_diameter_max=184.920, major_diameter_min=184.320, pitch_diameter_max=181.023,
                                pitch_diameter_min=180.823, minor_diameter_max=178.425, minor_diameter_min=177.127,
                                thread_class="4g6g", diameter=185, pitch=6)
thread["4g6g"][185][4] = Thread(major_diameter_max=184.940, major_diameter_min=184.465, pitch_diameter_max=182.342,
                                pitch_diameter_min=182.162, minor_diameter_max=180.610, minor_diameter_min=179.698,
                                thread_class="4g6g", diameter=185, pitch=4)
thread["4g6g"][185][3] = Thread(major_diameter_max=184.952, major_diameter_min=184.577, pitch_diameter_max=183.003,
                                pitch_diameter_min=182.843, minor_diameter_max=181.704, minor_diameter_min=180.995,
                                thread_class="4g6g", diameter=185, pitch=3)
thread["4g6g"][185][2] = Thread(major_diameter_max=184.962, major_diameter_min=184.682, pitch_diameter_max=183.663,
                                pitch_diameter_min=183.531, minor_diameter_max=182.797, minor_diameter_min=182.299,
                                thread_class="4g6g", diameter=185, pitch=2)
thread["4g6g"][190][8] = Thread(major_diameter_max=189.900, major_diameter_min=189.190, pitch_diameter_max=184.704,
                                pitch_diameter_min=184.480, minor_diameter_max=181.240, minor_diameter_min=179.552,
                                thread_class="4g6g", diameter=190, pitch=8)
thread["4g6g"][190][6] = Thread(major_diameter_max=189.920, major_diameter_min=189.320, pitch_diameter_max=186.023,
                                pitch_diameter_min=185.823, minor_diameter_max=183.425, minor_diameter_min=182.127,
                                thread_class="4g6g", diameter=190, pitch=6)
thread["4g6g"][190][4] = Thread(major_diameter_max=189.940, major_diameter_min=189.465, pitch_diameter_max=187.342,
                                pitch_diameter_min=187.162, minor_diameter_max=185.610, minor_diameter_min=184.698,
                                thread_class="4g6g", diameter=190, pitch=4)
thread["4g6g"][190][3] = Thread(major_diameter_max=189.952, major_diameter_min=189.577, pitch_diameter_max=188.003,
                                pitch_diameter_min=187.843, minor_diameter_max=186.704, minor_diameter_min=185.995,
                                thread_class="4g6g", diameter=190, pitch=3)
thread["4g6g"][190][2] = Thread(major_diameter_max=189.962, major_diameter_min=189.682, pitch_diameter_max=188.663,
                                pitch_diameter_min=188.531, minor_diameter_max=187.797, minor_diameter_min=187.299,
                                thread_class="4g6g", diameter=190, pitch=2)
thread["4g6g"][195][6] = Thread(major_diameter_max=194.920, major_diameter_min=194.320, pitch_diameter_max=191.023,
                                pitch_diameter_min=190.823, minor_diameter_max=188.425, minor_diameter_min=187.127,
                                thread_class="4g6g", diameter=195, pitch=6)
thread["4g6g"][195][4] = Thread(major_diameter_max=194.940, major_diameter_min=194.465, pitch_diameter_max=192.342,
                                pitch_diameter_min=192.162, minor_diameter_max=190.610, minor_diameter_min=189.698,
                                thread_class="4g6g", diameter=195, pitch=4)
thread["4g6g"][195][3] = Thread(major_diameter_max=194.952, major_diameter_min=194.577, pitch_diameter_max=193.003,
                                pitch_diameter_min=192.843, minor_diameter_max=191.704, minor_diameter_min=190.995,
                                thread_class="4g6g", diameter=195, pitch=3)
thread["4g6g"][195][2] = Thread(major_diameter_max=194.962, major_diameter_min=194.682, pitch_diameter_max=193.663,
                                pitch_diameter_min=193.531, minor_diameter_max=192.797, minor_diameter_min=192.299,
                                thread_class="4g6g", diameter=195, pitch=2)
thread["4g6g"][200][8] = Thread(major_diameter_max=199.900, major_diameter_min=199.190, pitch_diameter_max=194.704,
                                pitch_diameter_min=194.480, minor_diameter_max=191.240, minor_diameter_min=189.552,
                                thread_class="4g6g", diameter=200, pitch=8)
thread["4g6g"][200][6] = Thread(major_diameter_max=199.920, major_diameter_min=199.320, pitch_diameter_max=196.023,
                                pitch_diameter_min=195.823, minor_diameter_max=193.425, minor_diameter_min=192.127,
                                thread_class="4g6g", diameter=200, pitch=6)
thread["4g6g"][200][4] = Thread(major_diameter_max=199.940, major_diameter_min=199.465, pitch_diameter_max=197.342,
                                pitch_diameter_min=197.162, minor_diameter_max=195.610, minor_diameter_min=194.698,
                                thread_class="4g6g", diameter=200, pitch=4)
thread["4g6g"][200][3] = Thread(major_diameter_max=199.952, major_diameter_min=199.577, pitch_diameter_max=198.003,
                                pitch_diameter_min=197.843, minor_diameter_max=196.704, minor_diameter_min=195.995,
                                thread_class="4g6g", diameter=200, pitch=3)
thread["4g6g"][200][2] = Thread(major_diameter_max=199.962, major_diameter_min=199.682, pitch_diameter_max=198.663,
                                pitch_diameter_min=198.531, minor_diameter_max=197.797, minor_diameter_min=197.299,
                                thread_class="4g6g", diameter=200, pitch=2)
thread["4g6g"][205][6] = Thread(major_diameter_max=204.920, major_diameter_min=204.320, pitch_diameter_max=201.023,
                                pitch_diameter_min=200.823, minor_diameter_max=198.425, minor_diameter_min=197.127,
                                thread_class="4g6g", diameter=205, pitch=6)
thread["4g6g"][205][4] = Thread(major_diameter_max=204.940, major_diameter_min=204.465, pitch_diameter_max=202.342,
                                pitch_diameter_min=202.162, minor_diameter_max=200.610, minor_diameter_min=199.698,
                                thread_class="4g6g", diameter=205, pitch=4)
thread["4g6g"][205][3] = Thread(major_diameter_max=204.952, major_diameter_min=204.577, pitch_diameter_max=203.003,
                                pitch_diameter_min=202.843, minor_diameter_max=201.704, minor_diameter_min=200.995,
                                thread_class="4g6g", diameter=205, pitch=3)
thread["4g6g"][205][2] = Thread(major_diameter_max=204.962, major_diameter_min=204.682, pitch_diameter_max=203.663,
                                pitch_diameter_min=203.531, minor_diameter_max=202.797, minor_diameter_min=202.299,
                                thread_class="4g6g", diameter=205, pitch=2)
thread["4g6g"][210][8] = Thread(major_diameter_max=209.900, major_diameter_min=209.190, pitch_diameter_max=204.704,
                                pitch_diameter_min=204.480, minor_diameter_max=201.240, minor_diameter_min=199.552,
                                thread_class="4g6g", diameter=210, pitch=8)
thread["4g6g"][210][6] = Thread(major_diameter_max=209.920, major_diameter_min=209.320, pitch_diameter_max=206.023,
                                pitch_diameter_min=205.823, minor_diameter_max=203.425, minor_diameter_min=202.127,
                                thread_class="4g6g", diameter=210, pitch=6)
thread["4g6g"][210][4] = Thread(major_diameter_max=209.940, major_diameter_min=209.465, pitch_diameter_max=207.342,
                                pitch_diameter_min=207.162, minor_diameter_max=205.610, minor_diameter_min=204.698,
                                thread_class="4g6g", diameter=210, pitch=4)
thread["4g6g"][210][3] = Thread(major_diameter_max=209.952, major_diameter_min=209.577, pitch_diameter_max=208.003,
                                pitch_diameter_min=207.843, minor_diameter_max=206.704, minor_diameter_min=205.995,
                                thread_class="4g6g", diameter=210, pitch=3)
thread["4g6g"][210][2] = Thread(major_diameter_max=209.962, major_diameter_min=209.682, pitch_diameter_max=208.663,
                                pitch_diameter_min=208.531, minor_diameter_max=207.797, minor_diameter_min=207.299,
                                thread_class="4g6g", diameter=210, pitch=2)
thread["4g6g"][215][6] = Thread(major_diameter_max=214.920, major_diameter_min=214.320, pitch_diameter_max=211.023,
                                pitch_diameter_min=210.823, minor_diameter_max=208.425, minor_diameter_min=207.127,
                                thread_class="4g6g", diameter=215, pitch=6)
thread["4g6g"][215][4] = Thread(major_diameter_max=214.940, major_diameter_min=214.465, pitch_diameter_max=212.342,
                                pitch_diameter_min=212.162, minor_diameter_max=210.610, minor_diameter_min=209.698,
                                thread_class="4g6g", diameter=215, pitch=4)
thread["4g6g"][215][3] = Thread(major_diameter_max=214.952, major_diameter_min=214.577, pitch_diameter_max=213.003,
                                pitch_diameter_min=212.843, minor_diameter_max=211.704, minor_diameter_min=210.995,
                                thread_class="4g6g", diameter=215, pitch=3)
thread["4g6g"][220][8] = Thread(major_diameter_max=219.900, major_diameter_min=219.190, pitch_diameter_max=214.704,
                                pitch_diameter_min=214.480, minor_diameter_max=211.240, minor_diameter_min=209.552,
                                thread_class="4g6g", diameter=220, pitch=8)
thread["4g6g"][220][6] = Thread(major_diameter_max=219.920, major_diameter_min=219.320, pitch_diameter_max=216.023,
                                pitch_diameter_min=215.823, minor_diameter_max=213.425, minor_diameter_min=212.127,
                                thread_class="4g6g", diameter=220, pitch=6)
thread["4g6g"][220][4] = Thread(major_diameter_max=219.940, major_diameter_min=219.465, pitch_diameter_max=217.342,
                                pitch_diameter_min=217.162, minor_diameter_max=215.610, minor_diameter_min=214.698,
                                thread_class="4g6g", diameter=220, pitch=4)
thread["4g6g"][220][3] = Thread(major_diameter_max=219.952, major_diameter_min=219.577, pitch_diameter_max=218.003,
                                pitch_diameter_min=217.843, minor_diameter_max=216.704, minor_diameter_min=215.995,
                                thread_class="4g6g", diameter=220, pitch=3)
thread["4g6g"][220][2] = Thread(major_diameter_max=219.962, major_diameter_min=219.682, pitch_diameter_max=218.663,
                                pitch_diameter_min=218.531, minor_diameter_max=217.797, minor_diameter_min=217.299,
                                thread_class="4g6g", diameter=220, pitch=2)
thread["4g6g"][225][6] = Thread(major_diameter_max=224.920, major_diameter_min=224.545, pitch_diameter_max=221.023,
                                pitch_diameter_min=220.823, minor_diameter_max=218.425, minor_diameter_min=217.127,
                                thread_class="4g6g", diameter=225, pitch=6)
thread["4g6g"][225][4] = Thread(major_diameter_max=224.940, major_diameter_min=224.465, pitch_diameter_max=222.342,
                                pitch_diameter_min=222.162, minor_diameter_max=220.610, minor_diameter_min=219.698,
                                thread_class="4g6g", diameter=225, pitch=4)
thread["4g6g"][225][3] = Thread(major_diameter_max=224.952, major_diameter_min=224.577, pitch_diameter_max=223.003,
                                pitch_diameter_min=222.843, minor_diameter_max=221.704, minor_diameter_min=220.995,
                                thread_class="4g6g", diameter=225, pitch=3)
thread["4g6g"][225][2] = Thread(major_diameter_max=224.962, major_diameter_min=224.682, pitch_diameter_max=223.663,
                                pitch_diameter_min=223.531, minor_diameter_max=222.797, minor_diameter_min=222.299,
                                thread_class="4g6g", diameter=225, pitch=2)
thread["4g6g"][230][6] = Thread(major_diameter_max=229.920, major_diameter_min=229.320, pitch_diameter_max=226.023,
                                pitch_diameter_min=225.823, minor_diameter_max=223.425, minor_diameter_min=222.127,
                                thread_class="4g6g", diameter=230, pitch=6)
thread["4g6g"][230][4] = Thread(major_diameter_max=229.940, major_diameter_min=229.465, pitch_diameter_max=227.342,
                                pitch_diameter_min=227.162, minor_diameter_max=225.610, minor_diameter_min=224.698,
                                thread_class="4g6g", diameter=230, pitch=4)
thread["4g6g"][230][3] = Thread(major_diameter_max=229.952, major_diameter_min=229.577, pitch_diameter_max=228.003,
                                pitch_diameter_min=227.843, minor_diameter_max=226.704, minor_diameter_min=225.995,
                                thread_class="4g6g", diameter=230, pitch=3)
thread["4g6g"][230][2] = Thread(major_diameter_max=229.962, major_diameter_min=229.682, pitch_diameter_max=228.663,
                                pitch_diameter_min=228.531, minor_diameter_max=227.797, minor_diameter_min=227.299,
                                thread_class="4g6g", diameter=230, pitch=2)
thread["4g6g"][235][6] = Thread(major_diameter_max=234.920, major_diameter_min=234.320, pitch_diameter_max=231.023,
                                pitch_diameter_min=230.799, minor_diameter_max=228.425, minor_diameter_min=227.103,
                                thread_class="4g6g", diameter=235, pitch=6)
thread["4g6g"][235][4] = Thread(major_diameter_max=234.940, major_diameter_min=234.465, pitch_diameter_max=232.342,
                                pitch_diameter_min=232.162, minor_diameter_max=230.610, minor_diameter_min=229.698,
                                thread_class="4g6g", diameter=235, pitch=4)
thread["4g6g"][235][3] = Thread(major_diameter_max=234.952, major_diameter_min=234.577, pitch_diameter_max=233.003,
                                pitch_diameter_min=232.843, minor_diameter_max=231.704, minor_diameter_min=230.995,
                                thread_class="4g6g", diameter=235, pitch=3)
thread["4g6g"][240][8] = Thread(major_diameter_max=239.900, major_diameter_min=239.190, pitch_diameter_max=234.704,
                                pitch_diameter_min=234.480, minor_diameter_max=231.240, minor_diameter_min=229.552,
                                thread_class="4g6g", diameter=240, pitch=8)
thread["4g6g"][240][6] = Thread(major_diameter_max=239.920, major_diameter_min=239.320, pitch_diameter_max=236.023,
                                pitch_diameter_min=235.823, minor_diameter_max=233.425, minor_diameter_min=232.127,
                                thread_class="4g6g", diameter=240, pitch=6)
thread["4g6g"][240][4] = Thread(major_diameter_max=239.940, major_diameter_min=239.465, pitch_diameter_max=237.342,
                                pitch_diameter_min=237.162, minor_diameter_max=235.610, minor_diameter_min=234.698,
                                thread_class="4g6g", diameter=240, pitch=4)
thread["4g6g"][240][3] = Thread(major_diameter_max=239.952, major_diameter_min=239.577, pitch_diameter_max=238.003,
                                pitch_diameter_min=237.843, minor_diameter_max=236.704, minor_diameter_min=235.995,
                                thread_class="4g6g", diameter=240, pitch=3)
thread["4g6g"][240][2] = Thread(major_diameter_max=239.962, major_diameter_min=239.682, pitch_diameter_max=238.663,
                                pitch_diameter_min=238.531, minor_diameter_max=237.797, minor_diameter_min=237.299,
                                thread_class="4g6g", diameter=240, pitch=2)
thread["4g6g"][245][6] = Thread(major_diameter_max=244.920, major_diameter_min=244.320, pitch_diameter_max=241.023,
                                pitch_diameter_min=240.823, minor_diameter_max=238.425, minor_diameter_min=237.127,
                                thread_class="4g6g", diameter=245, pitch=6)
thread["4g6g"][245][4] = Thread(major_diameter_max=244.940, major_diameter_min=244.465, pitch_diameter_max=242.342,
                                pitch_diameter_min=242.162, minor_diameter_max=240.610, minor_diameter_min=239.698,
                                thread_class="4g6g", diameter=245, pitch=4)
thread["4g6g"][245][3] = Thread(major_diameter_max=244.952, major_diameter_min=244.577, pitch_diameter_max=243.003,
                                pitch_diameter_min=242.843, minor_diameter_max=241.704, minor_diameter_min=240.995,
                                thread_class="4g6g", diameter=245, pitch=3)
thread["4g6g"][245][2] = Thread(major_diameter_max=244.962, major_diameter_min=244.682, pitch_diameter_max=243.663,
                                pitch_diameter_min=243.531, minor_diameter_max=242.797, minor_diameter_min=242.299,
                                thread_class="4g6g", diameter=245, pitch=2)
thread["4g6g"][250][8] = Thread(major_diameter_max=249.900, major_diameter_min=249.190, pitch_diameter_max=244.704,
                                pitch_diameter_min=244.480, minor_diameter_max=241.240, minor_diameter_min=239.552,
                                thread_class="4g6g", diameter=250, pitch=8)
thread["4g6g"][250][6] = Thread(major_diameter_max=249.920, major_diameter_min=249.320, pitch_diameter_max=246.023,
                                pitch_diameter_min=245.823, minor_diameter_max=243.425, minor_diameter_min=242.127,
                                thread_class="4g6g", diameter=250, pitch=6)
thread["4g6g"][250][4] = Thread(major_diameter_max=249.940, major_diameter_min=249.465, pitch_diameter_max=247.342,
                                pitch_diameter_min=247.162, minor_diameter_max=245.610, minor_diameter_min=244.698,
                                thread_class="4g6g", diameter=250, pitch=4)
thread["4g6g"][250][3] = Thread(major_diameter_max=249.952, major_diameter_min=249.577, pitch_diameter_max=248.003,
                                pitch_diameter_min=247.843, minor_diameter_max=246.704, minor_diameter_min=245.995,
                                thread_class="4g6g", diameter=250, pitch=3)
thread["4g6g"][250][2] = Thread(major_diameter_max=249.962, major_diameter_min=249.682, pitch_diameter_max=248.663,
                                pitch_diameter_min=248.531, minor_diameter_max=247.797, minor_diameter_min=247.299,
                                thread_class="4g6g", diameter=250, pitch=2)
thread["4g6g"][255][6] = Thread(major_diameter_max=254.920, major_diameter_min=254.320, pitch_diameter_max=251.023,
                                pitch_diameter_min=250.799, minor_diameter_max=248.425, minor_diameter_min=247.103,
                                thread_class="4g6g", diameter=255, pitch=6)
thread["4g6g"][255][4] = Thread(major_diameter_max=254.940, major_diameter_min=254.465, pitch_diameter_max=252.342,
                                pitch_diameter_min=252.162, minor_diameter_max=250.610, minor_diameter_min=249.698,
                                thread_class="4g6g", diameter=255, pitch=4)
thread["4g6g"][255][3] = Thread(major_diameter_max=254.952, major_diameter_min=254.577, pitch_diameter_max=253.003,
                                pitch_diameter_min=252.843, minor_diameter_max=251.704, minor_diameter_min=250.995,
                                thread_class="4g6g", diameter=255, pitch=3)
thread["4g6g"][260][8] = Thread(major_diameter_max=259.900, major_diameter_min=259.190, pitch_diameter_max=254.704,
                                pitch_diameter_min=254.480, minor_diameter_max=251.240, minor_diameter_min=249.552,
                                thread_class="4g6g", diameter=260, pitch=8)
thread["4g6g"][260][6] = Thread(major_diameter_max=259.920, major_diameter_min=259.320, pitch_diameter_max=256.023,
                                pitch_diameter_min=255.823, minor_diameter_max=253.425, minor_diameter_min=252.127,
                                thread_class="4g6g", diameter=260, pitch=6)
thread["4g6g"][260][4] = Thread(major_diameter_max=259.940, major_diameter_min=259.465, pitch_diameter_max=257.342,
                                pitch_diameter_min=257.162, minor_diameter_max=255.610, minor_diameter_min=254.698,
                                thread_class="4g6g", diameter=260, pitch=4)
thread["4g6g"][260][3] = Thread(major_diameter_max=259.952, major_diameter_min=259.577, pitch_diameter_max=258.003,
                                pitch_diameter_min=257.843, minor_diameter_max=256.704, minor_diameter_min=255.995,
                                thread_class="4g6g", diameter=260, pitch=3)
thread["4g6g"][265][6] = Thread(major_diameter_max=264.920, major_diameter_min=264.320, pitch_diameter_max=261.023,
                                pitch_diameter_min=260.823, minor_diameter_max=258.425, minor_diameter_min=257.127,
                                thread_class="4g6g", diameter=265, pitch=6)
thread["4g6g"][265][4] = Thread(major_diameter_max=264.940, major_diameter_min=264.465, pitch_diameter_max=262.342,
                                pitch_diameter_min=262.162, minor_diameter_max=260.610, minor_diameter_min=259.698,
                                thread_class="4g6g", diameter=265, pitch=4)
thread["4g6g"][265][3] = Thread(major_diameter_max=264.952, major_diameter_min=264.577, pitch_diameter_max=263.003,
                                pitch_diameter_min=262.843, minor_diameter_max=261.704, minor_diameter_min=260.995,
                                thread_class="4g6g", diameter=265, pitch=3)
thread["4g6g"][270][6] = Thread(major_diameter_max=269.920, major_diameter_min=269.320, pitch_diameter_max=266.023,
                                pitch_diameter_min=265.823, minor_diameter_max=263.425, minor_diameter_min=262.127,
                                thread_class="4g6g", diameter=270, pitch=6)
thread["4g6g"][270][4] = Thread(major_diameter_max=269.940, major_diameter_min=269.465, pitch_diameter_max=267.342,
                                pitch_diameter_min=267.162, minor_diameter_max=265.610, minor_diameter_min=264.698,
                                thread_class="4g6g", diameter=270, pitch=4)
thread["4g6g"][270][3] = Thread(major_diameter_max=269.952, major_diameter_min=269.577, pitch_diameter_max=268.003,
                                pitch_diameter_min=267.843, minor_diameter_max=266.704, minor_diameter_min=265.995,
                                thread_class="4g6g", diameter=270, pitch=3)
thread["4g6g"][275][6] = Thread(major_diameter_max=274.920, major_diameter_min=274.320, pitch_diameter_max=271.023,
                                pitch_diameter_min=270.823, minor_diameter_max=268.425, minor_diameter_min=267.127,
                                thread_class="4g6g", diameter=275, pitch=6)
thread["4g6g"][275][4] = Thread(major_diameter_max=274.940, major_diameter_min=274.465, pitch_diameter_max=272.342,
                                pitch_diameter_min=272.162, minor_diameter_max=270.610, minor_diameter_min=269.698,
                                thread_class="4g6g", diameter=275, pitch=4)
thread["4g6g"][275][3] = Thread(major_diameter_max=274.952, major_diameter_min=274.577, pitch_diameter_max=273.003,
                                pitch_diameter_min=272.843, minor_diameter_max=271.704, minor_diameter_min=270.995,
                                thread_class="4g6g", diameter=275, pitch=3)
thread["4g6g"][280][8] = Thread(major_diameter_max=279.900, major_diameter_min=279.190, pitch_diameter_max=274.704,
                                pitch_diameter_min=274.480, minor_diameter_max=271.240, minor_diameter_min=269.552,
                                thread_class="4g6g", diameter=280, pitch=8)
thread["4g6g"][280][6] = Thread(major_diameter_max=279.920, major_diameter_min=279.320, pitch_diameter_max=276.023,
                                pitch_diameter_min=275.823, minor_diameter_max=273.425, minor_diameter_min=272.127,
                                thread_class="4g6g", diameter=280, pitch=6)
thread["4g6g"][280][4] = Thread(major_diameter_max=279.940, major_diameter_min=279.465, pitch_diameter_max=277.342,
                                pitch_diameter_min=277.162, minor_diameter_max=275.610, minor_diameter_min=274.698,
                                thread_class="4g6g", diameter=280, pitch=4)
thread["4g6g"][280][3] = Thread(major_diameter_max=279.952, major_diameter_min=279.577, pitch_diameter_max=278.003,
                                pitch_diameter_min=277.843, minor_diameter_max=276.704, minor_diameter_min=275.995,
                                thread_class="4g6g", diameter=280, pitch=3)
thread["4g6g"][285][6] = Thread(major_diameter_max=284.920, major_diameter_min=284.320, pitch_diameter_max=281.023,
                                pitch_diameter_min=280.823, minor_diameter_max=278.425, minor_diameter_min=277.127,
                                thread_class="4g6g", diameter=285, pitch=6)
thread["4g6g"][285][4] = Thread(major_diameter_max=284.940, major_diameter_min=284.465, pitch_diameter_max=282.342,
                                pitch_diameter_min=282.162, minor_diameter_max=280.610, minor_diameter_min=279.698,
                                thread_class="4g6g", diameter=285, pitch=4)
thread["4g6g"][285][3] = Thread(major_diameter_max=284.952, major_diameter_min=284.577, pitch_diameter_max=283.003,
                                pitch_diameter_min=282.843, minor_diameter_max=281.704, minor_diameter_min=280.995,
                                thread_class="4g6g", diameter=285, pitch=3)
thread["4g6g"][290][6] = Thread(major_diameter_max=289.920, major_diameter_min=289.320, pitch_diameter_max=286.023,
                                pitch_diameter_min=285.823, minor_diameter_max=283.425, minor_diameter_min=282.127,
                                thread_class="4g6g", diameter=290, pitch=6)
thread["4g6g"][290][4] = Thread(major_diameter_max=289.940, major_diameter_min=289.465, pitch_diameter_max=287.342,
                                pitch_diameter_min=287.162, minor_diameter_max=285.610, minor_diameter_min=284.698,
                                thread_class="4g6g", diameter=290, pitch=4)
thread["4g6g"][290][3] = Thread(major_diameter_max=289.952, major_diameter_min=289.577, pitch_diameter_max=288.003,
                                pitch_diameter_min=287.843, minor_diameter_max=286.704, minor_diameter_min=285.995,
                                thread_class="4g6g", diameter=290, pitch=3)
thread["4g6g"][295][6] = Thread(major_diameter_max=294.920, major_diameter_min=294.320, pitch_diameter_max=291.023,
                                pitch_diameter_min=290.823, minor_diameter_max=288.425, minor_diameter_min=287.127,
                                thread_class="4g6g", diameter=295, pitch=6)
thread["4g6g"][295][4] = Thread(major_diameter_max=294.940, major_diameter_min=294.465, pitch_diameter_max=292.342,
                                pitch_diameter_min=292.162, minor_diameter_max=290.610, minor_diameter_min=289.698,
                                thread_class="4g6g", diameter=295, pitch=4)
thread["4g6g"][295][3] = Thread(major_diameter_max=294.952, major_diameter_min=294.577, pitch_diameter_max=293.003,
                                pitch_diameter_min=292.843, minor_diameter_max=291.704, minor_diameter_min=290.995,
                                thread_class="4g6g", diameter=295, pitch=3)
thread["4g6g"][300][8] = Thread(major_diameter_max=299.900, major_diameter_min=299.190, pitch_diameter_max=294.704,
                                pitch_diameter_min=294.480, minor_diameter_max=291.240, minor_diameter_min=289.552,
                                thread_class="4g6g", diameter=300, pitch=8)
thread["4g6g"][300][6] = Thread(major_diameter_max=299.920, major_diameter_min=299.320, pitch_diameter_max=296.023,
                                pitch_diameter_min=295.823, minor_diameter_max=293.425, minor_diameter_min=292.127,
                                thread_class="4g6g", diameter=300, pitch=6)
thread["4g6g"][300][4] = Thread(major_diameter_max=299.940, major_diameter_min=299.465, pitch_diameter_max=297.342,
                                pitch_diameter_min=297.162, minor_diameter_max=295.610, minor_diameter_min=294.698,
                                thread_class="4g6g", diameter=300, pitch=4)
thread["4g6g"][300][3] = Thread(major_diameter_max=299.952, major_diameter_min=299.577, pitch_diameter_max=298.003,
                                pitch_diameter_min=297.843, minor_diameter_max=296.704, minor_diameter_min=295.995,
                                thread_class="4g6g", diameter=300, pitch=3)
thread["4g6g"][310][6] = Thread(major_diameter_max=309.920, major_diameter_min=309.320, pitch_diameter_max=306.023,
                                pitch_diameter_min=305.823, minor_diameter_max=303.425, minor_diameter_min=302.127,
                                thread_class="4g6g", diameter=310, pitch=6)
thread["4g6g"][310][4] = Thread(major_diameter_max=309.940, major_diameter_min=309.465, pitch_diameter_max=307.342,
                                pitch_diameter_min=307.162, minor_diameter_max=305.610, minor_diameter_min=304.698,
                                thread_class="4g6g", diameter=310, pitch=4)
thread["4g6g"][320][6] = Thread(major_diameter_max=319.920, major_diameter_min=319.320, pitch_diameter_max=316.023,
                                pitch_diameter_min=315.823, minor_diameter_max=313.425, minor_diameter_min=312.127,
                                thread_class="4g6g", diameter=320, pitch=6)
thread["4g6g"][320][4] = Thread(major_diameter_max=319.940, major_diameter_min=319.465, pitch_diameter_max=317.342,
                                pitch_diameter_min=317.162, minor_diameter_max=315.610, minor_diameter_min=314.698,
                                thread_class="4g6g", diameter=320, pitch=4)
thread["4g6g"][330][6] = Thread(major_diameter_max=329.920, major_diameter_min=329.320, pitch_diameter_max=326.023,
                                pitch_diameter_min=325.823, minor_diameter_max=323.425, minor_diameter_min=322.127,
                                thread_class="4g6g", diameter=330, pitch=6)
thread["4g6g"][330][4] = Thread(major_diameter_max=329.940, major_diameter_min=329.465, pitch_diameter_max=327.342,
                                pitch_diameter_min=327.162, minor_diameter_max=325.610, minor_diameter_min=324.698,
                                thread_class="4g6g", diameter=330, pitch=4)
thread["4g6g"][340][6] = Thread(major_diameter_max=339.920, major_diameter_min=339.320, pitch_diameter_max=336.023,
                                pitch_diameter_min=335.823, minor_diameter_max=333.425, minor_diameter_min=332.127,
                                thread_class="4g6g", diameter=340, pitch=6)
thread["4g6g"][340][4] = Thread(major_diameter_max=339.940, major_diameter_min=339.465, pitch_diameter_max=337.342,
                                pitch_diameter_min=337.162, minor_diameter_max=335.610, minor_diameter_min=334.698,
                                thread_class="4g6g", diameter=340, pitch=4)
thread["4g6g"][350][6] = Thread(major_diameter_max=349.920, major_diameter_min=349.320, pitch_diameter_max=346.023,
                                pitch_diameter_min=345.823, minor_diameter_max=343.425, minor_diameter_min=342.127,
                                thread_class="4g6g", diameter=350, pitch=6)
thread["4g6g"][350][4] = Thread(major_diameter_max=349.940, major_diameter_min=349.465, pitch_diameter_max=347.342,
                                pitch_diameter_min=347.162, minor_diameter_max=345.610, minor_diameter_min=344.698,
                                thread_class="4g6g", diameter=350, pitch=4)
thread["4g6g"][360][6] = Thread(major_diameter_max=359.920, major_diameter_min=359.320, pitch_diameter_max=356.023,
                                pitch_diameter_min=355.799, minor_diameter_max=353.425, minor_diameter_min=352.103,
                                thread_class="4g6g", diameter=360, pitch=6)
thread["4g6g"][360][4] = Thread(major_diameter_max=359.940, major_diameter_min=359.465, pitch_diameter_max=357.342,
                                pitch_diameter_min=357.152, minor_diameter_max=355.610, minor_diameter_min=354.688,
                                thread_class="4g6g", diameter=360, pitch=4)
thread["4g6g"][370][6] = Thread(major_diameter_max=369.920, major_diameter_min=369.320, pitch_diameter_max=366.023,
                                pitch_diameter_min=365.799, minor_diameter_max=363.425, minor_diameter_min=362.103,
                                thread_class="4g6g", diameter=370, pitch=6)
thread["4g6g"][370][4] = Thread(major_diameter_max=369.940, major_diameter_min=369.465, pitch_diameter_max=367.342,
                                pitch_diameter_min=367.152, minor_diameter_max=365.610, minor_diameter_min=364.688,
                                thread_class="4g6g", diameter=370, pitch=4)
thread["4g6g"][380][6] = Thread(major_diameter_max=379.920, major_diameter_min=379.320, pitch_diameter_max=376.023,
                                pitch_diameter_min=375.799, minor_diameter_max=373.425, minor_diameter_min=372.103,
                                thread_class="4g6g", diameter=380, pitch=6)
thread["4g6g"][380][4] = Thread(major_diameter_max=379.940, major_diameter_min=379.465, pitch_diameter_max=377.342,
                                pitch_diameter_min=377.152, minor_diameter_max=375.610, minor_diameter_min=374.688,
                                thread_class="4g6g", diameter=380, pitch=4)
thread["4g6g"][390][6] = Thread(major_diameter_max=389.920, major_diameter_min=389.320, pitch_diameter_max=386.023,
                                pitch_diameter_min=385.799, minor_diameter_max=383.425, minor_diameter_min=382.103,
                                thread_class="4g6g", diameter=390, pitch=6)
thread["4g6g"][390][4] = Thread(major_diameter_max=389.940, major_diameter_min=389.465, pitch_diameter_max=387.342,
                                pitch_diameter_min=387.152, minor_diameter_max=385.610, minor_diameter_min=384.688,
                                thread_class="4g6g", diameter=390, pitch=4)
thread["4g6g"][400][6] = Thread(major_diameter_max=399.920, major_diameter_min=399.320, pitch_diameter_max=396.023,
                                pitch_diameter_min=395.799, minor_diameter_max=393.425, minor_diameter_min=392.103,
                                thread_class="4g6g", diameter=400, pitch=6)
thread["4g6g"][400][4] = Thread(major_diameter_max=399.940, major_diameter_min=399.465, pitch_diameter_max=397.342,
                                pitch_diameter_min=397.152, minor_diameter_max=395.610, minor_diameter_min=394.688,
                                thread_class="4g6g", diameter=400, pitch=4)
thread["4g6g"][410][6] = Thread(major_diameter_max=409.920, major_diameter_min=409.320, pitch_diameter_max=406.023,
                                pitch_diameter_min=405.799, minor_diameter_max=403.425, minor_diameter_min=402.103,
                                thread_class="4g6g", diameter=410, pitch=6)
thread["4g6g"][420][6] = Thread(major_diameter_max=419.920, major_diameter_min=419.320, pitch_diameter_max=416.023,
                                pitch_diameter_min=415.799, minor_diameter_max=413.425, minor_diameter_min=412.103,
                                thread_class="4g6g", diameter=420, pitch=6)
thread["4g6g"][430][6] = Thread(major_diameter_max=429.920, major_diameter_min=429.320, pitch_diameter_max=426.023,
                                pitch_diameter_min=425.799, minor_diameter_max=423.425, minor_diameter_min=422.103,
                                thread_class="4g6g", diameter=430, pitch=6)
thread["4g6g"][440][6] = Thread(major_diameter_max=439.920, major_diameter_min=439.320, pitch_diameter_max=436.023,
                                pitch_diameter_min=435.799, minor_diameter_max=433.425, minor_diameter_min=432.103,
                                thread_class="4g6g", diameter=440, pitch=6)
thread["4g6g"][450][6] = Thread(major_diameter_max=449.920, major_diameter_min=449.320, pitch_diameter_max=446.023,
                                pitch_diameter_min=445.799, minor_diameter_max=443.425, minor_diameter_min=442.103,
                                thread_class="4g6g", diameter=450, pitch=6)
thread["4g6g"][460][6] = Thread(major_diameter_max=459.920, major_diameter_min=459.320, pitch_diameter_max=456.023,
                                pitch_diameter_min=455.799, minor_diameter_max=453.425, minor_diameter_min=452.103,
                                thread_class="4g6g", diameter=460, pitch=6)
thread["4g6g"][470][6] = Thread(major_diameter_max=469.920, major_diameter_min=469.320, pitch_diameter_max=466.023,
                                pitch_diameter_min=465.799, minor_diameter_max=463.425, minor_diameter_min=462.103,
                                thread_class="4g6g", diameter=470, pitch=6)
thread["4g6g"][480][6] = Thread(major_diameter_max=479.920, major_diameter_min=479.320, pitch_diameter_max=476.023,
                                pitch_diameter_min=475.799, minor_diameter_max=473.425, minor_diameter_min=472.103,
                                thread_class="4g6g", diameter=480, pitch=6)
thread["4g6g"][490][6] = Thread(major_diameter_max=489.920, major_diameter_min=489.320, pitch_diameter_max=486.023,
                                pitch_diameter_min=485.799, minor_diameter_max=483.425, minor_diameter_min=482.103,
                                thread_class="4g6g", diameter=490, pitch=6)
thread["4g6g"][500][6] = Thread(major_diameter_max=499.920, major_diameter_min=499.320, pitch_diameter_max=496.023,
                                pitch_diameter_min=495.799, minor_diameter_max=493.425, minor_diameter_min=492.103,
                                thread_class="4g6g", diameter=500, pitch=6)
thread["4g6g"][510][6] = Thread(major_diameter_max=509.920, major_diameter_min=509.320, pitch_diameter_max=506.023,
                                pitch_diameter_min=505.799, minor_diameter_max=503.425, minor_diameter_min=502.103,
                                thread_class="4g6g", diameter=510, pitch=6)
thread["4g6g"][520][6] = Thread(major_diameter_max=519.920, major_diameter_min=519.320, pitch_diameter_max=516.023,
                                pitch_diameter_min=515.799, minor_diameter_max=513.425, minor_diameter_min=512.103,
                                thread_class="4g6g", diameter=520, pitch=6)
thread["4g6g"][530][6] = Thread(major_diameter_max=529.920, major_diameter_min=529.320, pitch_diameter_max=526.023,
                                pitch_diameter_min=525.799, minor_diameter_max=523.425, minor_diameter_min=522.103,
                                thread_class="4g6g", diameter=530, pitch=6)
thread["4g6g"][540][6] = Thread(major_diameter_max=539.920, major_diameter_min=539.320, pitch_diameter_max=536.023,
                                pitch_diameter_min=535.799, minor_diameter_max=533.425, minor_diameter_min=532.103,
                                thread_class="4g6g", diameter=540, pitch=6)
thread["4g6g"][550][6] = Thread(major_diameter_max=549.920, major_diameter_min=549.320, pitch_diameter_max=546.023,
                                pitch_diameter_min=545.799, minor_diameter_max=543.425, minor_diameter_min=542.103,
                                thread_class="4g6g", diameter=550, pitch=6)
thread["4g6g"][560][6] = Thread(major_diameter_max=559.920, major_diameter_min=559.320, pitch_diameter_max=556.023,
                                pitch_diameter_min=555.799, minor_diameter_max=553.425, minor_diameter_min=552.103,
                                thread_class="4g6g", diameter=560, pitch=6)
thread["4g6g"][570][6] = Thread(major_diameter_max=569.920, major_diameter_min=569.320, pitch_diameter_max=566.023,
                                pitch_diameter_min=565.799, minor_diameter_max=563.425, minor_diameter_min=562.103,
                                thread_class="4g6g", diameter=570, pitch=6)
thread["4g6g"][580][6] = Thread(major_diameter_max=579.920, major_diameter_min=579.320, pitch_diameter_max=576.023,
                                pitch_diameter_min=575.799, minor_diameter_max=573.425, minor_diameter_min=572.103,
                                thread_class="4g6g", diameter=580, pitch=6)
thread["4g6g"][590][6] = Thread(major_diameter_max=589.920, major_diameter_min=589.320, pitch_diameter_max=586.023,
                                pitch_diameter_min=585.799, minor_diameter_max=583.425, minor_diameter_min=582.103,
                                thread_class="4g6g", diameter=590, pitch=6)
thread["4g6g"][600][6] = Thread(major_diameter_max=599.920, major_diameter_min=599.320, pitch_diameter_max=596.023,
                                pitch_diameter_min=595.799, minor_diameter_max=593.425, minor_diameter_min=592.103,
                                thread_class="4g6g", diameter=600, pitch=6)
