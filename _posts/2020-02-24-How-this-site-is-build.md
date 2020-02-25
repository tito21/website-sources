---
layout: post
title: "How this site is build"
slug: "how-site-build"
date: 2020-02-24 20:20:20 -0300
use_math: true
categories: ["Python", "pandoc", "github", "english"]
tags: ["markdown", "site generator", "pandoc", "websites"]
description: This site is generated using pandoc managed by a set of python
             scripts.
---

The old version of this site was hosted on Github pages and manage using Jekyll.
That system worked very well, I could write blog post on Markdown, easily tweak
the CSS and HTML of the theme and the website was always updated on every
commit. It only have one problem: Jekyll is written in Ruby. This is (imo) a
major problem as you have to manage a local Ruby environment, which can be
difficult if you don't really use it for anything else. I also think the whole
Jekyll ecosystem is a bit overkill for just converting Markdown to HTML
especially in light of tools like [pandoc](https://pandoc.org).


# Extra: generating `robots.txt` and `sitemap.xml`

One of the true advantages of a system like Jekyll is the ability to easily add
plugins. A `sitemap.xml` is generated with the website. Hopefully a 