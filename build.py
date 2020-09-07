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
from PIL import Image

# get current directory
path = os.getcwd()


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

        with urllib.request.urlopen(f'http://127.0.0.1:5000/{page}.html') as response:
            html = response.read()
            html = html.decode('utf-8')
            html=htmlmin.minify(html, remove_comments=True, remove_empty_space=True)
            html = html_minify(html)
            html = remove_spaces(html)
            save_file(html, f'{page}.html', '/build')


def build(files, file_type):
    for filename in files:
        # read file
        f = open(f'{path}/{filename}', "r")
        contents = f.read()
        f.close()
        # minify contents
        if file_type == 'js':
            contents = js_minify(contents)
        if file_type == 'css':
            contents = css_minify(contents, comments=False)
        contents = remove_spaces(contents)
        # save file
        f = open(f'{path}/build/{filename}', "x")
        f.write(contents)
        f.close()
        print(f'Created {path}/build/{filename}')


def build_images(images):
    for image in images:
        # save favicon.ico in /build folder
        # else save in /build/images
        if 'favicon.ico' in image:
            img = Image.open(f'{path}/{image}')
            img.save(f'{path}/build/{image}', optimize=True)
        else:
            img = Image.open(f'{path}/{image}')
            img.save(f'{path}/build/{image}', quality=20, optimize=True)
            print(f'Created {path}/build/{image}')


def copy_files(files):
    for filename in files:
        shutil.copyfile(f'{path}/{filename}', f'{path}/build/{filename}')

def build_sitemap(pages, url):
    sitemap = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    for page in pages:
        if '.html' not in page:
            page += '.html'
        sitemap += f'<url><loc>{url + page}</loc></url>'
    sitemap += '</urlset>'
    # save to file
    f = open(f'{path}/build/sitemap.xml', "x")
    f.write(sitemap)
    f.close()

website_url = 'http://indexdothtml.com/'

folders_to_create = ['build', 'build/blog', 'build/css', 'build/js', 'build/projects', 'build/images']

list_of_pages = ['index', 'about', 'contact', 'blog']
css_files = ['css/main.css']
js_files = []
image_files = []
other_files = []

# add blog pages to list of pages
blog_pages = os.listdir(f'{path}/blog/posts')
for page in blog_pages:
    list_of_pages.append(f'blog/{page[:-5]}')

# add project html, css, js, images, and other files to their lists
projects = os.listdir(f'{path}/projects')
for project in projects:
    folders_to_create.append(f'build/projects/{project}')
    files = os.listdir(f'{path}/projects/{project}')
    for f in files:
        f = f.lower()
        # if no . in f then its a folder
        if '.' in f:
            if '.html' in f:
                list_of_pages.append(f'projects/{project}/{f[:-5]}')
            elif '.css' in f:
                css_files.append(f'projects/{project}/{f}')
            elif '.js' in f:
                js_files.append(f'projects/{project}/{f}')
            elif '.jpeg' in f or '.jpg' in f or '.png' in f:
                image_files.append(f'projects/{project}/{f}')
            else:
                other_files.append(f'projects/{project}/{f}')
        else:
            folders_to_create.append(f'build/projects/{project}/{f}')
            files2 = os.listdir(f'{path}/projects/{project}/{f}')
            for f2 in files2:
                # if no . in f2 then its a folder
                if '.' in f2:
                    if '.html' in f2:
                        list_of_pages.append(f'projects/{project}/{f}/{f2[:-5]}')
                    elif '.css' in f2:
                        css_files.append(f'projects/{project}/{f}/{f2}')
                    elif '.js' in f2:
                        js_files.append(f'projects/{project}/{f}/{f2}')
                    elif '.jpeg' in f2 or '.jpg' in f2 or '.png' in f2.lower():
                        image_files.append(f'projects/{project}/{f}/{f2}')
                    else:
                        other_files.append(f'projects/{project}/{f}/{f2}')


# Delete build folder
try:
    shutil.rmtree(f'{path}/build')
except FileNotFoundError:
    _error = 'file not found'

# create folders
for folder in folders_to_create:
    create_folder(folder)

# build files
build_html()
build(css_files, 'css')
build(js_files, 'js')
build_images(image_files)

# copy files that shouldn't be compressed
copy_files(other_files)

# build sitemap.xml from list of pages
build_sitemap(list_of_pages, website_url)

# Zip files
print('Zipping files')
zip_build()

print('Build sucessful!')