from flask import flash, render_template, abort

def handle_error_404(error):
	flash('Page 404', 'info')
	return render_template('404.html')

def handle_error_500(error):
	flash('Page 500', 'info')
	return render_template('500.html')

def crash():
	abort(500)
