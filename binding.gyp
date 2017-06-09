{
  'targets': [
    {
      'target_name': 'cmark',
      'include_dirs': [
        '<!(node -e "require(\'nan\')")',
        'vendor/cmark/src',
        'vendor/cmark/extensions',
        'vendor/cmark/build/src',
        'vendor/cmark/build/extensions',
      ],
      'sources': [
        'src/cmark.cpp',
        'src/common.cpp',
        'src/sync.cpp',
        # TODO: Automate or improve this external source listing stuff?
        'vendor/cmark/src/arena.c',
        'vendor/cmark/src/blocks.c',
        'vendor/cmark/src/buffer.c',
        'vendor/cmark/src/cmark.c',
        'vendor/cmark/src/cmark_ctype.c',
        'vendor/cmark/src/commonmark.c',
        'vendor/cmark/src/houdini_href_e.c',
        'vendor/cmark/src/houdini_html_e.c',
        'vendor/cmark/src/houdini_html_u.c',
        'vendor/cmark/src/html.c',
        'vendor/cmark/src/inlines.c',
        'vendor/cmark/src/iterator.c',
        'vendor/cmark/src/latex.c',
        'vendor/cmark/src/linked_list.c',
        'vendor/cmark/src/main.c',
        'vendor/cmark/src/man.c',
        'vendor/cmark/src/node.c',
        'vendor/cmark/src/plugin.c',
        'vendor/cmark/src/references.c',
        'vendor/cmark/src/registry.c',
        'vendor/cmark/src/render.c',
        'vendor/cmark/src/scanners.c',
        'vendor/cmark/src/syntax_extension.c',
        'vendor/cmark/src/utf8.c',
        'vendor/cmark/src/xml.c',
        'vendor/cmark/extensions/autolink.c',
        'vendor/cmark/extensions/core-extensions.c',
        'vendor/cmark/extensions/ext_scanners.c',
        'vendor/cmark/extensions/strikethrough.c',
        'vendor/cmark/extensions/table.c',
        'vendor/cmark/extensions/tagfilter.c',
      ],
    },
  ],
}
