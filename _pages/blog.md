---
title: Blog
layout: post
permalink: /blog/
---

<p>Click link to view an article.</p>

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      - <span>{{ post.date | date: "%B %d, %Y" }}</span>
      <div class="post-meta-description">
        {% if post.description %}
          {{ post.description }}
        {% else %}
          {{ post.excerpt | strip_html | truncatewords: 30 }}
        {% endif %}
      </div>
    </li>
  {% endfor %}
</ul>
