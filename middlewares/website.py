from flask import render_template
import middlewares.api as api

def page_index():
	return render_template('index.html')

def page_about():
	return render_template('about.html')


def page_candidates():
	candidates = api.get_candidates(False)
	return render_template('candidates.html', candidates=candidates)


def page_interviews():
	interviews = api.get_interviews(False)
	return render_template('interviews.html', interviews=interviews)


def page_positions():
	positions = api.get_positions(False)
	return render_template('positions.html', positions=positions)
