---
title: Blog
layout: default
permalink: /blog/
sitemp: true
---

<h1 style="margin-bottom: 20px;">{{ page.title }}</h1>

<p>Click a tile below to view the corresponding article.</p>

<ul style="list-style-type: none; padding-left: 0;">
  {% for post in site.posts %}
    <li>
      
      <a href="{{ post.url | relative_url }}" class="well blog-post-card">

        {% if post.thumbnail %}
          <div class="blog-post-thumbnail-wrapper">
            <img src="{{ post.thumbnail | relative_url }}" alt="{{ post.title }}" class="blog-post-thumbnail">
          </div>
        {% endif %}

        <div style="flex-grow: 1;">
          <span class="blog-post-title">{{ post.title }}</span>
          <span style="font-size: 2.0rem;"> - {{ post.date | date: "%B %d, %Y" }}</span>
          <div class="post-meta-description" style="font-size: 1.8rem; margin-top: 10px;">
            {% if post.description %}
              {{ post.description }}
            {% else %}
              {{ post.excerpt | strip_html | truncatewords: 30 }}
            {% endif %}
          </div>
        </div>

      </a>
      
    </li>
  {% endfor %}
</ul>
