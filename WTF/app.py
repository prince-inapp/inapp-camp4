from flask import Flask, render_template
from myform import NameForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = NameForm()
    name = None
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('form.html', form=form, name=name)

if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)