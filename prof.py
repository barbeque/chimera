import pstats
p = pstats.Stats('out.dat')
p.strip_dirs().sort_stats('time').print_stats(100)