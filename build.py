# pre installed with python
from time import sleep
import urllib.request
import os
import shutil
import zipfile
import datetime

# installed with pip
import htmlmin
#from slimmer import html_slimmer # or xhtml_slimmer, css_slimmer
from css_html_js_minify import html_minify, js_minify, css_minify

# get current directory
path = os.getcwd()

# build css files
# build js files (no js files right now...)
# copy /images/favicon.ico to /favicon.ico
# create a sitemap.xml file for the website.


def save_file(contents, filename, folder_path):
    file = f'{path}/{folder_path}/{filename}'
    try:
        f = open(file, "x")
        f.write(contents)
        f.close()
        print(f'Writing {filename} to {folder_path}')
    except FileExistsError:
        print('Deleting old file...')
        os.remove(file)

def zip_build():
    date_time = datetime.datetime.now()
    zip_filename = date_time.strftime('%Y_%m_%d_%H_%M_%S')
    create_folder('/archive')
    zf = zipfile.ZipFile(f'{path}/archive/{zip_filename}.zip', 'x')
    for dirname, subdirs, files in os.walk(f'{path}/build'):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()
    print(f'File {path}/archive/{zip_filename}.zip created!')

def create_folder(folder):
    # Create folder if doesn't exist
    dirName = f'{path}/{folder}'
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print(f'Directory {dirName} created!')
    else:
        print(f' Directory {dirName} already exists...')

def remove_spaces(code):
    # remove line breaks
    new_code = code.split('\\n')
    new_code = ''.join(new_code)
    # remove double spaces
    new_code = new_code.split('  ')
    new_code = ' '.join(new_code)

    ### HTML ###
    #remove spaces between html tags
    new_code = new_code.split('> <')
    new_code = '><'.join(new_code)
    # remove space before end of closing html tag >
    new_code = new_code.split(' >')
    new_code = '>'.join(new_code)
    # remove space after <
    new_code = new_code.split('< ')
    new_code = '<'.join(new_code)

    ### JavaScript ###
    #remove space after ;
    new_code = new_code.split('; ')
    new_code = ';'.join(new_code)
    # remove spaces before and after =
    new_code = new_code.split(' = ')
    new_code = '='.join(new_code)
    return new_code


def build_html():
    # create all pages in list
    for page in list_of_pages:
        print(f'Building {page}')
        #build_html(page)

        with urllib.request.urlopen(f'http://127.0.0.1:5000/{page}.html') as response:
            html = response.read()
            html = html.decode('utf-8')
            html=htmlmin.minify(html, remove_comments=True, remove_empty_space=True)
            html = html_minify(html)
            html = remove_spaces(html)
            save_file(html, f'{page}.html', '/build')
            #print(html)


def build(folder):
    files = os.listdir(f'{path}/{folder}')
    for filename in files:
        # read file
        f = open(f'{path}/{folder}/{filename}', "r")
        contents = f.read()
        f.close()
        # minify contents
        if folder == 'js':
            contents = js_minify(contents)
        if folder == 'css':
            contents = css_minify(contents, comments=False)
        contents = remove_spaces(contents)
        # save file
        f = open(f'{path}/build/{folder}/{filename}', "x")
        f.write(contents)
        f.close()
        print(f'Created {path}/build/{folder}/{filename}')


list_of_pages = ['index', 'about', 'contact', 'blog']

# add blog pages to list of pages
blog_pages = os.listdir(f'{path}/blog/posts')
for page in blog_pages:
    list_of_pages.append(f'blog/{page[:-5]}')

folders_to_create = ['build', 'build/blog', 'build/css', 'build/js', 'build/html', 'build/images']

# Create folders
try:
    shutil.rmtree(f'{path}/build')
except FileNotFoundError:
    _error = 'file not found'

for folder in folders_to_create:
    print(folder)
    create_folder(folder)

# build files
build_html()
build('css')
build('js')

# Zip files
print('Zipping files')
zip_build()

print('Build sucessful!')