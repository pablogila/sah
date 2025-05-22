"""
This script is used to update the documentation automatically.
Requires pdoc and ATON, install it with `pip install pdoc aton`.
Run this script as `python3 makedocs.py`.
"""

import shutil
import aton

readme = './README.md'
temp_readme = './_README_temp.md'
# Update links from the README
fix_dict ={
    '[classes](https://pablogila.github.io/sah/sah/classes.html)'              : '`sah.classes`',
    '[fit](https://pablogila.github.io/sah/sah/fit.html)'                      : '`sah.fit`',
    '[normalize](https://pablogila.github.io/sah/sah/normalize.html)'          : '`sah.normalize`',
    '[plot](https://pablogila.github.io/sah/sah/plot.html)'                    : '`sah.plot`',
    '[deuterium](https://pablogila.github.io/sah/sah/deuterium.html)'          : '`sah.deuterium`',
    '[samples](https://pablogila.github.io/sah/sah/samples.html)'              : '`sah.samples`',
    'Check the [full documentation online](https://pablogila.github.io/sah/).' : '',
}

# Get the package version as __version__
exec(open('sah/_version.py').read())
print(f'Updating docs to {__version__}...')
# Copy the pics folder
shutil.copytree('pics', 'docs/pics', dirs_exist_ok=True)
# Fix the README
aton.txt.edit.from_template(readme, temp_readme, fix_dict)
# Run Pdoc with the dark theme template from the ./css/ folder
aton.call.bash(f"pdoc ./sah/ -o ./docs/ --mermaid --math --footer-text='SAH {__version__} documentation' -t ./css/")
aton.file.remove(temp_readme)
# Include google search verification
#search_verification_tag = '    <meta name="google-site-verification" content="u0Be1NUH4ztGm5rr5f_YFt6hqoqMJ-j9h7rk3wEJAUo" />'
#aton.txt.edit.insert_under('docs/aton.html', '<head>', search_verification_tag)

