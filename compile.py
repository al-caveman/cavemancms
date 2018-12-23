#!/usr/bin/python3
import argparse, configparser, os, re, shutil
import cavemark
cm = cavemark.CaveMark()


# page saver
def save_page(
        page_ids, articles_paths, templates_path, page_id_cur, page_path_cur
    ):
    print('compiling {}:'.format(page_path_cur))

    # make html page navigation links
    html_pagelinks = []
    with open('{}/pagelink.html'.format(templates_path)) as f:
        pagelink = f.read().strip()
        for i in page_ids:
            if i == page_id_cur:
                with open('{}/pagelink_cur.html'.format(templates_path)) as f:
                    pagelink_cur = f.read().strip()
                    html_pagelinks.append(pagelink_cur.format(**{'PAGEID': i}))
            else:
                html_pagelinks.append(pagelink.format(**{'PAGEID': i}))

    # make html articles
    with open('{}/article.html'.format(templates_path)) as f:
        template_article = f.read()
        html_articles = ''
        for article_path in articles_paths:
            print('   {}..'.format(article_path))
            with open(article_path) as h:
                article = h.read().strip()
            cm.parse(article)
            cm.flush()
            article_html = cm.get_html()
            html_article = template_article.format(**{
                'ARTICLE' : article_html
            })
            html_articles += '\n\n' + html_article

    # make html page
    with open('{}/page.html'.format(templates_path)) as f:
        html_page = f.read().format(**{
            'ARTICLES'   : html_articles,
            'PAGESLINKS' : ', '.join(html_pagelinks),
        })

    # save page
    os.makedirs(page_path_cur, exist_ok=True)
    with open('{}/index.html'.format(page_path_cur), 'w') as f:
        f.write(html_page)

    # forget cavemark citations
    cm.forget_citations()
    cm.forget_citation_counters()
    cm.forget_section_counters()
    cm.forget_resources()

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
    tmp_path = '{}/{}'.format(content_raw_path, i)
    if os.path.isdir(tmp_path):
        priority_path = '{}/priority'.format(tmp_path)
        article_path = '{}/article.md'.format(tmp_path)

        with open(priority_path, 'r') as f:
            priority = int(f.read())

        with open(article_path, 'r') as f:
            size = len(f.read())

        if priority in prioritized:
            prioritized[priority].append([article_path, size])
        else:
            prioritized[priority] = [[article_path, size]]

# figure out what pages to save
pages_ids = []
pages_sizes = []
pages_articles_paths = []
current_page_id = 1
current_page_size = 0
current_page_article_paths = []
for priority in sorted(prioritized):
    for article_path, article_size in prioritized[priority]:
        current_page_article_paths.append(article_path)
        current_page_size += article_size
    if (current_page_size > page_size_max):
        pages_ids.append(current_page_id)
        pages_sizes.append(current_page_size)
        pages_articles_paths.append(current_page_article_paths)
        current_page_id += 1
        current_page_size = 0
        current_page_article_paths = []

# merge unsaved articles, if any, to the last/newest page
if len(pages_ids) == 0: # nothing at all met page_size_max?
    pages_ids.append(current_page_id)
    pages_sizes.append(current_page_size)
    pages_articles_paths.append(current_page_article_paths)
elif current_page_size > 0: # somethings didn't meet page_size_max?
    pages_sizes[-1] += current_page_size
    pages_articles_paths[-1] += current_page_article_paths

# clean old compiled html
shutil.rmtree(content_compiled_path)

# save all pages
for i in range(0, len(pages_ids)):
    save_page(
        pages_ids[::-1],                # reversed page ids (for navigation)
        pages_articles_paths[i][::-1],  # reversed page's articles paths
        tmplt_cntnt_page_others,        # template
        pages_ids[i],                   # id of current page
        '{}/page/{}'.format(            # saving path
            content_compiled_path,
            pages_ids[i]
        )
    )

# save last page as index
save_page(
    pages_ids[::-1],
    pages_articles_paths[-1][::-1],
    tmplt_cntnt_page_last,
    pages_ids[i], # index page is the last page (i taken from code above)
    content_compiled_path
)

# update static files
compiled_site_static_files = '{}/{}'.format(
    content_compiled_path,
    site_static_files
)
try:
    shutil.rmtree(compiled_site_static_files)
except FileNotFoundError:
    pass
shutil.copytree(site_static_files, compiled_site_static_files)
