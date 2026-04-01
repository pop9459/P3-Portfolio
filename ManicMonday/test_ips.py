import ips as ips
import re

def test_read():
	l = ips.read_ips()
	assert len(l) == 360

def test_pattern():
	pp = ips.get_pattern()
	p = "47.82.11.68"
	assert re.match(pp, p) is not None
	p = "47.83.11.68"
	assert re.match(pp, p) is None
	p = "47.82.11.280"
	assert re.match(pp, p) is None
	p = "47.82.11.03"
	assert re.match(pp, p) is None

def test_filter():
	s = ips.read_ips()
	sout = ips.filter_ips(s)
	assert len(sout) in (68, 69, 70)

