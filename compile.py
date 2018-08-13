#!/usr/bin/python3
import argparse, configparser, os, re, shutil

# page saver
def save_page(page, template, cur_page_id, last_page_id, rootdir):
    # create articles

    # make html page navigation links
    with open('{}/pagelink.html'.format(template)) as f:
        pagelink = f.read().strip()
        html_pagelinks = ', '.join([
            pagelink.format(**{
                'PAGEID': i
            }) for i in reversed(range(1, last_page_id+1))
        ])

    # make html articles
    with open('{}/article.html'.format(template)) as f:
        article = f.read()
        html_articles = ''
        for article_path in page['articles_paths']:
            with open('{}/title'.format(article_path)) as g:
                title = g.read().strip()
            with open('{}/body'.format(article_path)) as h:
                body = h.read().strip()
                paragraphs = re.split(r'\n\n+', body)
                html_body = '\n\n'.join([
                    '<p>{}</p>'.format(p) for p in paragraphs
                ])
            html_article = article.format(**{
                'POST_TITLE': title,
                'POST_BODY' : html_body
            })
            html_articles += '\n\n' + html_article

    # make html page
    with open('{}/page.html'.format(template)) as f:
        html_page = f.read().format(**{
            'ARTICLES' : html_articles, 
            'PAGESLINKS' : html_pagelinks, 
        })

    # save page
    page_dir = '{}/{}'.format(rootdir, page['page_id'])
    os.makedirs(page_dir, exist_ok=True)
    with open('{}/index.html'.format(page_dir), 'w') as f:
        f.write(html_page)

# parse arguments
parser = argparse.ArgumentParser(description='CavemanCMS compiler')
parser.add_argument('configfile', type=str, help='Path to configuration file')
args = parser.parse_args()

# load config file
config = configparser.ConfigParser()
config.read_file(open(
    os.path.expanduser(args.configfile)
))
content_raw_path        = config['general']['content_raw_path']
site_static_files       = config['general']['site_static_files']
content_compiled_path   = config['general']['content_compiled_path']
page_size_max           = int(config['general']['page_size_max'])
tmplt_cntnt_page_last   = config['last_content_page']['template_path']
tmplt_cntnt_page_others = config['other_content_pages']['template_path']

# categorize articles by priority
prioritized = {}
for i in os.listdir(content_raw_path):
    article_path = '{}/{}'.format(content_raw_path, i)
    if os.path.isdir(article_path):
        priority_path = '{}/priority'.format(article_path)
        body_path = '{}/body'.format(article_path)

        with open(priority_path, 'r') as f:
            priority = int(f.read())

        with open(body_path, 'r') as f:
            size = len(f.read())

        if priority in prioritized:
            prioritized[priority].append([article_path, size])
        else:
            prioritized[priority] = [[article_path, size]]

# figure out what pages to save
pages_to_save = []
current_page_size = 0
current_page_id = 1
current_page_article_paths = []
for priority in sorted(prioritized, reverse=True):
    for article_path, article_size in prioritized[priority]:
        current_page_article_paths.append(article_path)
        current_page_size += article_size
    if (current_page_size > page_size_max):
        pages_to_save.append({
            'articles_paths': current_page_article_paths,
            'page_size'     : current_page_size,
            'page_id'       : current_page_id,
        })
        current_page_id += 1
        current_page_size = 0
        current_page_article_paths = []

# merge unsaved articles, if any, to the last page
if len(pages_to_save) == 0:
    pages_to_save.append({
        'articles_paths': current_page_article_paths,
        'page_size'     : current_page_size,
        'page_id'       : current_page_id,
    })
elif current_page_size > 0:
    pages_to_save[-1]['articles_paths'] += current_page_article_paths
    pages_to_save[-1]['page_size'] += current_page_size

# save all pages
for i in range(0, len(pages_to_save)):
    save_page(
        pages_to_save[i],                       # articles to save
        tmplt_cntnt_page_others,                # template
        i+1,                                    # current page id
        len(pages_to_save),                     # latest page
        '{}/page'.format(content_compiled_path) # root dir
    )

# save last page as index
save_page(
    {
        'articles_paths': pages_to_save[-1]['articles_paths'],
        'page_size'     : pages_to_save[-1]['page_size'],
        'page_id'       : '.',
    },                      # articles to save
    tmplt_cntnt_page_last,  # template
    len(pages_to_save),     # current page
    len(pages_to_save),     # latest page
    content_compiled_path   # root dir
)

# copy static files
try:
    shutil.copytree(site_static_files, '{}/{}'.format(
        content_compiled_path,
        site_static_files)
    )
except FileExistsError:
    pass
