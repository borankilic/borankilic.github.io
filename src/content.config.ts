import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const projects = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/projects' }),
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      blurb: z.string(), // one sentence, shown on the grid
      thumb: image(),
      thumbAlt: z.string(),
      year: z.string(),
      role: z.string().optional(),
      venue: z.string().optional(),
      tags: z.array(z.string()).default([]),
      links: z
        .array(z.object({ label: z.string(), href: z.string().url() }))
        .default([]),
      order: z.number().default(99),
      featured: z.boolean().default(false),
    }),
});

const courses = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/courses' }),
  schema: z.object({
    code: z.string(),
    title: z.string(),
    institution: z.enum(['UIUC', 'Boğaziçi University']),
    term: z.string(),
    field: z.string(),
    summary: z.string().optional(),
    materials: z
      .array(
        z.object({
          name: z.string(),
          href: z.string(),
          kind: z.enum(['pdf', 'notebook', 'code', 'slides']).default('pdf'),
        }),
      )
      .default([]),
    order: z.number().default(99),
  }),
});

const blog = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

export const collections = { projects, courses, blog };
