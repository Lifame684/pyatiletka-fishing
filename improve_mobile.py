import re

files = ['index.html', 'index-alt.html', 'index-minimal.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Enhance Hero titles for mobile
    content = content.replace('text-4xl md:text-5xl lg:text-6xl', 'text-3xl sm:text-4xl md:text-5xl lg:text-6xl')
    content = content.replace('text-4xl md:text-5xl', 'text-3xl sm:text-4xl md:text-5xl')
    content = content.replace('text-5xl md:text-7xl', 'text-4xl sm:text-5xl md:text-7xl')
    content = content.replace('text-4xl sm:text-5xl lg:text-6xl', 'text-3xl sm:text-4xl md:text-5xl lg:text-6xl') # minimal

    # 2. Make buttons full-width on mobile
    content = content.replace('flex flex-col sm:flex-row gap-4', 'flex flex-col sm:flex-row gap-3 w-full sm:w-auto')
    content = content.replace('flex flex-col sm:flex-row gap-6', 'flex flex-col sm:flex-row gap-4 w-full sm:w-auto')
    
    # Update anchor tags inside those flex containers to be w-full on mobile
    content = re.sub(r'class="([^"]*?)px-8 py-4', r'class="\1w-full sm:w-auto px-6 sm:px-8 py-3 sm:py-4', content)
    content = re.sub(r'class="([^"]*?)px-6 py-3', r'class="\1w-full sm:w-auto px-6 py-3 text-center justify-center', content)

    # 3. Reduce padding for mobile screens
    content = content.replace('py-16 md:py-24', 'py-12 md:py-24')
    content = content.replace('py-24', 'py-16 md:py-24')
    content = content.replace('py-20', 'py-12 md:py-20')
    content = content.replace('p-8 rounded', 'p-6 md:p-8 rounded')
    content = content.replace('p-10 md:p-14', 'p-6 sm:p-10 md:p-14')
    content = content.replace('p-12 md:p-20', 'p-6 sm:p-12 md:p-20')
    content = content.replace('section-padding', 'py-12 md:py-20') # for minimal

    # 4. Improve Gallery for mobile (smaller gaps)
    content = content.replace('gap-4 space-y-4', 'gap-2 space-y-2 md:gap-4 md:space-y-4')

    # 5. Mobile Menu - larger tap targets
    content = content.replace('px-3 py-3 text-base', 'px-4 py-4 text-lg border-b border-slate-100 last:border-0')
    content = content.replace('space-y-2', 'space-y-1')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML files updated for mobile!")
