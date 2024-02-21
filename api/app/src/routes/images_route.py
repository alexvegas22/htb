upload_folder = os.path.join('static', 'uploads')
 
app.config['UPLOAD'] = upload_folder
 
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        return render_template('image_render.html', img=img)
    return render_template('image_render.html')
 
