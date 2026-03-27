---
title: Blog
layout: default
permalink: /blog/
sitemp: true
---

<h1 style="margin-bottom: 20px;">{{ page.title }}</h1>

<p>Click a link or image below to view the corresponding article.</p>

<ul style="list-style-type: none; padding-left: 0;">
  {% for post in site.posts %}
    <li style="display: flex; align-items: center;">
      
      {% if post.thumbnail %}
        <a href="{{ post.url | relative_url }}" style="width: clamp(120px, 30vw, 300px); flex-shrink: 0; display: flex; justify-content: center;">
          <img src="{{ post.thumbnail | relative_url }}" alt="{{ post.title }}" style="width: 100%; max-height: 250px; object-fit: contain">
        </a>
      {% endif %}

      <div style="flex-grow: 1;">
        <a href="{{ post.url | relative_url }}" style="font-size: 2rem; font-weight: bold;">{{ post.title }}</a>
        - <span style="font-size: 2.0rem;">{{ post.date | date: "%B %d, %Y" }}</span>
        <div class="post-meta-description" style="font-size: 1.8rem;">
          {% if post.description %}
            {{ post.description }}
          {% else %}
            {{ post.excerpt | strip_html | truncatewords: 30 }}
          {% endif %}
        </div>
      </div>
      
    </li>
  {% endfor %}
</ul>
