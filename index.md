---
layout: default
title: Home
---

# Welcome to Torchbearer Lab

### Option 1: Direct Link (Try this first)
[Read the Welcome Post]
(https://meredithclikkie.github.io/torchbearerlab.github.io/welcome/)

### Option 2: Short Path
[Welcome Post (Alternative Link)](./2025/12/31/welcome/)

---

## All Posts (Automatic List)
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
