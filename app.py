from flask import Flask, url_for, redirect, request
from os import listdir, stat
from os.path import join

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    menu = f'''
            <a href="{url_for('static', filename='receipts/how to make a coffee.txt')}">How to make a coffee</a><br>
            <a href="{url_for('static', filename='receipts/how to make a tea.txt')}">How to make a tea</a><br><br><br>
            <a href="{url_for('show_recipe', recipe_name='coffee', step=1)}">Recipe for coffee</a><br>
            <a href="{url_for('show_recipe', recipe_name='tea', step=1)}">Recipe for tea</a><br><br>
            
            <a href="{url_for('leave_comment')}">Leave a comment</a><br>
            <a href="{url_for('show_comments')}">Show comments</a><br>
            '''

    return f'<h1>Select a receipt:</h1><br>{menu}'


@app.route('/leave_comment', methods=['GET', 'POST'])
def leave_comment():

    if request.method == 'GET':
        form_html = f'''
                    <form id="comment_id" action = "{url_for('leave_comment')}" method="POST">
                    <textarea id="comment" name="comment" rows="3" cols="50">
                    </textarea><br> 
                    <input type="submit" value="Send and return home">  
                    </form>
        '''

        return form_html

    else:
        comment = 'default'
        if 'comment' in request.form:
            comment = request.form['comment']

            if '<' in comment or '>' in comment:
                new_word = ''

                for item in comment:
                    if item == '<':
                        item = '&lt'

                    if item == '>':
                        item = '&gt'

                    new_word += item

                print(new_word)
                with open('static/comments/comments.txt', 'a') as file:
                    print(new_word, file=file)

            else:
                with open('static/comments/comments.txt', 'a') as file:
                    print(comment, file=file)

        return redirect(url_for('index'))


@app.route('/show_comments', methods=['GET'])
def show_comments():
    if stat('static/comments/comments.txt').st_size == 0:
        back_to_home = f'''
                <br><a href="{url_for('index')}">Back to home</a><br>
                '''
        return f'<h1>There is no any comments</h1><br>{back_to_home}'

    else:
        with open('static/comments/comments.txt', 'r') as file:
            content = file.read().splitlines()

        html_list_start = '<ul>'
        html_list_end = '</ul>'

        for line in content:
            html_list_start += f'<li>{line}</li>'

        html_list = html_list_start + html_list_end

        back_to_home = f'''
                <br><a href="{url_for('index')}">Back to home</a><br>
                '''

        return f'<h1>The comments</h1>{html_list + back_to_home}'


@app.route('/<string:recipe_name>/<int:step>', methods=['GET'])
def show_recipe(recipe_name, step):

    def recipe_calculations(recipe_name):
        static_address = 'static/receipts/'
        list_static = listdir(static_address)
        recipe_name_address = ''
        for el in list_static:
            if recipe_name in el:
                recipe_name_address = el
                break

        finall_address = join(static_address, recipe_name_address)

        with open(finall_address, 'r') as file:
            for count, line in enumerate(file):
                pass
            #print(count+1)
            number_of_pages = count+1
            #print(f'Potrzebna liczba stron dla {recipe_name} to {number_of_pages}')

        return [finall_address, number_of_pages]

    #recipe_calculations(recipe_name)

    with open(recipe_calculations(recipe_name)[0], 'r') as file:
        content = file.readlines()


    if step == 1:
        menu = f'''
        <h1>The step {step} for receipt how to make a {recipe_name}</h1>
        <h1>Number of needed pages: {recipe_calculations(recipe_name)[1]}</h1><br><br>
        <h1><a href="{url_for('static', filename='receipts/how to make a coffee.txt')}">How to make a {recipe_name}</a></h1>
    
        {content[step-1]}
        
        <br><br>
                    <ul>
                      <li><a href="{url_for('index')}">Home</a></li>
                      <li><a href="{url_for('show_recipe', recipe_name=recipe_name, step=step+1)}">Next</a></li>
                    </ul>
                '''
        return menu

    if step > 1 and step < recipe_calculations(recipe_name)[1]:

        menu = f'''
        <h1>The step {step} for receipt how to make a {recipe_name}</h1>
        <h1>Number of needed pages: {recipe_calculations(recipe_name)[1]}</h1><br><br>
        <h1><a href="{url_for('static', filename='receipts/how to make a coffee.txt')}">How to make a {recipe_name}</a></h1>
        
        {content[step-1]}
        
        <br><br>
                    <ul>
                      <li><a href="{url_for('index')}">Home</a></li>
                      <li><a href="{url_for('show_recipe', recipe_name=recipe_name, step=step+1)}">Next</a></li>
                      <li><a href="{url_for('show_recipe', recipe_name=recipe_name, step=step-1)}">Previous</a></li>
                    </ul>
                '''
        return menu

    if step == recipe_calculations(recipe_name)[1]:
        menu = f'''
        <h1>The step {step} for receipt how to make a {recipe_name}</h1>
        <h1>Number of needed pages: {recipe_calculations(recipe_name)[1]}</h1><br><br>
        <h1><a href="{url_for('static', filename='receipts/how to make a coffee.txt')}">How to make a {recipe_name}</a></h1>
        
        {content[step-1]}
        
        <br><br>
                    <ul>
                      <li><a href="{url_for('index')}">Home</a></li>
                      <li><a href="{url_for('show_recipe', recipe_name=recipe_name, step=step-1)}">Previous</a></li>
                    </ul>
                '''
        return menu



