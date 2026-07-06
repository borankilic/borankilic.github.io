// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

// Hosted at https://borankilic.github.io (a GitHub user page → base is root "/").
export default defineConfig({
  site: 'https://borankilic.github.io',
  integrations: [mdx(), sitemap()],
  markdown: {
    shikiConfig: { theme: 'github-light' },
  },
});
